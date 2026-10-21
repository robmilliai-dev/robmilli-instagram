---
title: The JARVIS Setup Guide
promise: Build your own JARVIS for the stock market, a Claude research assistant you text from your phone. It pulls live prices, trend, news, earnings dates and your portfolio risk with its own tools, answers in plain English and sends you a morning brief. One tested Python file, about 45 minutes.
minutes: 45
nextSystemSlug: ai-trading-desk-247
---

# The JARVIS Setup Guide

Most traders have twelve tabs open and still miss the one thing that mattered: the earnings date next week, the position sitting 1% above its stop, the headline that broke at 6am.

JARVIS fixes that. You text it like a person:

- "brief me"
- "how's NVDA looking?"
- "what's my risk right now?"
- "anything on my watchlist worth a closer look?"

…and it decides what to look up, pulls the real numbers with its own tools, and texts back a short answer with the evidence and the risk. It has **no trading tools**, so it can't place an order. It does the research; you make the call.

You need: Python 3.10+, an [Anthropic API key](https://console.anthropic.com/) (pay as you go; a few questions a day usually costs cents), and a free Telegram bot (step 3).

## How JARVIS thinks (the 4 parts)

**01 THE BRAIN.** Claude, with a strict system prompt: use tools for every number, lead with the answer, always name the risk and the counter-argument, never tell you to buy or sell, keep it short enough for a phone.

**02 THE TOOLS.** Five functions Claude can call on its own:

| Tool | What it returns |
|---|---|
| `get_quote` | close, % change, trend (20/50 EMA), RSI(14), ATR, volume vs average, 52-week range |
| `get_news` | the 5 latest headlines for a ticker |
| `get_earnings` | the next earnings date |
| `get_watchlist` | a one-line snapshot of every ticker you follow |
| `get_portfolio` | your positions with live P/L, distance to stop and dollars at risk |

Ask "should I worry about AAPL?" and Claude will usually call `get_quote`, `get_news`, `get_earnings` and `get_portfolio` before it says a word. You never tell it which tool to use.

**03 THE LOOP.** `ask_jarvis()` sends your question, runs whatever tools Claude asks for, hands the results back and repeats (up to 8 steps) until Claude has an answer. That loop is what turns a chatbot into an assistant.

**04 THE PHONE.** `run()` listens to your Telegram bot and **only answers your chat ID**, so nobody else can use your API key. `python jarvis.py brief` sends a morning brief on its own; put it on a schedule.

## Step 1: install

```bash
mkdir jarvis && cd jarvis
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install anthropic yfinance pandas requests
```

Save the full code at the bottom of this guide as `jarvis.py`.

## Step 2: tell it what you follow

Edit `WATCHLIST` at the top of `jarvis.py`. Then create `portfolio.json` next to it with your real positions (or skip it; JARVIS will tell you it's missing):

```json
[
  {"ticker": "AAPL", "shares": 10, "entry": 210.50, "stop": 199.00},
  {"ticker": "MSFT", "shares": 5, "entry": 415.00, "stop": 398.00}
]
```

The stop is what makes "what's my risk right now?" useful: JARVIS adds up the dollars you'd lose if every stop hit.

## Step 3: make your Telegram bot (5 minutes)

1. In Telegram, message **@BotFather**, send `/newbot`, pick a name. Copy the token it gives you.
2. Send any message to your new bot.
3. Open `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` in a browser and copy the number under `"chat":{"id":…}`. That's your chat ID.

## Step 4: set your keys and wake it up

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export TELEGRAM_BOT_TOKEN="123456:ABC..."
export TELEGRAM_CHAT_ID="987654321"
python jarvis.py
```

Text your bot "brief me". (Windows: use `set` instead of `export`.) Never paste your keys into the code or share them.

## Step 5: the morning brief, automatically

The brief prompt (`BRIEF` in the code) asks for: market mood from SPY and QQQ, the 2 tickers worth a closer look and why, any position near its stop or with earnings this week, and one thing to be careful about.

To get it every weekday at 8:45am without asking, add this with `crontab -e`:

```
45 8 * * 1-5 cd /path/to/jarvis && venv/bin/python jarvis.py brief
```

To keep the chat side running all day, leave `python jarvis.py` running on an always-on machine or a host like Replit (Reserved VM) with the three keys stored as secrets.

## Questions that get great answers

- "Brief me."
- "How's NVDA looking? Trend, momentum and anything in the news."
- "Which of my positions is closest to its stop?"
- "Does anything on my watchlist report earnings this week?"
- "Give me the bear case for MSFT using the data."
- "Compare AAPL and AMZN on trend and RSI."

## Make it yours

- **Add a tool.** Write a function, add it to `TOOLS` (name, description, input schema) and `HANDLERS`. Claude starts using it right away. Ideas: sector performance, options open interest, your own trading journal.
- **Change its personality.** Edit `SYSTEM`. Stricter, shorter, more skeptical: it follows the rules you write.
- **Keep it honest.** Leave the "use your tools for every number" rule in. It's the difference between an assistant and a guesser.

## Important

This is educational code, not financial advice. Yahoo Finance data can be delayed or wrong, and AI can misread it. JARVIS has no ability to trade; you make every decision. Test it for a few weeks and check its answers against your charts before you rely on it.

## The full code: jarvis.py

```python
"""JARVIS for the stock market: a Claude research assistant you text from your phone.
Ask it anything ("how's NVDA looking?", "brief me", "what's my risk right now?") and it pulls
live data with its own tools, then answers in plain English. Send /brief for the morning briefing.
Educational code. Not financial advice. JARVIS has no trading tools: it can't place orders.

pip install anthropic yfinance pandas requests
Env vars: ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
"""
import json
import os
import time

import anthropic
import pandas as pd
import requests

WATCHLIST = ["SPY", "QQQ", "AAPL", "MSFT", "NVDA", "AMZN"]
PORTFOLIO_FILE = "portfolio.json"   # [{"ticker": "AAPL", "shares": 10, "entry": 210.5, "stop": 199}]
MODEL = "claude-opus-5-5"

client = anthropic.Anthropic() if os.environ.get("ANTHROPIC_API_KEY") else None

SYSTEM = """You are JARVIS, a calm, sharp research assistant for a self-directed stock trader.
Rules:
- Use your tools for every number. Never invent a price, level, date or headline.
- Lead with the answer in one line, then the evidence, then what would change your view.
- Name the risk and the counter-argument every time. No hype words.
- You never tell the user to buy or sell and you cannot place trades. The user decides.
- Keep replies under 180 words; they're read on a phone. Plain text, no markdown tables."""

TOOLS = [
    {"name": "get_quote", "description": "Latest daily close, % change, trend (20/50 EMA), RSI(14), ATR, volume vs average and 52-week range for one ticker.",
     "input_schema": {"type": "object", "properties": {"ticker": {"type": "string"}}, "required": ["ticker"]}},
    {"name": "get_news", "description": "Up to 5 recent headlines for one ticker, with publisher.",
     "input_schema": {"type": "object", "properties": {"ticker": {"type": "string"}}, "required": ["ticker"]}},
    {"name": "get_earnings", "description": "Next scheduled earnings date for one ticker, if known.",
     "input_schema": {"type": "object", "properties": {"ticker": {"type": "string"}}, "required": ["ticker"]}},
    {"name": "get_watchlist", "description": "One-line snapshot (close, % change, trend) of every ticker on the watchlist.",
     "input_schema": {"type": "object", "properties": {}}},
    {"name": "get_portfolio", "description": "The user's open positions with live P/L, distance to stop and dollars at risk.",
     "input_schema": {"type": "object", "properties": {}}},
]


# ---- data tools (Yahoo Finance via yfinance) ----
def history(ticker: str) -> pd.DataFrame:
    import yfinance as yf
    df = yf.download(ticker, period="1y", interval="1d", auto_adjust=True, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df.dropna()


def quote(df: pd.DataFrame, ticker: str) -> dict:
    c = df["Close"]
    d = c.diff()
    rsi = 100 - 100 / (1 + d.clip(lower=0).rolling(14).mean() / (-d.clip(upper=0)).rolling(14).mean())
    tr = pd.concat([df.High - df.Low, (df.High - c.shift()).abs(), (df.Low - c.shift()).abs()], axis=1).max(axis=1)
    ema20, ema50 = c.ewm(span=20).mean().iloc[-1], c.ewm(span=50).mean().iloc[-1]
    last = float(c.iloc[-1])
    return {"ticker": ticker.upper(), "date": str(df.index[-1].date()), "close": round(last, 2),
            "change_pct": round(float(c.pct_change().iloc[-1] * 100), 2),
            "trend": "up" if last > ema20 > ema50 else "down" if last < ema20 < ema50 else "mixed",
            "ema20": round(float(ema20), 2), "ema50": round(float(ema50), 2),
            "rsi14": round(float(rsi.iloc[-1]), 1), "atr14": round(float(tr.rolling(14).mean().iloc[-1]), 2),
            "volume_vs_avg": round(float(df.Volume.iloc[-1] / df.Volume.rolling(20).mean().iloc[-1]), 2),
            "high_52w": round(float(df.High.max()), 2), "low_52w": round(float(df.Low.min()), 2)}


def get_quote(ticker: str) -> dict:
    return quote(history(ticker), ticker)


def get_news(ticker: str) -> list:
    import yfinance as yf
    out = []
    for item in (yf.Ticker(ticker).news or [])[:5]:
        c = item.get("content", item)
        out.append({"title": c.get("title"), "publisher": (c.get("provider") or {}).get("displayName", c.get("publisher"))})
    return out


def get_earnings(ticker: str) -> dict:
    import yfinance as yf
    try:
        dates = yf.Ticker(ticker).calendar.get("Earnings Date") or []
        return {"ticker": ticker.upper(), "next_earnings": str(dates[0]) if dates else "unknown"}
    except Exception:
        return {"ticker": ticker.upper(), "next_earnings": "unknown"}


def get_watchlist() -> list:
    rows = []
    for t in WATCHLIST:
        q = get_quote(t)
        rows.append({k: q[k] for k in ("ticker", "close", "change_pct", "trend", "rsi14")})
    return rows


def get_portfolio() -> list:
    if not os.path.exists(PORTFOLIO_FILE):
        return [{"note": f"No {PORTFOLIO_FILE} found. Add your positions to track risk."}]
    rows = []
    for p in json.load(open(PORTFOLIO_FILE)):
        price = get_quote(p["ticker"])["close"]
        rows.append({"ticker": p["ticker"], "shares": p["shares"], "entry": p["entry"], "price": price,
                     "pl_dollars": round((price - p["entry"]) * p["shares"], 2),
                     "pct_to_stop": round((price - p["stop"]) / price * 100, 2),
                     "dollars_at_risk": round(max(price - p["stop"], 0) * p["shares"], 2)})
    return rows


HANDLERS = {"get_quote": get_quote, "get_news": get_news, "get_earnings": get_earnings,
            "get_watchlist": get_watchlist, "get_portfolio": get_portfolio}


# ---- the brain: Claude decides which tools to call, then answers ----
def ask_jarvis(question: str, max_steps: int = 8) -> str:
    if client is None:
        return "Set ANTHROPIC_API_KEY to wake JARVIS up."
    messages = [{"role": "user", "content": question}]
    for _ in range(max_steps):
        response = client.messages.create(model=MODEL, max_tokens=2000, output_config={"effort": "medium"},
                                          system=SYSTEM, tools=TOOLS, messages=messages)
        if response.stop_reason == "refusal":
            return "JARVIS declined that one. Try asking it a different way."
        if response.stop_reason != "tool_use":
            return "".join(b.text for b in response.content if b.type == "text")
        messages.append({"role": "assistant", "content": response.content})
        results = []
        for b in response.content:
            if b.type != "tool_use":
                continue
            try:
                out = HANDLERS[b.name](**b.input)
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(out, default=str)})
            except Exception as e:
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": f"Error: {e}", "is_error": True})
        messages.append({"role": "user", "content": results})
    return "JARVIS ran out of steps. Ask a narrower question."


BRIEF = ("Morning brief. Check my watchlist and my portfolio. Give me: 1) the market mood from SPY and QQQ, "
         "2) the 2 tickers worth a closer look today and why, 3) any position close to its stop or with earnings "
         "this week, 4) one thing to be careful about. Short lines.")


# ---- the phone: Telegram long polling ----
def telegram(method: str, **params) -> dict:
    url = f"https://api.telegram.org/bot{os.environ['TELEGRAM_BOT_TOKEN']}/{method}"
    return requests.post(url, json=params, timeout=40).json()


def reply_to(text: str) -> str:
    text = text.strip()
    if text.lower() in ("/brief", "brief me", "/start"):
        return ask_jarvis(BRIEF)
    return ask_jarvis(text)


def run() -> None:
    me = str(os.environ["TELEGRAM_CHAT_ID"])
    offset = None
    print("JARVIS online. Text your bot.")
    while True:
        updates = telegram("getUpdates", timeout=30, offset=offset).get("result", [])
        for u in updates:
            offset = u["update_id"] + 1
            msg = u.get("message") or {}
            chat = str(msg.get("chat", {}).get("id"))
            if chat != me or "text" not in msg:   # only answer YOU
                continue
            telegram("sendChatAction", chat_id=chat, action="typing")
            answer = reply_to(msg["text"])
            telegram("sendMessage", chat_id=chat, text=answer + "\n\nResearch only. You make every decision.")
        time.sleep(1)


if __name__ == "__main__":
    import sys
    if sys.argv[1:] == ["brief"]:   # cron this at 8:45am for a morning brief without asking
        telegram("sendMessage", chat_id=os.environ["TELEGRAM_CHAT_ID"], text=ask_jarvis(BRIEF))
    else:
        run()
```

## The next problem

JARVIS answers questions. It doesn't watch the market for you while you sleep, argue every idea from six angles, or read your charts. **Solo Trader's AI Desk** gives you all four systems: AI Trading Desk 24/7, TradingView + Claude Chart Analyst, the AI Hedge Fund Blueprint and the Free Bloomberg Terminal Setup, plus 20 bonus systems. $1,166 combined listed value. Your price: $199 until Dec 1, 2026, then $349. Follow Live-in-60; not running in 7 days? Email support@milli-ai.com for a full refund and keep your downloads. [Get your complete trading AI desk]({{offerUrl}}).
