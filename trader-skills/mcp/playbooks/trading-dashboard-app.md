---
id: trading-dashboard-app
title: Build Your Trading Dashboard App
category: build
summary: Your own private dashboard on a link: watchlist, alert log via webhook, bot status with a KILL switch, weekly scoreboard. The exact starter prompt and the build order that avoids dead ends.
---

# TRADING DASHBOARD APP

Your bot runs somewhere. Your alerts land somewhere else. Your journal is a notes app. This puts all of it on one link.

## WHAT YOU'LL HAVE

- A private web app with sign-in (only you can see it)
- Watchlist with prices (delayed free data is fine)
- Alert log: every TradingView/bot alert, time-stamped (via a webhook URL)
- Bot status card: last run, last trade, today's P&L, KILL button that writes a stop flag
- Weekly scoreboard (fed by `/account-stats --format json` or a CSV upload)
- Works on your phone

## BUILD ORDER (this order avoids 90% of dead ends)

1. **Shell + sign-in first.** Nothing else until login works on your phone.
2. **Database tables:** `alerts`, `trades`, `bot_status`, `watchlist`. Have the builder show you the schema before writing pages.
3. **Webhook endpoint** for alerts, protected by a secret in the URL or header. Test it with curl before connecting TradingView.
4. **Pages:** Watchlist → Alerts → Bot → Scoreboard.
5. **KILL switch last,** and test it 3 times.
6. Deploy. Open on your phone. Add to home screen.

## THE STARTER PROMPT (paste into your builder)

```text
Build a private, mobile-first trading dashboard web app.

Must have:
- Email sign-in. Only signed-in users see anything. One user (me) for now.
- Tables: watchlist(symbol), alerts(id, received_at, source, symbol, message),
  trades(id, closed_at, symbol, side, qty, entry, exit, pnl),
  bot_status(updated_at, last_run, last_trade, day_pnl, kill boolean).
- POST /api/alerts?secret=<ALERT_SECRET> accepts JSON {symbol, message, source}
  and stores it. Reject wrong secret with 401. Read ALERT_SECRET from env.
- POST /api/bot-status?secret=<BOT_SECRET> lets my bot report status.
- GET /api/kill?secret=<BOT_SECRET> returns {"kill": true|false} so my bot can check it.
- Pages: Watchlist (add/remove symbols, show last price from a free delayed source,
  cache 60s), Alerts (newest first, filter by symbol), Bot (status card + big red
  KILL toggle with a confirm step), Scoreboard (upload trades CSV; show trades,
  win rate, average win vs loss, profit factor, worst drop, equity curve chart).
- Dark theme, big text, works one-handed on a phone.
- Never store broker API keys in the database or show them in the UI.
  All secrets come from environment variables.
Show me the database schema and the list of pages before you write code.
```

## CONNECT THE PIECES

- **TradingView alert → app:** alert webhook URL `https://<your-app>/api/alerts?secret=<ALERT_SECRET>`, message `{"symbol":"{{ticker}}","message":"{{strategy.order.action}} at {{close}}","source":"tradingview"}`.
- **Your bot → app:** at the end of each run, POST status; at the start of each run, GET `/api/kill` and exit if true.
- **Scoreboard:** export closed trades from your broker as CSV and upload weekly.

## WHAT GOES WRONG (and the fix)

| Problem | Fix |
|---|---|
| Builder adds features you didn't ask for | "Stop. Only build step N. Show me before moving on." |
| Login works on desktop, not phone | Ask it to test the mobile viewport and cookies over HTTPS |
| Webhook 401s from TradingView | Secret in the URL must match env exactly; no quotes |
| Prices don't load | Free sources rate-limit. Cache 60s and show "delayed" |
| App sleeps and misses alerts | Use the builder's always-on/reserved option, or accept a small delay on first hit |

## HARD RULES

- **Broker keys never go in the app.** The dashboard reads what the bot reports. It never places orders.
- **Every write endpoint needs a secret.** An open webhook is an open door.
- **KILL means the bot checks and stops,** not that the app trades. Test it before you rely on it.
- Educational only. Not financial advice.
