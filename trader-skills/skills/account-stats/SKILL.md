---
name: account-stats
description: Pull a trader's real account numbers (equity, today's P&L, period return, worst drop, exposure, open positions, win rate, profit factor) from Alpaca's API or any broker's CSV export, and return them as a scoreboard block, a short honest post, or JSON. Read-only. Knows the traps that make account stats lie.
argument-hint: "[alpaca | csv <file>] [block | post | json]"
---

# ACCOUNT STATS

Your real scoreboard in 5 seconds, not the one your memory keeps.

## WHY THIS EXISTS

Traders remember wins and forget the worst drop. Broker apps show today's P&L in green and hide the max drawdown three menus deep. This skill puts the numbers that matter on one screen, the same way every week, so you can't fool yourself.

## RUN IT

```bash
# Alpaca (paper or live). Read-only calls only.
python scripts/account_stats.py --source alpaca --period 1M

# Any broker: export closed trades as CSV (needs a P&L column)
python scripts/account_stats.py --source csv --file trades.csv --start-equity 5000

# As a post or as JSON for another tool
python scripts/account_stats.py --source csv --file trades.csv --format post
python scripts/account_stats.py --source alpaca --format json
```

## HOW TO USE THE OUTPUT

- **block**: the weekly scoreboard. Paste it into your journal or the `/trading-plan` scoreboard section.
- **post**: one honest paragraph for X, Threads or a Discord. Includes the worst drop and the trade count, always.
- **json**: feed it to another skill (`/trade-recap`, `/equity-video`) or a dashboard.

When the user asks "how am I doing?", run the block, then say in 3 lines: what's working, the one number that worries you, and the one rule to check this week.

## SETUP (once)

1. `cp .env.example .env`
2. Alpaca: make a key in the dashboard. **Use paper keys first.** Set `ALPACA_PAPER=true` for paper, `false` for live.
3. CSV: export "closed trades" or "realized P&L" from your broker. The script finds a column named pnl, p&l, realized_pnl, profit or gain/loss. If yours is named something else, rename it to `pnl`.
4. Python 3.8+. No packages needed.

## GOTCHAS (the traps that make stats lie)

- **Paper keys on the live URL fail with 401.** `ALPACA_PAPER` must match the key type.
- **Deposits look like profit.** Alpaca's portfolio history counts a deposit as an equity jump. If the return looks too good, check for a deposit that week and say so.
- **Under 30 closed trades proves nothing.** The script flags it. Repeat the flag in any summary.
- **Win rate alone is a lie.** 80% winners with tiny wins and one huge loss is a losing system. Always show average win vs. average loss next to it.
- **Unrealized P&L is not profit.** Keep open positions separate from closed-trade stats.
- **Pick the period before you look.** Never shorten the window to make the number prettier. The post format says "no cherry-picked window" because it's a rule, not a slogan.
- **CSV money formats vary.** "(125.40)" means -125.40. The script handles $, commas and brackets.

## HARD RULES

- Read-only. Never call any endpoint that creates, changes or cancels orders.
- Never print or log API keys. Never write them into a script.
- Never post the account number or exact balance publicly unless the user says to. Default post shows percentages only.
- Educational only. Not financial advice.

## PAIRS WITH

`/trading-plan` (weekly scoreboard), `/trade-recap` (turn the week into a post), `/equity-video` (animate the curve).
