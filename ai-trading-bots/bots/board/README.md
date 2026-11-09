# The AI Board Blueprint

Five top AIs, five jobs, one vote. Perplexity, Grok, Gemini, ChatGPT and Claude each check a trade, and Claude can veto. Here's how it works, how to build it, and 5 free prompts you can use today.

**How it works:** Perplexity finds the news → Grok reads the crowd → Gemini reads the chart → ChatGPT builds the case → Claude hunts for risk → vote

> **READ FIRST:** A trade only passes if 4 of 5 say yes and Claude doesn't veto. It never trades for you.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/board](https://milli-ai.com/free/board?utm_source=github&utm_medium=repo&utm_campaign=board)

## How it works
1. **Real data first.** The bot pulls a year of real prices, so the chart seat can't make up numbers.
2. **One call per AI.** Each AI gets its prompt automatically and sends back a vote.
3. **Backup plan.** No key for one of the AIs? Claude fills that seat. If an AI breaks or times out, that seat votes NO. A broken AI can never sneak through a yes.
4. **Hard rules in code.** 4 of 5 votes, no Claude veto, at least 2 real sources, a sensible stop, and a 1% max loss. The AIs can't argue past these.
5. **Ticket to your phone.** One text with every vote and the reason. Every run is saved, so you can see if the board's picks beat its rejects.

> Educational only. Not financial advice. AI can be wrong.

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter AI Board: 5 seats vote on a stock idea and Claude can block it. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir ai-board && cd ai-board
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called ai-board in Python 3: a starter AI Board: 5 seats vote on a stock idea and Claude can block it.

WHAT IT DOES
1. Command: python src/main.py --ticker NVDA. Pull prices with the free yfinance library.
2. Run 5 seats as 5 separate Claude calls with different jobs (News, Crowd, Chart, Bull case, Risk). If I add other AI keys later, each seat can use a different model; leave a clear setting for that.
3. Count the votes. Risk can block. Final: PASS, WATCH or CANDIDATE. Save to memos/.

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
| 5 different AI models (Perplexity, Grok, Gemini, ChatGPT, Claude) | ❌ | ✅ |
| Tested seat prompts | ❌ | ✅ |
| Vote scorecard over time | ❌ | ✅ |
| Weekly watchlist run | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| I don't have all 5 AIs | Free versions work. Missing one? Count it as a "no". |
| The AIs disagree a lot | Good. That's the point. Read the "no" reasons first. |
| One AI makes up a fact | Ask it for the source and date. No source = ignore it. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/board](https://milli-ai.com/free/board?utm_source=github&utm_medium=repo&utm_campaign=board)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=board)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
