# Milli Trader Skills: start here

**What you'll have:** 17 Claude skills and 6 prompt kits built for traders, plus the Milli MCP link that puts 30 trading playbooks inside Claude or ChatGPT.

**What you need:** Claude (any paid plan) or ChatGPT. Claude Code for the skills with scripts. Python or Node for 5 of them (each says which).

## Fastest start (2 minutes, no install)

1. Copy this link: `https://milli-ai.com/api/mcp`
2. Claude: Settings → Connectors → Add custom connector → paste → Add.
   ChatGPT: Settings → Apps & Connectors → Advanced → Developer mode on → Create → paste → no auth.
3. Ask: *"Use Milli. Audit my trading bot"* or *"Milli: list your playbooks."*

## Install all 17 skills in Claude Code (1 command)

```bash
curl -fsSL https://milli-ai.com/api/downloads/trader-skills/install-trader-skills.sh | bash
```

Or copy any folder under `skills/` here into `~/.claude/skills/`.

## Do these three first

1. **`/trading-plan me`**: your written plan. 10 minutes.
2. **`/bot-audit .`** in your bot's folder, before it trades real money.
3. **`/account-stats`**: your real scoreboard. Do it every Friday.

## Everything in the pack

| Skill | What it does |
|---|---|
| trading-plan | Your plan: Bot Ladder rung, risk rules first, 90 days to a bot |
| bot-audit | Six blind reviewers check a bot before it touches money |
| account-stats | Real scoreboard from Alpaca or any broker CSV (script) |
| watchlist-pull | Plain-English idea → ranked watchlist (script) |
| ticker-deep-dive | 8-pass research brief, every fact sourced |
| earnings-game-plan | If/then plan decided the night before |
| alert-inbox | Trading email → one morning brief, scams flagged |
| saved-posts-sorter | Saved reels → strategies worth testing (scripts) |
| strategy-to-bot-spec | Any idea → exact build spec |
| pine-script-writer | Plain English → checked Pine Script v6 |
| trading-dashboard-app | Build your own private dashboard app |
| skill-builder | Turn anything you repeat into a skill |
| equity-video | Equity curve → animated MP4 (Remotion template) |
| trade-carousel | Carousel slides + PDF (renderer) |
| reel-script | Hooks + full reel script + caption |
| reel-prompts | AI video prompts for trading B-roll |
| trade-recap | Honest trade post for X, Threads, StockTwits |

Prompt kits in `prompts/`: Yes-Man Off, Trader Bias Audit, Data Lockdown, Bot Brain, Claude Code for Traders, Local AI calculator.

## You're live when

- The MCP answers "Milli: list your playbooks" with 30 playbooks, **or**
- Typing `/` in Claude Code shows `trading-plan`, `bot-audit` and the rest.

## If something's off

| Problem | Fix |
|---|---|
| Connector won't add in ChatGPT | Developer mode must be on; needs a paid plan |
| Skill doesn't show in Claude Code | Folder must be `~/.claude/skills/<name>/SKILL.md`; restart Claude Code |
| Script says module not found | Run the install line in that skill's README |
| Anything else | Email robmilli.ai@gmail.com. We'll get it running with you within 7 days |

> Educational only. Not financial advice. Nothing in this pack places trades.
