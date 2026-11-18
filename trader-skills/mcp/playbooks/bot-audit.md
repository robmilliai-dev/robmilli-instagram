---
id: bot-audit
title: The Bot Audit skill
category: build
summary: Six blind reviewers audit a trading bot before it touches money: backtest honesty, risk and kill switches, order bugs, leaked keys, data timing, overfitting. Findings JSON + plain report + verified fixes.
---

# BOT AUDIT

The backtest said +300%. This finds out whether the bot or the backtest is lying, before your account does.

## WHEN TO RUN

- Before any bot goes live, even on a small account
- After you download a bot from anyone (including us)
- After an AI rewrote part of your bot
- When live results don't look like the backtest

## STEP 0: MAP THE BOT (5 minutes)

Read the whole folder first. Write `audit/MAP.md`: entry point, data source, signal logic, order placement, risk checks, config, where keys come from, schedule. If you can't find where orders are placed, stop and say so. That's finding #1.

## STEP 1: SIX BLIND REVIEWERS

Run each lens as a separate pass (subagents if available, otherwise one after another with a fresh read). A reviewer does not see the others' findings. Each one writes `audit/lens-<n>.json`.

| # | Lens | Hunts for |
|---|---|---|
| 1 | **Backtest honesty** | Uses today's close to trade today's close. Indicators computed on the full series then sliced. `shift()` missing or wrong. Survivorship (today's index members tested on 2015). No fees or slippage. Fills at the exact high/low. |
| 2 | **Risk and kill switches** | No max loss per day. No max position size. Size not capped by account equity. No kill switch file or flag. Retries that double an order. Stop loss only in the backtest, not live. Leverage set by default. |
| 3 | **Orders and broker** | Market orders outside trading hours. Partial fills ignored. Order status never checked. Quantity rounding that buys 10x. Wrong symbol format per broker. Paper/live URL mixed up. No idempotency (rerun = duplicate orders). |
| 4 | **Secrets and security** | API keys in code, notebooks, logs or git history. Keys with withdrawal permission. `.env` not in `.gitignore`. Webhook endpoint with no secret. Prints full account responses. |
| 5 | **Data and timing** | Time zones (UTC vs. exchange time). Missing bars treated as zero. Stale data used silently when the feed fails. Daylight saving shifts. Crypto 24/7 vs. stocks 9:30 to 16:00 ET. Splits and dividends unadjusted. |
| 6 | **Overfitting** | Parameters tuned on all years with nothing held back. Dozens of parameters for few trades. Fewer than 30 trades. Results only on one market. Magic numbers with no reason (e.g. RSI 37). |

## FINDING FORMAT (every lens, no exceptions)

```json
{
  "id": "L2-03",
  "lens": "risk",
  "file": "bot/live.py",
  "line": 88,
  "severity": "critical | high | medium | low",
  "title": "No daily loss limit in live loop",
  "failure_scenario": "Feed returns a bad tick at 10:02; signal fires 40 times; bot buys 40 x 100 shares with no stop and no daily cap.",
  "money_at_risk": "whole account",
  "fix": "Track realized + unrealized P&L since 00:00 ET; if below -2% of start-of-day equity, cancel open orders, flatten, write KILL file, exit.",
  "verify": "Unit test: simulate -2.1% day, assert flatten() called and no new orders after."
}
```

**No failure scenario, no finding.** "Could be better" is not a finding. Cut it.

## STEP 2: MERGE AND VERIFY

1. Merge the six files, dedupe (same file+line+cause = one finding, keep the clearest).
2. Re-read the code for every critical and high finding. If the scenario can't actually happen, drop it and say why.
3. Write `audit/findings.json` (machine) and `audit/REPORT.md` (human).

## REPORT.md (plain English)

```
VERDICT: DO NOT RUN LIVE | FIX FIRST | OK FOR SMALL SIZE
(one sentence why)

Critical (could lose the account)
1. <title>: <one-line scenario> → <one-line fix>

High (could lose a week of gains)
...

What's good (keep it)
- ...

The backtest: HONEST | PROBABLY INFLATED | CAN'T TELL (and why)
```

Rank by money at risk, not by how clever the bug is.

## STEP 3: FIX PHASE (only if asked)

- Fix one finding at a time, critical first.
- After each fix, run its `verify` step. Paste the result.
- Status is one of: `fixed (verified)`, `fixed (not verified: <why>)`, `not fixed`. **Never write "fixed" without a verify result.**
- Re-run lens 1 after any change to signal code. Backtest numbers usually drop after honest fixes. Say so, and say that's good news.

## HARD RULES

- **Never run the bot live during an audit.** Paper or offline only.
- **Never print a key you find.** Write "key found at file:line, rotate it now".
- **Never call a bot safe.** Best verdict is "OK for small size", with the list of what was checked.
- Educational only. Not financial advice.
