---
name: pine-script-writer
description: Write TradingView Pine Script v6 indicators and strategies from plain English, then check them for the bugs that make Pine backtests lie (repainting, lookahead in request.security, signals on unconfirmed bars, missing commission). Adds alert conditions with webhook-ready JSON messages. Explains every input in plain words.
argument-hint: "[what you want on the chart]"
---

# PINE SCRIPT WRITER

Pine is easy to write and easy to fool yourself with. This writes it, then tries to break it.

## INTAKE

1. Indicator (draws things) or strategy (backtests trades)?
2. The rule in plain English. Or paste a strategy spec from `/strategy-to-bot-spec`.
3. Timeframe and market you'll use it on.
4. Do you want alerts? Sent where (phone, webhook to your bot/dashboard)?

## WRITE

- Start with `//@version=6`.
- `indicator()` or `strategy()` with an honest title and `overlay` set correctly.
- **Strategies always set:** `initial_capital`, `default_qty_type`, `commission_type` + `commission_value`, `slippage`, `process_orders_on_close=false`.
- Every tunable number is an `input.*()` with a plain-English `tooltip`.
- Plot only what helps: signal shapes, the key line(s), a background color for "in trade". Max 3 colors.
- `alertcondition()` (indicators) or `alert()` (strategies) with a JSON message:
  `{"symbol":"{{ticker}}","signal":"BUY","price":{{close}},"time":"{{timenow}}"}`

## CHECK (always, before showing the script)

| Check | Bad | Good |
|---|---|---|
| Repainting via higher timeframe | `request.security(sym, "D", close)` | `request.security(sym, "D", close[1], lookahead=barmerge.lookahead_on)` |
| Signals on live bar | `if crossover(...)` acting intrabar | Gate with `barstate.isconfirmed` for alerts |
| Future leak | `close` used to decide a fill at the same bar's open | Decide on bar close, fill next bar |
| Costs | No commission | Commission + slippage set |
| Too few trades | 8 trades over 5 years | Say "not enough trades", no verdict |
| Magic numbers | `ta.rsi(close, 37)` | Inputs with sane defaults and a reason |

Write a short "Checked" list under the code with ✓ or the fix applied.

## EXPLAIN

After the code: what each input does (one line each), how to add it (Pine Editor → paste → Save → Add to chart), how to make the alert (Alert → Condition: the script → message is pre-filled), and how to read the Strategy Tester (net profit, max drawdown, trades, profit factor; ignore everything else at first).

## HARD RULES

- **Never claim a backtest result you didn't see.** You can't run TradingView. Say "run it and paste me the Strategy Tester summary".
- **Never write a strategy with no stop or exit.**
- **Never use `lookahead_on` without the `[1]` offset.** That's the #1 fake-backtest bug.
- Educational only. Not financial advice.
