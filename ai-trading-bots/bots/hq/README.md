# The AI Trading HQ

Send a stock idea up a 6-floor AI building. Each floor can stop it. Only the best ideas reach the top. Free in 15 minutes, plus how the automatic version is built.

**How it works:** Your idea rides up 6 floors → each floor can stop it → only the best reach the top → PASS, WATCH or CANDIDATE

> **READ FIRST:** It never places a trade. Most ideas stop on a lower floor. That's the point.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/hq](https://milli-ai.com/free/hq?utm_source=github&utm_medium=repo&utm_campaign=hq)

## How it works
The finished version does this on its own, every hour the market is open: it scans your watchlist, pulls real news and prices, runs the risk rules in plain code (so no AI can argue past them), and texts you only the ideas that reach the top.

> Educational only. Not financial advice.

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter 6-floor Trading HQ: an idea rides up 6 floors and any floor can stop it. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir trading-hq && cd trading-hq
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called trading-hq in Python 3: a starter 6-floor Trading HQ: an idea rides up 6 floors and any floor can stop it.

WHAT IT DOES
1. Command: python src/main.py --ticker MSFT. Pull prices with the free yfinance library.
2. Floors in order: Scan, Research, Charts, Test (simple check of how this setup did on this stock before, in Python), Risk (can stop anything), Decision. Each floor is a Claude call that replies as JSON with PASS or STOP and a reason.
3. Stop at the first STOP. Final: PASS, WATCH or CANDIDATE. Save the floor-by-floor memo to memos/.

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
| Six-Bot Trading Team, fully automated | ❌ | ✅ |
| Tested floor prompts | ❌ | ✅ |
| Runs your whole watchlist daily | ❌ | ✅ |
| Phone summary | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| It skips floors | Reply: "Go floor by floor, one line each." |
| Every idea reaches the top | Make floor 5 (Risk) stricter: "No stop = stop the idea." |
| It makes up facts | Paste the news yourself with a date. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/hq](https://milli-ai.com/free/hq?utm_source=github&utm_medium=repo&utm_campaign=hq)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=hq)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
