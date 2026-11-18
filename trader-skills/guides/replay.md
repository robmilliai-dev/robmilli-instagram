---
title: Turn Your Equity Curve Into a Video People Watch
promise: A free Remotion template that turns any backtest or account curve into a 12-second animated video, with the worst drop marked in red. Built for Reels and TikTok.
minutes: 15
nextSystemSlug: viral-reel-builder
---

# Turn Your Equity Curve Into a Video People Watch

**Everyone posts the green screenshot.** Nobody shows the drop.

**A curve that draws itself, with the worst drop marked in red, gets watched to the end. And trusted.**

**When you're done, you'll have:**

- ✅ A 12-second vertical video from a CSV
- ✅ The worst drop marked automatically
- ✅ Square and wide versions too
- ✅ A template you can restyle in 2 minutes

**Why this works:** Motion holds attention and honesty earns trust. Showing the drop is the part that makes people believe the rest.

## Step 1: Grab the skill (1 minute)

**[Download equity-video.zip →](https://milli-ai.com/api/downloads/trader-skills/equity-video.zip)**

Unzip it into `~/.claude/skills/` (works in every project) or `.claude/skills/` (one project).

**No Claude Code?** Two other ways:
- Open `SKILL.md`, copy all of it, and paste it into a Claude Project's instructions or a custom GPT.
- Or connect the free Milli MCP (comment **MCP**) and just ask for it by name.

## Step 2: Run it

You need Node 18+.

```bash
bash scripts/setup.sh equity-video
python scripts/csv_to_props.py curve.csv --title "My rule on SPY" --hook "10 years. Every drop shown." --out equity-video/data.json
cd equity-video && npm run render
```

Your video lands in `out/equity.mp4`.

> Educational only. Not financial advice. Nothing here places a trade.

## Want it done for you?

The free version gets you started. **The finished Viral Reel Builder turns one idea into a scripted, captioned, ready-to-post reel with the hooks already tested.**

I already did the hard part. I built it. I tested it. I wrote down every setting and every step.

Your part is a 60-minute setup. Copy. Paste. Done. You don't need to know how to code.

**Here's everything you get for one payment of $199:**

- ✅ **The finished Viral Reel Builder**, tested and ready to run
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

**[Yes, give me the finished Viral Reel Builder for $199 →]({{offerUrl}})**
