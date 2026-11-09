# The 15-Minute Market Watch

Stop staring at charts. Set one alert in 15 minutes, get pinged when your stock hits your price, and have AI check the move before you do anything.

**How it works:** Pick a stock and a price → TradingView alert → your phone pings → AI checks the move → you write down what happened

> **READ FIRST:** The alert only tells you the price was hit. AI checks the move. You make every decision.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/desk](https://milli-ai.com/free/desk?utm_source=github&utm_medium=repo&utm_campaign=desk)

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter Market Watch that checks your watchlist every 15 minutes and tells you when a price crosses your level. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir market-watch && cd market-watch
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called market-watch in Python 3: a starter Market Watch that checks your watchlist every 15 minutes and tells you when a price crosses your level.

WHAT IT DOES
1. Read watchlist.json: [{"ticker","level","direction":"above|below"}]. Every 15 minutes during US market hours, get the latest daily price with the free yfinance library.
2. When a close crosses a level, ask Claude to check it against rules.md and reply as JSON: {"verdict":"STILL VALID|WAIT|IGNORE","reason","stop_idea"}.
3. Log every check to logs/alerts.jsonl and print alerts in the terminal.

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
| Real-time TradingView alerts in, phone message out | ❌ | ✅ |
| Earnings and Fed-day blocker | ❌ | ✅ |
| Tested watch rules | ❌ | ✅ |
| Daily summary | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| The alert never fired | Check it's set to "Crossing" and the app has notifications on. |
| Too many alerts | Use one alert per stock, on prices that matter. |
| The AI check is vague | Paste the chart screenshot and the news headline with it. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/desk](https://milli-ai.com/free/desk?utm_source=github&utm_medium=repo&utm_campaign=desk)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=desk)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
