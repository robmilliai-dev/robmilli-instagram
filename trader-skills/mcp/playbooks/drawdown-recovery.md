---
id: drawdown-recovery
title: Drawdown Recovery Plan
category: plan
summary: You're down and it hurts. A calm plan: stop the bleeding, find out what actually went wrong (system vs. you vs. market), cut size, and the exact conditions to scale back up.
---
# DRAWDOWN RECOVERY

## Ask first
1. How much are you down, from what peak, over what time? 2. Manual or bot? 3. Your normal risk per trade. 4. Your last 20 trades (or the bot's log).

## Process
1. Stop the bleeding: pause new trades for 48 hours (bots: KILL file). Not forever: 48 hours.
2. Math check: show what it takes to get back (−20% needs +25%; −50% needs +100%). Explain why size must go DOWN, not up.
3. Diagnose with their trades:
   - SYSTEM: losses within the backtest's normal worst drop and rules followed → the system is in a normal bad patch.
   - YOU: rule breaks, size creep, revenge trades → behavior problem.
   - MARKET: the conditions the system needs are gone (e.g. trend system in a choppy range) → regime problem.
4. Plan by cause: SYSTEM → half size until a new equity high; YOU → one rule + pre-trade check + half size; MARKET → pause that system or switch to watch-only until the condition returns.
5. Scale-up rule: back to normal size only after N trades (default 10) with no rule breaks and recovered half the drawdown.

## Rules
- Never suggest bigger size, leverage or a "make it back" trade.
- If they mention debt, borrowed money, or distress, say plainly: stop trading, it's okay, and suggest talking to someone they trust.
- Educational only. Not financial advice.
