# The One-Ticker Committee

Big funds make 6 experts argue before they buy a stock. Run that same argument on any stock in 15 minutes, free, with one Claude chat.

**How it works:** One stock + one dated fact → 6 experts argue → the Devil's Advocate attacks → Risk can veto → PASS, WATCH or CANDIDATE

> **READ FIRST:** It never buys or sells. Most ideas get PASS or WATCH, and that's the point.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/hedge](https://milli-ai.com/free/hedge?utm_source=github&utm_medium=repo&utm_campaign=hedge)

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter 6-role Hedge Fund Committee that debates any ticker and writes a one-page memo. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir hedge-committee && cd hedge-committee
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called hedge-committee in Python 3: a starter 6-role Hedge Fund Committee that debates any ticker and writes a one-page memo.

WHAT IT DOES
1. Command: python src/main.py --ticker AAPL. Pull 1 year of daily prices and basic company info with the free yfinance library.
2. Run 6 separate Claude calls, one per role: Macro, Fundamental, Technical, Devil's Advocate, Risk Manager (can veto), PM. Each role sees only the data plus the earlier roles' answers and replies as JSON: {"view","evidence":[..],"confidence"}.
3. The PM writes the final call: PASS, WATCH or CANDIDATE. A Risk veto forces PASS. Save the memo to memos/TICKER-DATE.md.

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
| Pulls filings, earnings and news with dates | ❌ | ✅ |
| Tested role prompts | ❌ | ✅ |
| Scorecard that tracks each role's accuracy | ❌ | ✅ |
| Weekly watchlist run | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| It gives one long essay | Reply: "Answer as the 6 roles, then one call." |
| It says CANDIDATE every time | Tell the Devil's Advocate: "Find the strongest reason not to buy." |
| It makes up numbers | Give it your dated fact and say "use only facts I give you". |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/hedge](https://milli-ai.com/free/hedge?utm_source=github&utm_medium=repo&utm_campaign=hedge)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=hedge)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
