---
id: trading-plan
title: The Trading Plan skill
category: plan
summary: Your written trading plan: your honest rung on the Bot Ladder, one market that fits your time and money, risk rules first, a 90-day path from manual to automated, the don't-do list and a weekly scoreboard. HTML + PDF.
---

# THE TRADING PLAN

Turns "I want a bot that makes money" into a one-page plan a trader can follow on a bad day.

## PICK THE DEPTH FIRST

| Depth | When | Length |
|---|---|---|
| **Snapshot** | The trader gave you almost nothing. New, curious, no account yet. | One page. Where you are, one market, one rule, one next step. |
| **Plan** | You know their account size, hours per week, markets and one past result. | 6 sections, about 120 lines. |
| **Playbook** | They shared a trade log or backtest, broker, goals and rules they already use. | 11 sections, about 250 lines. |

If you can't tell, ask the five intake questions below. The most common failure is writing a Playbook for someone with no data. It reads like a horoscope.

## INTAKE (ask in one message, never one at a time)

1. How much money is in the account you'd trade with? (A range is fine.)
2. How many hours a week can you watch markets? Be honest.
3. What do you trade now, or want to trade? (Stocks, ETFs, crypto, futures, options, prediction markets.)
4. What's happened so far? (Never traded / up / down / blew an account.)
5. What would make the next 90 days a win for you? (In your words.)

Optional: paste a trade log or a backtest CSV. If they do, use it. Real numbers beat every assumption.

## WORKFLOW

1. **Place them on the Bot Ladder, honestly.** One paragraph, with the reason.
   1. Gut trades, no rules
   2. Rules in their head
   3. Rules written down
   4. Rules backtested on years they weren't tuned on
   5. Alerts fire on the rules, human clicks the button
   6. Bot places orders with a hard daily loss limit and a kill switch
   Most people who say "I want a bot" are on rung 1 or 2. Say so kindly. Skipping rungs is how accounts die.
2. **Match market to time and money.** 2 hours a week is not a day trader. A $500 account is not a futures account (margin). Recommend ONE market and ONE timeframe to start. Say what you cut and why.
3. **Write the rules in plain English.** Entry, exit, stop, size. Each rule must be testable by a computer: if a rule says "when it looks strong", rewrite it or flag it.
4. **Set the risk floor.** Max risk per trade (default 0.5% to 1% of account), max loss per day (default 2%), max open positions, and the "stop trading for the week" line. These are not optional and go above the rules in the document.
5. **Sequence 90 days in three blocks.**
   - Days 1 to 30: write the rules, backtest them (`/bot-audit` style checks: years it never saw, at least 30 trades, costs in, worst drop, vs. buy-and-hold).
   - Days 31 to 60: alerts only. Log every alert and what you did. Small size or simulated fills only.
   - Days 61 to 90: automate the part that passed. Hard limits in code. Review weekly.
   Every block ends in something the trader can see: a report, a log, a running bot.
6. **Write the "don't do this" section.** Always. Revenge trades, moving stops, adding to losers, tuning a backtest until it's pretty, running a bot without a daily loss limit, pasting API keys into chats. This is the section people screenshot.
7. **Write the scoreboard.** What to track weekly: number of trades, win rate, average win vs. average loss, worst drop, rule breaks. What number at day 30/60/90 means "keep going" vs. "stop and fix".
8. **End with one next step they can do today**, in under 20 minutes. Never "let me know".
9. **Render.** `.md` first, then a clean `.html` (dark background, one accent color, big section headers), then a PDF:
   ```bash
   # macOS
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
     --no-pdf-header-footer --print-to-pdf="./out/<Name>-Trading-Plan.pdf" "file://$PWD/out/<Name>-Trading-Plan.html"
   # Linux / Windows: use chromium or chrome.exe with the same flags
   ```

## HARD RULES

- **Never promise returns.** No "you'll make X% a month". Talk about process, risk and what the test showed.
- **Never invent a stat.** If you quote a number, it came from their data or a source you name.
- **Risk rules come before entry rules** in every version of the document.
- **Never recommend leverage, margin or options to someone on rungs 1 to 3.** Name it as out of scope until the rules are tested.
- **Respect what they already do.** If they have a method that works for them, build on it. Don't replace it with yours.
- **Plain English, short sentences.** A 12-year-old should follow it. No "alpha", no "edge decay", no "Sharpe" without a one-line explanation.
- End every document with: *Educational only. Not financial advice.*

## OUTPUT

```
./out/<Name>-Trading-Plan.md
./out/<Name>-Trading-Plan.html
./out/<Name>-Trading-Plan.pdf
```

## SECTION SKELETON (Playbook depth)

1. The one-paragraph summary (read only this on a bad day)
2. Where you are on the Bot Ladder
3. Your market, your timeframe, and what we cut
4. Risk rules (per trade, per day, per week)
5. Entry, exit and stop rules
6. Days 1 to 30: write and test
7. Days 31 to 60: alerts and a log
8. Days 61 to 90: automate what passed
9. Don't do this
10. Your weekly scoreboard
11. Today's 20-minute step

## PAIRS WITH

`/bot-audit` to check the bot before day 61, `/account-stats` for the weekly scoreboard, `/watchlist-pull` to pick the market.
