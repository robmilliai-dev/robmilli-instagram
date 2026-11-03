---
title: Claude × TradingView Blueprint
promise: Turn Claude into your own TradingView analyst tonight. Master Prompt, 25 copy-paste prompts, alert templates, risk rules and a free tested indicator. Level 1 takes 15 minutes.
minutes: 10
nextSystemSlug: tradingview-claude-chart-analyst
---

# Claude × TradingView: The Complete Analyst Kit

**"I connected Claude to TradingView, and now it reads every chart for me."**

You've seen the posts. Here's the full kit, free: the Master Prompt, 25 copy-paste prompts, the alert setup, the risk rules and a free indicator we actually tested. If you'd rather have it all running automatically, the finished version is at the end.

**When you're done, you'll have:**

- ✅ Your own Claude chart analyst that follows **your** rules (tonight, free)
- ✅ TradingView alerts that send Claude every number it needs
- ✅ A daily 10-minute routine, a risk calculator and a trade journal
- ✅ 25 copy-paste prompts for every step

**How it works:** Connect → Scan → Analyze → Decide → Alert → Review

> **READ FIRST (the honest truth):** TradingView has no official way for Claude to read your live charts on its own. Anyone promising that is selling you something. What really works: (1) screenshots or exported data into Claude, (2) Claude writing Pine Script for you, and (3) alert webhooks that send signals out (paid TradingView plan). That's what this kit uses. Claude helps you analyze. It never trades, and you make every decision.

## What connects to what

| Connection | Direction | What it does | Cost |
|---|---|---|---|
| Screenshot → Claude | TradingView → Claude | Claude reads the trend, levels and setup from a picture | Free |
| Export data → Claude | TradingView → Claude | Export the chart data (CSV), Claude reads the numbers | Free |
| Claude writes Pine Script | Claude → TradingView | Claude codes an indicator, you paste it in | Free |
| Phone alerts | TradingView → you | Your phone pings when a level or signal hits | Free |
| Webhook alerts | TradingView → your app → Claude | Each alert goes straight to Claude to check | Paid TradingView plan |

## The 15-minute setup

| Minutes | Do this |
|---|---|
| 0–3 | Make a Claude Project called **Chart Analyst**. Paste the Master Prompt (Step 1). |
| 3–7 | Paste your rules file (Step 2). Now Claude knows your setups. |
| 7–11 | Screenshot one chart, run the 4-step read (Step 3). Check it matches what you see. |
| 11–15 | Add the free Milli Dots indicator and one alert (Step 4). |

## Step 1: The Master Prompt (3 minutes)

In [Claude](https://claude.ai/), make a **Project** called **Chart Analyst**. Paste this into its instructions:

```text
You are my TradingView analyst. I send you chart screenshots, exported data or alert messages.
You analyze them against MY rules and help me decide. You never decide for me.

Your jobs:
1. Read every chart in 4 steps: STRUCTURE, LEVELS, SETUP MATCH, INVALIDATION.
2. Judge setups only against my rules file, not generic opinions.
3. Work out position size from my stop distance and show the math.
4. When an alert message comes in, re-check the setup. Still valid, or not?
5. After a closed trade, grade whether I followed my plan and give me one lesson.

Hard limits:
- Never predict prices. Never say "buy" or "sell". Say what MY rules say.
- You're reading a picture or numbers I paste. Say how sure you are.
  Tell me to confirm exact prices on the live chart.
- Never make up price data.
- Remind me: practice new setups with pretend money first. Not financial advice.

Start by asking for my rules file, my account size and my first chart.
```

## Step 2: Your rules file (4 minutes)

Claude is only as good as the rules you give it. Fill this in and paste it into the Project (or save it as a file in the Project):

```text
MY RULES FILE
Account size: $____
Max risk per trade: 1% of the account
Stop: only where the idea is proven wrong. Never moved further away.
Minimum reward: 2x the risk (2R)
Max open trades: 3
New setups: practice 30 times with pretend money before real money

MY SETUPS (2 or 3 max)
1. Breakout: daily close above the highest high of the last 20 days, above the 200 EMA, volume above average.
2. Pullback: uptrend (50 EMA above 200 EMA), price dips to the 20 EMA and closes back above it.
3. (Your own): ____
```

**Tip:** before you screenshot, add the **EMA 20, 50 and 200** and **volume** to the chart. Claude can only read what it can see.

## Step 3: The 4-step chart read (4 minutes)

In TradingView, open a chart and press **Alt+S** (Windows) or **Option+S** (Mac) to save a screenshot. Drop it into your Project with: *"Run the 4-step read."*

| Step | What Claude checks |
|---|---|
| 1. Structure | Trend direction, higher highs or lower lows, the bigger picture |
| 2. Levels | The key support and resistance prices, recent swing points |
| 3. Setup match | Does this match one of MY setups, or none? |
| 4. Invalidation | Where is the idea proven wrong? That's the stop. |

> **Honest limit:** Claude reads a picture. It can get exact prices wrong. Treat it as a second opinion that has to agree with what you see. Always check the levels on the real chart.

## Step 4: Add a free tested indicator + your first alert (4 minutes)

Want dots on your chart instead of eyeballing setups? Use our free **Milli Dots** indicators. We picked the settings on 2010–2019 data and tested them on 2020–2026, years they'd never seen: **Pullback Dots won 27 of 33 S&P 500 futures trades (hypothetical backtest)** and **Trend Dots was profitable on 41 of 43 markets**. Get the code free at [milli-ai.com/free/dots](https://milli-ai.com/free/dots).

Then set the alert:

1. Click the **alarm clock** (Alerts) on the right → **Create alert**.
2. Condition: **Milli Pullback Dots** (or Trend Dots) → **alert() function calls only**. Or pick a price level: **Crossing** your price.
3. Trigger: **Once per bar close**, so you don't get fooled by moves that reverse mid-candle.
4. Paste this into the **Message** box, so every alert carries the numbers Claude needs:

```text
{"ticker":"{{ticker}}","exchange":"{{exchange}}","timeframe":"{{interval}}","price":"{{close}}","high":"{{high}}","low":"{{low}}","volume":"{{volume}}","time":"{{time}}","setup":"breakout"}
```

5. Turn on **Notify in app** and install the TradingView phone app. When it pings, paste the message into Claude with prompt #16.

## Step 5: Your 10-minute daily routine

- [ ] Check which alerts fired (TradingView does the watching, not you)
- [ ] Screenshot those charts and run prompt #5 to rank them
- [ ] Run the 4-step read on the best one (prompt #6)
- [ ] If it passes, build the plan and size it (prompts #13 and #14)
- [ ] Log it in your journal, even the ones you skip

**Why only a few charts?** Claude reads what you show it. It can't watch 40 live charts. The edge is one consistent analyst applying **your** rules the same way every time.

## Step 6: Risk rules that keep you in the game

Keep these in your rules file. They're not optional:

- **Max 1% risk per trade.** Ten losses in a row costs about 10%, not your account.
- **Stop at invalidation only.** Never move it further away.
- **At least 2R.** If the target isn't twice the risk, skip it.
- **Max 3 open trades.**
- **Size from the stop:** shares = (account × 1%) ÷ (entry − stop). Prompt #13 does the math.

## Step 7: Review = where the edge grows

After every trade, screenshot the chart with your entry and exit marked and run prompt #18. Write 4 lines in your journal: the setup, the result in R, did you follow the plan, one lesson. Every week, paste the journal into Claude and run prompt #19. This loop is where traders actually get better.

## 25 copy-paste prompts

**Set up**
1. "Write a TradingView Pine Script v6 indicator for these rules: [rules]. Mark buy signals with dots, add alert() calls that include the ticker and price, and add strategy tester code with commissions."
2. "Turn this TradingView alert into a clean message with ticker, price, timeframe and setup name: [alert]."
3. "Here are my setups and risk rules: [paste]. Turn them into a rules file you'll apply to every chart I send."
4. "Explain step by step, like I'm a beginner, how to send a TradingView webhook alert to a free n8n or Make.com workflow that saves it to a sheet."

**Scan and analyze**
5. "Here are [N] chart screenshots. Rank them by how well each matches my setups. Best first, one line each."
6. "Run the 4-step read on this chart: structure, levels, setup match, invalidation."
7. "Here's exported OHLCV data for [ticker]: [paste CSV]. Find the trend, recent support and resistance, and any setup forming. Use only this data."
8. "Compare the daily chart and the 1-hour chart: [2 screenshots]. Do they agree or conflict? What do my rules say when they conflict?"

**Levels and setups**
9. "Mark the 3 strongest support and 3 strongest resistance prices on this chart. Rate each by how many times it was tested."
10. "Is this a real breakout or a fakeout risk? What would confirm it, and what would prove it wrong?"
11. "Score this setup 1 to 10 against my checklist and give me the single biggest reason to skip it."
12. "Where are the entry, stop and target on this chart, per my rules? Give it as a plan, not a prediction."

**Decide and risk**
13. "Position size: account $[X], 1% risk, entry $[A], stop $[B]. Show the math."
14. "Build a full trade plan from this setup. Flag it if the reward is less than 2x the risk."
15. "Talk me out of this trade. Give me the strongest case against it and the first warning signs it's failing."

**Alerts and monitoring**
16. "An alert just fired: [paste the alert message]. Re-check it against my rules. Still valid, or did something change?"
17. "Here's my watchlist with trigger prices: [paste]. Which are closest to triggering, and what should I have ready?"
18. "Review this closed trade: [screenshot with entry and exit + my plan]. Did I follow the plan? One lesson."
19. "Here's my journal for the week: [paste]. Which setups, times of day or habits show up in my wins vs my losses?"
20. "Am I ready for real money? Judge my pretend-money record: [stats]. My bar: 30+ trades, positive average R, followed my plan 90%+ of the time. Be brutal."

**Bonus prompts**
21. "Here's a Pine Script error from TradingView: [paste]. Fix the script and explain the fix in one line."
22. "Rewrite this indicator so it only fires when the daily trend agrees with the 1-hour signal: [paste code]."
23. "Check my rules for holes: [paste rules file]. What situations do they not cover?"
24. "Here are 20 of my past trades: [paste]. If I'd skipped every trade under 2R, what would my results have been?"
25. "Earnings or big news this week for [tickers]? List dates with sources. If you can't verify a date, say so."

## Level 3: Make it automatic (the honest version)

Here's how the fully automatic version works:

TradingView alert fires → webhook → your small web app → Claude checks it against your rules → a text on your phone → **you** decide.

To build it yourself you'd need: the Pine Script (Step 4), a hosted web app with a secret password so nobody can send fake alerts, Claude's API, a free Telegram bot for the texts, and a log of every alert. A few evenings if you've done this before. It needs a paid TradingView plan for webhooks.

## Build the starter bot with Claude Code (20 minutes)

Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter TradingView webhook analyst: alerts come in, Claude checks them against your rules. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir tv-analyst && cd tv-analyst
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called tv-analyst in Python 3: a starter TradingView webhook analyst: alerts come in, Claude checks them against your rules.

WHAT IT DOES
1. A small FastAPI app with POST /alert that accepts the alert JSON from this guide (ticker, exchange, timeframe, price, high, low, volume, time, setup). Protect it with a secret in the URL from .env.
2. For each alert, ask Claude to re-check it against rules.md and reply as JSON: {"verdict":"STILL VALID|WAIT|IGNORE","reason","stop","size_at_1pct"}.
3. Log every alert and verdict to webhooks/alerts-log.md. Add a --demo flag that sends 3 fake alerts without TradingView.

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
| Hosted for you, always on | ❌ | ✅ |
| Sends the verdict to your phone | ❌ | ✅ |
| Tested rules for 4 setups | ❌ | ✅ |
| Weekly review report | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Your first run checklist

- [ ] Master Prompt and rules file are in your Chart Analyst Project
- [ ] Claude ran the 4-step read on one chart, and it matched what you see
- [ ] You set one alert with the message template
- [ ] Your journal has its first entry

## Troubleshooting

| Problem | Fix |
|---|---|
| Claude misreads prices | Zoom in so the price axis is readable, or paste the key prices as text. |
| Claude says "buy" or "sell" | Paste the Master Prompt again. It should only say what your rules say. |
| The alert never fires | Use "Once per bar close" and turn on app notifications. Check the condition is right. |
| Webhook option is greyed out | Webhooks need a paid TradingView plan. Everything else in this kit is free. |
| "Script could not be translated" | Paste the error into Claude with prompt #21. |

> Hypothetical backtests on past prices; past results don't guarantee future results. Educational only, not financial advice. Claude analyzes. It never trades. You make every decision.

## Want it done for you?

You just did it once, by hand. **The finished setup does it for you: the TradingView script, the web app and the phone texts are all built and tested. Every setup gets read by Claude and lands on your phone.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished Claude × TradingView setup**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Hedge Fund Committee and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished Chart Analyst for $199 →]({{offerUrl}})**
