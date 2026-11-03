---
title: The Legends Algo Blueprint
promise: Turn the ideas of Buffett, Lynch, Dalio, Soros and Simons into 5 simple rules a computer can test. Plus a free prompt that turns your own idea into a rule in 10 minutes.
minutes: 15
nextSystemSlug: legends-strategy-lab
---

# The Legends Algo Blueprint

**Buffett. Lynch. Dalio. Soros. Simons.** Five of the most famous investors ever.

Most people "learn" from them by reading quotes. But quotes don't trade. **Rules do.**

This guide turns each legend's big idea into one simple rule a computer can follow and test. If you'd rather skip the building, the finished lab is at the end.

**When you're done, you'll have:**

- ✅ 5 legend-inspired rules, in plain English
- ✅ The 3 rules of an honest test, so you never fool yourself
- ✅ A free prompt that turns **your own** idea into a testable rule

**How it works:** Pick a legend's idea → turn it into one simple rule → test it on years it never saw → keep it only if it holds up

> **READ FIRST:** Old results don't promise future ones. A rule that only works on the years you tuned it on is a fake rule.

**Why this works:** A rule doesn't get scared or greedy. It does the same thing every time. And once your idea is a rule, you can test it on years of real prices and see the truth before you risk a dollar.

*These rules are inspired by each investor's public ideas. They're simple teaching models, not their real strategies. None of them endorse this guide.*

## The 5 legends as simple rules

**1. Buffett: great companies at a fair price.**
Buy companies that make lots of profit (return on equity over 15%), have little debt, and aren't too expensive (P/E under 25).

**2. Lynch: fast growth that's still cheap.**
Buy companies growing 15%+ a year where the price hasn't caught up yet (PEG ratio under 1).

**3. Dalio: spread out the risk.**
Own stocks, bonds, gold and commodities. Put less money in the jumpy ones and more in the calm ones. Rebalance once a month.

**4. Soros: ride the wave.**
When prices keep rising, people pile in, and that pushes prices higher. Stay in while the last 6 months are up. Go to cash when they're not.

**5. Simons: let the numbers decide.**
In a stock that's going up long-term, buy the short, sharp dips. Sell when it bounces back.

## The 3 rules of an honest test

Every idea sounds smart. A test tells you which ones actually work. Break any of these and your results are fake:

1. **No peeking.** If your signal uses today's closing price, you can only trade tomorrow.
2. **Pay the fees.** Every trade costs money. Include it.
3. **Test on new years.** Build your rule on old data (say, up to 2021). Then test it on the years after. Only the second result counts.

## Turn your own idea into a rule (10 minutes, free)

Paste this into [Claude](https://claude.ai/):

```text
You are my trading research assistant. Turn my idea into a simple rule
a computer can test.

My idea: [describe it in 1-2 sentences]

1. Write the rule so it's 100% clear: exactly when to buy, when to sell,
   and how often to check.
2. What data do I need, and where can I get it free?
3. The 3 most likely ways this rule fails.
4. How to test it honestly: no peeking, include fees, test on new years.
Don't give me any results. You haven't tested anything yet.
Plain English.
```

**Tip:** change one thing at a time when you test. If you tweak a rule 20 times until it looks amazing, you've fooled yourself.

## How to build the test lab

**To build it yourself,** you'd write a Python program that downloads years of prices, turns each legend's rule into code, runs an honest test with the 3 rules above, and prints a scorecard next to "just buy and hold." If you know Python, that's a weekend.

> Educational only. Not financial advice. Past results never promise future ones.

## Make it yours: your testing rules (3 minutes)

Paste this into Claude before you test any idea, so it can't fool you (or itself):

```text
MY TESTING RULES
Pick settings on older years only. Test on newer years the rules never saw.
Include trading costs. No using tomorrow's price to decide today.
Report: number of trades, win rate, average win vs average loss, worst drop,
and how it compares to simply buying and holding.
If the result only works on one market or one short period, say so.
```

## 12 copy-paste prompts

**Turning ideas into rules**

1. "Turn this idea into one simple rule with exact numbers: [idea]."
2. "Here's my rule. List every way it could be cheating (looking ahead, ignoring costs, tiny sample)."
3. "Make this rule simpler. Fewer settings = less chance it's just luck."

**Testing**

4. "Write a simple Python test for this rule using free daily data, with costs and an older/newer year split."
5. "Here are my test results: [paste]. Is this real, or luck? Be blunt."
6. "Run the same rule on 5 other markets. Does it still work?"
7. "What's the worst losing streak in these results? Could I stick with it?"

**Comparing legends**

8. "Compare the 5 legends' rules side by side: how often they trade, how long they hold, what they need to work."
9. "Which legend rule fits someone with $___ and 15 minutes a day?"
10. "Combine two rules into one. Does the mix do better on the newer years, or worse?"
11. "Write the rule as TradingView Pine Script v6 so I can see it on a chart."
12. "Give me a 1-page summary of this test I can save: rule, result, honest weaknesses."

## Your weekly routine

| When | Do this |
|---|---|
| One evening (20 min) | Pick one idea. Turn it into a rule (prompt 1). Check it for cheating (prompt 2). |
| Test (20 min) | Run the test (prompt 4). Judge it (prompt 5). |
| Save | Keep a list of every rule tested, including the ones that failed. |

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

- [ ] You picked one legend rule (or your own idea)
- [ ] You wrote it as one clear rule a computer could follow
- [ ] You know the 3 rules of an honest test

## Troubleshooting

| Problem | Fix |
|---|---|
| My rule has "feel" words | Swap them for numbers: not "cheap", but "price under 15x earnings". |
| It looks amazing in the test | Check it on years you didn't tune on. Most "amazing" rules fail there. |
| Too few trades to judge | Test more markets or more years. |

## Want it done for you?

You just did it once, by hand. **The finished Legends Lab tests all five legends for you with one click, honestly, and prints a scorecard next to buy-and-hold. It runs free in Google Colab, with nothing to install.**

We already did the hard part. We built it. We tested it. We wrote every setting and every step. **Your part: follow the 60-minute setup. Copy, paste, done.** No coding skills needed.

**Here's everything you get for one payment of $199:**

- ✅ **The finished Legends Strategy Lab**, tested and ready to run
- ✅ **10 more finished trading bots:** POLYBOT, JARVIS, ARENA, ARB, the AI Board, the 24/7 Market Watch, the Claude Chart Analyst and more
- ✅ **30 AI business systems** for sales, content, apps and outreach
- ✅ **The Never-Blow-Up Kit**, so one bad trade can't sink your account
- ✅ **A step-by-step setup for every bot**, start to finish
- ✅ **Every new bot we release, free for 12 months**

**Total value: $1,792. You pay $199. Once.** No monthly fee. Nothing to cancel.

**The price goes up to $349 on December 1.** Same bots, same files. You just pay $150 more for waiting.

**Our "It Runs or It's Free" promise:** Follow the steps. If your bot isn't running in 7 days, email support@milli-ai.com. You get every dollar back, and you keep the files anyway. You can't lose.

**[Yes! Give me the finished Legends Lab for $199 →]({{offerUrl}})**
