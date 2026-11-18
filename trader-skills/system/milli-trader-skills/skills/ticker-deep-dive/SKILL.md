---
name: ticker-deep-dive
description: Know a stock (or ETF, or coin) cold before you trade it. Eight research passes (what they actually sell, the numbers, the last 4 earnings, insiders and big holders, the chart, news and filings from the last 90 days, upcoming catalysts, the bear case) merged into one 8-section brief with a source on every fact, the one thing most people miss, and an honest list of what couldn't be found.
argument-hint: "[ticker]"
---

# TICKER DEEP DIVE

Twenty minutes of homework the person on the other side of your trade probably didn't do.

## THE 8 PASSES

Run in parallel if you can (subagents or parallel web searches). Each pass returns facts with a source URL and date. No source, no fact.

1. **What they sell, in their words.** Latest 10-K/annual report business section, investor deck. Which product makes the most money. Who the customers are. (Crypto: what the token is actually used for, who issues it, supply schedule.)
2. **The numbers.** Revenue and profit trend (last 8 quarters), margins, cash vs. debt, share count trend (buybacks or dilution). From filings or the company IR page, not from a blog.
3. **The last 4 earnings.** Beat or miss on revenue and EPS, what guidance did, and how the stock moved the next day. The pattern matters more than any single quarter.
4. **Insiders and big holders.** Form 4 insider buys/sells in the last 6 months (open-market buys matter, planned 10b5-1 sales mostly don't). Big holder changes from 13F if available.
5. **The chart.** Price vs. 50- and 200-day averages, 52-week high/low, average daily range, average dollar volume. Where the obvious levels are. No predictions.
6. **Last 90 days of news and filings.** 8-Ks, lawsuits, management changes, product launches, analyst changes. Dated list, newest first.
7. **What's coming.** Next earnings date, product events, lockup expiry, index changes, FDA dates, token unlocks. Dated list.
8. **The bear case.** The strongest honest argument against owning it. Short reports if any, and what the company said back.

## THE BRIEF

`./research/<TICKER>-<YYYY-MM-DD>.md`

```
# <TICKER> · <Company> · <date>

## 1. In one paragraph
## 2. How they make money
## 3. The numbers that matter (table, with sources)
## 4. Earnings pattern (last 4: beat/miss, guide, next-day move)
## 5. Who's buying and selling (insiders, holders)
## 6. The chart, plainly (levels, trend, liquidity; no forecast)
## 7. What's coming (dated catalysts)
## 8. The bear case

### The one thing most people miss
(one specific, non-obvious observation, backed by a source)

### What I couldn't find
(honest list; never fill gaps with guesses)

Sources (numbered, with dates)
```

## RULES

- **Every number has a source and a date** in the Sources list. Aggregator numbers get double-checked against a filing when possible; if not, label them "per <site>".
- **Write "the company says"** for anything from the company's own marketing.
- **No price targets. No buy/sell call.** If asked "should I buy", answer with the 3 questions they should answer first and point them to `/earnings-game-plan` or the HEDGE committee.
- **The bear case is mandatory**, even for a stock the user loves. Especially then.
- **Date-stamp the brief.** Research goes stale. Say "as of <date>" at the top.
- Educational only. Not financial advice.

## PAIRS WITH

`/earnings-game-plan` (turn this into an if/then plan), `/watchlist-pull` (find tickers worth a deep dive).
