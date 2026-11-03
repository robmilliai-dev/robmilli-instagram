---
title: The Milli Dots Indicators
promise: Two free TradingView indicators we built and then tried to break. Buy dots, exit dots and phone alerts. Copy, paste, done in 2 minutes.
minutes: 10
nextSystemSlug: tradingview-claude-chart-analyst
---

# The Milli Dots Indicators

Two free TradingView indicators. Paste them in, and blue dots show up on your chart when the setup happens.

**When you're done you'll have:**
- **Pullback Dots** on your daily charts (buy the sharp dip, only in an uptrend)
- **Trend Dots** on your daily or 4-hour charts (buy the breakout, ride it with a trailing stop)
- A phone alert every time a new dot shows up

**How it works:** Paste the code → blue dot on the setup → phone alert → exit dot or red stop line

> **READ FIRST:** Pullback Dots: daily charts only. A dot is a setup, not a promise. Risk small: we tested 1% per trade.

## Why this works

We locked the settings using 2010 to 2019 data only. Then we tested on 2020 to now: years the indicators had never seen.

- **Pullback Dots, S&P 500 futures, daily:** 27 of 33 trades won (82%). Worst drop: -2.4% risking 1% per trade.
- **Pullback Dots, all 43 markets:** profitable on 34. It lost on 9, including COST, META, AMZN and gold futures.
- **Trend Dots, daily:** profitable on 41 of 43 markets. It lost on EURUSD and TLT.
- **Trend Dots, gold 4-hour (Jun 2024 to now):** 26 of 48 trades won (54%). Worst drop: -4.5%.

Pullback Dots failed our 4-hour test, so use it on **daily charts only**.

## Step 1: Add Pullback Dots (2 minutes)

1. Open [TradingView](https://www.tradingview.com/) on a computer and open any chart.
2. Click **Pine Editor** at the bottom of the screen.
3. Delete everything in the editor. Paste the code below.
4. Click **Save**, then **Add to chart**.
5. Switch the chart to **1D** (daily).

```pine
//@version=6
// Milli Pullback Dots by Milli.ai (DAILY charts: the 4-hour version did not hold up in testing)
// Buy dot: 50 EMA above 200 EMA, price above the 200 EMA, and RSI(2) under 5 (a sharp dip inside an uptrend).
// Exit: first close above the 5 EMA (next bar's open), or a 2 x ATR(14) stop set at entry.
// Settings were picked on 2010-2019 data only, then tested on 2020-2026 data they never saw.
// Educational tool. Hypothetical backtests. Not financial advice. Past results do not guarantee future results.
strategy("Milli Pullback Dots", overlay = true, initial_capital = 10000, commission_type = strategy.commission.percent,
     commission_value = 0.05, process_orders_on_close = false)

rsiLen  = input.int(2, "RSI length", minval = 1)
lo      = input.float(5, "Buy when RSI below", minval = 1)
k       = input.float(2.0, "Stop (x ATR 14)", minval = 0.5, step = 0.5)
exitLen = input.int(5, "Exit when close crosses this EMA", minval = 1)
riskPct = input.float(1.0, "Risk per trade (% of equity)", minval = 0.1, step = 0.1)
maxLev  = input.float(5.0, "Max position (x equity)", minval = 0.1)

r   = ta.rsi(close, rsiLen)
e50 = ta.ema(close, 50)
e200 = ta.ema(close, 200)
ex  = ta.ema(close, exitLen)
atr = ta.atr(14)
warm = bar_index > 200
buySig = warm and e50 > e200 and close > e200 and r < lo
flat = strategy.position_size == 0

var float stopPx = na
if flat and buySig
    stopPx := close - k * atr
    qty = math.min(strategy.equity * riskPct / 100 / (k * atr), strategy.equity * maxLev / close)
    strategy.entry("Long", strategy.long, qty = qty)
if strategy.position_size > 0
    strategy.exit("Stop", "Long", stop = stopPx)
    if close > ex
        strategy.close("Long", comment = "Exit dot")

plot(e200, "200 EMA", color.new(color.gray, 40))
plotshape(flat and buySig, "Buy dot", shape.circle, location.belowbar, color.new(#3987e5, 0), size = size.small)
plotshape(strategy.position_size > 0 and close > ex, "Exit dot", shape.xcross, location.abovebar, color.new(color.orange, 0), size = size.tiny)
if flat and buySig
    alert("Milli Pullback Dots: BUY dot on " + syminfo.ticker + " at " + str.tostring(close), alert.freq_once_per_bar_close)
```

## Step 2: Add Trend Dots (2 minutes)

Same steps. Open a new Pine Editor tab, paste this, Save, Add to chart.

```pine
//@version=6
// Milli Trend Dots by Milli.ai
// Buy dot: close breaks the highest high of the last 20 bars while price is above the 200 EMA.
// Exit: a 3 x ATR(14) trailing stop that only moves in your favour (the red line). One trade at a time.
// Settings were picked on 2010-2019 data only, then tested on 2020-2026 data they never saw.
// Educational tool. Hypothetical backtests. Not financial advice. Past results do not guarantee future results.
strategy("Milli Trend Dots", overlay = true, initial_capital = 10000, commission_type = strategy.commission.percent,
     commission_value = 0.05, process_orders_on_close = false, calc_on_every_tick = false)

n        = input.int(20, "Breakout lookback (bars)", minval = 2)
emaLen   = input.int(200, "Trend filter EMA", minval = 1)
k        = input.float(3.0, "Trailing stop (x ATR 14)", minval = 0.5, step = 0.5)
riskPct  = input.float(1.0, "Risk per trade (% of equity)", minval = 0.1, step = 0.1)
maxLev   = input.float(5.0, "Max position (x equity)", minval = 0.1)
allowShort = input.bool(false, "Also take sell dots (off in the tested version)")

ema = ta.ema(close, emaLen)
hh  = ta.highest(high, n)[1]
ll  = ta.lowest(low, n)[1]
atr = ta.atr(14)
warm = bar_index > math.max(n, emaLen)

buySig  = warm and close > hh and close[1] <= hh[1] and close > ema
sellSig = warm and allowShort and close < ll and close[1] >= ll[1] and close < ema

var float trail = na
flat = strategy.position_size == 0

if flat and buySig
    stopPx = close - k * atr
    qty = math.min(strategy.equity * riskPct / 100 / (k * atr), strategy.equity * maxLev / close)
    strategy.entry("Long", strategy.long, qty = qty)
    trail := stopPx
else if flat and sellSig
    stopPx = close + k * atr
    qty = math.min(strategy.equity * riskPct / 100 / (k * atr), strategy.equity * maxLev / close)
    strategy.entry("Short", strategy.short, qty = qty)
    trail := stopPx

if strategy.position_size > 0
    trail := math.max(nz(trail, close - k * atr), close - k * atr)
    strategy.exit("Long exit", "Long", stop = trail)
else if strategy.position_size < 0
    trail := math.min(nz(trail, close + k * atr), close + k * atr)
    strategy.exit("Short exit", "Short", stop = trail)
else if not (buySig or sellSig)
    trail := na

plot(ema, "Trend EMA", color.new(color.gray, 40))
plot(strategy.position_size != 0 ? trail : na, "Trailing stop", color.new(color.red, 0), 2, plot.style_linebr)
plotshape(flat and buySig, "Buy dot", shape.circle, location.belowbar, color.new(#3987e5, 0), size = size.small)
plotshape(flat and sellSig, "Sell dot", shape.circle, location.abovebar, color.new(#e66767, 0), size = size.small)
if flat and buySig
    alert("Milli Trend Dots: BUY dot on " + syminfo.ticker + " " + timeframe.period + " at " + str.tostring(close), alert.freq_once_per_bar_close)
if flat and sellSig
    alert("Milli Trend Dots: SELL dot on " + syminfo.ticker + " " + timeframe.period + " at " + str.tostring(close), alert.freq_once_per_bar_close)
```

## Step 3: Read the dots

- **Blue dot under a candle:** the setup happened. That's the signal.
- **Orange x (Pullback Dots):** the bounce came. That's the exit.
- **Red line (Trend Dots):** the trailing stop. If price closes under it, the trade is over.
- **Strategy Tester tab:** shows how the dots did on the chart you're looking at. Try your own tickers.

## Step 4: Get a phone alert for every new dot

1. Click the **alarm clock** (Alerts) on the right.
2. Condition: pick **Milli Pullback Dots** (or Trend Dots), then **alert() function calls only**.
3. Turn on **Notify in app**. Click **Create**.
4. Install the TradingView app on your phone and log in. New dots now ping your phone.

## Your first run checklist

- [ ] Both indicators are on your chart
- [ ] You can see at least one blue dot when you scroll back
- [ ] Your phone got a test alert

## Troubleshooting

| Problem | Fix |
|---|---|
| No dots on the chart | Switch to the 1D chart and scroll back. Dots only show in an uptrend. |
| "Script could not be translated" error | Delete everything in the Pine Editor first, then paste. Line 1 must be //@version=6. |
| Alert doesn't fire | Pick "alert() function calls only" in the alert condition. |

## Keep it safe

- Risk a small amount per trade. We tested 1% of the account.
- A dot is a setup, not a promise. Some dots lose. That's in the numbers above.
- Use it on the timeframes we tested: Pullback Dots daily only.

> Hypothetical backtests on Yahoo Finance prices, next-bar entries, costs included. Past results don't guarantee future results. Educational tool, not financial advice. You make every decision.

## Want it done for you?

Dots tell you *when*. The **TradingView + Claude Chart Analyst** inside the AI Desk tells you *whether to care*. It reads every alert, checks the chart and the news, and texts you VALID or SKIP with the reason. It comes with 10 more trading bots and 30 AI business systems: a $1,792 value for $199 (it goes to $349 on Dec 1). It runs or it's free. [Get the AI Desk for $199]({{offerUrl}}).
