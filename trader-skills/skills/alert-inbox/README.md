# alert-inbox: a Claude Code skill from Milli.ai

The Alert Inbox skill. Forty trading emails a day into one morning brief: real alerts by ticker, newsletters in 2 lines, hype counted and ignored, scams flagged. Drafts replies, never sends, never trades.

From the Milli.ai Trader Skills pack · milli-ai.com/free · comment INBOX on @robmilli.ai

## Install
1. Copy this folder to `~/.claude/skills/alert-inbox/` (every project) or `.claude/skills/alert-inbox/` (one project).
2. Open Claude Code. It finds the skill automatically.
3. Run `/alert-inbox` or just describe the task.

No Claude Code? Paste SKILL.md into a Claude Project's instructions or a custom GPT. Or connect the Milli MCP (milli-ai.com/mcp) and ask for "Alert Inbox".

## Edit first
Fill every `[bracket]` with your own numbers: your risk %, broker, watchlist. Someone else's constants are worse than none.

## Requirements
A Gmail connector or Gmail MCP server (read + create draft).

## Safety
Read every file before you run it. Nothing in this pack places trades. Keep API keys in `.env`, never in code or chats.

## License
MIT. Use it, change it, share it.

Educational only. Not financial advice.
