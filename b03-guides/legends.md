---
title: The Legends Algo Playbook
promise: Turn the ideas behind Buffett, Lynch, Dalio, Soros and Simons into five rule sets you can actually test, in Python, with Claude writing the code. One script, one test harness, about 30 minutes, $0.
minutes: 30
nextSystemSlug: ai-trading-desk-247
---

# The Legends Algo Playbook

Most people "learn from the legends" by reading quotes. Quotes don't trade. Rules do.

This playbook turns five famous investing styles into five rule sets a computer can follow, then runs every one of them through the **same** honest test: trading costs included, no peeking at tomorrow's price, and a final exam on years the rules have never seen. In about 30 minutes you'll know which ideas survive contact with real data and which only sound smart.

You need: a free [Claude](https://claude.ai/) account, Python 3.10+ (or a free [Google Colab](https://colab.research.google.com/) notebook, nothing to install), and this file.

> These rule sets are *inspired by* each investor's public philosophy. They are simplified teaching models, not the investors' actual strategies, and nobody named here endorses this guide.

## Minutes 0–5: set up

In Colab (or your terminal) run:

```bash
pip install yfinance pandas numpy
```

Then paste the full script at the bottom of this guide into a cell or a file called `playbook.py` and run it. It downloads free daily prices for SPY, TLT, GLD and DBC from Yahoo Finance and prints a scorecard for each idea.

## Minutes 5–20: the five legends as rules

### 1. Buffett: quality at a fair price
**The idea:** wonderful businesses, little debt, don't overpay.
**The rules:** return on equity above 15%, debt-to-equity under 0.5, P/E under 25, free-cash-flow margin above 10%. Rank survivors by ROE.
**What the code does:** `buffett_screen()` filters a table of fundamentals. Get the numbers from each company's latest 10-K or a free screener (Finviz, Yahoo) and write down the date you pulled them.

### 2. Lynch: growth at a reasonable price
**The idea:** buy companies growing fast whose price hasn't caught up.
**The rule:** PEG ratio (P/E ÷ earnings-growth %) under 1, with growth above 15% a year.
**What the code does:** `lynch_screen()` computes PEG and sorts from cheapest growth to most expensive.

### 3. Dalio: balance the risk, not the dollars
**The idea:** stocks, bonds, gold and commodities each carry a different amount of risk, so give each one a similar *risk* budget.
**The rule:** weight each asset by 1 ÷ its recent volatility.
**What the code does:** `risk_parity_weights()` uses the last 63 trading days (about 3 months) and returns weights that add to 100%. Rebalance monthly.

### 4. Soros: ride the feedback loop
**The idea:** reflexivity. Rising prices change behavior, which pushes prices further until the loop breaks.
**The rule:** be invested when the 6-month return (skipping the most recent month) is positive; otherwise sit in cash.
**What the code does:** `momentum_signal()` returns 1 (in) or 0 (out) every day.

### 5. Simons: let the numbers decide
**The idea:** small, repeatable statistical edges, executed without emotion.
**The rule:** inside an uptrend (price above its 200-day average), buy when 2-day RSI drops below 10; sell when it climbs above 70 or the uptrend breaks.
**What the code does:** `mean_reversion_signal()` tracks the position day by day.

## Minutes 20–27: the test every idea has to pass

`backtest()` is the referee, and it is strict on purpose:

- **Trades happen on the next bar.** A signal computed from today's close is traded tomorrow. Skip this and your backtest is fiction.
- **Costs are charged on every trade** (`COST = 0.001`, i.e. 0.10% per side). Set it to your broker's real number.
- **It reports the ugly stuff first:** max drawdown and trade count sit next to the return, and buy-and-hold is printed beside every result so you can see if the "strategy" beat doing nothing.

`split_test()` builds on data before 2021 and then grades the rules on 2021 onward. **Judge an idea by its out-of-sample column, not the in-sample one.** If it only works on the years you tuned it on, it doesn't work.

## Minutes 27–30: make Claude your quant intern

Paste the script into Claude with this prompt:

```text
You are my quant research assistant. Here is my backtest script. Do not change backtest() or split_test(): costs, next-bar execution and the out-of-sample split stay exactly as written.
1. Explain in plain English what each signal function does and one way it could fail.
2. Write ONE new signal function for this idea: [describe your rule in one sentence].
3. List every assumption your function makes.
4. Tell me which number in the output I should look at first, and why.
Never invent results. If you have not run the code, say "not run".
```

Run what it writes. Compare the out-of-sample row with buy-and-hold. Change one thing at a time, and write each change down. Twenty tweaks until something looks great is how people fool themselves (it's called overfitting).

> **Before you rely on this:** Educational only, not financial advice. A backtest is a simplified history lesson: it can't model every cost, gap or liquidity problem, and no strategy works forever. Test with small size first; you make every decision.

## The full script

```python
"""The Legends Algo Playbook: five rule sets inspired by five famous investors.
Educational code. Not financial advice. Needs: pip install yfinance pandas numpy
"""
import numpy as np
import pandas as pd

COST = 0.001  # 0.10% per side for commissions + slippage. Change to your broker's real cost.

def get_prices(tickers, start="2015-01-01"):
    import yfinance as yf
    px = yf.download(tickers, start=start, auto_adjust=True, progress=False)["Close"]
    return px.to_frame() if isinstance(px, pd.Series) else px

# 1. BUFFETT-STYLE QUALITY SCREEN: good business, sane debt, fair price.
def buffett_screen(f: pd.DataFrame) -> pd.DataFrame:
    """f has one row per ticker with columns roe, debt_to_equity, pe, fcf_margin."""
    keep = (f.roe > 0.15) & (f.debt_to_equity < 0.5) & (f.pe < 25) & (f.fcf_margin > 0.10)
    return f[keep].sort_values("roe", ascending=False)

# 2. LYNCH-STYLE GROWTH AT A REASONABLE PRICE: PEG under 1.
def lynch_screen(f: pd.DataFrame) -> pd.DataFrame:
    """f has columns pe, eps_growth (0.20 = 20% a year)."""
    f = f.assign(peg=f.pe / (f.eps_growth * 100))
    return f[(f.eps_growth > 0.15) & (f.peg < 1.0)].sort_values("peg")

# 3. DALIO-STYLE RISK PARITY: each asset contributes similar risk.
def risk_parity_weights(px: pd.DataFrame, lookback=63) -> pd.Series:
    vol = px.pct_change().tail(lookback).std() * np.sqrt(252)
    w = 1 / vol
    return (w / w.sum()).round(4)

# 4. SOROS-STYLE MOMENTUM (reflexivity: trends feed on themselves until they break).
def momentum_signal(close: pd.Series, lookback=126, skip=21) -> pd.Series:
    """1 = in the market, 0 = in cash. 6-month return, skipping the last month."""
    mom = close.shift(skip) / close.shift(lookback) - 1
    return (mom > 0).astype(int)

# 5. SIMONS-STYLE MEAN REVERSION: buy short-term oversold inside an uptrend.
def mean_reversion_signal(close: pd.Series, rsi_len=2, buy_below=10, exit_above=70) -> pd.Series:
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1 / rsi_len, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / rsi_len, adjust=False).mean()
    rsi = 100 - 100 / (1 + up / dn.replace(0, np.nan))
    uptrend = close > close.rolling(200).mean()
    pos, out = 0, []
    for r, t in zip(rsi.fillna(50), uptrend):
        if pos == 0 and t and r < buy_below:
            pos = 1
        elif pos == 1 and (r > exit_above or not t):
            pos = 0
        out.append(pos)
    return pd.Series(out, index=close.index)

# THE TEST HARNESS: same backtest for every idea, costs included, no look-ahead.
def backtest(close: pd.Series, signal: pd.Series) -> dict:
    pos = signal.shift(1).fillna(0)          # trade on the NEXT bar, never the same one
    ret = close.pct_change().fillna(0)
    trades = pos.diff().abs().fillna(0)
    strat = pos * ret - trades * COST
    eq = (1 + strat).cumprod()
    yrs = len(close) / 252
    dd = (eq / eq.cummax() - 1).min()
    sharpe = strat.mean() / strat.std() * np.sqrt(252) if strat.std() > 0 else 0.0
    return {
        "cagr": round(float(eq.iloc[-1] ** (1 / yrs) - 1), 4),
        "max_drawdown": round(float(dd), 4),
        "sharpe": round(float(sharpe), 2),
        "trades": int(trades.sum()),
        "buy_and_hold_cagr": round(float((close.iloc[-1] / close.iloc[0]) ** (1 / yrs) - 1), 4),
    }

def split_test(close: pd.Series, signal_fn, split="2021-01-01") -> dict:
    """Build on the past, judge on data the rules have never seen."""
    sig = signal_fn(close)
    return {"in_sample": backtest(close[:split], sig[:split]),
            "out_of_sample": backtest(close[split:], sig[split:])}

if __name__ == "__main__":
    spy = get_prices("SPY")["SPY"]
    print("Momentum:", split_test(spy, momentum_signal))
    print("Mean reversion:", split_test(spy, mean_reversion_signal))
    print("Risk parity weights:", risk_parity_weights(get_prices(["SPY", "TLT", "GLD", "DBC"])).to_dict())
```

## The next problem

You now have five ideas and a fair test. The hard part is running it every day without babysitting it: watching the market, reading the chart, arguing the trade, and sizing the risk before you click anything. **Solo Trader's AI Desk** gives you all four systems that do that: AI Trading Desk 24/7, TradingView + Claude Chart Analyst, the six-role AI Hedge Fund Blueprint and the Free Bloomberg Terminal Setup, plus 20 bonus systems. $1,166 combined listed value. Your price: $199 until Dec 1, 2026, then $349. Follow Live-in-60; not running in 7 days? Email support@milli-ai.com for a full refund and keep your downloads. [Get your complete trading AI desk]({{offerUrl}}).
