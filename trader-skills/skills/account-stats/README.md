# account-stats: a Claude Code skill from Milli.ai

The Account Stats skill. Your real scoreboard from Alpaca or any broker CSV: equity, today's P&L, return, worst drop, exposure, win rate, profit factor. As a block, an honest post or JSON. Knows the traps that make stats lie.

From the Milli.ai Trader Skills pack · milli-ai.com/free · comment STATS on @robmilli.ai

## Install
1. Copy this folder to `~/.claude/skills/account-stats/` (every project) or `.claude/skills/account-stats/` (one project).
2. Open Claude Code. It finds the skill automatically.
3. Run `/account-stats` or just describe the task.

No Claude Code? Paste SKILL.md into a Claude Project's instructions or a custom GPT. Or connect the Milli MCP (milli-ai.com/mcp) and ask for "Account Stats".

## Edit first
Fill every `[bracket]` with your own numbers: your risk %, broker, watchlist. Someone else's constants are worse than none.

## Requirements
Python 3.8+ (no packages). Alpaca keys or a broker CSV.

## Safety
Read every file before you run it. Nothing in this pack places trades. Keep API keys in `.env`, never in code or chats.

## License
MIT. Use it, change it, share it.

Educational only. Not financial advice.
