---
id: earnings-game-plan
title: The Earnings Game Plan skill
category: plan
summary: Decide before the number drops: landmines table, the move options expect vs. the last four, three if/then scenarios, size math, minute-by-minute plan and a one-page cheat sheet.
---

# EARNINGS GAME PLAN

Every bad earnings trade was decided in the 30 seconds after the number. This moves the decision to the night before.

## INTAKE (one message)

1. Ticker or event, and the date/time (before open or after close?)
2. Do you hold it now? How much, at what price?
3. What are you thinking of doing? (Hold through, trim, buy after, stay out, options)
4. Max you're willing to lose on this event, in dollars

## BUILD THE PLAN

1. **Facts first** (or run `/ticker-deep-dive`): last 4 reports (beat/miss, guide, next-day move), what analysts expect (EPS, revenue, the one metric everyone watches for this company), time of release and call.
2. **The expected move.** If options are listed: the at-the-money straddle price for the nearest expiry after the event ÷ stock price ≈ the move the market is pricing. Compare with the last 4 actual moves. Say plainly: "the market expects about ±X%; the last four were A, B, C, D."
3. **Landmines table.** Things that blow up plans:

   | Landmine | Why it matters | What I'll do |
   |---|---|---|
   | Guide matters more than the beat | Stock can beat and drop 10% | Judge on guidance line, not headline |
   | After-hours liquidity is thin | Spreads wide, fake prints | No market orders after hours |
   | Gap through my stop | Stop fills far below | Size so a 2x expected-move gap = max loss |
   | Call changes the story | First move reverses | Don't act in first 5 min of the call |

4. **Three scenarios**, each as IF → THEN, with numbers:
   - **Beat + raise:** IF guide above consensus and stock > +X% → THEN …
   - **Mixed:** IF beat but guide in line/below → THEN …
   - **Miss:** IF revenue miss or guide cut → THEN …
   Every THEN is a specific action (hold / sell N shares / limit order at $ / do nothing) and a "wrong if" line.
5. **Size check.** Show the math: position size × (2 × expected move) ≤ max loss. If it doesn't fit, the plan says to trim before the event. Show the number of shares to hold.
6. **Minute-by-minute.** T-1 day (set alerts, write limit prices), T-15 min (re-read this sheet, no new positions), release (read guidance line first), +5 min, +30 min, next open (first 15 minutes: no market orders), end of day 1 (journal it).
7. **Cheat sheet.** One page, big text, the three IF → THEN lines, the max-loss number, and the one sentence that stops you from doing something dumb.

## OUTPUT

```
./earnings/<TICKER>-<date>/PLAN.md
./earnings/<TICKER>-<date>/CHEATSHEET.md     # one page, printable
./earnings/<TICKER>-<date>/AFTER.md          # template: what happened vs. plan
```

## HARD RULES

- **The max-loss number comes from the user and is never raised by you.**
- **No predictions of direction.** Scenarios only.
- **No options strategies for users who haven't traded options before.** Say it's out of scope and why (you can lose 100% fast).
- **Always write AFTER.md** as a template. The plan only makes you better if you grade it.
- Educational only. Not financial advice.
