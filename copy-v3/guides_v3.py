#!/usr/bin/env python3
"""Rewrite the non-technical parts of the free guides in the Halbert I-voice.
Steps, prompts, code, tables, READ FIRST boxes and How-it-works lines are untouched."""
import re, sys, pathlib

D = pathlib.Path(sys.argv[1])

BOTS_ALL = "**11 finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more"
ALL = ["POLYBOT", "JARVIS", "ARENA", "ARB", "the AI Board", "the 24/7 Market Watch", "the Claude Chart Analyst"]
SKIP = {"the 24/7 AI Trader": "the 24/7 Market Watch", "the Chart Analyst": "the Claude Chart Analyst"}
def bots_other(name):
    drop = SKIP.get(name, name)
    return "**10 more finished trading bots:** " + ", ".join(b for b in ALL if b != drop) + " and more"

def tail(first_item, bots_line, button, what="bot"):
    return f"""**Here's everything you get for one payment of $199:**

- ✅ {first_item}
- ✅ {bots_line}
- ✅ **Bots in your inbox for 3 months:** a morning email with what my 5 tested bots see on your markets. Nothing to install
- ✅ **The Milli Indicator Pack** for TradingView. Paste it and see the dots on your chart in 2 minutes
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **Every new bot I release for the next 12 months, free**

That's $2,175 of systems. **You pay $199. Once.** There's no monthly fee and nothing to cancel.

On December 1 the price goes to $349. Same bots. Same files. You'd just be paying $150 more for waiting.

**My promise.** Follow the steps. If your {what} isn't running in 7 days, email robmilli.ai@gmail.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files anyway.

**[{button}]({{{{offerUrl}}}})**
"""

def offer(hook_lines, item, bots, button, what="bot", lead="You just did it once, by hand. That was the hard way."):
    body = "\n\n".join(hook_lines)
    return f"""## Want it done for you?

{lead}

{body}

I already did the hard part. I built it. I tested it. I wrote down every setting and every step.

Your part is a 60-minute setup. Copy. Paste. Done. You don't need to know how to code.

""" + tail(item, bots, button, what)

def dots_offer():
    return """## Want it done for you?

Dots tell you *when*. They don't tell you *whether to care*.

That's what the **TradingView + Claude Chart Analyst** inside the AI Desk is for. Every time a dot fires, it reads the alert, checks the chart and the news, and texts you VALID or SKIP with the reason. You only open the chart when it's worth your time.

I built it. I tested it. I wrote every step. Your part is a 60-minute setup. Copy. Paste. Done.

""" + tail("**The finished TradingView + Claude Chart Analyst**, tested and ready to run",
           bots_other("the Chart Analyst"),
           "Yes, give me the finished Chart Analyst for $199 →")

G = {}

G["24-7"] = dict(
 promise="What if a trader watched the market for you all day and only texted when something was worth a look? Here's how that AI trader works, and a free prompt that runs it on any chart today.",
 intro="""**What if you had a trader watching the market for you all day? And he only texted you when something good showed up?**

No more checking your phone at lunch. No more finding the big move after it's already gone.

I built that trader. This guide shows you exactly how he thinks. You'll run him on a real chart today, free.

And if you'd rather skip the building, the finished one is waiting at the bottom of the page.""",
 why="""**Why this works:** It uses two plain setups traders have trusted for decades. The **breakout**: price pushes above its recent high. The **pullback**: price dips in an uptrend, then bounces. Then a strict risk check throws out anything where the reward is too small. That's it. Simple rules beat gut feelings. Every time.""",
 offer=offer(["**The finished 24/7 AI Trader does it for you.** Every hour the market is open. On every stock you follow. And it texts the answer straight to your phone."],
   "**The finished 24/7 AI Trader**, tested and ready to run", bots_other("the 24/7 AI Trader").replace("the 24/7 Market Watch, ",""),
   "Yes, give me the finished 24/7 AI Trader for $199 →"))

G["arb"] = dict(
 promise="A Polymarket bot reportedly turned $1 into $3.3 million by comparing prices, not predicting games. I took the idea apart and rebuilt it. Here's how it works, and a free prompt to check any game in 10 minutes.",
 intro="""**A Polymarket bot reportedly turned $1 into $3.3 million.**

*(That's a viral claim from a video on X. It isn't my result, and nobody has checked it.)*

Here's the part that got my attention. **It doesn't predict games. It compares prices.**

So I rebuilt the idea from scratch and tested it. This guide shows you exactly how it works. You'll check a real game yourself, free, in 10 minutes.

The finished bot is waiting at the bottom of the page.""",
 why="""**Why this works:** The big sportsbooks set their odds with mountains of money and data. Polymarket prices come from whoever happens to be trading that minute. So when the two disagree about the same game, guess which one is usually wrong? Polymarket. That gap is the whole opportunity.""",
 offer=offer(["**The finished ARB bot does it for you on every game day.** It watches the books and Polymarket. It does the math. It reads the fine print. And it texts you only the gaps that pass."],
   "**The finished ARB bot**, tested and ready to run", bots_other("ARB").replace("ARB, ",""),
   "Yes, give me the finished ARB bot for $199 →"))

G["arena"] = dict(
 promise="An AI beat ChatGPT, Claude, Gemini and Grok in a real-money trading contest: +22% in 17 days. It didn't win by being smarter. I rebuilt its playbook as a 4-agent team, and you can run it free in 10 minutes.",
 intro="""**An AI beat ChatGPT, Claude, Gemini and Grok in a real-money trading contest. +22% in 17 days.**

In Nof1's Alpha Arena (Season 1, fall 2025), six top AIs each got $10,000 of real money to trade crypto on their own. Qwen 3 Max finished first, up 22.3%. *(Those are Nof1's reported results from one short contest, not mine. One contest doesn't predict the future.)*

Now here's the interesting part. The winner didn't win by being smarter. **It won by being more disciplined.**

So I rebuilt its playbook as a team of 4 AIs. This guide shows you how it works. You'll run it free in 10 minutes. The finished bot is at the bottom of the page.""",
 why="""**Why this works:** Look at what the winner did that the others didn't:""",
 offer=offer(["**The finished ARENA desk does it for you every hour.** Bitcoin, Ethereum and Solana, with the winner's discipline built right in. Only the trades that pass every rule ever reach your phone."],
   "**The finished ARENA desk**, tested and ready to run", bots_other("ARENA").replace("ARENA, ",""),
   "Yes, give me the finished ARENA desk for $199 →"))

G["backtest"] = dict(
 promise="Saw a trading strategy in a reel? Find out if it's real before you risk a dollar. The prompt, the 5 checks that catch a fake backtest, and a starter build.",
 intro="""**"This strategy made 400%."** You've seen a hundred reels like that. So have I.

A few are real. Most were tuned and tuned until the chart looked pretty.

**This guide shows you how to tell which is which, in about 10 minutes.** Before it costs you a dime.""",
 why="""**Why this works:** A strategy is just a rule. A rule can be run on old prices. And if it only works on the years it was tuned on? It's a story. Not an edge.""",
 offer=offer(["**The finished Backtest Any Idea kit tests any idea you type, on any market, and hands you a plain grade in about a minute.**"],
   "**The finished Backtest Any Idea kit**, tested and ready to run", BOTS_ALL,
   "Yes, give me the finished tester for $199 →", what="tester"))

G["board"] = dict(
 promise="Five top AIs, five jobs, one vote. Perplexity, Grok, Gemini, ChatGPT and Claude each check a trade, and Claude can veto all of them. Here's how it works, and 5 free prompts you can use today.",
 intro="""**What if the 5 smartest AIs in the world all had to agree before you made a trade?**

Perplexity finds the news. Grok reads the crowd on X. Gemini reads the chart. ChatGPT builds the case. And Claude hunts for risk, and can say no to all of them.

I call it the AI Board. This guide shows you how it works and hands you 5 free prompts to run it today.

The finished bot is at the bottom of the page.""",
 why="""**Why this works:** Every AI has blind spots. So the board gives each one the job it's best at, and none of them can push a trade through alone. One AI can be fooled. Five checking each other? Much harder.""",
 offer=offer(["**The finished AI Board does it for you every day after the market closes.** All 5 AIs vote on your watchlist, and only the trades that pass land on your phone. It even runs on just one Claude key."],
   "**The finished AI Board**, tested and ready to run", bots_other("the AI Board").replace("the AI Board, ",""),
   "Yes, give me the finished AI Board for $199 →"))

G["bots"] = dict(
 promise="Seven AI bots, one vote, and a risk bot that can veto anything. Run any stock idea past all seven in 15 minutes, free, and see how the automatic desk is built.",
 intro="""**Real trading desks never let one person decide.** A scout spots the move. Analysts check the news and the chart. Someone tests it. Risk sizes it. A chief makes the call.

You probably don't have a desk like that. Most people don't.

So in the next 15 minutes, you'll build one out of 7 AI bots, free, and run your first stock idea through it.""",
 why="""**Why this works:** When you fall for an idea, you stop seeing the warning signs. Everybody does. Seven bots that each hunt for a different problem catch what you'd miss. And the risk bot can veto anything, so no amount of excitement can sneak a bad trade through.""",
 offer=offer(["**The finished bot team does it for you.** Every hour. On every stock you follow. And it texts you only the ideas that win the vote."],
   "**The finished 7-bot trading team**, tested and ready to run", bots_other("the 7-bot team"),
   "Yes, give me the finished bot team for $199 →"))

G["chart"] = dict(
 promise="Upload one chart. Get a clear, plain-English read in 15 minutes: the trend, the key prices, the setup and the biggest red flag.",
 intro="""**What if you could hand any chart to a sharp analyst and get a straight answer in 60 seconds?**

You can. It's free. And it takes 15 minutes to set up.

I'll show you exactly how.""",
 why="""**Why this works:** Claude can read pictures. Give it a clean chart and strict rules, and it reads that chart the same careful way every single time. No moods. No hope. No fear. And you'll check its work yourself in step 4, so you know it's real.""",
 offer=offer(["**The finished Claude Chart Analyst does it for you on every alert.** TradingView spots the setup. Claude reads it. The answer lands on your phone. You never open a chart unless it's worth your time."],
   "**The finished Claude Chart Analyst**, tested and ready to run", bots_other("the Chart Analyst"),
   "Yes, give me the finished Chart Analyst for $199 →"))

G["desk"] = dict(
 promise="Stop staring at charts. Set one alert in 15 minutes, get pinged when your stock hits your price, and have AI check the move before you do anything.",
 intro="""**Stop staring at charts all day.**

Pros don't do it. They pick a price, set an alert and walk away. The market taps them on the shoulder when it's time.

In the next 15 minutes, you'll set that up too. Free.""",
 why="""**Why this works:** Most bad trades start the same way. You see a move by accident and chase it. An alert flips that around. You pick your price while you're calm. Then AI checks the move with fresh eyes. You'll see it work on your own screen in step 3.""",
 offer=offer(["**The finished 24/7 Market Watch does it for you all day.** It scans your whole watchlist every hour. It finds the setups. It does the math. And it texts you one clear answer."],
   "**The finished 24/7 Market Watch**, tested and ready to run", bots_other("the 24/7 Market Watch").replace("the 24/7 Market Watch, ",""),
   "Yes, give me the finished Market Watch for $199 →"))

G["dip"] = dict(
 promise="The free TradingView indicator that won 57 of 70 S&P 500 dip-buys on years it never saw. Copy, paste, done in 2 minutes.",
 intro="""One free TradingView indicator. I built it, then I tried hard to break it.

When the S&P 500 has a panic day inside an uptrend, a blue dot shows up. When it bounces, you get the exit. That's the whole idea.""",
 why=None, offer=dots_offer())

G["dots"] = dict(
 promise="Two free TradingView indicators I built and then tried to break. Buy dots, exit dots and phone alerts. Copy, paste, done in 2 minutes.",
 intro="""Two free TradingView indicators. I built them, then I tried hard to break them.

Paste them in, and a blue dot shows up on your chart when the setup happens. No staring. No guessing.""",
 why=None, offer=dots_offer())

G["hedge"] = dict(
 promise="Big funds make 6 experts argue before they buy a stock. Run that same argument on any stock in 15 minutes, free, in one Claude chat.",
 intro="""**Big hedge funds never let one person buy a stock alone.**

They make a team argue about it first. One looks at the economy. One reads the company's numbers. One reads the chart. One hunts for risk. One argues the other side, on purpose. And a boss makes the call.

You can run that same team on any stock. Tonight. Free. Here's how.""",
 why="""**Why this works:** One brain falls in love with an idea. A team with a skeptic in the room doesn't. When an AI has to argue against itself, the weak ideas die early. That's the whole trick, and you'll watch it happen in step 3.""",
 offer=offer(["**The finished Hedge Fund Committee runs every idea past all six experts the same way, every time.** The Risk Manager veto, a sizing sheet and a trade journal are built right in."],
   "**The finished Hedge Fund Committee**, tested and ready to run", bots_other("the Committee"),
   "Yes, give me the finished Committee for $199 →"))

G["hq"] = dict(
 promise="Send a stock idea up a 6-floor AI building. Any floor can stop it. Only the best ideas reach the top. Free in 15 minutes, plus how the automatic version is built.",
 intro="""**Most traders see a move and buy it. Real trading firms send every idea up a building first.**

Each floor checks one thing. Any floor can stop it. Only the best ideas ever make it to the top.

In the next 15 minutes, you'll build that 6-floor HQ out of AI, free, and send your first idea up.""",
 why="""**Why this works:** A bad trade almost always has one obvious flaw. The one you didn't want to see. Six floors, each hunting for a different flaw, find it fast. So if an idea makes it all the way to the top, it has earned your attention.""",
 offer=offer(["**The finished HQ does it for you.** Every hour. On every stock you follow. And it texts you only the ideas that make it to the top floor."],
   "**The finished AI Trading HQ**, tested and ready to run", bots_other("the HQ"),
   "Yes, give me the finished HQ for $199 →"))

G["jarvis"] = dict(
 promise="Text your own AI market assistant like a friend. \"Brief me.\" \"How's NVDA?\" It looks up the real numbers and texts back. Here's how it works, and a free version you can use in 10 minutes.",
 intro="""**Picture this. It's 8 a.m. You text "brief me." And 30 seconds later, your phone tells you everything you need to know about your stocks.**

Your positions. What moved. What's coming up. What to watch.

That's JARVIS. You've seen the "I built JARVIS for the stock market" posts. So I rebuilt it from scratch and tested it.

This guide shows you how it works, and gives you a free version you can use in 10 minutes. The finished one is at the bottom of the page.""",
 why="""**Why this works:** Most traders have 12 tabs open and still miss the one thing that mattered. JARVIS looks it all up for you. It gives you the answer first. Then it shows you the proof and the risk. One question. One straight answer.""",
 offer=offer(["**The finished JARVIS lives on your phone.** Text it any question, any time, and get real numbers back. Plus a morning brief that shows up on its own every weekday."],
   "**The finished JARVIS**, tested and ready to run", bots_other("JARVIS").replace("JARVIS, ",""),
   "Yes, give me the finished JARVIS for $199 →"))

G["journal"] = dict(
 promise="Most traders don't need a new strategy. They need to stop 2 or 3 habits. A 60-second journal and a Claude prompt that finds yours.",
 intro="""**Most traders don't need a new strategy.**

They need to stop the two or three things that keep costing them money. Over and over.

The trouble is, you can't see those things from inside your own head. Nobody can. **A journal can.**""",
 why="""**Why this works:** Every trader remembers their trades wrong. We remember the smart wins. We forget the angry losses. Rows in a sheet don't forget anything.""",
 offer=offer(["**The finished AI Trade Journal Coach does the math in code, ranks every leak by what it cost you, and hands Claude a clean review to coach you on.**"],
   "**The finished AI Trade Journal Coach**, tested and ready to run", BOTS_ALL,
   "Yes, give me the finished Journal Coach for $199 →", what="coach"))

G["legends"] = dict(
 promise="Turn the big ideas of Buffett, Lynch, Dalio, Soros and Simons into 5 simple rules a computer can test. Plus a free prompt that turns your own idea into a rule in 10 minutes.",
 intro="""**Buffett. Lynch. Dalio. Soros. Simons.** Five of the most famous investors who ever lived.

Most people "learn" from them by reading quotes. But here's the problem. Quotes don't trade. **Rules do.**

So this guide turns each legend's big idea into one simple rule a computer can follow and test. And if you'd rather skip the building, the finished lab is at the bottom of the page.""",
 why="""**Why this works:** A rule doesn't get scared. It doesn't get greedy. It does the same thing every time. And once your idea is a rule, you can test it on years of real prices and see the truth before you risk a dollar.""",
 offer=offer(["**The finished Legends Lab tests all five legends for you with one click.** Honestly. It prints a scorecard right next to plain buy-and-hold, and it runs free in Google Colab with nothing to install."],
   "**The finished Legends Lab**, tested and ready to run", BOTS_ALL,
   "Yes, give me the finished Legends Lab for $199 →", what="lab"))

G["polybot"] = dict(
 promise="Somebody says their Polymarket bot turned $150 into $279,053. I can't prove that. So I took the idea apart, rebuilt it and tested it. Here's how its 6 AI agents work, and a free prompt that runs the whole team in 10 minutes.",
 intro="""**A Polymarket bot reportedly turned $150 into $279,053.**

*(That's the original creator's own claim. It isn't my result, and nobody has checked it.)*

When I saw that number, I had one question. Not "is it true?" I can't know that. Neither can you.

My question was: how would a bot like that even work?

So I rebuilt the system behind it from scratch. Then I tested it.

This guide shows you exactly what I found. You'll run the whole thing yourself, free, in about 10 minutes. No code.

And if you'd rather skip the building, the finished bot is waiting at the bottom of the page.""",
 why="""**Why this works:** Here's the part almost nobody tells you. The secret is not one genius AI. It's a **team**. Each agent has one job, and any one of them can kill a bad bet. Most bots lose for a simple reason: nobody on the inside ever says "no." This one is built to say no. A lot. So the few bets that make it through are the ones worth your time.""",
 offer=offer(["**The finished POLYBOT does it for you every hour.** It scans the busiest markets. It runs all six agents. It sends the best tickets straight to your phone. It even grades itself, so you can see if it's working before you bet a dollar."],
   "**The finished POLYBOT**, tested and ready to run", bots_other("POLYBOT").replace("POLYBOT, ",""),
   "Yes, give me the finished POLYBOT for $199 →", lead="You just ran it once, by hand. That was the hard way."))

G["practice"] = dict(
 promise="Before you pay a challenge fee, find out if your trading could pass. The risk table, the 8 questions to ask any firm, and the daily stop rule.",
 intro="""**Most people who buy a prop challenge blow it.**

Usually not because their idea was bad. They risked too much. Or they pushed on a bad day.

A challenge fee is real money. **So practice first. This guide shows you how, free.**""",
 why="""**Why this works:** A challenge is math. Target. Max loss. Daily loss. At a given risk size, your trades either fit inside those lines or they don't. And you can find out which before you pay a cent.""",
 offer=offer(["**The finished Prop Challenge Practice Kit runs any firm's rules against your trades, tells you your risk number, and checks your room every morning with one command.**"],
   "**The finished Prop Challenge Practice Kit**, tested and ready to run", BOTS_ALL,
   "Yes, give me the finished Practice Kit for $199 →", what="kit"))

G["prop"] = dict(
 promise="83 simulated prop challenges since 2020. 64 passed, 2 blown at 1% risk. Here are the exact rules, the free indicator and the daily checklist.",
 intro="""Most people blow prop challenges the same way. Too much risk, too fast.

This playbook does the opposite. Small risk. A tested trend indicator. And patience. It's boring on purpose, because boring is what passes.""",
 why=None, offer=dots_offer())

G["team"] = dict(
 promise="Hire your first AI employee in 15 minutes. It writes your customer replies. You check them and hit send.",
 intro="""**Imagine never writing another customer reply from scratch.**

You read the message. Your AI employee writes the answer. You check it and hit send. Thirty seconds, done.

In the next 15 minutes, you'll hire that employee. It costs you nothing.""",
 why="""**Why this works:** AI is great at writing and terrible at guessing. So you give it one job, clear rules and one big rule on top: you hit send, not the AI. That's how real companies use AI support safely. You'll see a finished reply in step 3.""",
 offer=None)

G["terminal"] = dict(
 promise="Get a free, Bloomberg-style data terminal on your computer in 10 minutes. Then have Claude write you a market brief using only real data. No subscription.",
 intro="""**A Bloomberg Terminal costs about $30,000 a year.** Most traders will never touch one.

Here's what they don't tell you. OpenBB is a free, open-source tool that pulls real market data for you.

In 10 minutes, you'll have it on your computer. In 15, Claude will write you a market brief using **only real numbers**.""",
 why="""**Why this works:** Ask AI about the market with no data, and it guesses. Hand it real data, and it can't guess. It has to use your numbers. That's the difference between a toy and a tool. You'll check it yourself in step 4.""",
 offer=offer(["**The finished Terminal setup gives you a ready-made script and a daily desk sheet, so your morning market brief builds itself the same way every day.**"],
   "**The finished Terminal setup**, tested and ready to run", BOTS_ALL,
   "Yes, give me the finished Terminal setup for $199 →", what="setup"))

G["tradingview"] = dict(
 promise="Turn Claude into your own TradingView analyst tonight. The Master Prompt, 25 copy-paste prompts, alert templates, risk rules and a free tested indicator. Level 1 takes 15 minutes.",
 intro="""**"I connected Claude to TradingView, and now it reads every chart for me."**

You've seen the posts. Here's the full kit, free. The Master Prompt, 25 copy-paste prompts, the alert setup, the risk rules, and a free indicator I actually tested.

And if you'd rather have it all running on its own, the finished version is at the bottom of the page.""",
 why=None,
 offer=offer(["**The finished setup does it for you.** The TradingView script, the web app and the phone texts are all built and tested. Every setup gets read by Claude and lands on your phone."],
   "**The finished TradingView + Claude Chart Analyst**, tested and ready to run", bots_other("the Chart Analyst"),
   "Yes, give me the finished Chart Analyst for $199 →"))

G["whale"] = dict(
 promise="Find the Polymarket wallets that actually win, throw out the lucky ones, and see what the smart money holds right now. 6 AI agents, public data, no code.",
 intro="""**Every Polymarket wallet is public.** The #1 wallet this month made over $7.7 million, and you can see every bet it holds.

But big profit isn't the same as skill. Not even close.

So this guide gives you 6 AI agents that find the wallets worth watching, throw out the lucky ones, and check if a bet still has value before you touch it.""",
 why="""**Why this works:** Copying blindly is how people lose. Most "top wallets" are one lucky bet, a brand-new account, or a high-speed bot you could never copy by hand. When I ran the Luck Filter on the top 25 wallets on Nov 3, 2026, **9 of 25 failed.**""",
 offer=offer(["**The finished POLYBOT inside the AI Desk runs the research for you every hour.** It scans the busiest markets, runs six agents, and texts the best tickets straight to your phone.",
              "Pair it with your Luck Filter shortlist, and you'll know what the smart money holds and whether it's still worth a look. It even grades itself, so you can see if it's working before you bet a dollar."],
   "**The finished POLYBOT**, tested and ready to run", bots_other("POLYBOT").replace("POLYBOT, ",""),
   "Yes, give me the finished POLYBOT for $199 →"))

TEAM_OFFER = """## Want a whole team of AI employees?

You just hired one. That was the hard way.

**The full AI Employee Pack gives you 8 of them:** support, sales, research, writing, admin and more. Each one comes with its job, its rules, and a "you approve it" step built in. Ready to copy and paste.

**And you don't pay a cent extra for it.** It comes free inside the AI Desk. Here's everything you get for one payment of $199:

- ✅ **The AI Employee Pack:** 8 ready-to-use AI workers
- ✅ **11 finished AI trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch and more
- ✅ **29 more AI business systems** for sales, content, apps and outreach
- ✅ **A step-by-step setup for everything**, start to finish
- ✅ **Every new system I release for the next 12 months, free**

That's $2,175 of systems. **You pay $199. Once.** There's no monthly fee and nothing to cancel.

On December 1 the price goes to $349. Same files. You'd just be paying $150 more for waiting.

**My promise.** Follow the steps. If it isn't working in 7 days, email robmilli.ai@gmail.com and I'll set it up with you. Still not working? You get every dollar back, and you keep the files anyway.

**[Yes, give me the AI team and all 11 bots for $199 →]({{offerUrl}})**
"""

def apply(slug, g):
    p = D / f"{slug}.md"
    s = p.read_text()
    # promise
    s, n = re.subn(r"^promise: .*$", "promise: " + g["promise"].replace("\\", "\\\\"), s, count=1, flags=re.M)
    assert n == 1, slug
    # intro: between H1 line and **When you're done
    m = re.search(r"(^# [^\n]*\n\n)(.*?)(\n\n\*\*When you're done)", s, flags=re.S | re.M)
    assert m, slug + " intro"
    s = s[:m.start(2)] + g["intro"] + s[m.end(2):]
    if g.get("why"):
        s, n = re.subn(r"^\*\*Why this works:\*\*.*$", lambda _: g["why"], s, count=1, flags=re.M)
        assert n == 1, slug + " why"
    off = TEAM_OFFER if slug == "team" else g["offer"]
    hdr = "## Want a whole team of AI employees?" if slug == "team" else "## Want it done for you?"
    i = s.index(hdr)
    s = s[:i] + off
    p.write_text(s)

import hashlib
def body(t):
    a = t.find("\n## "); b = t.find("\n## Want")
    return t[a:b]
done, missing = [], []
for slug, g in G.items():
    p = D / f"{slug}.md"
    if not p.exists():
        missing.append(slug); continue
    before = p.read_text()
    if "That's $2,175 of systems." in before:
        done.append(slug + "(already)"); continue
    apply(slug, g)
    assert body(before) == body(p.read_text()), slug + ": technical body changed, aborting"
    done.append(slug)
print("free guides rewritten:", len(done), done)
print("free guides not found (skipped):", missing)
