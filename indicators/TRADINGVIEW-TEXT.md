# Copy-paste text for TradingView

For each script: copy the Title into the title box and everything under Description into the description box. Do not add links or prices.

## Script 1: Milli Trend Dots

**Title:** Milli Trend Dots: 20-bar breakout with ATR trailing stop

**Description:**
Milli Trend Dots marks simple trend breakouts and manages the exit for you.

How it works:
- Buy dot: the close breaks above the highest high of the last 20 bars while price is above the 200 EMA (only trades with the trend).
- Exit: a 3 x ATR(14) trailing stop, drawn as a red line. It only moves up, never down.
- One trade at a time. Sell dots are off by default.

Settings you can change: breakout lookback, trend EMA length, trailing stop size, risk per trade (default 1% of equity), and a max position size.

How we tested it: the settings were chosen using 2010-2019 data only, then checked on 2020-2026 data the settings had never seen, across 43 daily markets (stocks, ETFs, futures, forex and crypto), with 0.05% commission per trade. It did not work on every market (for example EURUSD and TLT lost). Treat a dot as a setup to check, not a promise.

Alerts: create an alert on the script and pick "alert() function calls only" to get a message on every new buy dot.

Educational tool. Hypothetical backtest results. Not financial advice. Past results do not guarantee future results.

## Script 2: Milli Pullback Dots

**Title:** Milli Pullback Dots: buy sharp dips inside an uptrend (daily)

**Description:**
Milli Pullback Dots looks for sharp, short dips inside a strong uptrend on daily charts.

How it works:
- Buy dot: the 50 EMA is above the 200 EMA, price is above the 200 EMA, and RSI(2) drops below 5 (a sharp short-term dip).
- Exit dot: the first close above the 5 EMA (exit at the next bar's open), or a 2 x ATR(14) stop set at entry.
- Risk per trade defaults to 1% of equity.

Use it on DAILY charts only. We tested a 4-hour version and it did not hold up, so we don't recommend it on intraday charts.

How we tested it: settings chosen on 2010-2019 data only, then checked on 2020-2026 data the settings had never seen, across 43 daily markets, with 0.05% commission. It lost on some markets (including COST, META, AMZN and gold futures), so check it on your own market before using it.

Alerts: create an alert on the script and pick "alert() function calls only".

Educational tool. Hypothetical backtest results. Not financial advice. Past results do not guarantee future results.

## Script 3: Milli Index Dip

**Title:** Milli Index Dip: RSI(2) dip-buying for index markets (daily)

**Description:**
Milli Index Dip is a dip-buying tool built for index markets like the S&P 500 and Nasdaq 100 on daily charts.

How it works:
- Buy dot: price is above its 200-day average, RSI(2) is under 20, and the close is in the bottom 25% of the day's range.
- Exit: the first close with RSI(2) above 70 (exit at the next open), or after 10 bars, or a 5 x ATR(14) disaster stop.

Built for indexes. On single stocks it was weaker, and on Bitcoin it lost money in our tests, so we don't recommend it there.

How we tested it: settings chosen on 2010-2019 data only, then checked on January 2020 to October 2026 data the settings had never seen, on 22 markets, with 0.05% commission. On SPY the worst drop in that period was about 10%.

Alerts: create an alert on the script and pick "alert() function calls only".

Educational tool. Hypothetical backtest results. Not financial advice. Past results do not guarantee future results.

