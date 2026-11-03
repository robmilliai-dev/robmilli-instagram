---
title: The Milli Index Dip Indicator
promise: The free TradingView indicator that won 57 of 70 S&P 500 dip-buys on years it never saw. Copy, paste, done in 2 minutes.
minutes: 10
nextSystemSlug: tradingview-claude-chart-analyst
---

# The Milli Index Dip Indicator

One free TradingView indicator. When the S&P 500 has a panic day inside an uptrend, a blue dot shows up. When it bounces, you get the exit.

**When you're done you'll have:**
- **Index Dip** on your daily S&P 500 or Nasdaq chart
- Buy dots on panic days, exit marks on the bounce
- A phone alert every time a new dot shows up

**How it works:** Uptrend check → panic day = blue dot → you get a phone alert → sell the bounce (orange x)

> **READ FIRST:** Daily charts only. Big indexes only (SPY, QQQ, S&P or Nasdaq futures). No leverage. It never places a trade for you.

## Why this works

We picked the settings using 2010 to 2019 data only. Then we tested on January 2020 to October 2026: years the indicator had never seen.

- **SPY, daily:** 57 of 70 trades won (81%). $2.03 won for every $1 lost. Worst drop: -10% (SPY itself fell -34%).
- **S&P 500 futures:** 80% won. **QQQ:** 80%. **Nasdaq futures:** 77%.
- **We tested 22 markets.** Single stocks did worse (65-75%), gold about 70%, and it **lost money on Bitcoin**. So use it on the big indexes.
- It's in the market only about 17% of the time, about 4 days per trade. Holding SPY made more over the whole period (+156% vs +36%), with much bigger drops on the way.

## Step 1: Add Index Dip (2 minutes)

1. Open [TradingView](https://www.tradingview.com/) on a computer and open a **SPY** (or QQQ) chart.
2. Click **Pine Editor** at the bottom of the screen.
3. Delete everything in the editor. Paste the code below.
4. Click **Save**, then **Add to chart**.
5. Switch the chart to **1D** (daily).

```pine
//@version=6
// Milli Index Dip by Milli.ai (DAILY charts, built for index markets: S&P 500, Nasdaq 100)
// Buy dot: price above its 200-day average, RSI(2) under 20, and the close in the bottom 25% of the day's range.
// Exit: the first close with RSI(2) above 70 (sell next open), or after 10 bars, or a 5 x ATR(14) disaster stop.
// Settings were picked on 2010-2019 data only, then tested on 2020-2026 data they never saw.
// Educational tool. Hypothetical backtests. Not financial advice. Past results do not guarantee future results.
strategy("Milli Index Dip", overlay = true, initial_capital = 10000, default_qty_type = strategy.percent_of_equity,
     default_qty_value = 100, commission_type = strategy.commission.percent, commission_value = 0.05, process_orders_on_close = false)

rsiBuy  = input.float(20, "Buy when RSI(2) below", minval = 1)
ibsMax  = input.float(0.25, "Close in bottom part of day's range (0-1)", minval = 0.01, maxval = 1)
rsiExit = input.float(70, "Exit when RSI(2) above", minval = 1)
maxBars = input.int(10, "Max bars in trade", minval = 1)
stopAtr = input.float(5.0, "Disaster stop (x ATR 14)", minval = 0.5)

r    = ta.rsi(close, 2)
sma  = ta.sma(close, 200)
ibs  = high > low ? (close - low) / (high - low) : 0.5
atr  = ta.atr(14)
flat = strategy.position_size == 0
buySig = bar_index > 200 and close > sma and r < rsiBuy and ibs < ibsMax

var float stopPx = na
var int entryBar = na
if flat and buySig
    stopPx := na
    strategy.entry("Long", strategy.long)
if strategy.position_size > 0
    if na(stopPx)
        stopPx := strategy.position_avg_price - stopAtr * atr[1]
        entryBar := bar_index
    strategy.exit("Stop", "Long", stop = stopPx)
    if r > rsiExit or bar_index - entryBar + 1 >= maxBars
        strategy.close("Long", comment = "Exit dot")

plot(sma, "200 SMA", color.new(color.gray, 40))
plotshape(flat and buySig, "Buy dot", shape.circle, location.belowbar, color.new(#3987e5, 0), size = size.small)
plotshape(strategy.position_size > 0 and r > rsiExit, "Exit dot", shape.xcross, location.abovebar, color.new(color.orange, 0), size = size.tiny)
if flat and buySig
    alert("Milli Index Dip BUY on " + syminfo.ticker + " at " + str.tostring(close), alert.freq_once_per_bar_close)
if strategy.position_size > 0 and r > rsiExit
    alert("Milli Index Dip EXIT on " + syminfo.ticker + " at " + str.tostring(close), alert.freq_once_per_bar_close)
```

## Step 2: Read the dots

- **Blue dot under a candle:** a panic day in an uptrend. That's the buy signal (the test bought at the next day's open).
- **Orange x:** the bounce came (2-day RSI over 70). That's the exit.
- **Gray line:** the 200-day average. No dots when price is under it.
- **Strategy Tester tab:** shows how the dots did on the chart you're looking at.

## Step 3: Get a phone alert for every new dot

1. Click the **alarm clock** (Alerts) on the right.
2. Condition: pick **Milli Index Dip**, then **alert() function calls only**.
3. Turn on **Notify in app**. Click **Create**.
4. Install the TradingView app on your phone and log in. New dots now ping your phone.

## 12 copy-paste prompts (use with Claude)

Take a screenshot of the chart with the dots showing and paste it in with any of these:

1. "Here's my chart with a new blue dot. Is the market still in an uptrend? What on the chart shows it?"
2. "Account $___, risk 1%, entry $___, stop $___. How many shares or contracts? Show the math."
3. "Is there earnings, a Fed meeting or CPI in the next 2 days? Dates only."
4. "What's the strongest reason to skip this dot?"
5. "Here are 5 charts with dots. Which ones are the cleanest? One line each."
6. "Write the TradingView alert message so each alert tells me the ticker, price, time and timeframe."
7. "This trade hit the exit. Write one journal line: date, market, entry, exit, result in R."
8. "Here's my journal for the month. What's my win rate, average win, average loss?"
9. "Did I follow every dot, or did I skip some? Did skipping help or hurt?"
10. "My last 3 trades lost. Is that normal for this indicator, or did I do something wrong?"
11. "Explain in plain English what this indicator is waiting for before it shows a dot."
12. "Explain this Pine Script line by line so I understand what it does: [paste code]."

## Your 5-minute daily routine

| When | Do this |
|---|---|
| After the close (2 min) | Check your alerts. Any new dots? |
| New dot (3 min) | Prompts 1, 2 and 3. Write the plan before you act. |
| Exit (1 min) | Journal it (prompt 7). |

## Weekly review (10 minutes, every Sunday)

This is where you actually get better. Paste your week's notes into Claude with this:

```text
Here are my notes from this week: [paste]
1. Which ideas worked and which didn't? Look for patterns (setup, day, time, market).
2. Where did I break my own rules?
3. Give me ONE change to make next week. Just one.
Use only what's in my notes. Don't guess.
```

## Your first run checklist

- [ ] Index Dip is on your daily SPY or QQQ chart
- [ ] You can see blue dots when you scroll back
- [ ] Your phone got a test alert

## Troubleshooting

| Problem | Fix |
|---|---|
| No dots on the chart | Switch to the **1D** (daily) chart and scroll back. Dots only appear when price is above the gray 200-day line. |
| "Script could not be translated" error | Make sure you deleted everything in the Pine Editor before pasting, and that the first line is `//@version=6`. |
| Alert doesn't fire | In the alert, pick **alert() function calls only**, not "Buy dot". |
| Lots of dots on a stock or crypto | It's built for indexes. On single stocks it's weaker and on Bitcoin it lost money. |

## Keep it safe

- **Daily charts, big indexes, no leverage.** That's what we tested. With leverage it failed our prop-challenge tests, so don't use it for that.
- A dot is a setup, not a promise. 13 of the 70 SPY trades lost. That's in the numbers above.

> Hypothetical backtest on Yahoo Finance daily prices, next-day entries, costs included, settings chosen on 2010-2019 data. Past results don't guarantee future results. Educational tool, not financial advice. You make every decision.

## Want it done for you?

Dots tell you *when*. The **TradingView + Claude Chart Analyst** inside the AI Desk tells you *whether to care*. It reads every alert, checks the chart and the news, and texts you VALID or SKIP with the reason. It comes with 10 more trading bots and 30 AI business systems: a $1,792 value for $199 (it goes to $349 on Dec 1). It runs or it's free. [Get the AI Desk for $199]({{offerUrl}}).
