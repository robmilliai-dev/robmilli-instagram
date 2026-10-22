---
title: The POLYBOT 6-Agent Setup Guide
promise: Build a 6-agent AI research team for Polymarket. Scout, Odds, News, Thesis, Risk and Execution scan the busiest markets, verify the catalyst, argue both sides, size the position and send you one ticket to approve. One tested Python file, about 40 minutes.
minutes: 40
nextSystemSlug: ai-hedge-fund-blueprint
---

# The POLYBOT 6-Agent Setup Guide

You've seen the screenshots: a Polymarket bot that reportedly turned $150 into $279,053. That's the original creator's self-reported claim, not mine, and nobody has independently verified it. What you *can* copy is the structure behind bots like that: not one AI guessing, but a team where every agent has one job and any of them can kill the trade.

This guide gives you that team in one Python file:

**SCOUT → ODDS → NEWS → THESIS → RISK → EXECUTION**

It reads live Polymarket data, uses Claude to research and argue each idea, and sends you a ticket that ends in **READY FOR YOUR REVIEW** or **BLOCKED BY RISK**. It never places a bet. You approve every one.

You need: Python 3.10+, an [Anthropic API key](https://console.anthropic.com/) (pay as you go; a run of 3 markets with web search usually costs well under a dollar), and optionally a free Telegram bot so tickets land on your phone. Check that Polymarket is available where you live before you trade on it.

## The six agents (what each one does)

**01 SCOUT finds the opportunity.** `scout()` pulls the 100 most active markets from Polymarket's free public API and flags three things:
- **VOLUME SPIKE:** 24-hour volume at least 2× its daily average for the week.
- **ODDS MOVING:** the price moved 5+ points in a day.
- **CATALYST AHEAD:** the market resolves within 14 days.

It keeps simple YES/NO markets only and passes the top 3 to the team.

**02 NEWS checks what everyone else missed.** `news_agent()` gives Claude the web search tool and one job: find the latest reporting that could move this market, and only count a fact if it can name the **source** and the **timestamp**. Every report ends in `VERIFIED`, `RUMOR` or `NOTHING NEW`. Rumors get blocked later.

**03 THESIS builds both sides.** `thesis_agent()` reads the market's resolution rules and the news report, then returns structured JSON: a probability estimate, the **YES case**, the **NO case** and the **invalidation rule** (the one thing that kills the trade). It's told to stay close to the market price when the news is thin.

**04 ODDS looks for the gap.** `odds_agent()` compares the market price with the team's estimate. Market says 42%, team says 57%? That's a +15 point edge on YES. If the team thinks YES is overpriced, it flips to the NO side automatically.

**05 RISK can cancel any trade.** `risk_agent()` sizes the stake with quarter-Kelly, capped at `MAX_STAKE_PCT` of your bankroll, then runs six checks. Any failure is a veto:

| Check | Default |
|---|---|
| Edge | at least 5 points |
| Liquidity | at least $50,000 |
| Time left | more than 1 day |
| News | not a rumor |
| Thesis confidence | not low |
| Stake | above $0 |

**06 EXECUTION only acts when the team agrees.** `execution_agent()` writes the ticket. If every check passed, it reads `✅ TEAM AGREES: READY FOR YOUR REVIEW` with the side, shares, price, stake and max loss. If not, it says exactly which check blocked it. Either way: *"Nothing has been placed. You decide."*

Every run is logged to `polybot_log.csv`, so after a month you can grade the team: how often was its estimate closer than the market's?

## Step 1: install

```bash
mkdir polybot && cd polybot
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install anthropic requests
```

Save the full code at the bottom of this guide as `polybot.py`.

## Step 2: set your rules

At the top of the file:

- `BANKROLL`: the money you've set aside for prediction markets (not your rent).
- `MAX_STAKE_PCT`: the most any single market can get. 2% is a sane start.
- `MIN_EDGE`, `MIN_LIQUIDITY`, `MIN_DAYS_LEFT`: tighten these to see fewer, cleaner tickets.

## Step 3: run it

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
python polybot.py
```

(Windows: `set` instead of `export`.) Tickets print in your terminal. To get them on your phone, make a Telegram bot with @BotFather, then set `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` (send your bot a message, then open `https://api.telegram.org/bot<TOKEN>/getUpdates` to find the chat ID).

## Step 4: run it every hour

With cron (`crontab -e`):

```
0 * * * * cd /path/to/polybot && venv/bin/python polybot.py
```

Or use a scheduled job on Replit or GitHub Actions with the keys stored as secrets. Never paste keys into the code.

## Example ticket

```
✅ TEAM AGREES: READY FOR YOUR REVIEW

Will the Fed cut rates in December?
SCOUT: VOLUME SPIKE · ODDS MOVING · CATALYST AHEAD
ODDS: market 42% vs team 57% on YES (edge +15%)
NEWS: CATALYST: CPI cooler than expected
YES CASE: Cooling inflation
NO CASE: Strong jobs data
KILL RULE: Hot CPI print before the meeting
TICKET: YES · ~47 shares @ 0.42 · stake $20.0 · max loss $20.0

Nothing has been placed. You decide.
```

(Illustrative example from a test run, not a real market call.)

## Make it yours

- **Change what Scout hunts for.** Filter by tag (politics, sports, crypto) or raise the volume-spike threshold.
- **Give Thesis your edge.** Add your own notes or data sources to the prompt.
- **Make Risk stricter.** Add a max number of open positions, or block markets that resolve on a single person's decision.

## Important

Educational code, not financial advice. Prediction markets can go to zero for the side you pick, and AI estimates can be badly wrong. The $279,053 figure is a third party's self-reported, unverified claim and says nothing about what you'll make. POLYBOT never places orders; you make every decision.

## The full code: polybot.py

```python
"""POLYBOT: a 6-agent research team for Polymarket.
SCOUT finds markets with unusual activity -> NEWS verifies the catalyst on the web ->
THESIS builds the YES case, the NO case and the rule that kills the trade -> ODDS measures the gap ->
RISK can veto anything -> EXECUTION writes a ticket for YOU to approve. It never places a bet.
Educational code. Not financial advice. Check that Polymarket is available where you live.

pip install anthropic requests
Env vars: ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID (optional)
"""
import csv
import datetime as dt
import json
import os

import anthropic
import requests

GAMMA = "https://gamma-api.polymarket.com"   # Polymarket's public, read-only market data
BANKROLL = 1_000          # dollars set aside for prediction markets
MAX_STAKE_PCT = 2.0       # never more than this % of bankroll on one market
MIN_EDGE = 0.05           # team estimate must differ from the market by 5+ points
MIN_LIQUIDITY = 50_000    # skip thin markets you can't get out of
MIN_DAYS_LEFT = 1         # skip markets resolving in under a day
MODEL = "claude-opus-5-5"
LOG_FILE = "polybot_log.csv"

client = anthropic.Anthropic() if os.environ.get("ANTHROPIC_API_KEY") else None


def _num(x, default=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def _list(x):
    return json.loads(x) if isinstance(x, str) else (x or [])


# 01 SCOUT: scan the most active markets for unusual volume, moving odds and a catalyst ahead
def fetch_markets(limit: int = 100) -> list:
    r = requests.get(f"{GAMMA}/markets", params={"active": "true", "closed": "false", "limit": limit,
                                                  "order": "volume24hr", "ascending": "false"}, timeout=20)
    r.raise_for_status()
    return r.json()


def scout(markets: list, top: int = 3) -> list:
    now = dt.datetime.now(dt.timezone.utc)
    picks = []
    for m in markets:
        outcomes, prices = _list(m.get("outcomes")), [_num(p) for p in _list(m.get("outcomePrices"))]
        if outcomes != ["Yes", "No"] or len(prices) != 2:
            continue
        try:
            end = dt.datetime.fromisoformat(m["endDate"].replace("Z", "+00:00"))
        except (KeyError, ValueError):
            continue
        days_left = (end - now).total_seconds() / 86400
        vol24, vol_week = _num(m.get("volume24hr")), _num(m.get("volume1wk"))
        volume_spike = vol24 / (vol_week / 7) if vol_week else 0
        odds_move = abs(_num(m.get("oneDayPriceChange")))
        flags = [f for f, hit in (("VOLUME SPIKE", volume_spike >= 2), ("ODDS MOVING", odds_move >= 0.05),
                                  ("CATALYST AHEAD", 0 < days_left <= 14)) if hit]
        if not flags:
            continue
        picks.append({"question": m.get("question"), "slug": m.get("slug"), "yes_price": prices[0],
                      "liquidity": _num(m.get("liquidityNum", m.get("liquidity"))), "volume24h": vol24,
                      "volume_spike": round(volume_spike, 1), "odds_move_24h": round(odds_move, 3),
                      "days_left": round(days_left, 1), "end_date": m["endDate"], "flags": flags,
                      "description": (m.get("description") or "")[:1500]})
    return sorted(picks, key=lambda p: (len(p["flags"]), p["volume_spike"]), reverse=True)[:top]


# 02 NEWS: search the web, check source + timestamp, block rumors
NEWS_RULES = """You are NEWS on a prediction-market research team. Search the web for the latest
reporting that could move this market. Only count a fact if you can name the source and when it was published.
Reply in this exact format:
CATALYST: <one line, or NONE>
SOURCE: <outlet + date, or NONE>
STATUS: VERIFIED | RUMOR | NOTHING NEW
NOTES: <2-3 lines, plain English>"""


def news_agent(market: dict) -> str:
    messages = [{"role": "user", "content": f"Market: {market['question']}\nResolves: {market['end_date']}\nRules: {market['description']}"}]
    for _ in range(3):   # web search runs server-side; resume if the server pauses a long search
        response = client.messages.create(model=MODEL, max_tokens=3000, output_config={"effort": "medium"},
                                          system=NEWS_RULES, messages=messages,
                                          tools=[{"type": "web_search_20260209", "name": "web_search", "max_uses": 5}])
        if response.stop_reason != "pause_turn":
            break
        messages = messages[:1] + [{"role": "assistant", "content": response.content}]
    if response.stop_reason == "refusal":
        return "STATUS: NOTHING NEW\nNOTES: News agent declined."
    return "".join(b.text for b in response.content if b.type == "text").strip()


# 03 THESIS: both sides plus the rule that kills the trade, and a probability estimate
THESIS_RULES = """You are THESIS on a prediction-market research team. Using ONLY the market rules and the
news report you're given, estimate the probability the market resolves YES. Argue both sides honestly.
Be calibrated: if the news is thin or a rumor, stay close to the market price. Never state certainty."""
THESIS_SCHEMA = {
    "type": "object",
    "properties": {
        "probability_yes": {"type": "number"},
        "yes_case": {"type": "string"},
        "no_case": {"type": "string"},
        "invalidation_rule": {"type": "string"},
        "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
    },
    "required": ["probability_yes", "yes_case", "no_case", "invalidation_rule", "confidence"],
    "additionalProperties": False,
}


def thesis_agent(market: dict, news: str) -> dict:
    payload = {k: market[k] for k in ("question", "yes_price", "end_date", "description")}
    response = client.messages.create(
        model=MODEL, max_tokens=2000, system=THESIS_RULES,
        output_config={"effort": "medium", "format": {"type": "json_schema", "schema": THESIS_SCHEMA}},
        messages=[{"role": "user", "content": f"MARKET:\n{json.dumps(payload)}\n\nNEWS REPORT:\n{news}"}])
    if response.stop_reason == "refusal":
        return {"probability_yes": market["yes_price"], "yes_case": "-", "no_case": "-",
                "invalidation_rule": "-", "confidence": "low"}
    t = json.loads("".join(b.text for b in response.content if b.type == "text"))
    t["probability_yes"] = min(max(float(t["probability_yes"]), 0.01), 0.99)
    return t


# 04 ODDS: the gap between the market price and the team's estimate
def odds_agent(market: dict, thesis: dict) -> dict:
    yes, est = market["yes_price"], thesis["probability_yes"]
    side = "YES" if est > yes else "NO"
    price = yes if side == "YES" else 1 - yes            # cost of one share of that side
    win_prob = est if side == "YES" else 1 - est
    return {"side": side, "market_price": round(price, 3), "team_estimate": round(win_prob, 3),
            "edge": round(win_prob - price, 3)}


# 05 RISK: can veto anything. Sizing = quarter-Kelly, capped at MAX_STAKE_PCT of bankroll
def risk_agent(market: dict, odds: dict, thesis: dict, news: str) -> dict:
    p, q = odds["team_estimate"], odds["market_price"]
    kelly = max((p - q) / (1 - q), 0) if q < 1 else 0
    stake = round(min(kelly / 4, MAX_STAKE_PCT / 100) * BANKROLL, 2)
    checks = {
        "edge >= 5 points": odds["edge"] >= MIN_EDGE,
        "liquidity >= $50k": market["liquidity"] >= MIN_LIQUIDITY,
        "resolves in > 1 day": market["days_left"] >= MIN_DAYS_LEFT,
        "news is not a rumor": "STATUS: RUMOR" not in news,
        "thesis confidence not low": thesis["confidence"] != "low",
        "stake > $0": stake > 0,
    }
    return {"checks": checks, "passed": all(checks.values()), "stake": stake,
            "max_loss": stake, "shares": int(stake / q) if q else 0}


# 06 EXECUTION: only acts when every check passes, and even then it asks YOU
def execution_agent(market: dict, odds: dict, thesis: dict, risk: dict, news: str) -> str:
    failed = [k for k, ok in risk["checks"].items() if not ok]
    head = "✅ TEAM AGREES: READY FOR YOUR REVIEW" if risk["passed"] else "⛔ BLOCKED BY RISK: " + ", ".join(failed)
    lines = [head, "", market["question"], f"https://polymarket.com/market/{market['slug']}", "",
             f"SCOUT: {' · '.join(market['flags'])}",
             f"ODDS: market {odds['market_price']:.0%} vs team {odds['team_estimate']:.0%} on {odds['side']} (edge {odds['edge']:+.0%})",
             f"NEWS: {news.splitlines()[0] if news else 'none'}",
             f"YES CASE: {thesis['yes_case']}", f"NO CASE: {thesis['no_case']}",
             f"KILL RULE: {thesis['invalidation_rule']}"]
    if risk["passed"]:
        lines.append(f"TICKET: {odds['side']} · ~{risk['shares']} shares @ {odds['market_price']:.2f} · stake ${risk['stake']} · max loss ${risk['max_loss']}")
    lines += ["", "Nothing has been placed. You decide."]
    return "\n".join(lines)


def notify(text: str) -> None:
    token, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if token and chat:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={"chat_id": chat, "text": text}, timeout=15)
    else:
        print(text, "\n" + "-" * 60)


def log(row: dict) -> None:
    new = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(row))
        if new:
            w.writeheader()
        w.writerow(row)


def run(fetch=fetch_markets) -> None:
    if client is None:
        raise SystemExit("Set ANTHROPIC_API_KEY first.")
    for market in scout(fetch()):
        news = news_agent(market)
        thesis = thesis_agent(market, news)
        odds = odds_agent(market, thesis)
        risk = risk_agent(market, odds, thesis, news)
        notify(execution_agent(market, odds, thesis, risk, news))
        log({"time": dt.datetime.now().isoformat(timespec="minutes"), "market": market["question"],
             "side": odds["side"], "market_price": odds["market_price"], "team_estimate": odds["team_estimate"],
             "edge": odds["edge"], "risk_passed": risk["passed"], "stake": risk["stake"]})


if __name__ == "__main__":
    run()
```

## The next problem

POLYBOT argues one kind of market. The full desk runs the same team approach on stocks: the six-role AI Hedge Fund committee, a 24/7 scanner, a chart analyst that reads any screenshot and a free Bloomberg-style terminal. **Solo Trader's AI Desk** gives you all four systems: AI Trading Desk 24/7, TradingView + Claude Chart Analyst, the AI Hedge Fund Blueprint and the Free Bloomberg Terminal Setup, plus 20 bonus systems. $1,166 combined listed value. Your price: $199 until Dec 1, 2026, then $349. Follow Live-in-60; not running in 7 days? Email support@milli-ai.com for a full refund and keep your downloads. [Get your complete trading AI desk]({{offerUrl}}).
