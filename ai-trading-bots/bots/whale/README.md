# The Whale Team

Find the Polymarket wallets that actually win, kill the lucky ones, and see what the smart money holds right now. 6 AI agents, public data, no code.

**How it works:** Wallet Scout → Luck Filter → Market Scanner → Odds Analyst → Risk Manager (can veto) → Tracker (simulated log)

> **READ FIRST:** This is research, not auto-copying. It never places a bet. Past profits don't predict future ones. Check that prediction markets are legal where you live.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/whale](https://milli-ai.com/free/whale?utm_source=github&utm_medium=repo&utm_campaign=whale)

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter Whale Team that runs the Luck Filter on the Polymarket leaderboard and finds shared bets. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir whale-team && cd whale-team
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called whale-team in Python 3: a starter Whale Team that runs the Luck Filter on the Polymarket leaderboard and finds shared bets.

WHAT IT DOES
1. Pull the monthly profit leaderboard from the public Polymarket data API (https://data-api.polymarket.com/v2/leaderboard?timePeriod=MONTH&orderBy=PNL&limit=50) and the all-time one. If a field name is unclear, print a sample and leave a TODO.
2. Apply the Luck Filter in Python: fail wallets with profit under 1% of volume, wallets not on the all-time list, and wallets with fewer than 20 markets traded.
3. For passing wallets, pull open positions (https://data-api.polymarket.com/v2/positions?user=WALLET) and list markets that 2+ passing wallets hold on the same side. Ask Claude for a WATCH or SKIP on each. Never place bets.

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
| Runs daily and messages you new shared bets | ❌ | ✅ |
| Price-moved-already check | ❌ | ✅ |
| Wallet scorecard over time | ❌ | ✅ |
| Pairs with the finished POLYBOT | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| The leaderboard won't show volume | Open each wallet's profile; volume is shown there. |
| No markets are shared | Normal on some days. Try the weekly leaderboard, or widen to the top 50. |
| Claude invents numbers | Reply: "Use only the numbers I gave you." |
| Every lead gets vetoed | Good. The Risk Manager is doing its job. Most copy ideas should die. |

> Real public Polymarket data. Wallet names are public usernames. Past profits don't predict future results. Educational, not financial advice. You make every decision.

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/whale](https://milli-ai.com/free/whale?utm_source=github&utm_medium=repo&utm_campaign=whale)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=whale)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
