# Start here: your AI market-watch notebook

**What this does:** You give AI a snapshot of the market. It checks your watchlist, spots your levels, and writes a clean note in your journal. It thinks with you. **It never places trades.**

**What you'll have in 30 minutes:**

- ✅ A ready-to-paste [market-watch prompt](prompts/market-watch-system.md)
- ✅ Your first market check, done
- ✅ A [trading journal](templates/watch-journal.md) with your first note in it
- ✅ (Optional) A small script that runs the check for you on a schedule

**What you need:** [Claude](https://claude.ai/) (free works to start) and a chart or quote site you already use, like TradingView or your broker.

## Step 1: Do a 5-minute warm-up

Pick one stock or coin. Write down:

1. The ticker
2. The time of the price **and your time zone**
3. Is the market open right now?
4. One price level you're watching
5. One thing that would prove your idea wrong

**Don't know when the price is from?** Stop. Old prices are the #1 way people fool themselves. This step alone fixes it.

## Step 2: Run your first watch

Open [the 30-minute watch run](01-first-watch.md) and follow it. You'll paste the prompt into Claude, give it your snapshot, and get a clean note back.

If the AI isn't sure the data is fresh, it says **"NO SETUP / DATA UNAVAILABLE"**. That's on purpose. It means it won't make stuff up.

## Step 3 (optional): Put it on a schedule

Want it to check for you every day? Follow [the schedule guide](02-schedule-and-review.md). It uses the included [script](code/market-watch.mjs). The script reads a price file you save. It does not fetch prices or place trades.

✅ **You're set when** you have one journal note with: ticker, price time, your level, and what would prove you wrong.

## Your rules (set these first)

- A short watchlist (3 to 5 tickers is plenty)
- How old a price can be before the AI stops (say, 15 minutes)
- Is it pre-market, regular hours, or after close? Label it.

## What it costs

Free to start with a free Claude account. If you use the scheduled script, the Claude API is billed separately from a Claude chat plan. Check [Claude pricing](https://claude.com/pricing) and [API pricing](https://platform.claude.com/docs/en/about-claude/pricing).

## If something goes wrong

| Problem | Fix |
|---|---|
| It always says "DATA UNAVAILABLE" | Add the price time and time zone to your snapshot. |
| It tells you what to buy | Paste the full prompt again. It's built to only take notes. |
| The script errors | Go back through [the schedule guide](02-schedule-and-review.md) one step at a time. Most errors are a missing API key or a wrong file name. |

Educational only, not financial advice. Never trade money you can't afford to lose.

Stuck? Email support@milli-ai.com. If it's not working in 7 days, you get every dollar back, and you keep the files.
