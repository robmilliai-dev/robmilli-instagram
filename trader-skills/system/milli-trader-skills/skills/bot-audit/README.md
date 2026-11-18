# bot-audit: a Claude Code skill from Milli.ai

The Bot Audit skill. Six blind reviewers audit a trading bot before it touches money: backtest honesty, risk and kill switches, order bugs, leaked keys, data timing, overfitting. Findings JSON + plain report + verified fixes.

From the Milli.ai Trader Skills pack · milli-ai.com/free · comment AUDIT on @robmilli.ai

## Install
1. Copy this folder to `~/.claude/skills/bot-audit/` (every project) or `.claude/skills/bot-audit/` (one project).
2. Open Claude Code. It finds the skill automatically.
3. Run `/bot-audit` or just describe the task.

No Claude Code? Paste SKILL.md into a Claude Project's instructions or a custom GPT. Or connect the Milli MCP (milli-ai.com/mcp) and ask for "Bot Audit".

## Edit first
Fill every `[bracket]` with your own numbers: your risk %, broker, watchlist. Someone else's constants are worse than none.

## Requirements
Nothing beyond Claude Code (or paste SKILL.md into a Claude Project / ChatGPT custom GPT).

## Safety
Read every file before you run it. Nothing in this pack places trades. Keep API keys in `.env`, never in code or chats.

## License
MIT. Use it, change it, share it.

Educational only. Not financial advice.
