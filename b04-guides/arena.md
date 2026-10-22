---
title: The ARENA Playbook Blueprint
promise: Six AIs got $10,000 of real money to trade, and four lost it. Here's what the winner did differently, how my 4-agent rebuild of that playbook works, how to build it, and a free prompt that runs the whole team in a Claude chat in 10 minutes.
minutes: 10
nextSystemSlug: arena-trading-team
---

# The ARENA Playbook Blueprint

In Nof1's Alpha Arena (Season 1, October 18 to early November 2025), six AI models each got $10,000 of real money and traded crypto on their own for about 17 days. Same money, same data, no humans.

The reported results: Qwen 3 Max finished +22.3% and DeepSeek +4.9%. The other four lost roughly 30% to 60% each. Those are Nof1's reported numbers from one short contest, not mine, and one contest proves nothing about the future.

What stood out wasn't who predicted best. It was who **behaved** best:

| The 4 that lost | The winner |
|---|---|
| Traded far too often (one reportedly made 200+ trades and paid heavy fees) | Made the fewest trades |
| Chased hype and headlines | Only took high-confidence setups |
| No stops, or stops that moved | A stop and a target on every trade |
| All in one direction | Simple signals: MACD + RSI |

I rebuilt that playbook as a team of 4 AIs. This guide shows how it works and how to build it yourself. If you'd rather skip the build, the finished, tested bot is at the end.

**SIGNAL → JUDGE → RISK → JOURNAL**

It never places a trade. It sends you a ticket that ends in **READY FOR YOUR REVIEW** or **BLOCKED BY RISK**, and you decide.

Educational only, not financial advice. Crypto and leverage can lose you money fast.

## Try it in 10 minutes, no code

Open any chart (TradingView's free plan is fine) on the 1-hour timeframe and add the MACD, RSI and a 50 EMA. Copy the numbers into a new [Claude](https://claude.ai/) chat with this prompt:

```text
You are a 4-person crypto trading desk built on the Alpha Arena winner's habits:
few trades, high confidence only, a stop and a target on every trade. You never place trades.
Educational only.

COIN: [e.g. ETH]   TIMEFRAME: 1h   PRICE: [ ]   50 EMA: [ ]
RSI(14): [ ]   MACD line: [ ]   MACD signal: [ ]   Did MACD just cross? [up/down/no]
ATR(14) if you have it: [ ]   Trades I've already taken today: [ ]
My account: $[ ]

1. SIGNAL: is there a setup? LONG only if MACD just crossed up, RSI 40-65 and price is above
   the 50 EMA. SHORT only if MACD just crossed down, RSI 35-60 and price is below the 50 EMA.
   Otherwise say "NO SETUP" and stop.
2. JUDGE: score the setup 0-100. 70+ only if trend, momentum and price action all agree.
   Set a stop where the idea is clearly wrong (about 1-2 ATR) and a target at least 1.5x as far.
3. RISK: PASS/FAIL on: confidence at least 70, stop on the correct side, stop 0.5-3 ATR away,
   reward:risk at least 1.5, fewer than 3 trades today. Any FAIL = BLOCKED.
   If it passes, size it so hitting the stop loses 1% of my account, and never above 3x leverage.
4. JOURNAL: one ticket. "READY FOR YOUR REVIEW" or "BLOCKED BY RISK: <checks>".
   End with: "Nothing has been placed. You decide."
Use only the numbers I gave you. Never invent prices.
```

**NO SETUP and BLOCKED will be the most common answers.** That's the whole lesson of the arena: the AIs that kept trading lost.

## How each agent works (the build blueprint)

This is everything you need to build the automated version yourself in Python.

**01 SIGNAL finds the setup (plain code, no AI).** Pull hourly candles for BTC, ETH and SOL from Hyperliquid's free public data endpoint (`POST https://api.hyperliquid.xyz/info` with type `candleSnapshot`). Calculate four things from the closes:
- **MACD** (12, 26, 9): the 12 EMA minus the 26 EMA, plus a 9 EMA of that line as the signal.
- **RSI** (14) with Wilder smoothing.
- **50 EMA** for the trend.
- **ATR** (14) for how far price normally moves in an hour.

Only two setups count: MACD crossing up with RSI 40-65 above the 50 EMA (LONG), or crossing down with RSI 35-60 below it (SHORT). No setup means no AI call, so most hours it costs nothing.

**02 JUDGE scores it (Claude).** Send Claude the setup and the last 24 closes, and ask for structured JSON: `decision` (TAKE or SKIP), `confidence` (0-100), `stop`, `target` and a one-line `reason`. Tell it most setups aren't worth taking and to SKIP when in doubt. That one instruction is the difference between the winner and the losers.

**03 RISK enforces the rules (plain code).** The rules outrank the AI. Block the trade if any of these fail:

| Check | Default |
|---|---|
| JUDGE says TAKE | required |
| Confidence | at least 70 |
| Stop | on the correct side of price |
| Stop distance | 0.5 to 3 ATR |
| Reward : risk | at least 1.5 |
| Trades today | fewer than 3 |

Sizing: divide 1% of your account by the distance to the stop. That's how many coins you can hold so a stopped-out trade costs exactly 1%. Then cap the position at 3x your account.

**04 JOURNAL logs everything.** Write one row per idea to a CSV (time, coin, side, price, confidence, stop, target, passed or blocked, and why). Send the ticket to Telegram so it reaches your phone. The trade counter for "max 3 a day" reads from this log.

**Run it every hour** with a cron job or any scheduler. After a month, open the log and check: did the trades JUDGE scored 80+ do better than the ones scored 70-79? That's how you tune it.

## Want the finished bot?

Building this takes an evening if you code. If you don't, the finished, tested ARENA bot is in the **AI Desk**: all 4 agents wired up, one-command install, step-by-step setup, Telegram alerts and the trade journal, with clear instructions from zero to your first ticket.

Every free guide we release, including this one, is also included as a bonus inside the AI Desk.
