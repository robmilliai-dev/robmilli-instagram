---
title: The ARB Bot Gap-Finder Blueprint
promise: A Polymarket bot reportedly turned $1 into $3.3 million by comparing prices, not predicting games. I rebuilt it for you. Here's how it works, how to build it, and a free prompt to check any game in 10 minutes.
minutes: 10
nextSystemSlug: arb-gap-finder
---

# The ARB Bot Gap-Finder Blueprint

**A Polymarket bot reportedly turned $1 into $3.3 million.**

*(That's a viral claim from a video on X, not my result, and nobody has checked it independently.)*

Here's the wild part: **it doesn't predict games. It compares prices.**

I rebuilt the idea from scratch and tested it. This guide shows you exactly how it works. You'll check a real game free in 10 minutes. The finished bot is at the end.

**When you're done, you'll have:**

- ✅ A free prompt that checks any game for a price gap
- ✅ A clear answer: **READY FOR YOUR REVIEW** or **BLOCKED BY RISK**
- ✅ The full plan for the automatic bot

**How it works:** Same game, two prices → strip the bookie's cut → find the gap → Claude checks the fine print → risk kills most → you decide

> **READ FIRST:** Gaps are rare and close fast. Most checks end in "no bet", and that's the system working. Check that prediction markets are legal where you live.

**Why this works:** Big sportsbooks set their odds with huge amounts of money and data. Polymarket prices come from whoever happens to be trading that minute. When the two disagree on the same game, Polymarket is usually the one that's off. That gap is the opportunity.

## Try it now: 10 minutes, no code

1. Pick one upcoming game.
2. Look up the moneyline odds for both teams on 2 or 3 sportsbooks. Any odds comparison site shows them side by side.
3. Open the same game on Polymarket. Copy both prices and the **Rules** text.
4. Paste it all into [Claude](https://claude.ai/) with this:

```text
You are a 4-agent price checker for ONE game. You never place bets.

GAME: [Team A] vs [Team B], starts [date/time]
SPORTSBOOK ODDS: Book 1: [A] / [B]   Book 2: [A] / [B]   Book 3: [A] / [B]
POLYMARKET: [A] [price]¢ / [B] [price]¢
POLYMARKET RULES: [paste rules]
MY BANKROLL: $[ ]

1. MATH: Turn each book's odds into a % chance. Remove the bookie's cut
   so both sides add up to 100%. Average the books. Show the fair % per team.
2. GAP: Fair % minus Polymarket price, for each team. Which side is cheap?
3. FINE PRINT: Is the Polymarket bet the SAME bet as the sportsbook?
   Same teams, same date, does overtime count? Any difference = MISMATCH.
4. RISK: Pass or fail: gap of 4+ points, fine print matches, 3+ books.
   Any fail = BLOCKED. If it passes, bet no more than 2% of my bankroll.
   End with "READY FOR YOUR REVIEW" or "BLOCKED BY RISK: [why]",
   then "Nothing has been placed. You decide."
Only use my numbers. Never make up odds.
```

**BLOCKED will be the most common answer.** Most of the time the prices agree. The bot waits for the times they don't.

## How each agent works

1. **WATCHER** pulls the odds from the sportsbooks (The Odds API has a free plan) and the prices from Polymarket (free public data), and matches up the same games.
2. **MATH** removes the bookie's cut and works out the fair price. No AI needed. Just math.
3. **CLAUDE** reads the fine print. This is where most "gaps" turn out to be fake. For example, a bet that ignores overtime isn't the same bet as one that counts it.
4. **RISK** blocks anything that fails a check: gap too small, not enough money in the market, odds too old, or fine print doesn't match. It keeps every bet small.

Every ticket goes to your phone and into a log. After a month, the log shows if the gaps were real.

**To build it yourself,** you'd connect both price feeds in Python, match team names across two sites, write the math, call Claude for the fine print, set up phone texts, and run it every few minutes on game days. A weekend if you code.

> Educational only. Not financial advice. Fast pro bots close most gaps quickly. Check that sports prediction markets are legal where you live.

## Your first run checklist

- [ ] You checked one real game with the free prompt
- [ ] You worked out the fair price without the bookie's cut
- [ ] You got a clear BET or NO BET with the reason

## Troubleshooting

| Problem | Fix |
|---|---|
| The odds look different in different places | Use odds from the same minute. Old odds make fake gaps. |
| The gap is under 4 points | Skip it. Small gaps are usually eaten by fees and slippage. |
| The rules don't match (overtime, dates) | Not a real gap. Skip it. |

## Want it done for you?

You just did it once, by hand. **The finished ARB bot does it for you on every game day: it watches the books and Polymarket, does the math, reads the fine print, and texts you only the gaps that pass.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished ARB gap-finder**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, JARVIS, ARENA, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst, the Hedge Fund Committee and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished ARB bot for $199 →]({{offerUrl}})**
