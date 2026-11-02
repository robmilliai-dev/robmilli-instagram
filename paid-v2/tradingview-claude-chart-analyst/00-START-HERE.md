# Start here: your Claude Chart Analyst

**What you'll have:**

1. **In 10 minutes:** a Claude "chart analyst" that reads any chart screenshot and tells you the trend, key prices, the setup and the biggest red flag, in plain English.
2. **In about 90 minutes (optional):** TradingView watches your charts for breakouts and pullbacks, Claude reads every alert, and the answer texts your phone, with the position size already worked out.

It never places a trade. You make every call.

> Educational only, not financial advice. Never risk money you can't afford to lose.

---

## Part 1: Claude reads your charts (10 minutes, no code)

### Step 1: Set up the analyst

1. Open [Claude](https://claude.ai/) and make a new **Project** called **Chart Analyst**. (No Projects? A normal chat works too.)
2. Paste this into the Project's instructions:

```text
You are my chart analyst. You never tell me to buy or sell. I decide.
When I upload a chart:
1. Name the stock, timeframe and dates you can see. If you can't read them, ask me.
2. TREND: up, down or sideways, and what on the chart shows it.
3. KEY PRICES: the 2 most important support and resistance prices you can see.
4. SETUP: breakout, pullback, reversal or none. Explain it simply.
5. PLAN IF I TAKE IT: entry, stop (where the idea is wrong), target, reward:risk.
6. RED FLAG: the strongest reason NOT to take it.
7. VERDICT: TAKE A CLOSER LOOK, WATCH or SKIP.
Only use what is on the chart. If a number isn't visible, write "not visible".
Never make up prices or indicator values. Plain English, short.
```

Want a stricter version that also tracks what's missing? Use [prompts/chart-reading.md](prompts/chart-reading.md).

### Step 2: Take a clean screenshot

1. Open any chart in [TradingView](https://www.tradingview.com/chart/). Set it to **1D** (daily).
2. Add the **EMA 20**, **EMA 50** and **Volume** (click "Indicators" and search for them). Claude can only read what it can see.
3. Press **Alt+S** (Windows) or **Option+S** (Mac) to save a screenshot. Make sure the stock name and the prices on the right are visible.

### Step 3: Get your read

Drop the screenshot into the Project and type **"Read this chart."** You'll get an answer in about a minute.

### Step 4: Check it once

Find 2 prices Claude mentioned. Can you see them on your chart? Good. If Claude names a number that isn't on the chart, reply: *"Show me where that is, or remove it."*

**✅ Part 1 is done when** you've got a chart read and you've checked 2 of its claims yourself. Save it with the [review sheet](templates/review-sheet.md) if you like.

---

## Part 2: Alerts that text your phone (about 90 minutes)

This part needs a few things first:

- A **TradingView plan that includes webhook alerts** (check your plan's features).
- **Python 3.10 or newer** on your computer ([python.org](https://www.python.org/downloads/)).
- An **Anthropic API key** from [console.anthropic.com](https://console.anthropic.com/) (pay as you go; set a spending limit).
- A free **Telegram bot** for your phone (step 2 shows how).
- Somewhere to host a small web app that stays on (Replit, Render, Railway or similar).

**Never used a terminal?** Open [Claude Code](https://claude.com/claude-code) in this folder and paste the [install prompt](install/INSTALL-PROMPT.md). It does these steps with you.

### Step 1: Add the indicator to TradingView (10 minutes)

1. In TradingView, click **Pine Editor** at the bottom of the chart.
2. Delete what's there. Paste everything from `code/setup-alerts.pine`. Click **Save**, then **Add to chart**.
3. Click the indicator's gear icon. Set **Webhook secret** to a long made-up phrase, like four random words and a number. Write it down.

You'll see support, resistance and two EMA lines on the chart, with small markers under past setups.

### Step 2: Test the app on your computer (20 minutes)

Open a terminal in this folder and paste:

```bash
cd code
python3 -m venv .venv && .venv/bin/pip install -r app-requirements.txt
cp app.env.example app.env
```

Open `code/app.env` in a text editor and fill in:

- `WEBHOOK_SECRET`: the phrase from step 1
- `ANTHROPIC_API_KEY`: your key
- `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`: [chapter 04](04-webhook-setup.md) shows how to get these in 5 minutes
- `ACCOUNT_SIZE` and `RISK_PCT`: your account and how much to risk per trade (1 means 1%)

Then run:

```bash
.venv/bin/python app.py --check
.venv/bin/python app.py --test-alert
```

A message labelled **"TEST (made-up alert)"** should land on your phone. If it does, the app works.

### Step 3: Put the app online (20 to 30 minutes)

TradingView needs a web address to send alerts to. On Replit, for example: make a new Python app, upload `app.py` and `app-requirements.txt`, add the values from `app.env` as **Secrets** (not as a file), set the run command to `python app.py`, and deploy it as an always-on web service. Free plans often go to sleep, and a sleeping app misses alerts.

When it's live, open `https://<your-app-address>/health`. You should see `{"ok": true, "claude": true, "telegram": true}`.

### Step 4: Create the alert (5 minutes)

1. On the chart, click **Alert** (the clock icon) → **Create alert**.
2. **Condition:** Claude Setup Alerts → **Any alert() function call**.
3. **Notifications:** tick **Webhook URL** and enter `https://<your-app-address>/tradingview`.
4. Leave the message box alone. Click **Create**.

Repeat for each stock you want watched.

### Step 5: Prove it works (10 minutes)

Real setups are rare, so test it on purpose: switch a busy stock to a **1-minute** chart and add a second alert there. Pullbacks fire often on 1-minute charts. When the message hits your phone, check its numbers against the chart. Then delete the test alert.

**✅ Part 2 is done when** a real alert from TradingView has landed on your phone and its numbers match the chart.

---

## How to read a message

```text
📈 NVDA D · BREAKOUT
PLAN: entry 146.53, stop 142.48, target 154.63 (2R)
SIZE: 24 shares, max loss $97
RED FLAGS: 3.3% above EMA20, breakouts often retest
VERDICT: TAKE A CLOSER LOOK
```

(Example only, not a real signal.) **TAKE A CLOSER LOOK** means it's worth opening the chart. It is not a "buy" button.

## If something goes wrong

| What you see | What to do |
|---|---|
| Claude can't read the prices | Take a bigger, sharper screenshot with the price axis showing. |
| Nothing arrives, but `/health` works | Make sure the alert's webhook address ends in `/tradingview`. |
| `403` in the app's logs | The secret in TradingView and in `WEBHOOK_SECRET` don't match. Re-type both. Spaces count. |
| `/health` won't load | The app isn't running, or the host put it to sleep. |
| No Webhook URL option in TradingView | Your plan doesn't include webhooks. Part 1 still works on any plan. |
| Anything else | See [chapter 05](05-operations.md) and [chapter 07](07-setup-alerts-and-python-webhook.md), or paste the error into Claude and ask how to fix it. |

**Still not running after 7 days?** Email support@milli-ai.com. You get every dollar back, and you keep the files.
