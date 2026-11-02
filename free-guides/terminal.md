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
