# The Prop Challenge Playbook

83 simulated prop challenges since 2020. 64 passed, 2 blown at 1% risk. Here are the exact rules, the free indicator and the daily checklist.

**How it works:** 8 daily charts → blue breakout dot → 1% risk to the red stop line → the stop only moves up → +10% = pass

> **READ FIRST:** This is a simulation, not a promise. It's slow on purpose. Never raise risk to catch up. Not affiliated with any prop firm.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/prop](https://milli-ai.com/free/prop?utm_source=github&utm_medium=repo&utm_campaign=prop)

## What we tested
We simulated a new $100k challenge every month from January 2020 to now: **83 challenges**. FTMO-style rules: +10% to pass, 10% max loss, 5% max daily loss, no time limit. Each one traded Milli Trend Dots on 8 daily markets at once, picked using 2010-2019 data only.

| Risk per trade | Passed | Blown | Still running | Median time to pass |
|---|---|---|---|---|
| 0.5% | 59 | 0 | 24 | about 12 months |
| **1%** | **64** | **2** | **17** | **about 4.5 months** |
| 2% | 55 | 21 | 7 | about 2.3 months |

**The lesson:** more risk = faster passes but way more blown accounts. 1% was the sweet spot. It's not fast. It's survivable.

The 8 markets: BTC, SPY, COST, DIA, AAPL, TSLA, S&P 500 futures, gold futures. Check which of these your firm lets you trade, and use the closest ones it offers.

## Step 1: Add Trend Dots (2 minutes)
1. Open [TradingView](https://www.tradingview.com/) on a computer and open any chart.
2. Click **Pine Editor**, delete everything, paste the code below.
3. Click **Save**, then **Add to chart**. Use the **1D** (daily) chart.

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

## Step 2: Set your risk (1 minute)
- Open the indicator settings and set **Risk per trade** to **1**.
- On a $100k account, 1% = **$1,000 per trade**, measured from your entry to the red trailing-stop line.
- Position size = $1,000 ÷ (entry price − stop price). The indicator does this math for you in the Strategy Tester.

## Step 3: Alerts on all 8 markets (5 minutes)
1. Open each market's daily chart with Trend Dots on it.
2. Click the **alarm clock** → Condition: **Milli Trend Dots** → **alert() function calls only** → **Notify in app** → Create.
3. Repeat for each market. New dots now ping your phone.

## Step 4: The 1-minute daily checklist
1. **Any new blue dot?** Enter with 1% risk. Set the stop at the red line.
2. **Open trades:** move each stop to today's red line (it only moves up).
3. **Up 10%?** You passed. Stop trading the challenge.

Optional extra safety (not part of our test, so it can make passes slower): stop for the day if you're down 3%, and cut risk to 0.5% if you're down 6% overall.

## Keep it safe
- Never raise risk to "catch up". That's how the 2% runs blew 21 accounts.
- Patience is the edge. At 1% risk, half the passes took longer than 4.5 months, and 17 challenges were still running when we stopped the test.

> Hypothetical simulation on Yahoo Finance daily prices, costs included, settings and markets chosen on 2010-2019 data. Real prop firms have their own rules, fees and instrument lists. Not affiliated with or endorsed by FTMO or any prop firm. Past results don't guarantee future results. Educational, not financial advice.

## Troubleshooting
| Problem | Fix |
|---|---|
| No dots on the chart | Use the **1D** chart. Dots only appear on a fresh 20-day breakout above the 200 EMA. Some weeks have none. |
| "Script could not be translated" error | Delete everything in the Pine Editor first, then paste. The first line must be `//@version=6`. |
| My firm doesn't offer BTC or TSLA | Skip them, or use the closest market it offers (e.g. another big US stock or index). |
| Two dots on the same day | Take both at 1% each. That's how the test ran. |
| Down a lot in one week | Normal for trend systems. Keep 1% risk. The test's worst cases came from raising risk. |

## Want the finished version?

These indicators are free forever. Want finished trading bots that do the watching for you (one-command install, plain setup steps, and help if you get stuck)? They are in the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/prop](https://milli-ai.com/free/prop?utm_source=github&utm_medium=repo&utm_campaign=prop)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=prop)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
