---
title: Your Real Trading Scoreboard in 5 Seconds
promise: Your memory keeps the wins and drops the worst day. This free script pulls your real numbers from Alpaca or any broker CSV: return, worst drop, win rate, profit factor.
minutes: 10
nextSystemSlug: ai-trade-journal-coach
---

# Your Real Trading Scoreboard in 5 Seconds

**Ask a trader how they're doing and you'll hear about the best trade.** Not the worst drop.

**This skill shows the numbers you'd rather not look at. On one screen. Every week.**

**When you're done, you'll have:**

- ✅ Equity, today's P&L and return for any period
- ✅ Your worst drop (the number that matters most)
- ✅ Win rate next to average win vs. average loss
- ✅ A warning when you have too few trades to judge
- ✅ An honest post version you can share

**Why this works:** Win rate alone lies. 80% winners with tiny wins and one huge loss is a losing system. The scoreboard always shows the average loss right next to the win rate, so you can't fool yourself.

## Step 1: Grab the skill (1 minute)

**[Download account-stats.zip →](https://milli-ai.com/api/downloads/trader-skills/account-stats.zip)**

Unzip it into `~/.claude/skills/` (works in every project) or `.claude/skills/` (one project).

**No Claude Code?** Two other ways:
- Open `SKILL.md`, copy all of it, and paste it into a Claude Project's instructions or a custom GPT.
- Or connect the free Milli MCP (comment **MCP**) and just ask for it by name.

## Step 2: Run it

**Any broker:** export your closed trades as a CSV, then:

```bash
python scripts/account_stats.py --source csv --file trades.csv --start-equity 5000
```

**Alpaca:** copy `.env.example` to `.env`, add your keys (paper keys first), then:

```bash
python scripts/account_stats.py --source alpaca --period 1M
```

No packages to install. Just Python. Read-only: it can't place a trade.

## The 5 traps it warns you about

- Deposits look like profit
- Under 30 trades proves nothing
- Win rate without average loss is a lie
- Open positions aren't profit yet
- Shortening the date range to look better

> Educational only. Not financial advice. Nothing here places a trade.

## Want it done for you?

The free version gets you started. **The finished AI Trade Journal Coach does the math in code, ranks every leak by what it cost you, and coaches you on the worst one.**

I already did the hard part. I built it. I tested it. I wrote down every setting and every step.

Your part is a 60-minute setup. Copy. Paste. Done. You don't need to know how to code.

**Here's everything you get for one payment of $199:**

- ✅ **The finished AI Trade Journal Coach**, tested and ready to run
- ✅ **11 finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **Bots in your inbox for 3 months:** a morning email with what my 5 tested bots see on your markets. Nothing to install
- ✅ **The Milli Indicator Pack** for TradingView. Paste it and see the dots on your chart in 2 minutes
- ✅ **All 17 Milli trader skills + 6 prompt kits** in one download, plus the Milli MCP
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **Every new bot I release for the next 12 months, free**

That's $2,175 of systems. **You pay $199. Once.** There's no monthly fee and nothing to cancel.

On December 1 the price goes to $349. Same bots. Same files. You'd just be paying $150 more for waiting.

**My promise.** Follow the steps. If it isn't running in 7 days, email robmilli.ai@gmail.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files anyway.

**[Yes, give me the finished AI Trade Journal Coach for $199 →]({{offerUrl}})**
