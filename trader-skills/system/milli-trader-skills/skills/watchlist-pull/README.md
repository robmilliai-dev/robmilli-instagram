# watchlist-pull: a Claude Code skill from Milli.ai

The Watchlist Pull skill. Plain-English market idea into a screened, deduped, ranked watchlist CSV plus a TradingView import line and a why-each-one note. Resumable, free data, logs every drop.

From the Milli.ai Trader Skills pack · milli-ai.com/free · comment SCAN on @robmilli.ai

## Install
1. Copy this folder to `~/.claude/skills/watchlist-pull/` (every project) or `.claude/skills/watchlist-pull/` (one project).
2. Open Claude Code. It finds the skill automatically.
3. Run `/watchlist-pull` or just describe the task.

No Claude Code? Paste SKILL.md into a Claude Project's instructions or a custom GPT. Or connect the Milli MCP (milli-ai.com/mcp) and ask for "Watchlist Pull".

## Edit first
Fill every `[bracket]` with your own numbers: your risk %, broker, watchlist. Someone else's constants are worse than none.

## Requirements
Python 3.9+, `pip install yfinance pandas`.

## Safety
Read every file before you run it. Nothing in this pack places trades. Keep API keys in `.env`, never in code or chats.

## License
MIT. Use it, change it, share it.

Educational only. Not financial advice.
