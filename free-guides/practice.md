---
title: The Free Prop Challenge Practice Run
promise: Before you pay a challenge fee, find out if your trading could pass. The risk table, the 8 questions to ask any firm and the daily stop rule.
minutes: 12
nextSystemSlug: prop-challenge-practice-kit
---

# The Free Prop Challenge Practice Run

**Most people who buy a prop challenge blow it.** Usually not because the idea was bad. They risked too much, or pushed on a bad day.

A challenge fee is real money. **This guide lets you practice first, for free.**

**When you're done, you'll have:**

- ✅ The one table that shows why fast and safe pull in opposite directions
- ✅ A simple way to pick your risk per trade
- ✅ 8 questions to ask any firm before you pay
- ✅ A daily stop rule that takes 30 seconds

**Why this works:** a challenge is math. Target, max loss, daily loss. Your trades either fit inside those lines at a given risk size, or they don't. You can check that before you pay.

*We are not affiliated with any prop firm. Everything here is practice and education.*

## Step 1: Look at this table

We took one simple trend rule on 8 markets (Bitcoin, SPY, Costco, DIA, Apple, Tesla, S&P futures, gold futures). 227 trades, 2020 to October 2026. They won 48% of the time, with 8 losses in a row at one point.

Then we started a new practice challenge every month (+10% target, 10% max loss, 5% daily loss, no time limit) at five risk sizes:

| Risk per trade | Challenges | Passed | Blown | Still running | Median days to pass |
|---|---|---|---|---|---|
| 0.25% | 69 | 41 | 0 | 28 | 679 |
| 0.5% | 69 | 47 | 0 | 22 | 405 |
| 1.0% | 69 | 53 | 0 | 16 | 164 |
| 1.5% | 69 | 57 | 1 | 11 | 130 |
| 2.0% | 69 | 56 | 5 | 8 | 82 |

Same trades every row. Only the risk changed.

At 2%, passes came twice as fast, and 5 accounts died. At 1%, zero died, and the median pass took about 5 months. **Slow is the price of safe.** Anyone promising a pass in a week is selling you the bottom row without the Blown column.

*Hypothetical. Trades counted on the day they closed, so real results would be a bit worse. Not financial advice.*

## Step 2: Pick your risk

1. List your last 30 trades as R. Lost what you planned to risk: -1. Made twice that: +2.
2. Find your longest losing streak.
3. **Longest streak x your risk should be under half the max loss.**

Example: 8 losses in a row, 10% max loss. Half is 5%. So 5% / 8 = about 0.6% per trade. Round down to 0.5%.

Don't have 30 trades? Then you don't have a challenge-ready method yet. That's worth knowing before you pay.

## Step 3: Ask the firm 8 questions

1. What's the target for each step?
2. Is the max loss fixed, or does it trail up as I make money?
3. What's the daily loss, and does it count open trades?
4. What time does the day reset?
5. Is there a time limit?
6. Can I hold overnight and over the weekend?
7. Is there a consistency rule (no single day over X% of my profit)?
8. What does a retry cost?

Paste the firm's rules page into Claude with this:

```text
Here is a prop firm's rules page. List: target per step, max loss (fixed or
trailing, on balance or equity), daily loss (does it count open trades?),
reset time, time limit, overnight/weekend rules, consistency rule, retry cost.
If the page doesn't say, write "not stated, ask support". Don't guess.
```

## Step 4: The 30-second daily stop rule

Before you trade, work out two numbers:

- **Room today** = balance at the start of today, minus the daily loss, minus where you are now.
- **Room overall** = balance now, minus the max loss line.

Take the smaller one. If it's less than **1.5 losses** at your risk size, you're done for the day. And whatever the numbers say: **two losses in a row, close the platform.**

## Step 5: Build a starter simulator

Paste into Claude Code:

```text
Build a small Python script. It reads a CSV with columns date_out and R.
Starting on the first day of each month, simulate a challenge: start at 100,
add R x risk% for each trade in date order. Pass at +10. Fail at -10 total
or -5 in one day. Run it for risk = 0.25, 0.5, 1, 1.5 and 2.
Print passed, blown, still running and median days to pass for each.
```

| | Starter (free) | Finished kit |
|---|---|---|
| Firm rules | One fixed set | Any: trailing loss, two steps, time limits |
| Verdict | You read the table | Tells you the highest risk with zero blown |
| Daily guard rail | By hand | One command: TRADE, HALF SIZE or STOP FOR TODAY |
| Sample trades to learn on | No | 227 included |
| Tracker and weekly review | No | Included |

> Educational only. Not financial advice. Past results never promise future ones.

## Want it done for you?

You just did it once, by hand. **The finished Prop Challenge Practice Kit runs any firm's rules against your trades and tells you your risk number, then checks your room every morning with one command.**

We already did the hard part. We built it. We tested it. We wrote every step. **Your part: follow the setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished Prop Challenge Practice Kit**, tested and ready to run
- ✅ **11 finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **Bots in your inbox for 3 months:** a morning email with what our 5 tested bots see on your markets. Nothing to install
- ✅ **The Milli Indicator Pack** for TradingView: paste it and see the dots on your chart in 2 minutes
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **Every new bot we release, free for 12 months**

**Total value: $2,175. You pay $199. Once.**

**The price goes up to $349 on December 1.** Same bots, same files.

**Our promise:** Follow the steps. If it isn't running in 7 days, email support@milli-ai.com and we'll set it up with you. Still not running? You get every dollar back, and you keep the files anyway.

**[Yes! Give me the finished practice kit for $199 →]({{offerUrl}})**
