# Claude × TradingView Blueprint

Turn Claude into your own TradingView analyst tonight. Master Prompt, 25 copy-paste prompts, alert templates, risk rules and a free tested indicator. Level 1 takes 15 minutes.

**How it works:** Connect → Scan → Analyze → Decide → Alert → Review

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/tradingview](https://milli-ai.com/free/tradingview?utm_source=github&utm_medium=repo&utm_campaign=tradingview)

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter TradingView webhook analyst: alerts come in, Claude checks them against your rules. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir tv-analyst && cd tv-analyst
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called tv-analyst in Python 3: a starter TradingView webhook analyst: alerts come in, Claude checks them against your rules.

WHAT IT DOES
1. A small FastAPI app with POST /alert that accepts the alert JSON from this guide (ticker, exchange, timeframe, price, high, low, volume, time, setup). Protect it with a secret in the URL from .env.
2. For each alert, ask Claude to re-check it against rules.md and reply as JSON: {"verdict":"STILL VALID|WAIT|IGNORE","reason","stop","size_at_1pct"}.
3. Log every alert and verdict to webhooks/alerts-log.md. Add a --demo flag that sends 3 fake alerts without TradingView.

RULES FOR THE BUILD
4. Use the official Anthropic Python SDK. Put the model name in config.json. Read ANTHROPIC_API_KEY from .env with python-dotenv. Create .env.example with placeholders and add .env, data/ and logs/ to .gitignore. Never hardcode keys.
5. It never places real trades or bets. No broker or wallet code, no private keys.
6. Put every setting (limits, tickers, thresholds) in config.json so I can change them without touching code.
7. Add a --demo flag that runs the whole thing on made-up data with no internet, so I can test it first.
8. Handle errors and rate limits with a short wait and retry. If you are not sure an API endpoint or field exists, leave a clear TODO instead of guessing.
9. Write a README.md for a total beginner: install, add the key, run --demo, run for real, read the logs.
10. Keep it simple and well commented, under about 400 lines. When done, explain what you built and list anything you could not check.
```

**4. Install and test:**

```bash
pip install -r requirements.txt
cp .env.example .env
python src/main.py --demo
```

Add your key to `.env` with a text editor, then run it for real (the README shows the exact command).

> **Keep your key safe:** never paste API keys into a chat, a screenshot or GitHub. Keep `.env` in `.gitignore`.

**Starter vs finished**

| | Starter (free, this prompt) | Finished (AI Desk) |
|---|---|---|
| Works on your computer | ✅ | ✅ |
| Hosted for you, always on | ❌ | ✅ |
| Sends the verdict to your phone | ❌ | ✅ |
| Tested rules for 4 setups | ❌ | ✅ |
| Weekly review report | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| Claude misreads prices | Zoom in so the price axis is readable, or paste the key prices as text. |
| Claude says "buy" or "sell" | Paste the Master Prompt again. It should only say what your rules say. |
| The alert never fires | Use "Once per bar close" and turn on app notifications. Check the condition is right. |
| Webhook option is greyed out | Webhooks need a paid TradingView plan. Everything else in this kit is free. |
| "Script could not be translated" | Paste the error into Claude with prompt #21. |

> Hypothetical backtests on past prices; past results don't guarantee future results. Educational only, not financial advice. Claude analyzes. It never trades. You make every decision.

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/tradingview](https://milli-ai.com/free/tradingview?utm_source=github&utm_medium=repo&utm_campaign=tradingview)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=tradingview)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
