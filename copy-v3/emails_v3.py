#!/usr/bin/env python3
"""Rewrite email bodies in the Halbert I-voice, in place.
Usage: python3 emails_v3.py <content/email dir>
Keeps each file's delayHours and its trailing compliance footer lines
("Educational only..." / "Unsubscribe: ..."). Keeps the subject unless a new one is given.
Refuses to write a file if any {{placeholder}} from the live body would be lost or a new one added.
Safe to run twice."""
import re, sys, pathlib

D = pathlib.Path(sys.argv[1])
MARK = "<!-- copy-v3 -->"  # not used in output; idempotence is by body comparison
PROMISE = "Follow the steps. If it isn't running in 7 days, email support@milli-ai.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files."
SEVEN = """I built it. I tested it. I wrote every step. You never touch the code.

And you can start with just this one, for $7: {{starterUrl}}

Why so cheap? Because I'd rather you watch it run on your own laptop than take my word for anything.

Rob

P.S. If it doesn't do what I say, email support@milli-ai.com within 14 days and I'll send your $7 back."""

def try_it(action, did, tip):
    return f"""Hey {{{{firstName}}}},

Quick question. Did you {action} yet?

If you did, good. {did}

If you didn't, I get it. You saved it "for later." Everybody does. And later never comes.

So just do step 1. Right now. It takes two minutes: {{{{guideUrl}}}}

One tip. {tip}

Rob"""

def done_for_you(name, bots):
    return f"""Hey {{{{firstName}}}},

Let me make this dead simple.

You pay $199. Once. Here's what lands in your account:

- The finished {name}, tested and ready to run
- {bots}
- 30 AI business systems
- The Never-Blow-Up Kit, so one bad trade can't sink you
- Step-by-step setup for every bot
- Every new bot I release for the next 12 months, free

Bought one by one, that's $2,175 worth of systems.

Now here's my promise. {PROMISE}

Think about that for a second. The only way to lose is to never try it.

Get everything for $199: {{{{offerUrl}}}}

Rob"""

def price_date(name):
    return f"""Hey {{{{firstName}}}},

I'll keep this short.

On {{{{priceEndsDate}}}}, the AI Desk goes from $199 to $349.

Same bots. Same files. Same promise. You'd just be paying $150 more for waiting.

If you've been on the fence about the finished {name}, this is the moment: {{{{offerUrl}}}}

And if it's not for you? No hard feelings at all. You'll still get my weekly email with one useful idea in it.

Rob

P.S. My promise still stands. {PROMISE}"""

def guide_ready(story, first_step, ps, minutes="10"):
    return f"""Hey {{{{firstName}}}},

Here it is: {{{{guideTitle}}}}. The whole thing is below this email, and it's online here too: {{{{guideUrl}}}}

{story}

Do one thing right now. {first_step} That's step one. The rest takes about {minutes} minutes.

Talk soon,
Rob

P.S. {ps}"""

ALLB = ["JARVIS", "ARENA", "ARB", "POLYBOT"]
def ten_more(exclude):
    names = [b for b in ALLB if b != exclude][:3]
    return f"10 more finished trading bots, like {names[0]}, {names[1]} and {names[2]}"
ELEVEN = "11 finished trading bots, like POLYBOT, JARVIS and ARENA"

E = {}  # path -> (subject or None, body)

# ---------- lead sequences ----------
L = {
 "polybot": dict(name="POLYBOT", bots=ten_more("POLYBOT"),
  e0=guide_ready("Quick story. Somebody posted that their Polymarket bot turned $150 into $279,053. (Their claim, not mine. Nobody has checked it.)\n\nI didn't believe it. I didn't disbelieve it either. I just wanted to know how a bot like that would even work. So I rebuilt it. Six AI agents, each with one job, and any one of them can kill a bet.\n\nYou can run the whole team yourself in about 10 minutes. Free.",
     "Open any market on Polymarket and copy the question and the rules.",
     "Don't be surprised when it says BLOCKED. It will, most of the time. A bot that says yes to everything isn't smart. It's broken."),
  e1=try_it("run the six agents", "Here's your next move: try a market where the news is changing fast. That's where the team earns its keep.", "Turn on web search in Claude first. Without it, your News agent is working blind."),
  s2="Why most Polymarket bots blow up",
  e2="""Hey {{firstName}},

Want to know why most Polymarket bots blow up?

It's not the math. It's not the AI.

It's that nobody inside the bot is allowed to say no.

POLYBOT has six agents, and any one of them can kill a bet. That's the whole secret.

But here's the catch. Running six agents by hand, on every market, every day? You'll quit by Thursday. I would.

So I built the finished one. It scans the busiest markets every hour. It runs all six agents. It texts the best tickets to your phone. And it grades itself, so you can see if it's working before you bet a dollar.

""" + SEVEN),
 "arb": dict(name="ARB gap-finder", bots=ten_more("ARB"),
  e0=guide_ready("A Polymarket bot reportedly turned $1 into $3.3 million. (A viral claim, not mine. Nobody has checked it.)\n\nBut here's the part that hooked me. It doesn't predict games. It compares prices.\n\nSo I rebuilt the idea from scratch. Below is exactly how it works, and you can check a real game yourself, free.",
     "Pick one game that's coming up.",
     "BLOCKED will be the most common answer. Most of the time the prices agree. The bot waits for the times they don't."),
  e1=try_it("check your first game", "Now try 3 or 4 games on the same night. Gaps don't show up on every game.", "Always read the Polymarket rules. A bet that ignores overtime isn't the same bet as one that counts it. That's where most fake gaps come from."),
  e2="""Hey {{firstName}},

Here's the truth about price gaps nobody likes to hear.

They don't last.

When a real one shows up, you might have minutes. Check games by hand and you'll miss almost all of them.

That's why this has to be a bot.

So I built the finished ARB gap-finder. It watches the sportsbooks and Polymarket on game days. It does the math. It reads the fine print. And it texts you only the gaps that pass.

""" + SEVEN),
 "arena": dict(name="ARENA desk", bots=ten_more("ARENA"),
  e0=guide_ready("In a real-money trading contest, Qwen 3 Max beat ChatGPT, Claude, Gemini and Grok. +22% in 17 days. (Those are Nof1's reported results from one contest, not mine.)\n\nHere's what nobody talks about. It didn't win with brains. It won with discipline.\n\nBelow is its playbook, rebuilt as a team of 4 AIs.",
     "Open a 1-hour crypto chart and add MACD, RSI and EMA 50.",
     "NO SETUP will be the most common answer. That's the lesson of the whole contest. The winner waited."),
  e1=try_it("run the 4-agent team", "Check back in a few hours and run it again. Setups come and go on the 1-hour chart.", "Be honest about how many trades you already took today. The 3-a-day limit is one of the winner's best habits."),
  e2="""Hey {{firstName}},

The AIs that did worst in the contest all had the same problem.

They traded way too much.

The winner waited for strong setups and used a stop every single time. Sounds easy, right?

Try doing it at 2 a.m. when Bitcoin is ripping.

That's why I built the finished ARENA desk. It checks Bitcoin, Ethereum and Solana every hour with the winner's discipline built right in. Only the trades that pass every rule ever reach your phone.

""" + SEVEN),
 "board": dict(name="AI Board", bots=ten_more(""),
  e0=guide_ready("Below are 5 free prompts. Perplexity finds the news. Grok reads the crowd. Gemini reads the chart. ChatGPT builds the case. And Claude hunts for risk.\n\nA trade only passes if 4 of the 5 say yes and Claude doesn't veto. One AI can be fooled. Five checking each other? Much harder.",
     "Pick one stock and open Perplexity in a new tab.",
     "Only have Claude? Run all 5 prompts in Claude. It still works.", "15"),
  e1=try_it("run your first board vote", "Look at which AI said no first. Over time you'll see which seat saves you the most money.", "Copy each answer into the next AI exactly as it came out. Don't summarize it. The details matter."),
  e2="""Hey {{firstName}},

Five tabs. Five prompts. Copy, paste. Copy, paste.

It works. But be honest. You won't do it every day. Nobody does.

So I built the bot that does it for you.

The finished AI Board runs every day after the market closes. All 5 AIs vote on your watchlist, and only the trades that pass land on your phone. It even runs on just one Claude key.

""" + SEVEN),
 "bots": dict(name="Bot Trading Team", bots=ten_more(""),
  e0=guide_ready("Real trading desks never let one person decide. So in about 15 minutes, you'll build a 7-bot AI desk in one Claude chat and run a stock idea past all seven.\n\nOne of them can veto anything. That's the one that saves you money.",
     "Pick one stock you saw moving today.",
     "Look for the first NO in the vote. That bot found the weak spot.", "15"),
  e1=try_it("run your first idea past the desk", "Save the call. After 20 ideas, you'll see which bot saves you the most.", "Give it one real, dated headline. When the News bot has nothing to work with, it votes no."),
  e2="""Hey {{firstName}},

Running the desk by hand teaches you how it thinks. That's worth a lot.

But the market doesn't wait for you to open Claude. The big moves happen while you're busy doing something else.

So I built the version that runs on its own.

The finished Bot Trading Team checks every stock you follow, every hour. It runs the vote. And it texts you only the ideas that win.

""" + SEVEN),
 "chart": dict(name="Claude Chart Analyst", bots=ten_more(""),
  e0=guide_ready("You're about to set up an AI that reads any chart you hand it. The trend. The key prices. The setup. And the biggest red flag. In plain English, the same careful way every time.\n\nNo moods. No hope. No fear.",
     "Open TradingView and take a screenshot of one daily chart.",
     "Don't skip step 4. Checking two of Claude's claims with your own eyes is what turns a cool trick into a tool you trust.", "15"),
  e1=try_it("upload your first chart", "Next, try it on a stock you already own. It feels different when it's your money on the line.", "Add the EMA 20, EMA 50 and volume before you take the screenshot. Claude can only read what it can see."),
  e2="""Hey {{firstName}},

Reading one chart by hand is great.

But good setups don't wait for you to take a screenshot. They show up while you're at work. Or asleep.

So I hooked Claude straight up to TradingView.

The finished Claude Chart Analyst works like this. TradingView spots the setup. Claude reads it. The answer lands on your phone. You never open a chart unless it's worth your time.

""" + SEVEN),
 "desk": dict(name="24/7 Market Watch", bots=ten_more(""),
  e0=guide_ready("This one's simple, and it might be the most useful habit in trading.\n\nYou pick a price while you're calm. TradingView watches it for you. When it hits, AI checks the move before you do anything. No more staring at charts all day.",
     "Open TradingView and pick one stock you care about.",
     "No alert going off tonight? There's a practice example in step 3, so you can try the AI check right now.", "15"),
  e1=try_it("set your first alert", "When it goes off, paste it into the AI check in step 3 before you touch anything. That 2-minute pause is where the good decisions happen.", "Pick a price that actually means something, like a recent high. Random prices give you random alerts."),
  e2="""Hey {{firstName}},

One alert is great. But you don't follow one stock. You follow ten. Maybe twenty.

Nobody has time to set 20 alerts, watch every one, and run the AI check on each, every single day.

That's where most people quit.

So I built the finished 24/7 Market Watch. It scans your whole watchlist every hour the market is open. It finds the setups. It does the math. And it texts you one clear answer.

You only look when it's worth your time.

""" + SEVEN),
 "hedge": dict(name="Hedge Fund Committee", bots=ten_more(""),
  e0=guide_ready("You're about to put six AI experts in a room and make them argue about one stock.\n\nOne of them has a single job: tell you why you're wrong. Big funds pay people a lot of money to do that. You get it free.",
     "Pick one stock you've been thinking about buying.",
     "Read the Devil's Advocate part first. It's the most useful part of the whole thing.", "15"),
  e1=try_it("run your first committee", "If it said PASS or WATCH, good. That's not a fail. That's the team saving you from a weak idea.", "Give it one real, dated fact from the company's report. The more real facts it has, the sharper it gets."),
  e2="""Hey {{firstName}},

Big funds don't lose money because they're dumb.

They lose it when nobody is allowed to say no.

That's why every real fund has a risk manager with a veto. When you trade alone, nobody sits in that chair. Unless you put someone there.

So I did. The finished Hedge Fund Committee gives you all six experts, a Risk Manager who can veto, a sizing sheet and a trade journal. Every idea gets checked the same way. Every single time.

""" + SEVEN),
 "hq": dict(name="Trading HQ", bots=ten_more(""),
  e0=guide_ready("In about 15 minutes you'll build a 6-floor AI building in one Claude chat.\n\nEach floor checks one thing about a stock idea. Any floor can stop it. Only the best ideas ever reach the top.",
     "Pick one stock you saw moving today.",
     "Most ideas stop on floor 2 or 3. That's the HQ doing its job.", "15"),
  e1=try_it("send your first idea up the building", "Try one more idea today. You'll start to see which floors matter most.", "Give it a real, dated headline. Floor 2 stops anything without one."),
  e2="""Hey {{firstName}},

Sending one idea up the building by hand is great practice.

But to do it right, you'd have to do it for every stock, every day. That's a full-time job. And you already have one.

So the bot does it for you.

The finished Trading HQ sends every stock you follow up the building, every hour the market is open. And it texts you only the ideas that reach the top floor.

""" + SEVEN),
 "jarvis": dict(name="JARVIS", bots=ten_more("JARVIS"),
  e0=guide_ready("In 10 minutes you'll have your own JARVIS for the stock market.\n\nType \"brief me\" and it looks up the real numbers for you. Your stocks. What moved. What's coming up. No more 12 open tabs.",
     "Open a new Claude chat with web search turned on.",
     "Check one number against your own chart the first few times. Trust is earned."),
  e1=try_it("ask JARVIS your first question", "Now ask it \"Which of my positions is closest to its stop?\" It's the question most traders forget to ask.", "Put your real positions in the setup message, with your stop prices. That's when it gets really useful."),
  e2="""Hey {{firstName}},

JARVIS in a chat is cool.

JARVIS on your phone is a whole different animal. You text "brief me" from the coffee line, and your whole morning shows up in 30 seconds.

That's the version I built.

The finished JARVIS lives on your phone. Text it any question, any time, and get real numbers back. Plus a morning brief that shows up on its own every weekday.

""" + SEVEN),
 "legends": dict(name="Legends Strategy Lab", bots=ten_more(""),
  e0=guide_ready("Buffett. Lynch. Dalio. Soros. Simons.\n\nMost people learn from them by reading quotes. But quotes don't trade. Rules do. Below are 5 famous investing styles turned into simple rules a computer can test.",
     "Pick the legend whose style sounds most like you.",
     "Try the free prompt at the end with your own idea. Most trading ideas are a lot fuzzier than they feel until you write them down as a rule.", "15"),
  e1=try_it("turn your own idea into a rule", "Now look at the 3 ways Claude said it could fail. Those are worth more than the rule itself.", "Change one thing at a time. If you tweak a rule 20 times until it looks amazing, you've fooled yourself."),
  e2="""Hey {{firstName}},

Every one of these styles sounds smart.

But there's only one way to know which one works. Test it. Honestly. On years the rule has never seen.

That takes code. And that's exactly where most people stop.

So I built the finished Legends Strategy Lab. It tests all five legends for you, honestly, and prints a scorecard right next to plain buy-and-hold. It runs free in Google Colab, with nothing to install.

""" + SEVEN),
 "team": dict(name="AI Employee Pack", bots=ELEVEN,
  e0=guide_ready("Imagine never writing another customer reply from scratch.\n\nIn about 15 minutes you'll have an AI that drafts your replies. You check them and hit send. Thirty seconds, done.",
     "Grab one customer message you need to answer, or use the practice one in step 1.",
     "Keep the send button. The AI writes, you decide. That's how you use AI without getting burned.", "15"),
  e1=try_it("try your first reply", "Do 5 more this week. You'll be surprised how much time you get back.", "Paste in your real policy, word for word. When the AI has your rules, it stops guessing."),
  e2="""Hey {{firstName}},

Your new support rep does one job.

But you also write sales emails. Posts. Research. Reports. Follow-ups. That's a lot of jobs for one person.

Each of those can have its own AI worker, with its own rules.

So I built the AI Employee Pack. 8 ready-made AI workers: support, sales, research, writing, admin and more. Each one comes with its job, its rules, and a "you approve it" step built in.

""" + SEVEN),
 "terminal": dict(name="Bloomberg-style Terminal setup", bots=ten_more(""),
  e0=guide_ready("A Bloomberg Terminal costs about $30,000 a year.\n\nYou're about to get real market data on your computer for free, and have Claude write you a brief from it using only real numbers.",
     "Check that you have Python. Step 1 shows you how.",
     "Never typed a command before? Paste the guide into Claude and say \"walk me through this one step at a time.\" It works.", "15"),
  e1=try_it("pull your first price file", "Try a different stock next. Just change \"SPY\" in the file to any ticker you like.", "If you get an error, copy the whole thing into Claude and ask how to fix it. That fixes most problems fast."),
  e2="""Hey {{firstName}},

Pulling data once feels great.

But tomorrow morning you have to do it all over again. And the day after that. And the day after that.

Most people give up by day 3.

So I built the finished Bloomberg-style Terminal setup. A ready-made script and a daily desk sheet, so your morning market brief builds itself the same way every day.

""" + SEVEN),
 "tradingview": dict(name="Claude Chart Analyst", bots=ten_more(""),
  e0=guide_ready("Level 1 takes 5 minutes and it's free. Claude reads any chart you upload.\n\nLevels 2 and 3 show you how it can watch the charts for you and text your phone.",
     "Make a Claude Project called Chart Analyst and paste in the prompt.",
     "Add the EMA 20, EMA 50 and volume to your chart before the screenshot. Claude can only read what it sees."),
  e1=try_it("upload your first chart to the Project", "Now try the same stock on a different timeframe. You'll learn a lot from where the two reads disagree.", "Use the TradingView screenshot shortcut (Alt+S, or Option+S on a Mac). It's much cleaner than a phone photo."),
  e2="""Hey {{firstName}},

Level 1 is great. But you still have to take the screenshot.

Levels 2 and 3 are where it gets fun. TradingView watches the charts. Claude reads every alert. Your phone buzzes.

Building that yourself means Pine Script, a web app and hosting. Most people stop right there.

So I built it. The finished Claude Chart Analyst gives you the TradingView script, the web app and the phone texts, all built and tested. Every setup gets read by Claude and lands on your phone.

""" + SEVEN),
 "24-7": dict(name="24/7 AI Trader", bots=ten_more(""),
  e0=guide_ready("What if a trader watched the market for you all day, and only texted you when something good showed up?\n\nThat's what this shows you how to build. You'll run it on a real chart today, free.",
     "Pick one stock and open its daily chart.",
     "REJECT will be the most common answer. That's good. It means the AI is protecting your money.", "15"),
  e1=try_it("run the prompt on a chart", "Try 3 more stocks. You'll start to see which setups it likes and which ones it throws out.", "Use stocks you know well. It's easier to tell if the AI's thinking makes sense."),
  e2="""Hey {{firstName}},

Running the prompt by hand works.

But the market moves while you're at work. The breakout happens at 10:30. You see it at 4.

That's the whole reason this bot exists.

So I built the finished 24/7 AI Trader. It checks every stock on your watchlist every hour the market is open, and texts you only the setups that pass the risk check.

""" + SEVEN),
 "backtest": dict(name="Backtest Any Idea kit", bots=ELEVEN,
  e0=guide_ready("\"This strategy made 400%.\" You've seen a hundred reels like that. So have I.\n\nA few are real. Most were tuned until the chart looked pretty. This guide shows you how to tell which is which, before it costs you a dime.",
     "Pick one trading idea you've been wanting to try.",
     "If Claude can't turn your idea into an exact rule, that's your first answer. A strategy that can't be written as a rule can't be tested, and can't be trusted."),
  e1=try_it("test your idea", "Now look hard at two things: the costs, and the years the idea never saw. Those two checks change more results than anything else.", "Change one thing at a time. If you tweak a rule until it looks amazing, you've fooled yourself."),
  e2="""Hey {{firstName}},

The free prompt is great for one idea at a time.

But you'll see a new "can't lose" strategy every week. Testing each one by hand gets old fast.

So I built the finished Backtest Any Idea kit. You type a rule in plain English. It turns it into a repeatable test, adds the costs, shows you the worst drop, and counts every try, so you can't fool yourself. It never places a trade.

""" + SEVEN.replace("watch it run on your own laptop", "see it work on your own ideas")),
 "journal": dict(name="AI Trade Journal Coach", bots=ELEVEN,
  e0=guide_ready("Most traders don't need a new strategy. They need to stop the two or three habits that keep costing them money.\n\nThe trouble is, you can't see those habits from inside your own head. A journal can.",
     "Open a blank sheet and add the columns from step 1.",
     "Write the mood before you click buy, not after. One word. That single column catches more leaks than any other."),
  e1=try_it("log your first trade", "Keep going until you have 20 rows. That's when the leaks start to show.", "A loss where you followed your plan is a yes. A win where you doubled your size is a no. It's about the plan, not the result."),
  e2="""Hey {{firstName}},

The free journal works. But the math gets tedious, and the math is where the truth is.

So I built the finished AI Trade Journal Coach. Once a week you run one command. It ranks your three biggest leaks by what they actually cost you, gives you one rule for next week, and hands Claude your real numbers to coach you on.

""" + SEVEN.replace("watch it run on your own laptop", "see your own numbers")),
 "practice": dict(name="Prop Challenge Practice Kit", bots=ELEVEN,
  e0=guide_ready("Most people who buy a prop challenge blow it. Usually not because their idea was bad. They risked too much, or pushed on a bad day.\n\nA challenge fee is real money. So practice first. This shows you how, free.",
     "Write down the rules of the challenge you're thinking about: target, max loss and daily loss.",
     "Not affiliated with any prop firm. This is practice and education, so you find out before you pay, not after."),
  e1=try_it("check your risk size against the table", "Now ask any firm you're looking at the 8 questions in the guide before you pay a cent.", "Use the daily stop rule even on practice days. It's the habit that passes challenges."),
  e2="""Hey {{firstName}},

The guide shows you how to practice before you pay a challenge fee.

The finished Prop Challenge Practice Kit does the hard part for you. It runs any firm's rules against your trades at five risk sizes. And every morning, a daily guard rail tells you TRADE, HALF SIZE or STOP FOR TODAY. It's educational and not affiliated with any prop firm.

""" + SEVEN.replace("watch it run on your own laptop", "see it work on your own trades")),
}

for slug, g in L.items():
    seq = f"lead-{slug}"
    E[f"{seq}/00-your-guide.md"] = (None, g["e0"])
    E[f"{seq}/01-did-you-try-it.md"] = (None, g["e1"])
    E[f"{seq}/02-the-finished-bot.md"] = (g.get("s2"), g["e2"])
    E[f"{seq}/03-done-for-you.md"] = (None, done_for_you(g["name"], g["bots"]))
    E[f"{seq}/04-price-date.md"] = (None, price_date(g["name"]))

for slug, story, step in [
  ("dip", "It's one free TradingView indicator I built, then tried hard to break. When the S&P 500 has a panic day inside an uptrend, a blue dot shows up. When it bounces, you get the exit.", "Open a daily S&P 500 chart in TradingView."),
  ("dots", "They're two free TradingView indicators I built, then tried hard to break. Paste them in, and a blue dot shows up on your chart when the setup happens. No staring. No guessing.", "Open any daily chart in TradingView."),
  ("prop", "Most people blow prop challenges the same way. Too much risk, too fast. This playbook does the opposite: small risk, a tested trend indicator, and patience. It's boring on purpose, because boring is what passes.", "Open TradingView and pick the first of your 8 daily charts."),
  ("whale", "Every Polymarket wallet is public. But big profit isn't the same as skill. These 6 AI agents find the wallets worth watching, throw out the lucky ones, and check if a bet still has value before you touch it.", "Open the Polymarket leaderboard in a new tab."),
]:
    E[f"lead-{slug}/00-your-guide.md"] = ("Your free guide is here", f"""Hey {{{{firstName}}}},

Here it is: {{{{guideTitle}}}}. The whole thing is below this email, and it's online here too: {{{{guideUrl}}}}

{story}

Do one thing right now. {step} That's step one. Then follow the guide, one step at a time.

Stuck? Just hit reply and tell me which step.

Rob""")

# ---------- lead-site ----------
E["lead-site/00-all-free-guides.md"] = (None, """I test viral AI trading bots so you don't have to.

Hey {{firstName}},

You asked for all {{guideCount}} free guides. Here they are:

{{guideList}}

Now, a word of advice. Don't try to read them all. That's how people end up doing none of them.

Pick one. Do it tonight.

Not sure which? Start with **The Claude Chart Read**. It takes 15 minutes, and you'll watch AI read a chart for you in plain English.

Rob""")
E["lead-site/01-did-you-open-one.md"] = (None, """Hey {{firstName}},

Be honest with me. Did you open one of the guides? Or did you "save it for later"?

No judgment. That's what almost everybody does.

But here's the thing. Fifteen minutes tonight is all it takes to watch one of these work on your own screen. Pick the one that sounds most fun: {{siteUrl}}/free

Rob""")
E["lead-site/02-done-for-you.md"] = (None, """Hey {{firstName}},

The free guides show you how each bot works. That's the hard way.

Here's the easy way. I built all 11 bots. I tested them. I wrote every step. Most of them run on a schedule and text your phone when something is worth a look.

You pay $199. Once. You get all 11 trading bots, 30 AI business systems, the Never-Blow-Up Kit, and every new bot I release for the next 12 months. That's $2,175 worth of systems.

My promise: """ + PROMISE + """

See everything: {{offerUrl}}

Rob""")
E["lead-site/03-price-date.md"] = (None, """Hey {{firstName}},

I'll keep this short.

On {{priceEndsDate}}, the AI Desk goes from $199 to $349.

Same bots. Same files. Same promise. Just $150 more for waiting.

Lock in $199 now: {{offerUrl}}

Rob

P.S. My promise: """ + PROMISE)

# ---------- abandoned ----------
E["abandoned/00-left-checkout-open.md"] = (None, """Hey {{firstName}},

You got all the way to checkout. Then life pulled you away. Happens to everybody.

Here's what's still sitting there with your name on it:

- 11 finished AI trading bots, like POLYBOT, JARVIS and ARENA
- 30 AI business systems
- The Never-Blow-Up Kit, so one bad trade can't sink you
- Step-by-step setup for every bot
- Every new bot I release for the next 12 months, free

That's $2,175 worth of systems. For $199. Once.

Pick up right where you left off: {{checkoutUrl}}

Rob

P.S. The price goes to $349 on {{priceEndsDate}}. Already bought? Ignore this and go set up your first bot.""")
E["abandoned/01-whats-stopping-you.md"] = (None, """Hey {{firstName}},

Can I guess what stopped you?

"What if it doesn't work for me?"

Fair. Here's my answer. """ + PROMISE + """

Read that again. You can buy it, use it, keep it, and still get your money back.

I've taken every bit of the risk. The only risk left is paying $349 after {{priceEndsDate}} instead of $199 today.

Try it with zero risk: {{checkoutUrl}}

Rob""")
E["abandoned/02-start-with-seven.md"] = (None, """Hey {{firstName}},

Maybe $199 felt like a lot for something you haven't tried yet. I get it. I'd feel the same way.

So start small. Get one finished bot for $7 and run it tonight. See it work with your own eyes first.

Get a finished bot for $7: {{starterUrl}}

Or grab everything at the $199 founding price, good until {{priceEndsDate}}: {{checkoutUrl}}

Rob""")
E["abandoned/03-two-easier-ways-in.md"] = (None, """Hey {{firstName}},

If $199 is the part holding you back, here are two smaller ways in.

**Option 1: Split the AI Desk into 3 monthly payments of $75.** You get the full Desk after the first payment. The next two come monthly.

{{siteUrl}}/checkout/desk-plan

**Option 2: Get the Trading Bot Vault for $99.** It's the current trading systems only. No business systems, bonuses or future releases.

{{siteUrl}}/checkout/trading-bot-vault

Pick the one that fits. Or leave it for now. No hard feelings.

Rob""")
E["abandoned/04-final-payment-plan-reminder.md"] = (None, """Hey {{firstName}},

Last reminder, I promise.

If paying $199 all at once is the problem, split the AI Desk into 3 monthly payments of $75. You get access after the first one.

{{siteUrl}}/checkout/desk-plan

Only want the trading systems? The $99 Trading Bot Vault is the other way in:

{{siteUrl}}/checkout/trading-bot-vault

The Standard founding price is $199 through November 30. It goes to $349 on December 1, 2026. No pressure. Pick what fits your budget.

Rob""")

# ---------- checkout-reminder ----------
E["checkout-reminder/00-waiting.md"] = (None, """Hey, you made it to checkout for {{product}} but didn't finish.

No problem. Your spot is saved right here: {{checkoutUrl}}

If something went wrong, or you've got a question, just hit reply.

- Rob""")
E["checkout-reminder/01-legit.md"] = (None, """Fair question. Here's how it works.

You get the files and the step-by-step setup the minute you pay. And every order is covered by my promise: if you can't get it running, email me and I'll help you set it up or give your money back.

Finish here: {{checkoutUrl}}

- Rob""")
E["checkout-reminder/02-last-note.md"] = (None, """I won't keep emailing you about this.

If you still want it, here's your link: {{checkoutUrl}}

Any questions, just hit reply.

- Rob""")

# ---------- custom-build ----------
E["custom-build/00-welcome.md"] = ("Your custom bot is booked. Now tell me what to build.", """Hey {{firstName}},

Payment received. You're in, and your AI Desk Pro access is included.

Now the fun part. Tell me what you want built, in plain English:

{{intakeUrl}}

Your 7-day clock starts the moment your form comes in. I build it, I test it, then I email you the files, the installer and the setup guide.

One rule: never send me API keys or passwords. You'll add those yourself, on your own machine.

Rob""")
E["custom-build/01-reminder-24-hours.md"] = (None, """Hey {{firstName}},

Your custom bot is paid for. But I can't start building until I know what you want.

Your 7-day clock starts when you send the form. Five minutes, plain English:

{{intakeUrl}}

Never paste API keys or passwords into the form.

Rob""")
E["custom-build/02-reminder-72-hours.md"] = (None, """Hey {{firstName}},

I'm ready to build your bot. I just need your details.

The 7-day clock starts the moment your form arrives:

{{intakeUrl}}

Never paste API keys or passwords into the form. Stuck on what to ask for? Just reply and tell me your idea in one line.

Rob""")

# ---------- personal hello ----------
E["personal-hello.md"] = (None, """Hey {{firstName}},

Rob here. Your guide should be in your inbox already.

Quick question. What are you trying to do with AI and trading right now?

Just hit reply and tell me in one line. I'll point you to the exact part of the guide, or the bot, that fits.

Rob""")

# ---------- purchase ----------
E["purchase/00-access-confirmed.md"] = (None, """{{indicatorPackStep}}

Hey {{firstName}},

You're in. Great call.

{{purchaseAccessMessage}}

Here's everything you own now:

{{purchaseItems}}

Now the most important part. Don't let this sit in a folder. That's where good bots go to die.

Tonight, pick **one** bot. The one you came here for. Open its "Start Here" file and follow the 60-minute setup, one step at a time. Copy. Paste. Done.

Open my bots: {{membersUrl}}

Rob

My promise: """ + PROMISE)
E["purchase/01-is-it-running.md"] = (None, """Hey {{firstName}},

One question. Is your first bot running?

If yes: awesome. Let it do its thing for a few days, then read what it sends you.

If not: tonight's the night. Open the setup and do just the first step. One step is all it takes to get moving again: {{membersUrl}}

Stuck on a step? Just reply and tell me which bot and which step.

Rob""")
E["purchase/02-add-your-second-bot.md"] = (None, """Hey {{firstName}},

One bot is a nice start. Two is when it starts to feel like a real desk.

So open your members area and set up a second one. Pick one that does something different. If your first one watches stocks, try JARVIS for your morning brief, or POLYBOT for prediction markets.

Same deal as before. Follow the setup, one step at a time.

Add my second bot: {{membersUrl}}

Rob""")
E["purchase/03-custom-bot.md"] = (None, """Hey {{firstName}},

Want a new finished bot dropped in your account every month?

That's Desk Live. Every month I build, test and finish a new bot. I also run one real stock past the six-analyst committee and send you the whole argument in writing.

It's $29 a month, or $290 for a year (two months free). You bought the Desk, so your first month is free.

You get the Members' Bonus Bot on day one, and you can cancel in one click from your members area.

See Desk Live: {{siteUrl}}/live

Rob""")
E["purchase/04-custom-bot.md"] = (None, """Hey {{firstName}},

Got a trading idea nobody's built yet?

Tell me what you want in plain English. I write the code, I test it on your setup, and I hand it over with a one-command installer and a plain-language guide. You never touch the code.

One bot per order. Delivered within 7 days after you send me the details.

See the custom build: {{siteUrl}}/custom

Rob

P.S. I don't promise profits. These are research and alert tools, and you make every decision.""")
E["purchase/05-show-me.md"] = (None, """Hey {{firstName}},

It's been about 5 days. I'd love to see what your bot made for you.

Send me a screenshot of one thing it produced. A chart read. An alert. A ticket. Anything. It takes 2 minutes.

If something looks off, I'll tell you which step to redo. If it worked, I'd love one honest sentence about it. I'll only share it on the site if you say yes.

Upload it here: {{proofUrl}}

Rob

P.S. My promise: """ + PROMISE)
E["purchase/06-get-paid-to-share.md"] = (None, """Hey {{firstName}},

You know someone who trades on gut feel. Everybody does.

Here's your link: {{referralUrl}}

Every time someone buys the AI Desk through it, $50 goes straight back to the card you paid with. Automatically. No forms. No waiting.

Send it to 4 people who buy, and your whole desk paid for itself.

And they're covered by the same promise you are. """ + PROMISE + """

Copy my link: {{referralUrl}}

Rob""")

# ---------- beta ----------
E["beta/00-youre-in.md"] = (None, """Hey {{firstName}},

Your seat is locked in. You now have AI Desk Pro, all 50 systems, free.

Here's the deal. Set it up within 7 days. Then send me an honest review: a screenshot and a few sentences about what worked and what didn't. Video is optional. And tell me what to fix or add. That part matters most to me.

Create your account with this email to open your systems: {{membersUrl}}

I'll send you a short feedback form on day 7.

Rob

P.S. Public sharing is optional. I only share your review with your permission, and it's labeled as coming from a free beta tester.""")
E["beta/01-day-three.md"] = (None, """Hey {{firstName}},

You're halfway through your 7 days.

Short on time? The Claude Chart Read takes about 15 minutes. Do that one.

Then screenshot the result and upload it with one sentence: {{proofUrl}}

Rob""")
E["beta/02-last-call.md"] = (None, """Hey {{firstName}},

It's day 7 of your free AI Desk Pro seat. How did it go?

The form asks what worked, what broke, what you'd add, a 1 to 10 rating, and an honest review. Be blunt. Blunt helps me more than nice.

Sharing your review publicly is optional. I only share it with your permission, labeled as coming from a free beta tester.

Send your feedback here: {{betaFeedbackUrl}}

Rob""")

# ---------- weekly ----------
W = {
"00-the-one-question.md": """Hey {{firstName}},

Before your next trade, ask Claude this. Word for word:

"Argue against my trade on [ticker]. Give me the 3 strongest reasons it loses money."

If you can't answer all 3, you don't have a trade. You have a hope.

That's one seat on my AI committee. The full desk has six seats, and the Risk Manager can veto anything.

See all 11 bots: {{checkoutUrl}}

Rob""",
"01-size-before-you-buy.md": """Hey {{firstName}},

Most trading accounts don't die from bad picks.

They die from one bet that was too big.

Here's the fix, and it's boring. Never risk more than 1% of your account on one trade.

Say you have $10,000. 1% is $100. Your stop is $2 below your entry. So you buy 50 shares. If it goes wrong, you lose $100. Not $1,000.

That's it. Boring math that keeps you in the game.

The Never-Blow-Up Kit does this math for you in 2 minutes. It comes with every bot: {{checkoutUrl}}

Rob""",
"02-screenshot-trick.md": """Hey {{firstName}},

Here's a trick for when Claude reads your chart.

After it answers, reply with: "Show me exactly where on the chart you see that."

If it can't point to it, the claim is made up. Delete it.

One line. Keeps AI honest. Try it tonight with my free chart guide: {{guideUrl}}

Want Claude to read every setup and text you? That's the Chart Analyst bot: {{checkoutUrl}}

Rob""",
"03-alert-not-a-signal.md": """Hey {{firstName}},

An alert going off feels like a signal.

It's not. It's a tap on the shoulder.

Before you do anything, ask 2 questions:

1. Did the candle actually close past my price, or just poke through?
2. What would make this a fake-out?

Two minutes. That's the whole habit. And it'll save you more money than any indicator.

My 24/7 Market Watch bot does this check for you, on every stock, every hour: {{checkoutUrl}}

Rob""",
"04-free-terminal.md": """Hey {{firstName}},

A Bloomberg Terminal costs about $30,000 a year.

You can get real market data on your laptop for free, with a tool called OpenBB. Hand that data to Claude, and it writes you a brief using only real numbers. No guessing.

Free guide (10 minutes): {{guideUrl}}

Want the daily version that builds your morning brief by itself? It's in the AI Desk: {{checkoutUrl}}

Rob""",
"05-journal.md": """Hey {{firstName}},

Want an edge most traders don't have? Write down every trade.

Three lines. Why you got in. Where your stop was. What happened.

After 20 trades, read them back. You'll find your one bad habit. Everybody has one. I promise.

It's free. And almost nobody does it.

Every bot in the AI Desk logs its ideas for you automatically, so you can check if it's actually working: {{checkoutUrl}}

Rob""",
"06-risk-veto.md": """Hey {{firstName}},

When you trade alone, nobody can stop you.

Not when you're excited. Not when you're tired. Not when you're angry.

That's why every bot I build has a risk check that can say no. And the AI can't argue its way past it.

It's the most boring part of every bot. And the most important.

See the bots: {{checkoutUrl}}

Rob""",
"07-rebuilt-bots.md": """Hey {{firstName}},

You've seen the posts. "This Polymarket bot turned $150 into $279,053."

That's the original creator's claim, not mine, and nobody has checked it. Nobody can promise you that result. Anybody who does is selling something.

What I can give you is the bot itself. Rebuilt, tested, with a risk check that can say no, so you can see exactly how it decides.

POLYBOT, ARENA, ARB, JARVIS and 7 more are all in the AI Desk: {{checkoutUrl}}

Rob""",
"08-earnings.md": """Hey {{firstName}},

Holding a stock through earnings? Ask yourself one question first:

"Am I OK if this gaps 10% against me overnight?"

Your stop can't save you from a gap. The price can jump right past it while you sleep.

If the answer is no, make the position smaller before the report. Not after.

JARVIS can tell you which of your stocks have earnings coming up. Just text it "any earnings this week?": {{checkoutUrl}}

Rob""",
"09-one-ticker.md": """Hey {{firstName}},

Pick the stock you're most excited about right now.

Now make 6 AI experts argue about it. The economy. The company. The chart. The risk. The case against. And a boss who makes the call.

It takes 10 minutes. The free guides show you how: {{guideUrl}}

The finished Hedge Fund Committee does it the same way every time, with a sizing sheet and a journal: {{checkoutUrl}}

Rob""",
"10-guarantee.md": """Hey {{firstName}},

Here's the bet I'm making on you.

""" + PROMISE + """

I can only make that promise because the setups are that clear.

So the only real risk left is the price going from $199 to $349 on {{priceEndsDate}}.

Take me up on it: {{checkoutUrl}}

Rob""",
"11-whats-new.md": """Hey {{firstName}},

Quick update. New bots keep landing in the AI Desk, and I update the old ones whenever the AI models change.

See everything that's inside today: {{siteUrl}}

The $199 founding price ends {{priceEndsDate}}. Grab it here: {{checkoutUrl}}

Rob""",
}
# weekly/ is owned by the Expert Secrets thread (Seinfeld-style rewrite), so it is not applied here.
WEEKLY_NOT_APPLIED = W

# ---------- apply ----------
FOOT = re.compile(r"^(Educational only.*|Unsubscribe: \{\{unsubscribeUrl\}\})$")
PH = re.compile(r"\{\{\w+\}\}")

def split(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert m, "no front matter"
    fm, body = m.group(1), text[m.end():]
    lines = body.rstrip("\n").split("\n")
    foot = []
    while lines and (FOOT.match(lines[-1].strip()) or lines[-1].strip() == ""):
        foot.insert(0, lines.pop())
    while foot and foot[0].strip() == "":
        foot.pop(0)
    return fm, "\n".join(lines).strip("\n"), "\n".join(foot)

done, same, missing, errors = [], [], [], []
for rel, (subj, new) in E.items():
    p = D / rel
    if not p.exists():
        missing.append(rel); continue
    fm, old, foot = split(p.read_text())
    if old.strip() == new.strip() and (subj is None or f"subject: {subj}" in fm):
        same.append(rel); continue
    lost = set(PH.findall(old)) - set(PH.findall(new))
    added = set(PH.findall(new)) - set(PH.findall(old))
    if lost or added:
        errors.append(f"{rel}: lost {sorted(lost)} added {sorted(added)}"); continue
    if subj is not None:
        fm = re.sub(r"^subject: .*$", "subject: " + subj.replace("\\", "\\\\"), fm, count=1, flags=re.M)
    out = f"---\n{fm}\n---\n\n{new.strip()}\n" + (f"\n{foot}\n" if foot else "")
    p.write_text(out)
    done.append(rel)

print("emails rewritten:", len(done))
print("already up to date:", len(same))
print("not found (skipped):", missing)
print("refused (placeholder mismatch, left unchanged):", errors)
live = sorted(str(x.relative_to(D)) for x in D.rglob("*.md") if x.name != "README.md")
print("live emails not covered by this script:", [x for x in live if x not in E])
