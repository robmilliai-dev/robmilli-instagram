---
title: The Yes-Man Off Prompt for Traders
promise: Your AI agrees with every trade idea you show it. Here's why, and the 10 lines that make it argue back.
minutes: 5
nextSystemSlug: tradingview-claude-chart-analyst
---

# The Yes-Man Off Prompt for Traders

**Ask ChatGPT "is this a good trade?" and it finds a reason to say yes.** That's not a bug in your prompt. It's how these assistants are built.

## Why your AI agrees with you

Chat assistants are trained to be helpful and pleasant, and people rate agreeable answers higher. So the default leans toward:

1. **Matching your mood.** You sound excited, it sounds excited.
2. **Answering the question you asked,** not the one you should have asked. "Is this a good entry?" never gets "you shouldn't be in this stock."
3. **Hedging instead of disagreeing.** "There are some risks to consider" means "this is a bad idea" in assistant-speak.
4. **Finishing the task.** Ask for a bullish case and you get a bullish case, even if the chart is a mess.
5. **Avoiding numbers it can't back.** Good, but it fills the gap with confident-sounding words.

For most things that's fine. For trading it's dangerous. You want the friend who says "you're about to do something dumb".

## The override (paste at the top of any chat, or into Custom Instructions / a Claude Project)

```text
For anything about trading, investing or money, act as my risk manager, not my cheerleader.

1. Before answering, tell me the strongest reason I'm wrong. One paragraph. Always.
2. Never match my excitement. If I sound sure, push harder.
3. If the idea breaks a rule I've told you (risk per trade, daily loss limit), say STOP first.
4. Say "I don't know" or "you'd need to test this" instead of guessing. Never invent numbers.
5. Grade every idea: STRONG / UNTESTED / WEAK / DON'T, with one line why.
6. If I ask for a bullish case, also give the bearish case, same length.
7. Ask me the one question I'm avoiding (usually: where's your stop, and how much do you lose if it hits?).
8. No "great question", no praise, no "exciting opportunity".
9. Plain words. Short sentences. Numbers when you have them, sources when you cite them.
10. You are not giving financial advice, and I won't treat it as advice. Be blunt anyway.
```

## Test it in 60 seconds

Paste the override, then ask: *"I'm thinking of putting half my account into a stock that's up 300% this year because the momentum is crazy. Good idea?"*

Without the override you'll get "momentum can be powerful, but consider…". With it you should get **DON'T**, the stop question, and the math on what half your account at risk means.

## Make it permanent

- **ChatGPT:** Settings → Personalization → Custom instructions → paste it in "How would you like ChatGPT to respond?"
- **Claude:** make a Project called "Trading", paste it into the project instructions.
- **Your own bot:** put it at the top of the system prompt (see the BRAIN prompt for the full pattern).

> Educational only. Not financial advice.

## Want it done for you?

The free version gets you started. **The finished TradingView + Claude Chart Analyst reads your chart and argues with you before you click, using rules you set.**

I already did the hard part. I built it. I tested it. I wrote down every setting and every step.

Your part is a 60-minute setup. Copy. Paste. Done. You don't need to know how to code.

**Here's everything you get for one payment of $199:**

- ✅ **The finished TradingView + Claude Chart Analyst**, tested and ready to run
- ✅ **11 finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **Bots in your inbox for 3 months:** a morning email with what my 5 tested bots see on your markets. Nothing to install
- ✅ **The Milli Indicator Pack** for TradingView. Paste it and see the dots on your chart in 2 minutes
- ✅ **All 17 Milli trader skills + 6 prompt kits** in one download, plus the Milli MCP
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **Every new bot I release for the next 12 months, free**

That's $2,175 of systems. **You pay $199. Once.** There's no monthly fee and nothing to cancel.

On December 1 the price goes to $349. Same bots. Same files. You'd just be paying $150 more for waiting.

**My promise.** Follow the steps. If it isn't running in 7 days, email robmilli.ai@gmail.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files anyway.

**[Yes, give me the finished TradingView + Claude Chart Analyst for $199 →]({{offerUrl}})**
