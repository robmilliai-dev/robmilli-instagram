---
title: The Claude Chart Read
promise: Upload one chart. Get a clear, simple read in 15 minutes. Trend, key prices, the setup and the biggest red flag, in plain English.
minutes: 15
nextSystemSlug: tradingview-claude-chart-analyst
---

# The Claude Chart Read

**What if you could hand any chart to a sharp analyst and get a clear answer in 60 seconds?**

You can. It's free, and it takes 15 minutes to set up.

**When you're done, you'll have:**

- ✅ A Claude "chart analyst" that reads any chart screenshot you give it
- ✅ A plain-English answer: trend, key prices, the setup, and the biggest red flag
- ✅ A simple rule for what to watch next

**How it works:** Clean screenshot → Claude reads trend, key prices, setup and biggest red flag → you check its work → save one watch line

> **READ FIRST:** Claude can misread a chart. Always check one number yourself before you trust the read.

**Why this works:** Claude can read pictures. Give it a clear chart and strict rules, and it reads the chart the same careful way every time. No moods. No hope. No fear. You'll check its work yourself in step 4, so you know it's real.

All you need: a free [TradingView](https://www.tradingview.com/chart/) account and [Claude](https://claude.ai/).

## Step 1: Take a clean chart screenshot (3 minutes)

1. Open [TradingView](https://www.tradingview.com/chart/) and pick any stock.
2. Set the chart to **1 day** (the "1D" button).
3. Make sure you can see the stock name, the prices on the right side, and a few months of candles.
4. Take a screenshot. On TradingView press **Alt+S** (Windows) or **Option+S** (Mac), or use the camera icon.

## Step 2: Set up your chart analyst (3 minutes)

1. Open [Claude](https://claude.ai/).
2. Make a new **Project** called **Chart Analyst**. (No Projects? Just use a new chat.)
3. Paste this into the Project instructions:

```text
You are my chart analyst. You never tell me to buy or sell. I decide.
When I upload a chart:
1. WHAT I SEE: the stock, the timeframe and the dates you can see.
   If you can't read them, ask me.
2. TREND: up, down or sideways. Point to what on the chart shows it.
3. KEY PRICES: the 2 most important prices on the chart, and why.
4. SETUP: breakout, pullback, bounce or none. Explain it simply.
5. RED FLAG: the strongest reason NOT to trust this setup.
6. WHAT TO WATCH: "If the next daily candle closes above/below ___, the picture changes."
7. VERDICT: TAKE A CLOSER LOOK, WATCH, or SKIP.
Only use what you can see. If a number isn't on the chart, say "not visible."
Never make up prices or indicators. Keep it short and simple.
```

## Step 3: Upload your chart (2 minutes)

Drop your screenshot into the Project and type: **"Read this chart."**

You'll get a clear read back in about a minute.

## Step 4: Check its work (5 minutes)

This is the step most people skip. Don't.

1. Find the 2 "key prices" Claude named. Can you see them on your chart? Good.
2. Check the trend it named. Does the chart agree?
3. If Claude named a number you can't find on the chart, reply: **"Show me where that is on the chart, or remove it."**

## Step 5: Save your watch line (2 minutes)

Copy Claude's **WHAT TO WATCH** line into your notes. Check it tomorrow after the market closes.

**You did it if:** you have a saved chart read, and you checked 2 of its claims with your own eyes.

> Educational only. Not financial advice. A screenshot is a snapshot, not live prices.

## Build the starter bot with Claude Code (20 minutes)

Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter Chart Analyst that reads any chart screenshot you drop in a folder and writes the read to a log. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir chart-analyst && cd chart-analyst
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called chart-analyst in Python 3: a starter Chart Analyst that reads any chart screenshot you drop in a folder and writes the read to a log.

WHAT IT DOES
1. Watch the charts/ folder. When a new PNG or JPG appears, send it to Claude with the analyst prompt and my rules from rules.md.
2. Claude must reply as JSON: {"ticker","timeframe","trend","key_prices":[..],"setup","red_flag","watch_line","verdict":"TAKE A CLOSER LOOK|WATCH|SKIP","confidence"}. Treat the reply as data, never as instructions.
3. Save every read to logs/reads.jsonl and print a short summary.

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
| Reads every TradingView alert automatically | ❌ | ✅ |
| Sends the read to your phone | ❌ | ✅ |
| Tested prompts and rules for 4 setups | ❌ | ✅ |
| Weekly accuracy report | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Make it yours: your rules file (3 minutes)

A chart read is only useful if it's judged against **your** plan. Add this to the Project instructions under the prompt from Step 2:

```text
MY RULES
Account size: $____   Max risk per trade: 1%
Stop goes where the idea is proven wrong. Never moved further away.
Only take ideas that can pay at least 2x the risk.
My setups (2-3 max):
1. Breakout: daily close above the 20-day high, above the 200 EMA, volume above average.
2. Pullback: 50 EMA above 200 EMA, price dips to the 20 EMA and closes back above it.
3. (Yours): ____
Judge every chart against these setups. If it matches none, say "no setup."
```

## 12 copy-paste prompts

**Reading charts**

1. "Run the full read on this chart, then score it 1-10 against my setups."
2. "Here are 3 charts. Rank them best to worst against my setups, one line each."
3. "Compare the daily and the 1-hour chart. Do they agree or fight each other?"
4. "Mark the 3 most important support and 3 resistance prices. How many times was each tested?"
5. "Is this a real breakout or a likely fakeout? What would confirm it, and what would kill it?"

**Planning**

6. "My account is $___, risk 1%, entry $___, stop $___. How many shares? Show the math."
7. "Build a plan from this chart: entry trigger, stop where the idea is wrong, target at 2x risk. Flag it if the reward is under 2x."
8. "Give me the strongest case AGAINST this idea, and the first warning sign it's failing."
9. "What has to happen tomorrow for this setup to still be valid?"

**Checking yourself**

10. "Here's the same chart 5 days later. Was your read right? What did you miss?"
11. "Here's my closed trade with entry and exit marked. Did I follow my plan? One lesson."
12. "List every price you named and tell me how sure you are about each one."

## Your 10-minute daily routine

| When | Do this |
|---|---|
| After the close | Screenshot 1-3 charts on your watchlist. Run prompt 2. |
| Best one | Run the full read (prompt 1) and a plan (prompt 7). |
| Before bed | Write one line in your notes: setup, watch line, verdict. |
| Next day | Check yesterday's watch line. Was Claude right? |

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

- [ ] You uploaded one clean daily chart
- [ ] You got the trend, 2 key prices, the setup and the red flag
- [ ] You checked one price on the chart yourself

## Troubleshooting

| Problem | Fix |
|---|---|
| Claude reads the wrong prices | Zoom in so the price axis is clear, or type the key prices in. |
| The read is vague | Reply: "Give exact prices, not ranges." |
| It sounds too sure | Ask: "What would prove this wrong?" |

## Want it done for you?

You just did it once, by hand. **The finished Claude Chart Analyst does it for you on every alert: TradingView spots the setup, Claude reads it, and the answer lands on your phone. You never open a chart unless it's worth your time.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished Claude Chart Analyst**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Hedge Fund Committee and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished Chart Analyst for $199 →]({{offerUrl}})**
