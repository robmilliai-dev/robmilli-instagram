---
title: The 7-Bot Trading Desk
promise: Seven AI bots, one vote, and a risk bot that can veto anything. Run any stock idea past all seven in 15 minutes, free, and see how the automatic desk is built.
minutes: 15
nextSystemSlug: six-bot-trading-team
---

# The 7-Bot Trading Desk

**Real trading desks never let one person decide.** A scout spots the move. Analysts check the news and the chart. Someone tests it. Risk sizes it. A chief makes the call.

In 15 minutes, you'll build that desk with 7 AI bots, free, and run your first stock idea through it.

**When you're done, you'll have:**

- ✅ A 7-bot AI desk in one Claude chat
- ✅ A vote on your stock idea, with the #1 reason against it
- ✅ One clear call: **APPROVED**, **WATCHLIST** or **REJECTED**

**How it works:** Your idea → 7 bots each check one thing → Risk can veto → 5 of 7 must agree → one clear ticket

> **READ FIRST:** It never places an order. A "no" from the desk is a win: it saved you money.

**Why this works:** When one brain likes an idea, it ignores the warning signs. Seven bots that each look for a different problem catch what you'd miss. And the risk bot can veto anything, so no amount of excitement can push a bad trade through.

## Step 1: Pick one stock idea (3 minutes)

Pick one stock you saw moving today. Write down the ticker and why it caught your eye. If you can, grab a chart screenshot from [TradingView](https://www.tradingview.com/chart/) and one dated news headline.

## Step 2: Build your desk (3 minutes)

In [Claude](https://claude.ai/), make a **Project** called **7-Bot Desk** (or use a new chat). Paste this in:

```text
You are a 7-bot stock research team. You never place trades. I decide.
Each bot writes 3 short lines and ends with VOTE: YES or NO.

1. SCOUT: Did anything unusual happen? (Big volume, new high, a gap.)
2. NEWS: Only count facts with a source and date that I gave you.
3. MOOD: Is everyone already excited? If so, that's a warning.
4. CHART: Entry, stop (where it's wrong), target. Reward must be at
   least 1.5x the risk, or vote NO.
5. TESTER: What test would prove this idea works? What's the best
   case AGAINST it?
6. RISK: How many shares so hitting the stop loses only 1% of my
   account? Show the math. No stop or too big = VETO.
7. CHIEF: Count the votes. 5+ YES and no veto = APPROVED.
   3-4 YES = WATCHLIST. Otherwise REJECTED.
   Give me the call, the vote count, and the #1 reason against.

Never make up prices or news. If something is missing, say
"missing" and vote NO. Plain English.
```

## Step 3: Send your idea (4 minutes)

Send this as your next message:

```text
Stock: [TICKER]
Today's date: [DATE]
Why it caught my eye: [ONE SENTENCE]
Chart: [attach a screenshot, or "none"]
News I found: [headline, source, date, or "none"]
My practice account: $[10,000]

Run the team.
```

## Step 4: Read the vote (5 minutes)

1. **Look at the vote count.** Then find the first NO. That bot found the weak spot.
2. **Check every number** against what you gave it. If you didn't give it a number, it shouldn't be there.
3. **Read the Tester's case against.** Can't answer it? Treat it as WATCHLIST.
4. **Save it.** Ticker, date, call, votes. After 20 ideas, you'll see which bot saves you the most.

**You did it if:** you have one saved call with a vote count and a reason against.

## How the automatic desk works

The finished version runs the same desk on its own, every hour the market is open:

- **Scout** checks your whole watchlist for unusual moves.
- **News, Mood and Chart** get real data (real headlines, real prices), not a screenshot.
- **Risk** is plain code, not AI. It can't be talked out of the 1% rule.
- **Chief** counts the votes and texts the ticket to your phone.

**To build it yourself,** you'd write each bot in Python, connect real price and news data, write the risk rules, set up phone texts and schedule it. A few evenings if you code.

> Educational only. Not financial advice. One AI playing seven bots is still one AI, so check its facts.

## Make it yours: your desk rules (3 minutes)

Add this to your desk Project. All 7 bots follow it:

```text
DESK RULES (these beat any vote)
Account size: $____   Max risk per idea: 1%
Max open ideas: 3. Max in one stock: 10%.
5 of 7 bots must agree. The Risk bot can veto anything.
Every ticket needs: entry, a stop where the idea is wrong, and a target at least 2x the risk.
The desk never trades. I decide.
```

## 12 more copy-paste prompts

1. "Here's my watchlist. Which idea should go to the desk today, and why?"
2. "Trend bot only: is the trend up, down or sideways? What shows it?"
3. "News bot only: anything in the last 7 days that changes the story? Dates and links."
4. "Value bot only: is it cheap or expensive vs its own history and its rivals?"
5. "Risk bot: veto or allow? If allowed, size at 1% of $___."
6. "The vote was 4-3. What's the one fact that would flip a vote?"
7. "Write the ticket: entry, stop, target, size, and the date to check back."
8. "Give me the strongest case AGAINST this ticket."
9. "30 days later, here's the price: [paste]. Was the desk right? Which bot was most right?"
10. "Look at my last 10 tickets. Which bot is most often right? Which one should I trust less?"
11. "Send these 3 ideas to the desk. Which gets 5 of 7?"
12. "Run all 7 bots in one answer and give me a 5-line phone summary."

## Your daily routine

| When | Do this |
|---|---|
| Morning (3 min) | Pick one idea (prompt 1). |
| Vote (10 min) | Run all 7 bots (prompt 12). |
| Evening (2 min) | Save the ticket or the reason it failed. |

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

- [ ] You sent one stock idea to the desk
- [ ] You got all 7 votes back
- [ ] You read the Risk bot's answer first

## Troubleshooting

| Problem | Fix |
|---|---|
| It answers as one voice, not 7 | Reply: "Answer as all 7 bots, one line each, then the vote." |
| Every idea passes | Ask the Risk bot to be stricter: "No stop = no trade." |
| It makes up news | Paste the news yourself with a date and link. |

## Want it done for you?

You just did it once, by hand. **The finished bot team does it for you, every hour, on every stock you follow, and texts you only the ideas that win the vote.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished 7-Bot Trading Team**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished Bot Team for $199 →]({{offerUrl}})**
