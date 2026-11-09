# The 7-Bot Trading Desk

Seven AI bots, one vote, and a risk bot that can veto anything. Run any stock idea past all seven in 15 minutes, free, and see how the automatic desk is built.

**How it works:** Your idea → 7 bots each check one thing → Risk can veto → 5 of 7 must agree → one clear ticket

> **READ FIRST:** It never places an order. A "no" from the desk is a win: it saved you money.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/bots](https://milli-ai.com/free/bots?utm_source=github&utm_medium=repo&utm_campaign=bots)

## How it works
The finished version runs the same desk on its own, every hour the market is open:

- **Scout** checks your whole watchlist for unusual moves.
- **News, Mood and Chart** get real data (real headlines, real prices), not a screenshot.
- **Risk** is plain code, not AI. It can't be talked out of the 1% rule.
- **Chief** counts the votes and texts the ticket to your phone.

> Educational only. Not financial advice. One AI playing seven bots is still one AI, so check its facts.

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter 7-Bot Desk: 7 bots vote, 5 of 7 must agree, and Risk can veto. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir seven-bot-desk && cd seven-bot-desk
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called seven-bot-desk in Python 3: a starter 7-Bot Desk: 7 bots vote, 5 of 7 must agree, and Risk can veto.

WHAT IT DOES
1. Command: python src/main.py --ticker AMD. Pull prices with the free yfinance library.
2. 7 Claude calls, one per bot: Trend, Momentum, Value, News, Sentiment, Devil's Advocate, Risk. Each votes YES or NO as JSON with one reason.
3. 5 of 7 YES and no Risk veto = a ticket (entry, stop, target, size at 1% of a pretend $10,000). Otherwise no trade. Save to tickets/.

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
| Runs your watchlist automatically | ❌ | ✅ |
| Tested bot prompts | ❌ | ✅ |
| Bot scorecard (who is right most) | ❌ | ✅ |
| Phone tickets | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| It answers as one voice, not 7 | Reply: "Answer as all 7 bots, one line each, then the vote." |
| Every idea passes | Ask the Risk bot to be stricter: "No stop = no trade." |
| It makes up news | Paste the news yourself with a date and link. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/bots](https://milli-ai.com/free/bots?utm_source=github&utm_medium=repo&utm_campaign=bots)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=bots)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
