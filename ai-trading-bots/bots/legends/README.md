# The Legends Algo Blueprint

Turn the ideas of Buffett, Lynch, Dalio, Soros and Simons into 5 simple rules a computer can test. Plus a free prompt that turns your own idea into a rule in 10 minutes.

**How it works:** Pick a legend's idea → turn it into one simple rule → test it on years it never saw → keep it only if it holds up

> **READ FIRST:** Old results don't promise future ones. A rule that only works on the years you tuned it on is a fake rule.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/legends](https://milli-ai.com/free/legends?utm_source=github&utm_medium=repo&utm_campaign=legends)

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter Legends Test Lab that tests a simple rule on years it never saw. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir legends-lab && cd legends-lab
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called legends-lab in Python 3: a starter Legends Test Lab that tests a simple rule on years it never saw.

WHAT IT DOES
1. Read rule settings from config.json. Pull daily prices with the free yfinance library for the tickers listed.
2. Backtest one rule (start with: buy when price is above its 200-day average, sell when below). Include 0.05% costs per trade and use only today's close to decide tomorrow's trade.
3. Split the data: pick settings on years up to 2019, report results on 2020 onward. Report trades, win rate, average win vs loss, worst drop, and buy-and-hold for comparison. Save to reports/.

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
| All 5 legend rules built and tested | ❌ | ✅ |
| Many markets at once | ❌ | ✅ |
| Charts and a one-page report | ❌ | ✅ |
| Rule-cheating checks built in | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| My rule has "feel" words | Swap them for numbers: not "cheap", but "price under 15x earnings". |
| It looks amazing in the test | Check it on years you didn't tune on. Most "amazing" rules fail there. |
| Too few trades to judge | Test more markets or more years. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/legends](https://milli-ai.com/free/legends?utm_source=github&utm_medium=repo&utm_campaign=legends)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=legends)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
