---
name: strategy-to-bot-spec
description: Turn a trading idea (yours, a reel's, a book's) into an exact build spec a developer or an AI coder can turn into a bot without guessing. Pins down every rule, the data, the timing, the risk limits, the kill switch, the test plan and what "done" means. Flags every assumption it had to make.
argument-hint: "[the strategy in plain English, or a link/caption]"
---

# STRATEGY TO BOT SPEC

"Buy the dip" is not a bot. "Buy SPY at the next open after it closes 3% below its 20-day high while above its 200-day average" is.

## INTAKE

1. The idea, in any words. Paste the caption or transcript if it came from a post.
2. Market and timeframe (or "you pick").
3. Where it'll run: TradingView alerts, Python on a schedule, a broker API (which?).
4. Account size and max risk per trade.

## PROCESS

1. **Restate the idea in one sentence.** Ask the user to confirm before going on.
2. **Pin every rule.** For each, the exact condition a computer evaluates:
   - Universe (which symbols), bar size, session (regular hours? 24/7?)
   - Entry condition, evaluated on which bar's data, order type, when it fills
   - Exit conditions: target, stop, time stop, trailing rule. Which wins if two trigger on the same bar
   - Position sizing formula (risk-based, with the math)
   - Re-entry rule (can it buy again the next day?)
3. **List assumptions** in a table: what the original idea didn't say, what you chose, and why. The user approves or changes each.
4. **Risk and safety block (always):** max risk per trade, max daily loss, max open positions, KILL file check, paper mode default, behavior on stale data or API errors.
5. **Data:** source, history needed, adjustments (splits/dividends), how missing bars are handled.
6. **Test plan:** in-sample years, held-back years, costs/slippage, minimum 30 trades, compare vs. buy-and-hold, the pass/fail bar set *before* testing.
7. **Done means:** a numbered acceptance list (e.g. "backtest report generated", "paper run for 10 sessions with log", "KILL file stops it within one cycle").

## OUTPUT

`./specs/<strategy-slug>.md` with sections: Summary · Rules (numbered, exact) · Assumptions table · Risk & safety · Data · Test plan · Done means · Open questions.

Then offer: "Paste this into Claude Code (or hand it to a developer) with: *Build this spec exactly. Ask before changing any rule.*"

## HARD RULES

- **Never improve the strategy while specifying it.** Write what it is. Improvements go in a separate "ideas to test later" list, because mixing them makes the test meaningless.
- **Every rule must be evaluable on data available at that moment.** No "close of today" for a trade at today's open.
- **If a rule can't be made exact, say so.** "Not specifiable as posted" is a valid result.
- Educational only. Not financial advice.
