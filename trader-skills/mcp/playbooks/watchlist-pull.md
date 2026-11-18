---
id: watchlist-pull
title: The Watchlist Pull skill
category: research
summary: Plain-English market idea into a screened, deduped, ranked watchlist CSV plus a TradingView import line and a why-each-one note. Resumable, free data, logs every drop.
---

# WATCHLIST PULL

Most traders watch 40 tickers they picked by vibes. This gives you 25 you can defend.

## THE PIPELINE

```
market idea (plain English)
  → universe file (every candidate ticker)        step 1, you + Claude
  → price history for each (free, throttled)      pull.py
  → screen: price, liquidity, trend, jumpiness    pull.py
  → dedupe share classes                          pull.py
  → rank + top N                                  pull.py
  → WHY.md: one line per ticker                   step 5, Claude
```

## WORKFLOW

1. **Turn the idea into a screen.** Restate it as numbers and confirm in one message:
   - min price (default $5; under that, spreads and halts bite)
   - min 20-day average dollar volume (default $10M; $20M+ for day trading)
   - trend filter: any / above 50-day / above 200-day / new 20-day high
   - max daily range % (optional, keeps out names that move 10% on a sneeze)
   - rank by: 3-month return, 12-month return, or liquidity
   - how many to keep (default 25)
2. **Build the universe file.** One ticker per line in `watchlists/<campaign>/universe.txt`. Sources, in order: the user's own list; an index's public constituents page (S&P 500, Nasdaq-100); a sector ETF's published holdings; for crypto use Yahoo symbols like `BTC-USD`. Say where the list came from at the top of the file as a `#` comment.
3. **Say the size before running.** Tickers, minutes, cost ($0 on free data). Over 300 tickers, confirm first.
4. **Run it.**
   ```bash
   pip install yfinance pandas
   python scripts/pull.py --campaign tech-leaders --universe watchlists/tech-leaders/universe.txt \
     --min-price 10 --min-dollar-vol 20000000 --trend above200 --rank ret_3m --top 25
   ```
   If it stops (network, rate limit), run the same command again. It picks up where it left off.
5. **Write `WHY.md`.** For each ticker in the watchlist: one line on why it passed (the numbers) and one thing to check before trading it (earnings date, news, a gap). Ground it in the CSV, not in memory.
6. **Report what was dropped.** Read `dropped.log` and give the counts by reason. If 80% got dropped for one reason, say so: the filter might be wrong, not the market small.

## WORKSPACE (match exactly)

```
./watchlists/<campaign>/
  universe.txt                 # every candidate, with its source on line 1
  progress.jsonl               # checkpoint: a rerun resumes
  <campaign>_all.csv           # every ticker checked, with numbers
  <campaign>_passed.csv        # passed the screen, deduped
  WATCHLIST_<campaign>.csv     # ranked top N
  tradingview_import.txt       # paste into a TradingView watchlist
  dropped.log                  # ticker + reason, every one
  WHY.md                       # one line per pick
```

## RULES

- **Checkpoint everything.** A crash at 80% must not restart at 0%.
- **Stay polite to free data.** Default 0.7s between requests. Never hammer it in parallel.
- **Dedupe on share class** (GOOG/GOOGL, BRK-A/BRK-B): keep the more liquid one, log the other.
- **Log every drop with a reason.** A filter that silently removes half the list lies to you.
- **A watchlist is not a buy list.** Say it in WHY.md's first line.

## HARD RULE

**Never trades.** It builds and explains a list. What to do with it is a separate human decision.

Educational only. Not financial advice.

## If you can't run scripts here
This playbook uses helper scripts. In a chat app, do the steps by hand with the user (ask them to paste data), or point them to the downloadable skill at milli-ai.com/free (keyword SCAN).
