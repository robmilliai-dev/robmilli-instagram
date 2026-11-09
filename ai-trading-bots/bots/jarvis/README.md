# The JARVIS Blueprint

Text your own AI market assistant like a friend. "Brief me." "How's NVDA?" It looks up the real numbers and texts back. Here's how it works, how to build it, and a free version you can use in 10 minutes.

**How it works:** Your holdings + rules → JARVIS looks up real numbers → answers with sources → morning brief on your phone

> **READ FIRST:** Smart enough to research, never allowed to trade. Every claim needs a source and a date.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/jarvis](https://milli-ai.com/free/jarvis?utm_source=github&utm_medium=repo&utm_campaign=jarvis)

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter JARVIS research assistant that answers questions about your holdings with real numbers. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir jarvis && cd jarvis
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called jarvis in Python 3: a starter JARVIS research assistant that answers questions about your holdings with real numbers.

WHAT IT DOES
1. Read holdings.json (ticker, shares, buy price). Give Claude two tools: get_price(ticker) and get_info(ticker), both using the free yfinance library.
2. Run a chat loop in the terminal. Claude must use the tools for every number and show the date of each number. No trading tools at all.
3. Add a --brief flag that prints a morning brief of all holdings: value, day change, biggest mover.

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
| Phone version (message it from anywhere) | ❌ | ✅ |
| News and earnings tools | ❌ | ✅ |
| Portfolio risk checks | ❌ | ✅ |
| Daily brief sent to you | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| It answers without sources | Reply: "Every claim needs a source and a date." |
| It gives advice like "buy" | Remind it: "You research. I decide. No buy or sell calls." |
| The brief is too long | Ask for 3 bullets: what moved, what's on today, one risk. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/jarvis](https://milli-ai.com/free/jarvis?utm_source=github&utm_medium=repo&utm_campaign=jarvis)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=jarvis)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
