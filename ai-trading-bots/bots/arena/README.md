# The ARENA Playbook Blueprint

An AI beat ChatGPT, Claude, Gemini and Grok in a real-money trading contest: +22% in 17 days. I rebuilt its playbook as a 4-agent team. Here's how it works and a free prompt to run it in 10 minutes.

**How it works:** Market data → 4 agents (scout, analyst, risk, judge) → one trade plan with a stop → you decide

> **READ FIRST:** It's a research playbook, not a promise. It never places a trade. Use small risk on anything you try.

**Free full guide (step by step, with 12 copy-paste prompts, daily routine and weekly review):** [milli-ai.com/free/arena](https://milli-ai.com/free/arena?utm_source=github&utm_medium=repo&utm_campaign=arena)

## How it works
1. **SIGNAL** checks Bitcoin, Ethereum and Solana every hour (free data). It only looks for the two setups above. No setup? No AI call, no cost.
2. **JUDGE** is Claude. It scores the setup and sets the stop and target. It's told to skip when in doubt.
3. **RISK** is plain code. The AI can't argue with it. Score under 70, bad stop, small reward, or 3 trades already today? Blocked. Every trade is sized so a loss costs just 1%.
4. **JOURNAL** saves every idea and texts the ticket to your phone.

After a month, the log shows if the high-scoring trades really did better. That's how you tune it.

> Educational only. Not financial advice. Crypto moves fast and you can lose money.

## Build the free starter version with Claude Code (20 minutes)
Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter ARENA crypto desk: SIGNAL, JUDGE, RISK and JOURNAL agents on BTC, ETH and SOL. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir arena && cd arena
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called arena in Python 3: a starter ARENA crypto desk: SIGNAL, JUDGE, RISK and JOURNAL agents on BTC, ETH and SOL.

WHAT IT DOES
1. Pull daily candles for BTC, ETH and SOL from a free public source (for example the Coinbase Exchange public candles endpoint). If unsure of an endpoint, leave a TODO.
2. SIGNAL (Python): trend and 20-day breakout. JUDGE (Claude): builds a plan with entry, stop, target. RISK (Python): size at 1% of a pretend $10,000 account, reject if reward under 2x risk, no leverage.
3. Pretend-money only. Log every plan and result to journal.jsonl.

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
| Runs on a schedule with phone alerts | ❌ | ✅ |
| Tested risk rules | ❌ | ✅ |
| Weekly journal review | ❌ | ✅ |
| Multi-model judge | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Troubleshooting
| Problem | Fix |
|---|---|
| The AI makes up prices | Paste the real prices yourself and say "use only these numbers". |
| The plan has no stop | Reply: "Every plan needs a stop. Redo it." |
| All 4 agents agree every time | Ask the risk agent to argue against the trade first. |

## Want the finished version?

The prompt above builds a starter. The finished, tested version (one-command install, plain setup steps, and help if you get stuck) is part of the Milli.ai AI Desk.

- Free full guide: [milli-ai.com/free/arena](https://milli-ai.com/free/arena?utm_source=github&utm_medium=repo&utm_campaign=arena)
- Finished bot: [milli-ai.com](https://milli-ai.com/?utm_source=github&utm_medium=repo&utm_campaign=arena)

> Educational only. Not financial advice. It never places trades for you. You make every decision.
