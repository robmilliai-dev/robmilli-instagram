# Start here: your 24/7 AI Trader

**What you'll have in about 60 minutes:** a bot that checks your watchlist every trading day, finds two classic setups (breakouts and pullbacks), works out the plan and the safe size, and texts you one clear answer: **APPROVE FOR REVIEW**, **WATCHLIST** or **REJECT**.

It never places a trade. It does the homework. You make the call.

> Educational only, not financial advice. Never risk money you can't afford to lose.

## What you need

- A computer with **Python 3.10 or newer** (free from [python.org](https://www.python.org/downloads/)). Check with `python3 --version` (Mac/Linux) or `py --version` (Windows).
- **Optional:** an Anthropic API key, so Claude writes a short memo for each idea. No key? The bot still works for free with its built-in rules.
- **Optional:** a free Telegram bot, so the answers land on your phone. Without it, they print on your screen.

**Never used a terminal before?** Open [Claude Code](https://claude.com/claude-code) in this folder and paste the [install prompt](install/INSTALL-PROMPT.md). It walks you through every step and runs the commands with you.

## Step 1: Install it (10 minutes)

Open a terminal in this folder (the one with this file in it) and paste:

```bash
bash install/setup.sh ./ai-desk-work
```

That makes a folder called `ai-desk-work` with everything set up inside. It's safe to run again. It never overwrites your settings.

## Step 2: Add your stocks (5 minutes)

Open `ai-desk-work/code/trader.env` in any text editor. Change these lines:

| Setting | What to put |
|---|---|
| `WATCHLIST` | 5 to 20 stocks you follow, like `SPY,QQQ,AAPL,MSFT,NVDA` |
| `ACCOUNT` | The money in the account you'd trade with, like `10000` |
| `RISK_PCT` | How much of it you'd lose if a stop hits. `1.0` means 1%. Leave it if unsure. |
| `ANTHROPIC_API_KEY` | Your key from [console.anthropic.com](https://console.anthropic.com/), or leave it blank |

Save the file. **Never paste this file into an AI chat.** It holds your private keys.

## Step 3: Check it works (5 minutes)

```bash
ai-desk-work/code/.venv/bin/python ai-desk-work/code/trader.py --check
```

You'll see your settings and the last closing price for your first stock. **Open that stock on a chart and check the price matches.** If it does, the bot is reading real data.

## Step 4: Run it (5 minutes)

```bash
ai-desk-work/code/.venv/bin/python ai-desk-work/code/trader.py
```

It scans every stock on your list. For each setup it finds, you get a message like this (example only):

```text
🤖 NVDA · BREAKOUT
RISK: passed. 17 shares, max loss $82
PLAN: entry 146.53 / stop 141.72 / target 156.14
STRONGEST REASON NOT TO: extended moves often retest the breakout level
DECISION: APPROVE FOR REVIEW
Human approval required. Nothing has been traded.
```

**No setups today? That's normal.** Most days, most stocks have nothing. The bot only speaks up when the rules match.

## Step 5: Put it on your phone (15 minutes)

Follow the Telegram steps in [chapter 03](03-code-install-and-run.md#choose-one-private-notification-destination). Put your `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in `trader.env`, then run:

```bash
ai-desk-work/code/.venv/bin/python ai-desk-work/code/trader.py --test-notification
```

A test message should land on your phone. If it does, you're connected.

## Step 6: Make it run by itself (15 minutes)

New setups can only appear once a day, after the market closes. So run it once each weekday evening. Pick one:

- **Free, no laptop needed:** use the ready-made GitHub Actions file `code/trader-workflow.yml`. [Chapter 08](08-the-full-ai-trader.md#when-to-run-it) shows exactly where to put it.
- **On your own computer:** [chapter 08](08-the-full-ai-trader.md#when-to-run-it) has the one line to paste into your computer's scheduler.

## ✅ You're live when

- `--check` shows a price that matches your chart,
- a test message reached your phone, and
- the bot is scheduled to run every weekday evening.

## How to read the answer

- **APPROVE FOR REVIEW:** the rules passed and it's worth a look. Open the chart, read the "reason not to", then decide. It is not a "buy" button.
- **WATCHLIST:** something's forming. Keep an eye on it.
- **REJECT:** the risk check failed, or the reward is too small. Skip it.

After 30 trading days, open `trade_log.csv` and check: did the APPROVE ideas do better than the REJECT ones? [Chapter 08](08-the-full-ai-trader.md#grade-it-before-you-trust-it) shows how.

## If something goes wrong

| What you see | What to do |
|---|---|
| `Python 3.10+ required` | Install a newer Python from [python.org](https://www.python.org/downloads/), then run step 1 again. |
| `not enough completed daily bars` | That ticker is new or misspelled. Check it on finance.yahoo.com. |
| Decisions say "rules-only" but you added a key | The key isn't saved in `trader.env`. Fix it and run `--check`. |
| No message on your phone | Run `--test-notification`. If nothing arrives, re-check the Telegram token and chat ID. |
| Anything else | See [chapter 05](05-operations-and-troubleshooting.md), or paste the error into Claude and ask how to fix it. |

## Want to go further?

- [01](01-first-alert-in-30-minutes.md): set a TradingView alert and have AI check it (no code).
- [04](04-signal-rules-and-example.md): exactly how the breakout and pullback rules work.
- [07](07-trading-desk-launch-kit.md): the Never-Blow-Up Kit: position-size calculator, watchlist, journal and daily checklist.
- `code/desk.py`: a simpler watcher that checks one strict breakout rule ([chapter 03](03-code-install-and-run.md)).

**Still not running after 7 days?** Email support@milli-ai.com. You get every dollar back, and you keep the files.
