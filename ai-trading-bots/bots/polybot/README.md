# The POLYBOT 6-Agent Blueprint

A Polymarket bot reportedly turned $150 into $279,053. I rebuilt it for you. Here's how its 6 AI agents work, how to build it, and a free prompt that runs the whole team in 10 minutes.

**How it works:** Scout finds markets → Odds finds the gap → News checks the facts → Thesis builds both sides → Risk can cancel → you approve

> **READ FIRST:** It never places a bet on its own. Most ideas get cancelled. Check that prediction markets are legal where you live.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/polybot](https://milli-ai.com/free/polybot?utm_source=github&utm_medium=repo&utm_campaign=polybot)

## How it works
1. **SCOUT** checks the 100 busiest markets on Polymarket (free public data). It flags 3 things: a big jump in betting, odds moving 5+ points, or an end date coming soon.
2. **NEWS** searches the web for fresh reporting. It only counts facts with a source and a date.
3. **THESIS** builds the best case for YES and for NO, and names what would kill the bet.
4. **ODDS** is simple math. If the market says 42% and the team says 57%, that's a 15-point gap.
5. **RISK** is the bouncer. It sizes the bet small (never more than 2% of your money) and blocks anything that fails a check: gap too small, news is a rumor, not enough money in the market, or too little time left.
6. **EXECUTION** writes one ticket and sends it to your phone. It never bets for you.

Every run is saved to a log. After a month, you can see if the team beat the market. If it didn't, you don't trust it. Simple.

> Educational only. Not financial advice. You can lose what you bet. Check that Polymarket is allowed where you live.

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter POLYBOT that scans Polymarket markets and runs the 6 agents on the best ones. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir polybot && cd polybot
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called polybot in Python 3: a starter POLYBOT that scans Polymarket markets and runs the 6 agents on the best ones.

WHAT IT DOES
1. Pull active markets from the public Polymarket Gamma API (https://gamma-api.polymarket.com/markets?active=true&closed=false). If a field name is unclear, print a sample and leave a clear TODO instead of guessing.
2. Keep markets with enough volume that resolve within 60 days. For the top 5, run 6 Claude roles: Scout, Odds, News, Thesis, Risk (can veto), Execution (writes the ticket only). Each replies as JSON.
3. Never place bets. No wallet, no keys, no signing code. Log every ticket to logs/tickets.jsonl.

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
| Runs every hour and texts you the best tickets | ❌ | ✅ |
| News checks with dated sources | ❌ | ✅ |
| Self-grading log so you see if it works | ❌ | ✅ |
| Tested agent prompts | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| It treats rumors as news | Paste only dated, linked sources. |
| Every market looks good | Ask Risk: "Give 3 reasons to skip this." |
| It can't see live prices | Paste the current price and volume yourself. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/polybot](https://milli-ai.com/free/polybot?utm_source=github&utm_medium=repo&utm_campaign=polybot)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=polybot)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
