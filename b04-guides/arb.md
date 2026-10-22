---
title: The ARB Bot Gap-Finder Blueprint
promise: A Polymarket bot reportedly turned $1 into $3.3M by comparing prices, not predicting games. Here's how a 4-agent gap-finder works, how to build it, and a free prompt that checks any game in Claude in 10 minutes.
minutes: 10
nextSystemSlug: arb-gap-finder
---

# The ARB Bot Gap-Finder Blueprint

A video shared on X claimed a "Claude-powered" Polymarket bot turned $1 into $3.3 million between August 2025 and April 2026, mostly on sports. That's a viral claim, not my result, and nobody has independently verified it. The idea behind bots like that is simple, though, and I rebuilt it from scratch. This guide shows how it works and how to build it yourself. If you'd rather skip the build, the finished, tested bot is at the end.

**It doesn't predict games. It compares prices.** The big sportsbooks set their odds with huge amounts of money and data. Polymarket prices come from whoever is trading that minute. When the two disagree on the same game, one of them is probably wrong, and the sportsbooks are usually closer.

**WATCHER → MATH → CLAUDE → RISK**

It never places a bet. It sends you a ticket that ends in **READY FOR YOUR REVIEW** or **BLOCKED BY RISK**, and you decide.

Be honest with yourself about one thing: professional bots are fast, and most gaps close within seconds or minutes. This is a research tool, not a money printer.

Educational only, not financial advice. Check that sports prediction markets are legal where you live.

## Try it in 10 minutes, no code

Pick one upcoming game. Write down the moneyline odds for both teams from 2 or 3 sportsbooks (any odds site shows them side by side). Open the same game on Polymarket and copy both prices plus the full **Rules** text. Paste everything into a new [Claude](https://claude.ai/) chat with this prompt:

```text
You are a 4-agent price checker for ONE sports game. You never place bets. Educational only.

GAME: [Team A] vs [Team B], starts [date/time]
SPORTSBOOK ODDS (moneyline, any format): Book 1: [A] / [B]   Book 2: [A] / [B]   Book 3: [A] / [B]
POLYMARKET: [A] [price]¢  /  [B] [price]¢
POLYMARKET RULES: [paste the full rules]
MY BANKROLL: $[ ]

1. MATH: convert each book's odds to implied probability, remove the bookie's cut so both
   sides add to 100%, and average the books. Show the fair % for each team.
2. GAP: for each team, fair % minus the Polymarket price. Which side is cheapest, by how many points?
3. CLAUDE (fine print): is the Polymarket market the SAME bet as a sportsbook moneyline?
   Same teams, same date, does overtime count, what happens if the game is postponed?
   Any difference = MISMATCH.
4. RISK: PASS/FAIL on: gap at least 4 points, rules MATCH, at least 3 books.
   Any FAIL = BLOCKED. If it passes, stake = quarter-Kelly, capped at 2% of my bankroll.
   End with "READY FOR YOUR REVIEW" or "BLOCKED BY RISK: <checks>", then
   "Nothing has been placed. You decide."
Use only the numbers I gave you. Never invent odds.
```

**BLOCKED will be the most common answer.** Most of the time the prices agree.

## How each agent works (the build blueprint)

This is everything you need to build the automated version yourself in Python.

**01 WATCHER pulls both prices.** For sportsbook odds, use [The Odds API](https://the-odds-api.com/), which has a free tier. Ask for the `h2h` (moneyline) market in decimal format for NFL, NBA and NHL. For Polymarket, use the free public Gamma API: `GET https://gamma-api.polymarket.com/events?tag_slug=nfl&active=true&closed=false`. Each game market has two outcomes (team nicknames) and their prices.

**Match the games** by team nickname ("Denver Broncos" → "broncos") and by start time. Skip any market more than 2 days away from the sportsbook start time, because the same two teams can meet twice.

**02 MATH strips out the bookie's cut (no AI).** Decimal odds of 1.56 mean 1 ÷ 1.56 = 64%. Add both sides: 64% + 41% = 105%. The extra 5% is the bookie's cut. Divide each side by 1.05 to get the fair price: 61% / 39%. Do this for every sportsbook and average them. Require at least 3 books, and note how old the newest odds are.

**03 GAP finds the cheapest side.** Fair price minus Polymarket price for each team. Fair 61% vs Polymarket 54¢ = a 7-point gap. If there's no gap of 4+ points, stop here: no AI call, no cost.

**04 CLAUDE reads the fine print.** This is where most "gaps" turn out to be fake. Send Claude the sportsbook game and Polymarket's rules text and ask for structured JSON: `same_game`, `same_date`, `overtime_counts`, `issues` and a `verdict` of MATCH or MISMATCH. A market that settles on regulation time only isn't the same bet as a moneyline that includes overtime.

**05 RISK kills most of them (plain code).** Block the ticket if any of these fail:

| Check | Default |
|---|---|
| Gap | at least 4 points |
| Liquidity | at least $20,000 |
| Odds age | under 2 minutes |
| Fine print | MATCH |
| Stake | above $0 |

Sizing: quarter-Kelly. For a share costing q with fair probability p, full Kelly is `(p − q) ÷ (1 − q)`. Use a quarter of it, then cap it at 2% of your bankroll.

**Send the ticket** to Telegram so it reaches your phone, and log every gap to a CSV (game, team, Polymarket price, fair price, gap, verdict, passed or blocked). Run it every 5 minutes while games are on.

**After a month,** check the log: how often did Polymarket's price move toward the fair price after the ticket? That tells you if the gaps were real.

## Want the finished bot?

If you don't want to build it, the finished, tested ARB bot is in the **AI Desk**: all 4 agents wired up, one-command install, step-by-step setup for the odds feed, Telegram alerts and the gap log, with clear instructions from zero to your first ticket.

Every free guide we release, including this one, is also included as a bonus inside the AI Desk.
