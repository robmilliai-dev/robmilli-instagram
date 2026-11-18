#!/usr/bin/env python3
"""Rewrite keyword DM texts (dmText) in content/instagram/dm-rules.json, in place.
Usage: python3 dms_v3.py <path to dm-rules.json>
Only dmText changes, and only for the keywords below. Keeps every other field and keyword as is.
Refuses a keyword if its guide link would change. Safe to run twice."""
import json, re, sys, pathlib

P = pathlib.Path(sys.argv[1])
U = "https://milli-ai.com"
DESK = ("Want the finished version instead? It's in the AI Desk with 10 more tested bots and 30 AI business systems. "
        "One payment of $199. Not running in 7 days? I'll set it up with you, or you get every dollar back and keep the files.")
EDU = "Educational only, not financial advice."

def dm(title, slug, lines, offer=True, foot=EDU):
    parts = [f"Here it is: {title} 👉 {U}/free/{slug}"] + lines
    if offer:
        parts.append(DESK)
    if foot:
        parts.append(foot)
    return "\n\n".join(parts)

T = {
 "CHART": dm("The Claude Chart Read", "chart", ["One screenshot. One prompt. A plain-English read of the trend, the key prices and the biggest red flag, in 15 minutes.", "Do it now, while the chart's still open on your phone."]),
 "DESK": dm("The 15-Minute Market Watch", "desk", ["Pick a price while you're calm. TradingView watches it. When it hits, AI checks the move before you touch anything.", "No more staring at charts all day."]),
 "HEDGE": dm("The One-Ticker Committee", "hedge", ["Six AI experts argue about one stock. One of them has a single job: tell you why you're wrong.", "Run it on the stock you're most excited about. That's the one that needs it most."]),
 "TEAM": dm("Your First AI Employee", "team", ["Paste one real customer message. Your AI employee drafts the reply. You check it and hit send. Thirty seconds."], offer=False, foot="The full 8-worker AI Employee Pack comes free inside the AI Desk. One payment of $199. Not working in 7 days? I'll set it up with you, or you get every dollar back."),
 "TERMINAL": dm("OpenBB in 10 Minutes", "terminal", ["A Bloomberg Terminal costs about $30,000 a year. This gets you real market data free, and Claude writes your morning brief from real numbers only."], foot=EDU + " Open-source data, not a Bloomberg product."),
 "LEGENDS": dm("The Legends Algo Blueprint", "legends", ["Buffett, Lynch, Dalio, Soros and Simons, turned into simple rules a computer can test. Quotes don't trade. Rules do."], foot=EDU + " Simplified teaching models, not their real strategies, and none of them endorse this."),
 "TRADINGVIEW": dm("Claude × TradingView", "tradingview", ["Level 1 takes 5 minutes: Claude reads any chart you upload. Levels 2 and 3 show how it can watch your charts and text your phone."], foot=EDU + " AI can misread a chart. You make every decision."),
 "DOTS": dm("The Milli Dots Indicators", "dots", ["Two free TradingView indicators I built, then tried hard to break. Paste them in and blue dots show up when the setup happens. Two minutes."], offer=False, foot="Hypothetical backtests. " + EDU),
 "DIP": dm("The Milli Index Dip Indicator", "dip", ["When the S&P 500 has a panic day inside an uptrend, a blue dot shows up. When it bounces, you get the exit. Copy, paste, done in 2 minutes."], offer=False, foot="Hypothetical backtests. " + EDU),
 "PROP": dm("The Prop Challenge Playbook", "prop", ["Most people blow prop challenges the same way: too much risk, too fast. This does the opposite. Small risk, a tested trend indicator, and patience."], offer=False, foot=EDU + " Not affiliated with any prop firm."),
 "WHALE": dm("The Whale Team", "whale", ["Every Polymarket wallet is public. 6 AI agents find the ones worth watching and throw out the lucky ones. When I checked the top 25, 9 failed."], offer=False, foot=EDU + " Check that prediction markets are legal where you live."),
 "24/7": dm("The 24/7 AI Trader Blueprint", "24-7", ["What if a trader watched the market all day and only texted you when something good showed up? This shows you how it works. It never places a trade. You make the call."]),
 "JARVIS": dm("The JARVIS Blueprint", "jarvis", ["Text it \"brief me\" and it looks up the real numbers on your stocks. Your positions. What moved. What's coming. Thirty seconds."]),
 "POLYBOT": dm("The POLYBOT 6-Agent Blueprint", "polybot", ["Six AI agents, one job each, and any one of them can kill a bet. Don't be surprised when it says BLOCKED. A bot that says yes to everything is broken."], foot=EDU + " The $279,053 result is the original creator's own unverified claim, not mine."),
 "ARENA": dm("The ARENA Playbook Blueprint", "arena", ["The AI that won Nof1's real-money contest didn't win with brains. It won with discipline. Here's its playbook as a 4-agent team."], foot=EDU + " One short contest doesn't predict the future. Crypto can lose you money fast."),
 "ARB": dm("The ARB Bot Gap-Finder Blueprint", "arb", ["It doesn't predict games. It compares prices. When the sportsbooks and Polymarket disagree, that gap is the whole idea."], foot=EDU + " The $1 to $3.3 million claim is unverified and not mine. Check that prediction markets are legal where you live."),
 "BOARD": dm("The AI Board Blueprint", "board", ["Five AIs, five jobs, one vote. A trade only passes if 4 of 5 say yes, and Claude can veto all of them."], foot=EDU + " AI can be wrong. You make every decision."),
 "HQ": dm("The AI Trading HQ", "hq", ["Send a stock idea up a 6-floor AI building. Any floor can stop it. Only the best ideas reach the top."], foot=EDU + " AI can be wrong. You make every decision."),
 "BOTS": dm("The 7-Bot Trading Desk", "bots", ["Seven AI bots, one vote, and a risk bot that can veto anything. Run your next stock idea past all seven tonight."], foot=EDU + " AI can be wrong. You make every decision."),
 "BACKTEST": dm("The 10-Minute Strategy Lie Detector", "backtest", ["Saw a \"this made 400%\" strategy in a reel? Test it on years of real prices before you risk a dollar."]),
 "PRACTICE": dm("The Free Prop Challenge Practice Run", "practice", ["Before you pay a challenge fee, find out if your trading could pass. Practice first. Free."], offer=False, foot=EDU + " Not affiliated with any prop firm."),
 "JOURNAL": dm("Find Your 3 Trading Leaks", "journal", ["Most traders don't need a new strategy. They need to stop 2 or 3 habits. A 60-second journal and a Claude prompt that finds yours."]),
}

LINK = re.compile(r"https://milli-ai\.com/\S+")
rules = json.loads(P.read_text())
done, same, refused = [], [], []
for r in rules:
    k = r.get("keyword")
    if k not in T:
        continue
    new = T[k]
    old_links = set(LINK.findall(r.get("dmText", "")))
    if old_links and not old_links <= set(LINK.findall(new)):
        refused.append(f"{k}: link {sorted(old_links)} not in new text"); continue
    if r.get("dmText") == new:
        same.append(k); continue
    r["dmText"] = new
    done.append(k)
P.write_text(json.dumps(rules, ensure_ascii=False, indent=2) + "\n")
print("dm texts rewritten:", len(done), done)
print("already up to date:", same)
print("refused:", refused)
print("keywords left as is:", [r.get("keyword") for r in rules if r.get("keyword") not in T])
