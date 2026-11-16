---
title: The POLYBOT 6-Agent Blueprint
promise: Somebody says their Polymarket bot turned $150 into $279,053. I can't prove that. So I took the idea apart, rebuilt it and tested it. Here's how its 6 AI agents work, and a free prompt that runs the whole team in 10 minutes.
minutes: 10
nextSystemSlug: polymarket-research-team
---

# The POLYBOT 6-Agent Blueprint

**A Polymarket bot reportedly turned $150 into $279,053.**

*(That's the original creator's own claim. It isn't my result, and nobody has checked it.)*

When I saw that number, I had one question. Not "is it true?" I can't know that. Neither can you.

My question was: how would a bot like that even work?

So I rebuilt the system behind it from scratch. Then I tested it.

This guide shows you exactly what I found. You'll run the whole thing yourself, free, in about 10 minutes. No code.

And if you'd rather skip the building, the finished bot is waiting at the bottom of the page.

**When you're done, you'll have:**

- ✅ A free prompt that runs a 6-agent AI research team on any Polymarket bet
- ✅ A clear answer: **READY FOR YOUR REVIEW** or **BLOCKED BY RISK**
- ✅ The full plan for how the automatic bot works

**How it works:** Scout finds markets → Odds finds the gap → News checks the facts → Thesis builds both sides → Risk can cancel → you approve

> **READ FIRST:** It never places a bet on its own. Most ideas get cancelled. Check that prediction markets are legal where you live.

**Why this works:** Here's the part almost nobody tells you. The secret is not one genius AI. It's a **team**. Each agent has one job, and any one of them can kill a bad bet. Most bots lose for a simple reason: nobody on the inside ever says "no." This one is built to say no. A lot. So the few bets that make it through are the ones worth your time.

**SCOUT → NEWS → THESIS → ODDS → RISK → EXECUTION**

## Try it now: 10 minutes, no code

1. Open any market on Polymarket.
2. Copy 4 things: the question, the YES price, the end date, and the **Rules** text.
3. Open a new [Claude](https://claude.ai/) chat with web search turned on.
4. Paste this, filled in:

```text
You are a 6-agent research team for ONE Polymarket market. You never place bets.

MARKET: [question]
YES PRICE: [e.g. 0.42]
END DATE: [date]
RULES: [paste the rules]

1. SCOUT: Why might this price be wrong right now? If no reason, say so.
2. NEWS: Search the web. Only count facts with a named source and a date.
   End with: VERIFIED, RUMOR or NOTHING NEW.
3. THESIS: Best case for YES. Best case for NO. The one thing that kills
   the bet. Your YES chance in %. Keep it near the price if news is thin.
4. ODDS: Your % vs the price. Which side is cheap, and by how many points?
5. RISK: Pass or fail on each: gap of 5+ points, news isn't a rumor,
   rules are clear, more than 1 day left. Any fail = BLOCKED.
6. DECISION: "READY FOR YOUR REVIEW" or "BLOCKED BY RISK: [why]".
   End with: "Nothing has been placed. You decide."
Never make up prices, sources or dates.
```

**BLOCKED will be the most common answer.** That's the point. Most markets are priced about right. A bot that says yes to everything is broken.

## How each agent works

1. **SCOUT** checks the 100 busiest markets on Polymarket (free public data). It flags 3 things: a big jump in betting, odds moving 5+ points, or an end date coming soon.
2. **NEWS** searches the web for fresh reporting. It only counts facts with a source and a date.
3. **THESIS** builds the best case for YES and for NO, and names what would kill the bet.
4. **ODDS** is simple math. If the market says 42% and the team says 57%, that's a 15-point gap.
5. **RISK** is the bouncer. It sizes the bet small (never more than 2% of your money) and blocks anything that fails a check: gap too small, news is a rumor, not enough money in the market, or too little time left.
6. **EXECUTION** writes one ticket and sends it to your phone. It never bets for you.

Every run is saved to a log. After a month, you can see if the team beat the market. If it didn't, you don't trust it. Simple.

**To build it yourself,** you'd write each agent in Python, connect Polymarket's free data feed, call Claude for the news and thesis steps, set up a Telegram bot for texts, and schedule it to run every hour. If you're good with Python, that's a few evenings. If not, a lot longer.

> Educational only. Not financial advice. You can lose what you bet. Check that Polymarket is allowed where you live.

## Build the starter bot with Claude Code (20 minutes)

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

## Make it yours: your rules (3 minutes)

Paste this under the agent prompt so every agent follows **your** limits:

```text
MY PREDICTION MARKET RULES
Bankroll: $____   Max per idea: 2% of bankroll
Only markets with clear resolution rules and enough trading volume.
Skip anything that resolves more than 60 days out.
I need a reason the price is wrong, with a dated, linked source.
Track every idea with pretend money for 30 days before using real money.
Final call: WATCH or SKIP. You never place a bet. I decide.
```

## 12 copy-paste prompts

**Finding markets**

1. "Scout: list 5 active Polymarket markets in [topic] that resolve within 60 days. Link each one."
2. "Read the resolution rules for this market: [link]. Anything tricky that could surprise me?"
3. "Which of these markets has the most trading volume? Thin markets are risky."

**Checking the price**

4. "Odds: the market says [x]%. What do dated, linked sources say the real chance is? Show your reasoning."
5. "News: what happened in the last 7 days that could move this market? Dates and links only."
6. "Thesis: give me the best case for YES and the best case for NO, side by side."
7. "Has the price already moved on this news? Compare the price a week ago to now."

**Risk and review**

8. "Risk: veto or allow? If allowed, max size at 2% of $___."
9. "Turn this into one log line: date, market, side, price, WATCH/SKIP, reason."
10. "Here are my last 10 logged ideas and how they resolved. Was I better than the market price?"
11. "Which agent was most often right in my log? Which one should I listen to less?"
12. "Run all 6 agents on this market and give me a 5-line summary I can read on my phone."

## Your 10-minute daily routine

| When | Do this |
|---|---|
| Morning (3 min) | Prompt 1 on one topic you know well. |
| Best market (5 min) | Run all 6 agents (prompt 12). |
| Evening (2 min) | Log it (prompt 9). Check any that resolved. |

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

- [ ] You ran the team on one real market
- [ ] You got the YES case, the NO case and the kill rule
- [ ] You know why Risk passed or cancelled it

## Troubleshooting

| Problem | Fix |
|---|---|
| It treats rumors as news | Paste only dated, linked sources. |
| Every market looks good | Ask Risk: "Give 3 reasons to skip this." |
| It can't see live prices | Paste the current price and volume yourself. |

## Want it done for you?

You just ran it once, by hand. That was the hard way.

**The finished POLYBOT does it for you every hour.** It scans the busiest markets. It runs all six agents. It sends the best tickets straight to your phone. It even grades itself, so you can see if it's working before you bet a dollar.

I already did the hard part. I built it. I tested it. I wrote down every setting and every step.

Your part is a 60-minute setup. Copy. Paste. Done. You don't need to know how to code.

**Here's everything you get for one payment of $199:**

- ✅ **The finished POLYBOT**, tested and ready to run
- ✅ **10 more finished trading bots:** JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **Bots in your inbox for 3 months:** a morning email with what my 5 tested bots see on your markets. Nothing to install
- ✅ **The Milli Indicator Pack** for TradingView. Paste it and see the dots on your chart in 2 minutes
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **Every new bot I release for the next 12 months, free**

That's $2,175 of systems. **You pay $199. Once.** There's no monthly fee and nothing to cancel.

On December 1 the price goes to $349. Same bots. Same files. You'd just be paying $150 more for waiting.

**My promise.** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files anyway.

**[Yes, give me the finished POLYBOT for $199 →]({{offerUrl}})**
