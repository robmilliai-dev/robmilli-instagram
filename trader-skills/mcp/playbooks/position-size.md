---
id: position-size
title: Position Size Calculator (Never Blow Up)
category: risk
summary: Work out exactly how many shares, contracts or coins to buy so one losing trade costs a fixed, small slice of your account, including gap risk and what to do when the math says the trade is too big.
---
# POSITION SIZE

## Ask first
1. Account size. 2. Max risk per trade (% or $; suggest 0.5 to 1% if they don't know). 3. Entry price. 4. Stop price. 5. Market (stock, crypto, futures with point value, options).

## Process
1. Risk $ = account × risk %.
2. Risk per unit = |entry − stop| (futures: × point value; options: premium × 100 if risking the whole premium).
3. Size = floor(Risk $ ÷ risk per unit). Show the math line by line.
4. Cap checks: position value ≤ 25% of account (default), within buying power, no leverage for beginners.
5. Gap check: if it gaps 2× through the stop, what's the loss? If over 2% of account, cut size and say so.
6. If size rounds to 0 or the stop is so wide the size is tiny: say "this trade doesn't fit your account" and offer a tighter logical stop or skip.

## Output
A box: Shares/units · Risk $ · Position value · % of account · Loss if stop hits · Loss if 2× gap. Then one line: "Place the stop at $X when you enter, not later."

## Rules
- Never raise the user's risk %. Never suggest margin to make a trade fit.
- Use a calculator mindset: show the arithmetic so they can check it.
- Educational only. Not financial advice.
