---
title: OpenBB in 10 Minutes
promise: Get a free, Bloomberg-style data terminal on your computer in 10 minutes. Then have Claude write you a market brief using only real data. No subscription.
minutes: 15
nextSystemSlug: free-bloomberg-terminal-setup
---

# OpenBB in 10 Minutes

**A Bloomberg Terminal costs about $30,000 a year.** Most traders will never touch one.

OpenBB is a free, open-source tool that pulls real market data for you. In 10 minutes, you'll have it on your computer. In 15, Claude will write you a market brief using **only real numbers**.

**When you're done, you'll have:**

- ✅ OpenBB installed and working, free
- ✅ A file with real daily prices you pulled yourself
- ✅ A Claude market brief where every number comes from your file

**How it works:** Install OpenBB → pull real prices → Claude writes a brief using only that data → you check one number

> **READ FIRST:** Claude must use only the numbers you give it. Always check one number yourself.

**Why this works:** When you ask AI about the market with no data, it guesses. When you hand it real data, it can't guess. It has to use your numbers. That's the difference between a toy and a tool. You'll check it yourself in step 4.

All you need: a computer, Python (free, step 1 shows you), and [Claude](https://claude.ai/).

**Never typed a command before?** No problem. Copy each line exactly. Or paste this whole guide into Claude or ChatGPT and say "walk me through this one step at a time."

## Step 1: Install OpenBB (5 minutes)

1. Check you have Python. Open **PowerShell** (Windows) or **Terminal** (Mac). Type `python3 --version` (Mac) or `py --version` (Windows). You need 3.10 or newer. Don't have it? Get it free at [python.org](https://www.python.org/downloads/).
2. Copy and paste these lines, one at a time.

**Windows:**

```powershell
mkdir openbb-desk
cd openbb-desk
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install openbb
```

**Mac:**

```bash
mkdir openbb-desk
cd openbb-desk
python3 -m venv .venv
./.venv/bin/python -m pip install openbb
```

The last line takes a few minutes. That's normal. Grab a coffee.

## Step 2: Pull real prices (5 minutes)

1. In the `openbb-desk` folder, make a file called `first_query.py`. Paste this in it:

```python
from openbb import obb

data = obb.equity.price.historical(
    symbol="SPY", start_date="2025-01-01", provider="yfinance"
).to_df()
print(data.tail(5))
data.to_csv("spy_daily.csv")
print("Saved spy_daily.csv")
```

2. Run it. Windows: `.\.venv\Scripts\python.exe first_query.py`. Mac: `./.venv/bin/python first_query.py`
3. You'll see the last 5 days of prices, and a new file called **spy_daily.csv**. That's real data you pulled yourself.

Error? Copy the error into Claude and ask "how do I fix this?"

## Step 3: Have Claude write your brief (3 minutes)

Open [Claude](https://claude.ai/), attach **spy_daily.csv**, and paste this:

```text
You are my market brief writer. Use ONLY the attached file.
Don't use anything you remember about the market. Don't make up news.

1. What dates does the file cover? What's the last date?
2. Give me 3 simple facts from the data. For each one, say which date
   and which number it came from.
3. One possible reason for what you see, and one other possible reason.
4. What this file can't tell me.
Plain English. Short. Never tell me to buy or sell.
```

## Step 4: Check one number yourself (2 minutes)

Open **spy_daily.csv**. Find one number Claude used. Does it match? Good. Now you know the brief is real.

**You did it if:** you have a price file you pulled yourself, and a brief where you checked a number.

> Educational only. Not financial advice. OpenBB is free and open-source. It's not a Bloomberg product.

## Build the starter bot with Claude Code (20 minutes)

Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter Morning Brief that pulls real prices and writes a dated brief every morning. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir morning-brief && cd morning-brief
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called morning-brief in Python 3: a starter Morning Brief that pulls real prices and writes a dated brief every morning.

WHAT IT DOES
1. Read watchlist.json. Pull the last 1 year of daily prices with the free yfinance library (or OpenBB if installed) and save to data/prices.csv.
2. Compute: day and week change, distance from 50- and 200-day average, 52-week high/low. Do the math in Python, not in Claude.
3. Send only the computed table to Claude to write a brief under 200 words. Every number in the brief must come from the table. Save to briefs/DATE.md.

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
| OpenBB setup with earnings, news and macro data | ❌ | ✅ |
| Email or phone delivery | ❌ | ✅ |
| Number-checker that flags anything not in the data | ❌ | ✅ |
| Weekly trend report | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Make it yours: your morning brief rules (3 minutes)

Paste this to Claude once, then reuse it every morning:

```text
MY BRIEF RULES
My watchlist: ____
Use ONLY the data I paste. If something is missing, say "not in data."
Every number must show the date it came from.
Format: 1) one-line market mood, 2) biggest movers on my list, 3) anything near a 52-week high or low,
4) 3 things to watch today. Under 200 words.
```

## 12 copy-paste prompts

**Pulling data (OpenBB)**

1. "Write me the OpenBB command to get 1 year of daily prices for [tickers] and save them as a CSV."
2. "Write the OpenBB command for [ticker]'s last 4 quarters of income statements."
3. "My OpenBB command gave this error: [paste]. What's wrong and how do I fix it?"

**Reading it**

4. "Here's my CSV. Write my morning brief using my brief rules."
5. "Which stocks in this data are above their 50-day and 200-day averages? Show the numbers."
6. "Which stock moved the most this week, and is that unusual for it? Compare to its normal weekly move."
7. "Here are 4 quarters of results. Is revenue growing faster or slower? Are profits keeping up?"
8. "Compare these 3 stocks: growth, profit margin, debt. Simple table, no opinion."

**Keeping it honest**

9. "List every number in your brief and the line of data it came from."
10. "What's missing from my data that would change your brief?"
11. "Turn this brief into 3 questions I should answer before making any decision."
12. "Compare today's brief to yesterday's. What actually changed?"

## Your 10-minute daily routine

| When | Do this |
|---|---|
| Morning (5 min) | Run your saved OpenBB commands. Paste the CSV with prompt 4. |
| Check (2 min) | Pick one number and check it yourself (prompt 9 helps). |
| Note (3 min) | Save the brief. Write one thing to watch today. |

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

- [ ] OpenBB is installed and runs
- [ ] You pulled real prices for one stock
- [ ] Claude wrote a brief and you checked one number

## Troubleshooting

| Problem | Fix |
|---|---|
| "python" isn't found | Install Python from python.org and tick "Add to PATH", then reopen the terminal. |
| pip install fails | Run: python -m pip install --upgrade pip, then try again. |
| Claude adds numbers you didn't give it | Reply: "Use only the data I pasted." |

## Want it done for you?

You just did it once, by hand. **The finished Terminal setup gives you a ready-made script and a daily desk sheet, so your morning market brief builds itself the same way every day.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished Bloomberg-style Terminal setup**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished Terminal and all 11 bots for $199 →]({{offerUrl}})**
