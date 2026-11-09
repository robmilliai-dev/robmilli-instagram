# The ARB Bot Gap-Finder Blueprint

A Polymarket bot reportedly turned $1 into $3.3 million by comparing prices, not predicting games. I rebuilt it for you. Here's how it works, how to build it, and a free prompt to check any game in 10 minutes.

**How it works:** Same game, two prices → strip the bookie's cut → find the gap → Claude checks the fine print → risk kills most → you decide

> **READ FIRST:** Gaps are rare and close fast. Most checks end in "no bet", and that's the system working. Check that prediction markets are legal where you live.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/arb](https://milli-ai.com/free/arb?utm_source=github&utm_medium=repo&utm_campaign=arb)

## How it works
1. **WATCHER** pulls the odds from the sportsbooks (The Odds API has a free plan) and the prices from Polymarket (free public data), and matches up the same games.
2. **MATH** removes the bookie's cut and works out the fair price. No AI needed. Just math.
3. **CLAUDE** reads the fine print. This is where most "gaps" turn out to be fake. For example, a bet that ignores overtime isn't the same bet as one that counts it.
4. **RISK** blocks anything that fails a check: gap too small, not enough money in the market, odds too old, or fine print doesn't match. It keeps every bet small.

Every ticket goes to your phone and into a log. After a month, the log shows if the gaps were real.

> Educational only. Not financial advice. Fast pro bots close most gaps quickly. Check that sports prediction markets are legal where you live.

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter ARB gap-finder that compares a sportsbook price with a Polymarket price for the same game. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir gap-finder && cd gap-finder
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called gap-finder in Python 3: a starter ARB gap-finder that compares a sportsbook price with a Polymarket price for the same game.

WHAT IT DOES
1. Read games.json where I paste the sportsbook odds by hand (American or decimal). Pull the matching Polymarket market price from the public Gamma API.
2. Convert odds to percentages, remove the bookie's cut, and show the gap after fees. Skip gaps under 2%.
3. Ask Claude to compare both sites' settlement rules I paste in and reply as JSON: {"same_rules":true|false,"risks":[..],"verdict":"WORTH A LOOK|SKIP"}. Never place bets.

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
| Pulls odds automatically | ❌ | ✅ |
| Scans every game, not one | ❌ | ✅ |
| Rule-matching checks built in | ❌ | ✅ |
| Phone alerts on real gaps | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| The odds look different in different places | Use odds from the same minute. Old odds make fake gaps. |
| The gap is under 4 points | Skip it. Small gaps are usually eaten by fees and slippage. |
| The rules don't match (overtime, dates) | Not a real gap. Skip it. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/arb](https://milli-ai.com/free/arb?utm_source=github&utm_medium=repo&utm_campaign=arb)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=arb)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
