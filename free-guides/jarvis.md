---
title: The JARVIS Blueprint
promise: Text your own AI market assistant like a friend. "Brief me." "How's NVDA?" It looks up the real numbers and texts back. Here's how it works, how to build it, and a free version you can use in 10 minutes.
minutes: 10
nextSystemSlug: jarvis-market-assistant
---

# The JARVIS Blueprint

**Imagine texting "brief me" at 8 a.m. and getting back everything you need to know about your stocks.**

Your positions. What moved. What's coming up. What to watch. In 30 seconds, on your phone.

That's JARVIS. You've seen the "I built JARVIS for the stock market" posts. I rebuilt it from scratch and tested it. This guide shows you how it works, and gives you a free version you can use in 10 minutes. The finished one is at the end.

**When you're done, you'll have:**

- ✅ Your own JARVIS in a Claude chat, ready for questions
- ✅ Real numbers with a source, not guesses
- ✅ The full plan for the phone version

**How it works:** Your holdings + rules → JARVIS looks up real numbers → answers with sources → morning brief on your phone

> **READ FIRST:** Smart enough to research, never allowed to trade. Every claim needs a source and a date.

**Why this works:** Most traders have 12 tabs open and still miss the one thing that mattered. JARVIS looks it all up for you, gives you the answer first, then shows the proof and the risk. One question, one clear answer.

## Try it now: 10 minutes, no code

Open a new [Claude](https://claude.ai/) chat with web search turned on. Paste this, with your own stocks:

```text
You are JARVIS, my calm, sharp stock market assistant.
Rules:
- Look up every number on the web. Never make one up.
  Say where each number came from.
- Give the answer first in one line. Then the proof. Then the risk.
- Never tell me to buy or sell. I decide.
- Keep answers short and in plain English.

My watchlist: [SPY, QQQ, AAPL, NVDA]
My positions: [e.g. AAPL, 10 shares, bought at $210, stop at $199]

Reply "JARVIS ready" and wait for my question.
```

Now ask it things like:

- **"Brief me."**
- **"Which of my positions is closest to its stop?"**
- **"Give me the case against NVDA, with real numbers."**

Check one number against your own chart the first few times. Trust is earned.

## How the phone version works

The real JARVIS has 4 parts:

1. **The brain.** Claude, with strict rules (like the ones above). The #1 rule: look up every number, never guess.
2. **The tools.** Small programs Claude can use on its own: get a stock's price and trend, get the latest news, get the next earnings date, and check your positions and how close each one is to its stop.
3. **The loop.** Claude decides which tools it needs, uses them, then writes the answer. That loop is what turns a chatbot into an assistant.
4. **The phone.** A free Telegram bot. You text it. It texts back. It only answers **you**. Every weekday at 8:45 a.m., it sends your morning brief on its own.

**To build it yourself,** you'd write the tools in Python, connect them to Claude, build the loop, set up the Telegram bot, and keep it running all day. If you're good with Python, that's a few evenings. If not, a lot longer.

> Educational only. Not financial advice.

## Build the starter bot with Claude Code (20 minutes)

Want it running on your computer instead of in a chat? Paste one prompt and Claude Code builds a starter JARVIS research assistant that answers questions about your holdings with real numbers. It runs on pretend money or in read-only mode. It never places a trade or bet.

**You need:** [Claude Code](https://code.claude.com/docs/en/quickstart) (needs a paid Claude plan), Python 3, and an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/) (pay as you go, usually cents per run).

**1. Install Claude Code** (Mac/Linux terminal):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`

**2. Make a folder and open Claude Code in it:**

```bash
mkdir jarvis && cd jarvis
claude
```

**3. Paste this build prompt:**

```text
Build me a beginner-friendly starter bot called jarvis in Python 3: a starter JARVIS research assistant that answers questions about your holdings with real numbers.

WHAT IT DOES
1. Read holdings.json (ticker, shares, buy price). Give Claude two tools: get_price(ticker) and get_info(ticker), both using the free yfinance library.
2. Run a chat loop in the terminal. Claude must use the tools for every number and show the date of each number. No trading tools at all.
3. Add a --brief flag that prints a morning brief of all holdings: value, day change, biggest mover.

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
| Phone version (message it from anywhere) | ❌ | ✅ |
| News and earnings tools | ❌ | ✅ |
| Portfolio risk checks | ❌ | ✅ |
| Daily brief sent to you | ❌ | ✅ |
| Tested by us, with setup support | ❌ | ✅ |

## Make it yours: your JARVIS rules (3 minutes)

Paste this into your JARVIS Project so it knows you:

```text
ABOUT ME
My holdings: ____ (ticker, shares, buy price)
My watchlist: ____
I care about: ____ (e.g. income, growth, not losing big)
RULES FOR JARVIS
Every number needs a source and a date. If you can't find it, say so.
Never tell me to buy or sell. Give me facts and the questions I should ask.
Keep answers short enough to read on my phone.
```

## 12 copy-paste prompts

**Every morning**

1. "Morning brief: what moved in my holdings overnight and why? Sources and dates."
2. "Anything on my watchlist with earnings, dividends or big news this week?"
3. "Which of my holdings is down the most from its high? What's the reason?"

**Research**

4. "Explain [ticker]'s last earnings in 5 bullets, plain English."
5. "What are analysts and the news worried about with [ticker] right now?"
6. "Compare [ticker] to its 2 closest rivals: growth, profit, debt. Simple table."
7. "What would have to go wrong for [ticker] to drop 30%?"

**Risk**

8. "How much of my money is in each sector? Am I too heavy anywhere?"
9. "If the market dropped 10% tomorrow, which of my holdings would likely fall most? Why?"
10. "List every date this month that could move my holdings: earnings, Fed, CPI."

**Review**

11. "Here are my notes from this week. What did I learn and what should I check next week?"
12. "Give me 3 questions I should answer before adding to any position."

## Your 5-minute daily routine

| When | Do this |
|---|---|
| Morning (2 min) | Prompt 1 on your phone. |
| Lunch (1 min) | Prompt 2 if anything big is coming. |
| Evening (2 min) | Note one thing you learned. |

## Weekly review (10 minutes, every Sunday)

This is where you actually get better. Paste your week's notes into Claude with this:

```text
Here are my notes from this week: [paste]
1. Which ideas worked and which didn't? Look for patterns (setup, day, time, market).
2. Where did I break my own rules?
3. Give me ONE change to make next week. Just one.
Use only what's in my notes. Don't guess.
```

## Your first run checklist

- [ ] You set up JARVIS with your holdings and rules
- [ ] You asked it one real question and got sources back
- [ ] You got your first morning brief

## Troubleshooting

| Problem | Fix |
|---|---|
| It answers without sources | Reply: "Every claim needs a source and a date." |
| It gives advice like "buy" | Remind it: "You research. I decide. No buy or sell calls." |
| The brief is too long | Ask for 3 bullets: what moved, what's on today, one risk. |

## Want it done for you?

You just did it once, by hand. **The finished JARVIS lives on your phone: text it any question, any time, and get real numbers back. Plus a morning brief that shows up on its own every weekday.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished JARVIS**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst, the Hedge Fund Committee and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished JARVIS for $199 →]({{offerUrl}})**
