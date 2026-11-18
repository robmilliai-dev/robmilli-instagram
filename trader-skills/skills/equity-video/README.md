# equity-video: a Claude Code skill from Milli.ai

The Equity Curve Video skill. Equity curve CSV into a 12-second animated MP4: hook, the curve draws itself, the worst drop marked in red, final stats. Reel, square and wide presets.

From the Milli.ai Trader Skills pack · milli-ai.com/free · comment REPLAY on @robmilli.ai

## Install
1. Copy this folder to `~/.claude/skills/equity-video/` (every project) or `.claude/skills/equity-video/` (one project).
2. Open Claude Code. It finds the skill automatically.
3. Run `/equity-video` or just describe the task.

No Claude Code? Paste SKILL.md into a Claude Project's instructions or a custom GPT. Or connect the Milli MCP (milli-ai.com/mcp) and ask for "Equity Curve Video".

## Edit first
Fill every `[bracket]` with your own numbers: your risk %, broker, watchlist. Someone else's constants are worse than none.

## Requirements
Node 18+. `bash scripts/setup.sh` installs Remotion.

## Safety
Read every file before you run it. Nothing in this pack places trades. Keep API keys in `.env`, never in code or chats.

## License
MIT. Use it, change it, share it.

Educational only. Not financial advice.
