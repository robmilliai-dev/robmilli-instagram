# trade-carousel: a Claude Code skill from Milli.ai

The Trade Carousel skill. Carousel about a trade or backtest: giant-number hook slide, content slides, keyword CTA, caption. HTML to 1080x1350 PNGs plus a PDF DM asset. Dark and light.

From the Milli.ai Trader Skills pack · milli-ai.com/free · comment CAROUSEL on @robmilli.ai

## Install
1. Copy this folder to `~/.claude/skills/trade-carousel/` (every project) or `.claude/skills/trade-carousel/` (one project).
2. Open Claude Code. It finds the skill automatically.
3. Run `/trade-carousel` or just describe the task.

No Claude Code? Paste SKILL.md into a Claude Project's instructions or a custom GPT. Or connect the Milli MCP (milli-ai.com/mcp) and ask for "Trade Carousel".

## Edit first
Fill every `[bracket]` with your own numbers: your risk %, broker, watchlist. Someone else's constants are worse than none.

## Requirements
Node 18+, `npm i playwright` (or an existing Chrome via CHROME_PATH).

## Safety
Read every file before you run it. Nothing in this pack places trades. Keep API keys in `.env`, never in code or chats.

## License
MIT. Use it, change it, share it.

Educational only. Not financial advice.
