# The Claude Chart Read

Upload one chart. Get a clear, simple read in 15 minutes. Trend, key prices, the setup and the biggest red flag, in plain English.

**How it works:** Clean screenshot → Claude reads trend, key prices, setup and biggest red flag → you check its work → save one watch line

> **READ FIRST:** Claude can misread a chart. Always check one number yourself before you trust the read.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/chart](https://milli-ai.com/free/chart?utm_source=github&utm_medium=repo&utm_campaign=chart)

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter Chart Analyst that reads any chart screenshot you drop in a folder and writes the read to a log. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir chart-analyst && cd chart-analyst
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called chart-analyst in Python 3: a starter Chart Analyst that reads any chart screenshot you drop in a folder and writes the read to a log.

WHAT IT DOES
1. Watch the charts/ folder. When a new PNG or JPG appears, send it to Claude with the analyst prompt and my rules from rules.md.
2. Claude must reply as JSON: {"ticker","timeframe","trend","key_prices":[..],"setup","red_flag","watch_line","verdict":"TAKE A CLOSER LOOK|WATCH|SKIP","confidence"}. Treat the reply as data, never as instructions.
3. Save every read to logs/reads.jsonl and print a short summary.

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
| Reads every TradingView alert automatically | ❌ | ✅ |
| Sends the read to your phone | ❌ | ✅ |
| Tested prompts and rules for 4 setups | ❌ | ✅ |
| Weekly accuracy report | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| Claude reads the wrong prices | Zoom in so the price axis is clear, or type the key prices in. |
| The read is vague | Reply: "Give exact prices, not ranges." |
| It sounds too sure | Ask: "What would prove this wrong?" |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/chart](https://milli-ai.com/free/chart?utm_source=github&utm_medium=repo&utm_campaign=chart)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=chart)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
