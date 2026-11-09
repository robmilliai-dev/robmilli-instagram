# OpenBB in 10 Minutes

Get a free, Bloomberg-style data terminal on your computer in 10 minutes. Then have Claude write you a market brief using only real data. No subscription.

**How it works:** Install OpenBB → pull real prices → Claude writes a brief using only that data → you check one number

> **READ FIRST:** Claude must use only the numbers you give it. Always check one number yourself.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/terminal](https://milli-ai.com/free/terminal?utm_source=github&utm_medium=repo&utm_campaign=terminal)

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter Morning Brief that pulls real prices and writes a dated brief every morning. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir morning-brief && cd morning-brief
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called morning-brief in Python 3: a starter Morning Brief that pulls real prices and writes a dated brief every morning.

WHAT IT DOES
1. Read watchlist.json. Pull the last 1 year of daily prices with the free yfinance library (or OpenBB if installed) and save to data/prices.csv.
2. Compute: day and week change, distance from 50- and 200-day average, 52-week high/low. Do the math in Python, not in Claude.
3. Send only the computed table to Claude to write a brief under 200 words. Every number in the brief must come from the table. Save to briefs/DATE.md.

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
| OpenBB setup with earnings, news and macro data | ❌ | ✅ |
| Email or phone delivery | ❌ | ✅ |
| Number-checker that flags anything not in the data | ❌ | ✅ |
| Weekly trend report | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| "python" isn't found | Install Python from python.org and tick "Add to PATH", then reopen the terminal. |
| pip install fails | Run: python -m pip install --upgrade pip, then try again. |
| Claude adds numbers you didn't give it | Reply: "Use only the data I pasted." |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/terminal](https://milli-ai.com/free/terminal?utm_source=github&utm_medium=repo&utm_campaign=terminal)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=terminal)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
