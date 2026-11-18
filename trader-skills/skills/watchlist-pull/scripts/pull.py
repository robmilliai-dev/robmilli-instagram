#!/usr/bin/env python3
"""Milli.ai watchlist-pull: tickers in -> screened, deduped, ranked watchlist out.

  python pull.py --campaign tech-leaders --universe universe.txt --min-price 10 \
      --min-dollar-vol 20000000 --trend above200 --top 25

Resumable: every ticker's result is appended to progress.jsonl, so a rerun skips
what is done. Free data (Yahoo Finance via yfinance). Never places a trade.
Requires: pip install yfinance pandas
Educational only. Not financial advice.
"""
import argparse, csv, json, os, sys, time

DUP_GROUPS = [{"GOOG", "GOOGL"}, {"BRK-A", "BRK-B"}, {"FOX", "FOXA"}, {"NWS", "NWSA"}, {"UA", "UAA"}]


def norm(t):
    return t.strip().upper().replace(".", "-")


def read_universe(path):
    seen, out = set(), []
    for line in open(path):
        t = norm(line.split(",")[0].split("#")[0])
        if t and t not in seen and t != "TICKER":
            seen.add(t)
            out.append(t)
    return out


def metrics(df):
    """df: daily OHLCV with columns Open High Low Close Volume, oldest first."""
    close, high, low, vol = df["Close"], df["High"], df["Low"], df["Volume"]
    n = len(close)
    if n < 60:
        return None
    last = float(close.iloc[-1])
    dv20 = float((close * vol).tail(20).mean())
    sma200 = float(close.tail(200).mean()) if n >= 200 else None
    sma50 = float(close.tail(50).mean())
    hi20 = float(high.tail(21).iloc[:-1].max())
    tr = (high - low).tail(14)
    atr_pct = float(tr.mean() / last) if last else None
    ret63 = float(last / close.iloc[-64] - 1) if n >= 64 else None
    ret252 = float(last / close.iloc[-253] - 1) if n >= 253 else None
    return {
        "price": round(last, 2),
        "dollar_vol_20d": round(dv20),
        "above_200d": None if sma200 is None else last > sma200,
        "above_50d": last > sma50,
        "new_20d_high": last > hi20,
        "atr_pct": None if atr_pct is None else round(atr_pct, 4),
        "ret_3m": None if ret63 is None else round(ret63, 4),
        "ret_12m": None if ret252 is None else round(ret252, 4),
        "bars": n,
    }


def screen(m, a):
    """Return (passed, reason_if_dropped)."""
    if m is None:
        return False, "under 60 days of data"
    if m["price"] < a.min_price:
        return False, f"price {m['price']} < {a.min_price}"
    if m["dollar_vol_20d"] < a.min_dollar_vol:
        return False, f"20d dollar volume {m['dollar_vol_20d']:,} < {a.min_dollar_vol:,}"
    if a.trend == "above200" and m["above_200d"] is not True:
        return False, "not above 200-day average"
    if a.trend == "above50" and not m["above_50d"]:
        return False, "not above 50-day average"
    if a.trend == "breakout" and not m["new_20d_high"]:
        return False, "no new 20-day high"
    if a.max_atr and m["atr_pct"] and m["atr_pct"] > a.max_atr:
        return False, f"too jumpy: daily range {m['atr_pct']:.1%} > {a.max_atr:.1%}"
    return True, ""


def dedupe(rows):
    keep, dropped = [], []
    by = {r["ticker"]: r for r in rows}
    gone = set()
    for g in DUP_GROUPS:
        present = [t for t in g if t in by]
        if len(present) > 1:
            best = max(present, key=lambda t: by[t]["dollar_vol_20d"])
            for t in present:
                if t != best:
                    gone.add(t)
                    dropped.append((t, f"duplicate share class of {best}"))
    for r in rows:
        if r["ticker"] not in gone:
            keep.append(r)
    return keep, dropped


def fetch_yf(ticker):
    import yfinance as yf
    df = yf.download(ticker, period="2y", interval="1d", auto_adjust=True, progress=False, threads=False)
    if df is None or df.empty:
        return None
    if hasattr(df.columns, "levels"):  # newer yfinance returns MultiIndex columns
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
    return df.dropna()


def main(argv=None, fetch=fetch_yf):
    ap = argparse.ArgumentParser()
    ap.add_argument("--campaign", required=True)
    ap.add_argument("--universe", required=True, help="text/CSV file, one ticker per line")
    ap.add_argument("--min-price", type=float, default=5)
    ap.add_argument("--min-dollar-vol", type=float, default=10_000_000)
    ap.add_argument("--trend", choices=["any", "above50", "above200", "breakout"], default="any")
    ap.add_argument("--max-atr", type=float, default=0, help="e.g. 0.06 drops names with >6%% daily range")
    ap.add_argument("--rank", choices=["ret_3m", "ret_12m", "dollar_vol_20d"], default="ret_3m")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--sleep", type=float, default=0.7, help="seconds between requests (stay polite)")
    ap.add_argument("--yes", action="store_true", help="skip the size confirmation")
    a = ap.parse_args(argv)

    out = os.path.join("watchlists", a.campaign)
    os.makedirs(out, exist_ok=True)
    prog_path = os.path.join(out, "progress.jsonl")
    done = {}
    if os.path.exists(prog_path):
        for line in open(prog_path):
            try:
                r = json.loads(line)
                done[r["ticker"]] = r
            except Exception:
                pass

    tickers = read_universe(a.universe)
    todo = [t for t in tickers if t not in done]
    est = len(todo) * (a.sleep + 0.6)
    print(f"Universe {len(tickers)} tickers · {len(done)} already done · {len(todo)} to fetch · ~{est/60:.1f} min · $0 (free data)")
    if len(todo) > 300 and not a.yes:
        if input("Large pull. Continue? [y/N] ").strip().lower() != "y":
            sys.exit(0)

    with open(prog_path, "a") as prog:
        for i, t in enumerate(todo, 1):
            rec = {"ticker": t}
            try:
                df = fetch(t)
                m = metrics(df) if df is not None else None
                rec.update(m or {})
                ok, why = screen(m, a)
                rec["passed"], rec["drop_reason"] = ok, why
            except Exception as e:  # keep going, log it
                rec["passed"], rec["drop_reason"] = False, f"fetch error: {e.__class__.__name__}"
            prog.write(json.dumps(rec) + "\n")
            prog.flush()
            done[t] = rec
            if i % 25 == 0:
                print(f"  {i}/{len(todo)}")
            time.sleep(a.sleep)

    # Re-screen from stored numbers every run, so changing a filter never needs a re-download.
    rows = []
    for t in tickers:
        if t not in done:
            continue
        r = dict(done[t])
        if "price" in r:
            ok, why = screen({k: r.get(k) for k in ("price", "dollar_vol_20d", "above_200d", "above_50d", "new_20d_high", "atr_pct")}, a)
            r["passed"], r["drop_reason"] = ok, why
        rows.append(r)
    cols = ["ticker", "price", "dollar_vol_20d", "above_200d", "above_50d", "new_20d_high", "atr_pct", "ret_3m", "ret_12m", "passed", "drop_reason"]

    def write(path, rs):
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(rs)

    write(os.path.join(out, f"{a.campaign}_all.csv"), rows)
    passed = [r for r in rows if r.get("passed")]
    passed, dup_drops = dedupe(passed)
    write(os.path.join(out, f"{a.campaign}_passed.csv"), passed)
    ranked = sorted(passed, key=lambda r: (r.get(a.rank) is None, -(r.get(a.rank) or 0)))[: a.top]
    write(os.path.join(out, f"WATCHLIST_{a.campaign}.csv"), ranked)
    with open(os.path.join(out, "dropped.log"), "w") as f:
        for r in rows:
            if not r.get("passed"):
                f.write(f"{r['ticker']}\t{r.get('drop_reason')}\n")
        for t, why in dup_drops:
            f.write(f"{t}\t{why}\n")
    with open(os.path.join(out, "tradingview_import.txt"), "w") as f:
        f.write(",".join(r["ticker"].replace("-", ".") for r in ranked))
    reasons = {}
    for r in rows:
        if not r.get("passed"):
            k = (r.get("drop_reason") or "").split(" ")[0]
            reasons[k] = reasons.get(k, 0) + 1
    print(f"Done. {len(rows)} checked · {len(passed)} passed · top {len(ranked)} in WATCHLIST_{a.campaign}.csv")
    print("Dropped by first word of reason:", reasons)


if __name__ == "__main__":
    main()
