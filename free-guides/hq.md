---
title: The AI Trading HQ
promise: Send a stock idea up a 6-floor AI building. Each floor can stop it. Only the best ideas reach the top. Free in 15 minutes, plus how the automatic version is built.
minutes: 15
nextSystemSlug: six-bot-trading-team
---

# The AI Trading HQ

**Most traders see a move and buy it. Real trading firms send every idea up a building first.** Each floor checks one thing. Any floor can stop it. Only the best ideas make it to the top.

In 15 minutes, you'll build that 6-floor HQ with AI, free, and send your first idea up.

**When you're done, you'll have:**

- ✅ A 6-floor AI trading HQ in one Claude chat
- ✅ The exact floor where your idea got stopped, and why
- ✅ One clear call: **PASS**, **WATCH** or **CANDIDATE**

**How it works:** Your idea rides up 6 floors → each floor can stop it → only the best reach the top → PASS, WATCH or CANDIDATE

> **READ FIRST:** It never places a trade. Most ideas stop on a lower floor. That's the point.

**Why this works:** Bad trades usually have one obvious flaw you didn't want to see. Six floors, each hunting for a different flaw, find it fast. If an idea makes it all the way to the top, it's earned your attention.

| Floor | Checks | Stops the idea when |
|---|---|---|
| 1 Scan | Did anything unusual happen? | Nothing moved |
| 2 Research | Is there real, dated news? | It's a rumor |
| 3 Chart | Is there a clean setup? | Reward is too small |
| 4 Test | What's the best case against it? | The case against wins |
| 5 Risk | Is the size safe? **Can veto.** | No stop or too big |
| 6 Decision | Final call | Any floor said stop |

## Step 1: Pick one stock idea (3 minutes)

Pick one stock you saw moving today. Write down why it caught your eye. If you can, grab a chart screenshot from [TradingView](https://www.tradingview.com/chart/) and one dated headline.

## Step 2: Build your HQ (3 minutes)

In [Claude](https://claude.ai/), make a **Project** called **Trading HQ** (or use a new chat). Paste this in:

```text
You are a 6-floor stock research building. You never place trades. I decide.
An idea starts on Floor 1 and rides up. Each floor writes 2-3 short lines
and ends with GO UP or STOP and why.

FLOOR 1 SCAN: Did anything unusual happen? (Big volume, new high, a gap.)
FLOOR 2 RESEARCH: Only facts with a source and date that I gave you.
FLOOR 3 CHART: Entry, stop (where it's wrong), target. If the reward
  isn't at least 1.5x the risk, STOP.
FLOOR 4 TEST: Give the strongest case AGAINST this idea.
FLOOR 5 RISK: How many shares so hitting the stop loses only 1% of my
  account? Show the math. No stop or too big = VETO.
FLOOR 6 DECISION: PASS, WATCH or CANDIDATE. Name the floor that decided
  it, the #1 reason against, and what would change the call.
PASS and WATCH mean don't buy. If any floor said STOP, it can't be CANDIDATE.
Never make up prices or news. Plain English.
```

## Step 3: Send your idea up (4 minutes)

Send this as your next message:

```text
Stock: [TICKER]
Today's date: [DATE]
Why it caught my eye: [ONE SENTENCE]
Chart: [attach a screenshot, or "none"]
News I found: [headline, source, date, or "none"]
My practice account: $[10,000]

Send it up the building.
```

## Step 4: Read it top-down (5 minutes)

1. **Find the first floor that said STOP.** That's your real answer. Most ideas stop on Floor 2 (no real news) or Floor 3 (reward too small). That's the HQ doing its job.
2. **Check every number** against what you gave it.
3. **Save it.** Stock, date, call, and the floor that decided it.

**You did it if:** you have one saved call and you know exactly which floor stopped it (or why it made it to the top).

## How the automatic HQ works

The finished version does this on its own, every hour the market is open: it scans your watchlist, pulls real news and prices, runs the risk rules in plain code (so no AI can argue past them), and texts you only the ideas that reach the top.

**To build it yourself,** you'd write each floor in Python, connect real data, set up phone texts and schedule it. A few evenings if you code.

> Educational only. Not financial advice.

## Build the starter bot with Claude Code (20 minutes)

Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter 6-floor Trading HQ: an idea rides up 6 floors and any floor can stop it. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir trading-hq && cd trading-hq
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called trading-hq in Python 3: a starter 6-floor Trading HQ: an idea rides up 6 floors and any floor can stop it.

WHAT IT DOES
1. Command: python src/main.py --ticker MSFT. Pull prices with the free yfinance library.
2. Floors in order: Scan, Research, Charts, Test (simple check of how this setup did on this stock before, in Python), Risk (can stop anything), Decision. Each floor is a Claude call that replies as JSON with PASS or STOP and a reason.
3. Stop at the first STOP. Final: PASS, WATCH or CANDIDATE. Save the floor-by-floor memo to memos/.

RULES FOR THE BUILD
4. Use the official Anthropic Python SDK. Put the model name in config.json. Read ANTHROPIC_API_KEY from .env with python-dotenv. Create .env.example with placeholders and add .env, data/ and logs/ to .gitignore. Never hardcode keys.
5. It never places real trades or bets. No broker or wallet code, no private keys.
6. Put every setting (limits, tickers, thresholds) in config.json so I can change them without touching code.
7. Add a --demo flag that runs the whole thing on made-up data with no internet, so I can test it first.
8. Handle errors and rate limits with a short wait and retry. If you are not sure an API endpoint or field exists, leave a clear TODO instead of guessing.
9. Write a README.md for a total beginner: install, add the key, run --demo, run for real, read the logs.
10. Keep it simple and well commented, under about 400 lines. When done, explain what you built and list anything you could not check.
```

**4. Install and test:**

```bash
pip install -r requirements.txt
cp .env.example .env
python src/main.py --demo
```

Add your key to `.env` with a text editor, then run it for real (the README shows the exact command).

> **Keep your key safe:** never paste API keys into a chat, a screenshot or GitHub. Keep `.env` in `.gitignore`.

**Starter vs finished**

| | Starter (free, this prompt) | Finished (AI Desk) |
|---|---|---|
| Works on your computer | ✅ | ✅ |
| Six-Bot Trading Team, fully automated | ❌ | ✅ |
| Tested floor prompts | ❌ | ✅ |
| Runs your whole watchlist daily | ❌ | ✅ |
| Phone summary | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Make it yours: your HQ rules (3 minutes)

Add this to the top of your HQ Project. Every floor follows it:

```text
HQ RULES (every floor follows these)
Account size: $____   Max risk per idea: 1%
Max in one stock: 10%. Max open ideas: 3.
An idea needs a dated reason, a price where it's wrong, and reward at least 2x the risk.
Any floor can stop an idea. The Risk floor can stop anything.
Final call: PASS, WATCH or CANDIDATE. HQ never trades. I decide.
```

## 12 more copy-paste prompts

1. "Scan floor: here's my watchlist. Which 2 ideas deserve to go up the building today?"
2. "Research floor: what changed for [ticker] in the last 30 days? Dates and links."
3. "Charts floor: here's the chart. Trend, key prices, and where it's wrong."
4. "Test floor: has this kind of setup worked on this stock before? What would I need to check?"
5. "Risk floor: block or allow? If allowed, size at 1% of $___."
6. "Decision floor: PASS, WATCH or CANDIDATE, with the one reason that decided it."
7. "Which floor stopped this idea, and is that a good reason or too strict?"
8. "Send these 3 ideas up the building. Which one reaches the top?"
9. "Write one memo for the idea: floor by floor, one line each."
10. "30 days later, here's the price: [paste]. Was HQ right? Which floor was most right?"
11. "Look at my last 10 ideas. Which floor stops the most? Should I change its rule?"
12. "Run all 6 floors in one answer and give me a 5-line phone summary."

## Your daily routine

| When | Do this |
|---|---|
| Morning (3 min) | Scan floor (prompt 1). |
| Best idea (10 min) | Send it up all 6 floors (prompt 12). |
| Evening (2 min) | Log the floor that stopped it, or the CANDIDATE. |

## Weekly review (10 minutes, every Sunday)

This is where you actually get better. Paste your week's notes into Claude with this:

```text
Here are my notes from this week: [paste]
1. Which ideas worked and which didn't? Look for patterns (setup, day, time, market).
2. Where did I break my own rules?
3. Give me ONE change to make next week. Just one.
Use only what's in my notes. Don't guess.
```

## Your first run checklist

- [ ] You built your HQ in Claude
- [ ] You sent one idea up all 6 floors
- [ ] You know which floor stopped it, or why it reached the top

## Troubleshooting

| Problem | Fix |
|---|---|
| It skips floors | Reply: "Go floor by floor, one line each." |
| Every idea reaches the top | Make floor 5 (Risk) stricter: "No stop = stop the idea." |
| It makes up facts | Paste the news yourself with a date. |

## Want it done for you?

You just did it once, by hand. **The finished HQ does it for you every hour, on every stock you follow, and texts you only the ideas that make it to the top floor.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished AI Trading HQ (our 6-bot team)**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished Trading HQ for $199 →]({{offerUrl}})**
