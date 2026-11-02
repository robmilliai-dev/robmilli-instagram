# Start here: your free Bloomberg-style terminal

**What you'll have in about 45 minutes:** OpenBB (a free, open-source market data tool) on your computer, a file of real daily prices you pulled yourself, and a Claude market brief where every number comes from that file.

A Bloomberg Terminal costs about $30,000 a year. This costs nothing.

> Educational only, not financial advice. OpenBB is free and open-source. It's not a Bloomberg product, and the free data can be delayed.

## What you need

- A computer with **Python 3.10 to 3.14** (free from [python.org](https://www.python.org/downloads/)). Check with `python3 --version` (Mac/Linux) or `py --version` (Windows).
- [Claude](https://claude.ai/), for the brief.

**Never used a terminal before?** Open [Claude Code](https://claude.com/claude-code) in this folder and paste the [install prompt](install/INSTALL-PROMPT.md). It does the steps with you. Or paste this whole page into Claude and say *"walk me through this one step at a time."*

## Step 1: Install it (10 to 15 minutes)

Open a terminal in this folder and paste:

```bash
bash install/setup.sh ./openbb-desk
```

This makes a folder called `openbb-desk` and installs everything inside it. The download can take a few minutes. That's normal.

**On Windows?** Use the PowerShell steps in [chapter 02](02-install.md), or let Claude Code do it for you.

## Step 2: Pull real prices (5 minutes)

Paste this:

```bash
./openbb-desk/.venv/bin/python ./openbb-desk/code/export_prices.py --symbol SPY --provider yfinance --start-date 2025-01-01 --output ./openbb-desk/desk/spy_daily
```

You'll get two new files in `openbb-desk/desk/`:

- `spy_daily.csv`: the daily prices
- `spy_daily.metadata.json`: where and when the data came from

Want a different stock? Change `SPY` (both places) to any ticker.

## Step 3: Check the data (5 minutes)

Open `spy_daily.csv` in Excel, Google Sheets or Numbers. Look at the **last two rows**. Write down their dates and closing prices. Do they look right next to a chart? Good. That's real data you pulled yourself.

## Step 4: Get your Claude brief (10 minutes)

Open a new [Claude](https://claude.ai/) chat. Attach **both** files. Then paste the prompt from [prompts/market-brief.md](prompts/market-brief.md), or this short version:

```text
You are my market brief writer. Use ONLY the two attached files.
Don't use anything you remember about the market. Don't make up news.
1. What dates does the file cover? What's the last date?
2. Give me 3 simple facts from the data. For each, say which date and number it came from.
3. One possible reason for what you see, and one other possible reason.
4. What this file can't tell me.
Plain English. Short. Never tell me to buy or sell.
```

## Step 5: Check one number (2 minutes)

Pick one number from Claude's brief. Find it in the CSV. Does it match? Then you can trust the brief.

## ✅ You're live when

You have a price file you pulled yourself, and a Claude brief where you checked at least one number against the file.

## Make it a daily habit

- [Chapter 04](04-routine.md): a 10-minute morning routine using the [daily desk sheet](templates/daily-desk.md).
- [Chapter 03](03-providers.md): other free and paid data sources.
- [Chapter 07](07-research-questions.md): good questions to ask your data.

## If something goes wrong

| What you see | What to do |
|---|---|
| `Python 3.10+ required` or install errors | Install a supported Python from [python.org](https://www.python.org/downloads/), then run step 1 again. See [chapter 02](02-install.md). |
| The export is empty or shows an error | Check the ticker spelling and the date. See [chapter 06](06-troubleshooting.md). |
| The last date looks old | Markets close on weekends and holidays, and free data can lag a day. That's normal. |
| Claude quotes a date that isn't in the file | Don't trust that brief. Re-attach the files and ask again. |
| Anything else | Paste the error into Claude and ask how to fix it. |

**Not working after 7 days?** Email support@milli-ai.com. You get every dollar back, and you keep the files.
