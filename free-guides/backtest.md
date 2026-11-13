---
title: The 10-Minute Strategy Lie Detector
promise: Saw a trading strategy in a reel? Test it on years of real prices before you risk a dollar. Includes the prompt, the 5 checks and a starter build.
minutes: 12
nextSystemSlug: backtest-any-idea
---

# The 10-Minute Strategy Lie Detector

**"This strategy made 400%."** You've seen a hundred reels like that.

Some are real. Most are tuned until they look good. **This guide shows you how to tell which is which in about 10 minutes.**

**When you're done, you'll have:**

- ✅ A prompt that turns any strategy into a rule a computer can test
- ✅ The 5 checks that catch a fake backtest
- ✅ A real example with real numbers, so you know what "good" looks like
- ✅ A starter build prompt for Claude Code

**Why this works:** a strategy is just a rule. A rule can be run on old prices. If it only works on the years it was tuned on, it's a story, not an edge.

## Step 1: Turn the idea into a rule

Paste this into Claude. Put the strategy on the last line.

```text
Turn this trading idea into one exact rule a computer can test on daily prices.
Give me: 1) when to buy, 2) when to sell, 3) where the stop goes,
4) what you had to assume, 5) what you couldn't include (news, intraday moves).
Don't improve my idea. Don't give results. You haven't tested anything.

The idea:
```

If Claude can't make it exact, that's your first answer. **A strategy that can't be written as a rule can't be tested, and can't be trusted.**

## Step 2: The 5 checks

Ask these of any backtest, yours or someone else's.

**1. Was it graded on years it never saw?**
Tune on old years (say 2010 to 2019). Grade on new years (2020 to now). If they only show one period, assume it was tuned on it.

**2. Are there at least 30 trades?**
The famous "golden cross" on the S&P 500 fund gave **2 trades** from 2020 to 2026 in our test. Both won. That proves nothing.

**3. Are costs in, and does it buy the next day?**
A signal on today's close can't buy at today's close. An honest test buys at tomorrow's open and pays a fee.

**4. What was the worst drop?**
A result with no worst drop is half a result.

**5. How does it compare with doing nothing?**
Holding an index fund is free. A rule has to beat that on return or on worst drop.

## Step 3: See what "good" looks like

We ran one simple rule through all 5 checks: *buy when price closes above its 20-day high and is above its 200-day average. Trail the stop.*

On the S&P 500 fund (SPY), 2020 to October 2026, years the settings never saw, 1% risk per trade:

| | The rule | Just holding |
|---|---|---|
| Trades | 32 | 1 |
| Won | 47% | |
| Profit factor | 1.91 | |
| Total | +8.6% | +155% |
| Worst drop | -4.2% | -33.7% |

Read that honestly. The rule **passed**: it made money on years it never saw, with a tiny worst drop. It also made **far less than holding**. At 1% risk, it's steady, not a money printer. Anyone who shows you only the left column, or only the right one, is selling.

*Hypothetical backtest on daily bars, costs included. Not financial advice.*

## Step 4: Build a starter version

Paste this into Claude Code:

```text
Build me a small Python backtester. Keep it simple and explain each step.
- Download daily prices for SPY from Yahoo Finance (yfinance).
- Rule: buy at the next open when the close is above the highest high of the
  previous 20 days AND above the 200-day average. Stop 3 x ATR below, trailing.
- Risk 1% of the account per trade. Charge 0.05% per side.
- Print two tables: before 2020, and 2020 to now. Show trades, win rate,
  profit factor, total return, worst drop, and what holding did.
- Never use tomorrow's data to decide today.
```

That gets you one rule on one market. Good for learning.

| | Starter (free) | Finished kit |
|---|---|---|
| Rules | 1, typed into the code | Any idea, from plain English |
| Markets | 1 | Anything on Yahoo Finance, many at once |
| Grade | You read the numbers | HELD UP, WEAK, FAILED or NOT ENOUGH TRADES |
| Counts your tries | No | Yes |
| No-peeking self-test | No | Yes |
| Setup | You debug it | One command |

> Educational only. Not financial advice. Past results never promise future ones.

## Want it done for you?

You just did it once, by hand. **The finished Backtest Any Idea kit tests any idea you type, on any market, and hands you a plain grade in about a minute.**

We already did the hard part. We built it. We tested it. We wrote every step. **Your part: follow the setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished Backtest Any Idea kit**, tested and ready to run
- ✅ **11 finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **Bots in your inbox for 3 months:** a morning email with what our 5 tested bots see on your markets. Nothing to install
- ✅ **The Milli Indicator Pack** for TradingView: paste it and see the dots on your chart in 2 minutes
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **Every new bot we release, free for 12 months**

**Total value: $2,175. You pay $199. Once.**

**The price goes up to $349 on December 1.** Same bots, same files.

**Our promise:** Follow the steps. If it isn't running in 7 days, email support@milli-ai.com and we'll set it up with you. Still not running? You get every dollar back, and you keep the files anyway.

**[Yes! Give me the finished tester for $199 →]({{offerUrl}})**
