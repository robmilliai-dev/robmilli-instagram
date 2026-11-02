---
title: The ARENA Playbook Blueprint
promise: An AI beat ChatGPT, Claude, Gemini and Grok in a real-money trading contest: +22% in 17 days. I rebuilt its playbook as a 4-agent team. Here's how it works and a free prompt to run it in 10 minutes.
minutes: 10
nextSystemSlug: arena-trading-team
---

# The ARENA Playbook Blueprint

**An AI beat ChatGPT, Claude, Gemini and Grok in a real-money trading contest. +22% in 17 days.**

In Nof1's Alpha Arena (Season 1, fall 2025), six top AIs each got $10,000 of real money to trade crypto on their own. Qwen 3 Max finished first, up 22.3%. *(Those are Nof1's reported results from one short contest, not mine. One contest doesn't predict the future.)*

The winner didn't win by being smarter. **It won by being more disciplined.** I rebuilt its playbook as a team of 4 AIs. This guide shows you how it works. You'll run it free in 10 minutes. The finished bot is at the end.

**When you're done, you'll have:**

- ✅ The winner's 4 habits, in plain English
- ✅ A free prompt that runs the 4-agent team on any crypto chart
- ✅ A clear answer: **READY FOR YOUR REVIEW** or **BLOCKED BY RISK**

**Why this works:** Here's what the winner did differently:

| The winner | The rest |
|---|---|
| Made the fewest trades | Traded way too often and paid big fees |
| Only took high-confidence setups | Chased hype and headlines |
| A stop and a target on every trade | No stops, or stops that moved |
| Simple signals: MACD + RSI | Overthought it |

Those habits are easy to copy. That's what this team does.

## Try it now: 10 minutes, no code

1. Open any crypto chart in [TradingView](https://www.tradingview.com/chart/) (free) on the **1-hour** timeframe.
2. Add 3 indicators: **MACD**, **RSI** and **EMA 50**.
3. Copy the numbers into [Claude](https://claude.ai/) with this:

```text
You are a 4-person crypto trading team. You copy the Alpha Arena winner:
few trades, high confidence only, a stop and target on every trade.
You never place trades.

COIN: [e.g. ETH]   PRICE: [ ]   EMA 50: [ ]   RSI: [ ]
Did MACD just cross? [up / down / no]
Trades I already took today: [ ]   My account: $[ ]

1. SIGNAL: LONG only if MACD just crossed up, RSI is 40-65 and price
   is above EMA 50. SHORT only if MACD crossed down, RSI is 35-60 and
   price is below EMA 50. Otherwise say "NO SETUP" and stop.
2. JUDGE: Score it 0-100. Set a stop where the idea is clearly wrong
   and a target at least 1.5x as far away.
3. RISK: Pass or fail: score 70+, reward at least 1.5x risk, fewer
   than 3 trades today. Any fail = BLOCKED. If it passes, size it so
   hitting the stop loses only 1% of my account.
4. JOURNAL: "READY FOR YOUR REVIEW" or "BLOCKED BY RISK: [why]".
   End with "Nothing has been placed. You decide."
Only use my numbers. Never make up prices.
```

**NO SETUP and BLOCKED will be the most common answers.** That's the whole lesson. The winner waited.

## How each agent works

1. **SIGNAL** checks Bitcoin, Ethereum and Solana every hour (free data). It only looks for the two setups above. No setup? No AI call, no cost.
2. **JUDGE** is Claude. It scores the setup and sets the stop and target. It's told to skip when in doubt.
3. **RISK** is plain code. The AI can't argue with it. Score under 70, bad stop, small reward, or 3 trades already today? Blocked. Every trade is sized so a loss costs just 1%.
4. **JOURNAL** saves every idea and texts the ticket to your phone.

After a month, the log shows if the high-scoring trades really did better. That's how you tune it.

**To build it yourself,** you'd pull hourly prices in Python, calculate MACD, RSI and the EMA, connect Claude, write the risk rules, set up phone texts and run it every hour. An evening if you code.

> Educational only. Not financial advice. Crypto moves fast and you can lose money.

## Want it done for you?

You just did it once, by hand. **The finished ARENA desk does it for you every hour, on Bitcoin, Ethereum and Solana, with the winner's discipline built in. Only the trades that pass every rule reach your phone.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished ARENA desk**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, JARVIS, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst, the Hedge Fund Committee and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished ARENA desk for $199 →]({{offerUrl}})**
