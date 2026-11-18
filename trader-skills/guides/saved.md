---
title: You Saved 300 Strategy Reels. Test the Best 10.
promise: A free kit that turns your saved Instagram or TikTok trading posts into a ranked shortlist of strategies actually worth testing.
minutes: 20
nextSystemSlug: backtest-any-idea
---

# You Saved 300 Strategy Reels. Test the Best 10.

**You saved 300 "this strategy prints" reels.** You tested zero.

**This turns the pile into a queue, ranked by what's actually testable.**

**When you're done, you'll have:**

- ✅ Every saved post in one sheet
- ✅ The claim and the exact rule pulled out
- ✅ A testability score for each
- ✅ A top-10 shortlist to test next

**Why this works:** Most posted strategies can't be tested as posted. Scoring them sorts the real rules from the vibes in minutes.

## Step 1: Grab the skill (1 minute)

**[Download saved-posts-sorter.zip →](https://milli-ai.com/api/downloads/trader-skills/saved-posts-sorter.zip)**

Unzip it into `~/.claude/skills/` (works in every project) or `.claude/skills/` (one project).

**No Claude Code?** Two other ways:
- Open `SKILL.md`, copy all of it, and paste it into a Claude Project's instructions or a custom GPT.
- Or connect the free Milli MCP (comment **MCP**) and just ask for it by name.

## Step 2: Run it

1. Instagram: Settings → Accounts Center → Download your information → **Saved** → JSON.
2. When the email comes, unzip it and run:

```bash
python scripts/parse_saved.py ~/Downloads/instagram-export
```

3. Ask Claude to fill the sheet (`/saved-posts-sorter`), then:

```bash
python scripts/rank.py saved.csv --top 10
```

> Educational only. Not financial advice. Nothing here places a trade.

## Want it done for you?

The free version gets you started. **The finished Backtest Any Idea kit tests any idea you type, on any market, and hands you a plain grade in about a minute.**

I already did the hard part. I built it. I tested it. I wrote down every setting and every step.

Your part is a 60-minute setup. Copy. Paste. Done. You don't need to know how to code.

**Here's everything you get for one payment of $199:**

- ✅ **The finished Backtest Any Idea kit**, tested and ready to run
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

**[Yes, give me the finished Backtest Any Idea kit for $199 →]({{offerUrl}})**
