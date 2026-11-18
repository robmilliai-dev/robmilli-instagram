#!/usr/bin/env python3
"""Milli.ai account-stats: read-only trading account scoreboard.

Sources:
  --source alpaca   live account via Alpaca's REST API (read-only calls only)
  --source csv      any broker: a CSV of closed trades with a P&L column

Formats: block (default), post, json

Examples:
  python account_stats.py --source alpaca --period 1M
  python account_stats.py --source csv --file trades.csv --start-equity 5000 --format json

Standard library only. Never places, changes or cancels orders.
Educational only. Not financial advice.
"""
import argparse, csv, json, math, os, sys, urllib.request, urllib.error
from datetime import datetime, timezone

LIVE = "https://api.alpaca.markets"
PAPER = "https://paper-api.alpaca.markets"


def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def load_env(path=".env"):
    if not os.path.exists(path):
        return
    for line in open(path):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"'))


# ---------- math ----------
def max_drawdown(equity):
    peak, worst = None, 0.0
    for e in equity:
        if e is None or e <= 0:
            continue
        peak = e if peak is None else max(peak, e)
        worst = min(worst, e / peak - 1)
    return worst


def trade_stats(pnls):
    wins = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p < 0]
    n = len(pnls)
    gross_loss = -sum(losses)
    return {
        "trades": n,
        "win_rate": (len(wins) / n) if n else None,
        "avg_win": (sum(wins) / len(wins)) if wins else None,
        "avg_loss": (sum(losses) / len(losses)) if losses else None,
        "profit_factor": (sum(wins) / gross_loss) if gross_loss > 0 else None,
        "net_pnl": sum(pnls),
        "best": max(pnls) if pnls else None,
        "worst": min(pnls) if pnls else None,
        "too_few_trades": n < 30,
    }


# ---------- alpaca ----------
def alpaca_get(base, path, key, secret):
    req = urllib.request.Request(base + path, headers={
        "APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            die("Alpaca rejected the keys. Check ALPACA_KEY_ID / ALPACA_SECRET_KEY and that "
                "ALPACA_PAPER matches the account the keys belong to (paper keys only work on paper).")
        die(f"Alpaca HTTP {e.code} on {path}")
    except urllib.error.URLError as e:
        die(f"Could not reach Alpaca: {e.reason}")


def from_alpaca(period, fetch=alpaca_get):
    key, secret = os.environ.get("ALPACA_KEY_ID"), os.environ.get("ALPACA_SECRET_KEY")
    if not key or not secret:
        die("Set ALPACA_KEY_ID and ALPACA_SECRET_KEY in .env (use READ-ONLY or paper keys).")
    base = PAPER if os.environ.get("ALPACA_PAPER", "true").lower() == "true" else LIVE
    acct = fetch(base, "/v2/account", key, secret)
    pos = fetch(base, "/v2/positions", key, secret)
    hist = fetch(base, f"/v2/account/portfolio/history?period={period}&timeframe=1D", key, secret)
    equity = float(acct["equity"])
    last_eq = float(acct.get("last_equity") or equity)
    curve = [float(x) for x in (hist.get("equity") or []) if x is not None]
    long_mv = sum(float(p["market_value"]) for p in pos if float(p["market_value"]) > 0)
    short_mv = -sum(float(p["market_value"]) for p in pos if float(p["market_value"]) < 0)
    period_ret = (curve[-1] / curve[0] - 1) if len(curve) > 1 and curve[0] > 0 else None
    return {
        "source": "alpaca-paper" if base == PAPER else "alpaca-live",
        "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "period": period,
        "equity": equity,
        "day_pnl": equity - last_eq,
        "day_pnl_pct": (equity / last_eq - 1) if last_eq else None,
        "period_return": period_ret,
        "max_drawdown": max_drawdown(curve) if curve else None,
        "exposure_pct": (long_mv + short_mv) / equity if equity else None,
        "cash": float(acct.get("cash", 0)),
        "open_positions": len(pos),
        "positions": sorted([{
            "symbol": p["symbol"], "qty": float(p["qty"]),
            "market_value": float(p["market_value"]),
            "unrealized_pnl": float(p["unrealized_pl"]),
            "unrealized_pct": float(p["unrealized_plpc"]),
        } for p in pos], key=lambda x: -abs(x["market_value"]))[:10],
        "trades": None,
    }


# ---------- csv ----------
PNL_NAMES = ["pnl", "p&l", "realized_pnl", "realized p&l", "realized_pl", "profit", "net_pnl", "gain/loss", "profit/loss"]
DATE_NAMES = ["date", "close_date", "closed", "exit_date", "time", "datetime"]


def find_col(headers, names):
    low = {h.lower().strip(): h for h in headers}
    for n in names:
        if n in low:
            return low[n]
    return None


def money(s):
    s = str(s).strip().replace("$", "").replace(",", "")
    if s.startswith("(") and s.endswith(")"):
        s = "-" + s[1:-1]
    return float(s) if s not in ("", "-") else None


def parse_date(s):
    s = str(s).strip()
    for f in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y", "%m/%d/%Y %H:%M", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(s[:len(datetime.now().strftime(f))] if "%H" not in f else s, f)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(s.replace("Z", ""))
    except ValueError:
        return datetime.min


def from_csv(path, start_equity):
    if not os.path.exists(path):
        die(f"No file at {path}")
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8-sig")))
    if not rows:
        die("CSV is empty.")
    pcol = find_col(rows[0].keys(), PNL_NAMES)
    if not pcol:
        die(f"No P&L column found. Rename your profit column to 'pnl'. Columns seen: {list(rows[0].keys())}")
    dcol = find_col(rows[0].keys(), DATE_NAMES)
    if dcol:
        rows.sort(key=lambda r: parse_date(r[dcol]))
    pnls = [v for v in (money(r[pcol]) for r in rows) if v is not None]
    curve, eq = [start_equity], start_equity
    for p in pnls:
        eq += p
        curve.append(eq)
    return {
        "source": "csv", "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "period": f"{rows[0][dcol][:10]} to {rows[-1][dcol][:10]}" if dcol else f"{len(pnls)} trades",
        "equity": eq, "day_pnl": None, "day_pnl_pct": None,
        "period_return": eq / start_equity - 1 if start_equity else None,
        "max_drawdown": max_drawdown(curve), "exposure_pct": None, "cash": None,
        "open_positions": None, "positions": [], "trades": trade_stats(pnls),
    }


# ---------- output ----------
def pct(x):
    return "n/a" if x is None else f"{x*100:+.1f}%"


def usd(x):
    return "n/a" if x is None else f"${x:,.2f}"


def block(s):
    out = [f"ACCOUNT SCOREBOARD · {s['source']} · {s['as_of']}", "",
           f"Equity        {usd(s['equity'])}"]
    if s["day_pnl"] is not None:
        out.append(f"Today         {usd(s['day_pnl'])} ({pct(s['day_pnl_pct'])})")
    out += [f"Return        {pct(s['period_return'])}  ({s['period']})",
            f"Worst drop    {pct(s['max_drawdown'])}"]
    if s["exposure_pct"] is not None:
        out.append(f"Exposure      {s['exposure_pct']*100:.0f}% of equity in {s['open_positions']} positions")
    t = s.get("trades")
    if t:
        out += ["", f"Closed trades {t['trades']}" + ("   ⚠ under 30: too few to judge" if t["too_few_trades"] else ""),
                f"Win rate      {pct(t['win_rate']).lstrip('+')}",
                f"Avg win/loss  {usd(t['avg_win'])} / {usd(t['avg_loss'])}",
                f"Profit factor {'n/a' if t['profit_factor'] is None else round(t['profit_factor'], 2)}"]
    if s["positions"]:
        out += ["", "Top positions"]
        for p in s["positions"][:5]:
            out.append(f"  {p['symbol']:<8}{usd(p['market_value']):>14}  {pct(p['unrealized_pct'])}")
    out += ["", "Educational only. Not financial advice."]
    return "\n".join(out)


def post(s):
    t = s.get("trades") or {}
    bits = [f"Scoreboard ({s['period']}): {pct(s['period_return'])} with a worst drop of {pct(s['max_drawdown'])}."]
    if t:
        bits.append(f"{t['trades']} closed trades, {pct(t['win_rate']).lstrip('+')} winners.")
        if t["too_few_trades"]:
            bits.append("Under 30 trades, so this proves nothing yet.")
    bits.append("Real account, real numbers, no cherry-picked window. Not financial advice.")
    return " ".join(bits)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", choices=["alpaca", "csv"], required=True)
    ap.add_argument("--file")
    ap.add_argument("--start-equity", type=float, default=10000.0)
    ap.add_argument("--period", default="1M", help="Alpaca: 1D, 1W, 1M, 3M, 1A")
    ap.add_argument("--format", choices=["block", "post", "json"], default="block")
    a = ap.parse_args(argv)
    load_env()
    if a.source == "alpaca":
        s = from_alpaca(a.period)
    else:
        if not a.file:
            die("--file is required with --source csv")
        s = from_csv(a.file, a.start_equity)
    if a.format == "json":
        print(json.dumps(s, indent=2, default=lambda x: None if isinstance(x, float) and math.isnan(x) else x))
    elif a.format == "post":
        print(post(s))
    else:
        print(block(s))


if __name__ == "__main__":
    main()
