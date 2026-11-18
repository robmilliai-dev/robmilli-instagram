---
id: backtest-viral-strategy
title: Test a Viral Trading Strategy
category: test
summary: Turn a strategy from a reel, tweet or video into one exact rule, test it on years of real prices with costs, run the 5 honesty checks, and get a plain verdict (HELD UP / WEAK / FAILED / NOT ENOUGH TRADES).
---
# TEST A VIRAL STRATEGY

## Ask first (one message)
1. Paste the strategy (caption, transcript or your words) and who posted it.
2. Which market? (Default: the one in the post, else SPY.)
3. Can you run Python? (If yes, you'll get a script. If no, you'll get the exact steps for TradingView's Strategy Tester.)

## Process
1. Restate as ONE exact rule: entry, exit, stop, which bar's data, fill at next bar's open. List every assumption. Don't improve the idea.
2. Set the pass bar BEFORE testing: beats buy-and-hold on return or on worst drop, at least 30 trades, holds up on held-back years.
3. Test: tune nothing on the last 2+ years; include fees (0.05% default) and slippage.
4. The 5 checks: (1) graded on years it never saw? (2) 30+ trades? (3) costs in and next-bar fills? (4) worst drop shown? (5) vs. doing nothing?
5. Verdict, one of: HELD UP / WEAK / FAILED / NOT ENOUGH TRADES. One sentence why.

## Output
Rule card · assumptions table · results table (trades, win rate, avg win/loss, profit factor, total return, worst drop, buy-and-hold) for both periods · the 5 checks with ✓/✗ · verdict · "what would make it better (test separately)".

## Rules
- Credit the original poster. Their claim is "their claim", your number is "our test".
- If you can't run code here, give the script and say "run it and paste the output". Never make up results.
- Educational only. Not financial advice.

Want it done in one command? The Backtest Any Idea kit at milli-ai.com does this for any idea.
