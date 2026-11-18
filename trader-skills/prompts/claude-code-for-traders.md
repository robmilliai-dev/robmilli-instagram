---
title: Claude Code for Traders: the Starter Pack
keyword: SKILLS
promise: Install Claude Code, add 17 trading skills in one command, drop in a CLAUDE.md built for a trading repo, and write your own skill in five minutes.
---

# Claude Code for Traders

**Claude Code is an AI that works inside a folder on your computer.** It reads your files, runs your scripts, and builds things. For a trader that means: backtests, bots, scanners and reports, built and fixed by asking in plain English.

## 1. Install (5 minutes)

1. You need a paid Claude plan or an Anthropic API account.
2. Follow the install steps at **claude.com/claude-code** (Mac, Windows or Linux).
3. Make a folder for your trading work, open a terminal in it, type `claude`.

## 2. Add all 17 Milli trader skills (1 command)

```bash
curl -fsSL https://milli-ai.com/api/downloads/trader-skills/install-trader-skills.sh | bash
```

Or download `milli-trader-skills.zip` from milli-ai.com/free and unzip it into `~/.claude/skills/` (every project) or `.claude/skills/` (this project only).

What you get:

| Skill | Type `/…` | What it does |
|---|---|---|
| trading-plan | `/trading-plan` | Your written plan: Bot Ladder rung, rules, risk, 90 days |
| bot-audit | `/bot-audit` | Six blind reviewers check a bot before it touches money |
| account-stats | `/account-stats` | Real scoreboard from Alpaca or any broker CSV |
| watchlist-pull | `/watchlist-pull` | Plain-English idea → screened, ranked watchlist |
| ticker-deep-dive | `/ticker-deep-dive` | 8-pass research brief with a source on every fact |
| earnings-game-plan | `/earnings-game-plan` | If/then plan decided before the number drops |
| alert-inbox | `/alert-inbox` | Trading email → one morning brief; flags scams |
| saved-posts-sorter | `/saved-posts-sorter` | Your saved reels → strategies worth testing |
| equity-video | `/equity-video` | Equity curve → animated MP4 |
| trade-carousel | `/trade-carousel` | Carousel slides + PDF from a real result |
| reel-script | `/reel-script` | Hooks + script + caption for a trading reel |
| reel-prompts | `/reel-prompts` | AI video prompts for trading B-roll |
| trade-recap | `/trade-recap` | Honest trade post for X, Threads, StockTwits |
| trading-dashboard-app | `/trading-dashboard-app` | Build your own dashboard app |
| skill-builder | `/skill-builder` | Turn any repeated task into a skill |
| strategy-to-bot-spec | `/strategy-to-bot-spec` | Idea → exact spec a coder or AI can build |
| pine-script-writer | `/pine-script-writer` | Plain English → TradingView Pine Script, checked |

## 3. CLAUDE.md for a trading repo

Put this file in the root of your trading folder. Claude reads it every session.

```markdown
# Trading workspace rules

## What this folder is
[My bots, backtests and research. Markets: ... Broker: ...]

## Safety (never break)
- Never place, change or cancel a live order unless I type "LIVE OK" in this session.
- Paper/test mode is the default for every script. Live needs an explicit flag.
- Never print, log or commit API keys. Keys live only in .env (in .gitignore).
- Every bot checks a KILL file at start and exits if it exists.
- Max risk per trade: [1%]. Max daily loss: [2%]. Never raise these.

## Backtests
- Signals use only data available at the time (shift by 1 bar).
- Costs and slippage always included. Fill at next bar's open.
- Hold back the most recent [2] years; never tune on them.
- Report: trades, win rate, avg win/loss, profit factor, worst drop, vs buy-and-hold.
- Under 30 trades = "not enough trades", no verdict.

## Style
- Python 3.11, pandas. Small files. A README per bot.
- Plain-English summaries. No hype.
```

## 4. Write your own skill in 5 minutes

A skill is a folder with a `SKILL.md`. That's it.

```markdown
---
name: morning-check
description: Every morning, check my 5 bots' logs and tell me which ones ran, which failed, and today's P&L.
---
# MORNING CHECK
1. Read logs/*.log from the last 24 hours.
2. For each bot: ran? errors? trades? P&L?
3. Output a 5-line table. Failures first.
## Rules
- Never restart a bot. Just report.
```

Save it as `.claude/skills/morning-check/SKILL.md`, then type `/morning-check`. Or run `/skill-builder` and answer its questions.

## 5. More skills

- Anthropic's official skills: **github.com/anthropics/skills** (documents, spreadsheets, PDFs, and more)
- Read any skill before installing it. A skill is instructions plus scripts: only install what you've looked at.

> Educational only. Not financial advice.
