# The 24/7 AI Trader Blueprint

An AI trader that watches the market while you work and texts you only when there's a real setup. Here's how it works, how to build it, and a free prompt that runs it on any chart today.

**How it works:** Pick a chart → paste the free prompt → AI checks breakout or pullback → strict risk check → APPROVE FOR REVIEW, WATCHLIST or REJECT

> **READ FIRST:** It never places a trade. It does the homework, you make the call. A REJECT is a win: it saved you from a bad trade.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/24-7](https://milli-ai.com/free/24-7?utm_source=github&utm_medium=repo&utm_campaign=24-7)

## How it works
The real AI trader does the same thing, on its own, every hour:

1. **Scan.** It pulls prices for every stock on your watchlist. Free data.
2. **Spot.** It looks for the two setups: breakout or pullback.
3. **Plan.** It works out the entry, stop and target.
4. **Risk check.** It sizes the trade so a loss only costs 1%. If the reward is too small, it's a hard **no**. The AI can't argue past this.
5. **Decide.** Claude writes one short note: approve, watch or reject, and why.
6. **Text you.** The note goes straight to your phone. Every idea is saved in a log.

> Educational only. Not financial advice.

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter 24/7 Market Watch that scans your watchlist on a schedule and writes a risk-checked memo. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir trader-247 && cd trader-247
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called trader-247 in Python 3: a starter 24/7 Market Watch that scans your watchlist on a schedule and writes a risk-checked memo.

WHAT IT DOES
1. Every hour, pull daily prices for watchlist.json with the free yfinance library. Flag breakouts (close above the 20-day high) and pullbacks (uptrend, close back above the 20-day average).
2. Send each flagged ticker's numbers to Claude with rules.md. Reply as JSON: {"verdict":"APPROVE FOR REVIEW|WATCHLIST|REJECT","rule_that_decided","stop","target"}.
3. Never place orders. Log to logs/memos.jsonl and print a morning summary.

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
| Runs 24/7 on a cheap server | ❌ | ✅ |
| Phone alerts | ❌ | ✅ |
| Earnings and Fed-day blocker | ❌ | ✅ |
| Tested scan and risk rules | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| It says it can't see the chart | Upload a clear screenshot with the price axis showing, or paste the last 20 closes as text. |
| Every answer is REJECT | Normal on quiet days. Try a stock that moved a lot this week. |
| The answer is long and messy | Reply: "Answer only in the format I gave you." |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/24-7](https://milli-ai.com/free/24-7?utm_source=github&utm_medium=repo&utm_campaign=24-7)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=24-7)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
