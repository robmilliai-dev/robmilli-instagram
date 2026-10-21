---
title: Claude × TradingView Setup
promise: Connect Claude to your TradingView charts in three levels, from a 5-minute screenshot workflow to automatic alerts that Claude reads and sends to your phone. Copy-paste prompts, a Pine Script alert indicator and a tested webhook app.
minutes: 45
nextSystemSlug: tradingview-claude-chart-analyst
---

# Claude × TradingView Setup

You stare at charts. You second-guess. You miss the setup while you're at work, then chase it at the top.

This guide fixes that in three levels. Do Level 1 tonight in 5 minutes. Do Level 3 this weekend and every alert you set in TradingView gets read by Claude, checked against **your** rules and sent to your phone with the levels, the risk math and the reasons to skip it.

You need: a free [TradingView](https://www.tradingview.com/) account and a [Claude](https://claude.ai/) account. Level 3 also needs a TradingView plan that includes webhook alerts, an [Anthropic API key](https://console.anthropic.com/) (pay as you go, usually cents a day for a handful of alerts) and a free [Telegram](https://telegram.org/) account.

## Level 1 (5 minutes): Claude reads your chart

1. In Claude, create a Project called **Chart Analyst** and paste this into its instructions:

```text
You are my chart analyst. You analyze; you never tell me to buy or sell.
When I upload a chart screenshot:
1. Name the symbol, timeframe and date range you can see. If you can't read them, ask.
2. TREND: up, down or sideways, with the evidence on the chart.
3. KEY LEVELS: the 2 most important support and resistance prices you can see.
4. SETUP: breakout, pullback, reversal or none. Explain in plain English.
5. PLAN IF I TAKE IT: entry, stop (where the idea is wrong), target, reward:risk.
6. RED FLAGS: the strongest reason NOT to take it.
7. VERDICT: TAKE A CLOSER LOOK / WATCH / SKIP.
Only use what is visible. If a number isn't on the chart, write "not visible". Never invent indicator values.
```

2. In TradingView, open any chart and press **Alt+S** (Option+S on Mac) to download a screenshot, or use the camera icon → *Download image*.
3. Drop the image into the project. That's it: a second set of eyes on every chart, with the same rules every time.

## Level 2 (10 minutes): let TradingView do the watching

Paste this Pine Script into TradingView's **Pine Editor** (bottom panel), click **Add to chart**, then set an alert on it: *Create alert → Condition: Claude Setup Alerts → Any alert() function call*.

```pine
//@version=6
indicator("Claude Setup Alerts", overlay = true)
len    = input.int(20, "Lookback bars")
secret = input.string("change-me", "Webhook secret (match WEBHOOK_SECRET)")

resistance = ta.highest(high, len)[1]
support    = ta.lowest(low, len)[1]
ema20      = ta.ema(close, 20)
ema50      = ta.ema(close, 50)
volRatio   = volume / ta.sma(volume, 20)

breakout = ta.crossover(close, resistance)
pullback = ema20 > ema50 and low <= ema20 and close > ema20

plot(resistance, "Resistance", color.red)
plot(support, "Support", color.green)
plot(ema20, "EMA 20", color.blue)

setup = breakout ? "breakout" : pullback ? "pullback" : ""
if barstate.isconfirmed and setup != ""
    stopLevel = setup == "breakout" ? ema20 : math.min(low, ema50)
    msg = '{"secret":"' + secret + '","ticker":"' + syminfo.ticker + '","interval":"' + timeframe.period + '","setup":"' + setup + '","close":' + str.tostring(close, format.mintick) + ',"stop":' + str.tostring(stopLevel, format.mintick) + ',"resistance":' + str.tostring(resistance, format.mintick) + ',"support":' + str.tostring(support, format.mintick) + ',"ema20":' + str.tostring(ema20, format.mintick) + ',"ema50":' + str.tostring(ema50, format.mintick) + ',"volume_ratio":' + str.tostring(volRatio, "#.##") + '}'
    alert(msg, alert.freq_once_per_bar_close)
```

It draws support, resistance and the 20 EMA, and fires one alert per closed bar when price **breaks out** above the 20-bar high or **pulls back** to the 20 EMA inside an uptrend (20 EMA above 50 EMA). The alert message is JSON with every number Claude needs, so nothing gets guessed. Change the secret in the indicator's settings to any random phrase.

Without Level 3, you still get a phone notification from TradingView. Paste its message into your Chart Analyst project and Claude reads the numbers.

## Level 3 (30 minutes): Claude reads every alert and texts you

**Step 1: Telegram bot.** In Telegram, message **@BotFather**, send `/newbot` and copy the token. Send your new bot any message, then open `https://api.telegram.org/bot<TOKEN>/getUpdates` and copy the `chat` → `id` number.

**Step 2: deploy the webhook.** The app below runs on any Python host (Replit, Render, Railway or your own server). Set these environment variables / secrets:

| Variable | Example | What it is |
|---|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-…` | From console.anthropic.com |
| `WEBHOOK_SECRET` | `blue-otter-42` | Same phrase as the Pine Script setting |
| `TELEGRAM_BOT_TOKEN` | `123:ABC…` | From BotFather |
| `TELEGRAM_CHAT_ID` | `555123456` | From getUpdates |
| `ACCOUNT_SIZE` | `10000` | Used for position sizing |
| `RISK_PCT` | `1` | % of the account you'd risk per idea |

Install with `pip install anthropic flask requests`, then run `python app.py`. Your webhook URL is `https://<your-app-url>/tradingview`.

```python
"""Claude x TradingView: a TradingView alert hits this webhook, Claude reads it
against YOUR rules, and the analysis lands on your phone via Telegram.
Educational code. Not financial advice. It never places orders.

pip install anthropic flask requests
Env vars: ANTHROPIC_API_KEY, WEBHOOK_SECRET, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID,
          ACCOUNT_SIZE (e.g. 10000), RISK_PCT (e.g. 1)
"""
import json
import os

import anthropic
import requests
from flask import Flask, abort, request

app = Flask(__name__)
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY

RULES = """You are my chart analyst. You only analyze; you never place trades.
Use ONLY the alert data you are given. If something you need is missing, write "not provided".
Reply in this exact format, under 120 words:
SETUP: breakout / pullback / reversal / none
TREND: up / down / sideways, and why in one line
KEY LEVELS: support and resistance from the data
PLAN: entry, stop, target (from the data), reward:risk
SIZE: shares = (account x risk%) / (entry - stop), show the math
RED FLAGS: anything that argues against it
VERDICT: TAKE A CLOSER LOOK / WATCH / SKIP"""


def position_size(entry: float, stop: float) -> dict:
    account = float(os.environ.get("ACCOUNT_SIZE", "10000"))
    risk_pct = float(os.environ.get("RISK_PCT", "1"))
    risk_dollars = account * risk_pct / 100
    per_share = abs(entry - stop)
    shares = int(risk_dollars // per_share) if per_share > 0 else 0
    return {"account": account, "risk_pct": risk_pct, "risk_dollars": risk_dollars, "shares": shares}


def analyze(alert: dict) -> str:
    sizing = position_size(float(alert["close"]), float(alert["stop"])) if "stop" in alert else {}
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=2000,
        output_config={"effort": "medium"},
        system=RULES,
        messages=[{"role": "user", "content": f"TradingView alert:\n{json.dumps(alert)}\nSizing inputs:\n{json.dumps(sizing)}"}],
    )
    if response.stop_reason == "refusal":
        return "Claude declined to analyze this alert."
    return "".join(b.text for b in response.content if b.type == "text")


def send_telegram(text: str) -> None:
    token, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        print(text)  # no Telegram set up yet: print to the logs instead
        return
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                  json={"chat_id": chat, "text": text}, timeout=15)


@app.post("/tradingview")
def tradingview():
    alert = request.get_json(force=True, silent=True) or {}
    if alert.get("secret") != os.environ.get("WEBHOOK_SECRET"):
        abort(403)  # only your own alerts get through
    alert.pop("secret", None)
    text = f"📈 {alert.get('ticker', '?')} {alert.get('interval', '')}\n\n{analyze(alert)}"
    send_telegram(text)
    return {"ok": True}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
```

**Step 3: point TradingView at it.** Edit your alert → *Notifications* → tick **Webhook URL** and paste the URL. Next time the indicator fires, your phone gets something like:

```text
📈 SPY 60
SETUP: pullback
TREND: up, 20 EMA above 50 EMA
KEY LEVELS: support 175.10, resistance 183.00
PLAN: entry 182.40, stop 178.40, target 183.00 … reward:risk 0.15 → poor
SIZE: (10,000 × 1%) ÷ (182.40 − 178.40) = 25 shares
RED FLAGS: target sits right under resistance; reward too small for the risk
VERDICT: SKIP
```

(Example output. Your numbers come from your chart.) Notice it said **SKIP**. A good analyst saves you from more bad trades than it finds good ones.

## Make it yours

- Change `RULES` in `app.py` to your own checklist. The tighter your rules, the more useful Claude gets.
- Add more alerts: every symbol you set the indicator on reports to the same webhook.
- Keep a log: forward the Telegram messages to a note and review which verdicts were right after 30 days.

> **Before you rely on this:** Educational only, not financial advice. Claude can misread data and no indicator predicts the future. The app never places trades; you check the chart and make every decision. Test with small size first.

## The next problem

Alerts tell you *when* to look. They don't watch the whole market overnight, argue both sides of the trade or keep your risk rules when you're tired. **Solo Trader's AI Desk** gives you all four systems: TradingView + Claude Chart Analyst (the full version of this guide), AI Trading Desk 24/7, the six-role AI Hedge Fund Blueprint and the Free Bloomberg Terminal Setup, plus 20 bonus systems. $1,166 combined listed value. Your price: $199 until Dec 1, 2026, then $349. Follow Live-in-60; not running in 7 days? Email support@milli-ai.com for a full refund and keep your downloads. [Get your complete trading AI desk]({{offerUrl}}).
