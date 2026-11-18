---
title: The Trader Bias Audit
keyword: BIAS
promise: One prompt makes your AI build a profile of you as a trader from everything you've told it, then names the bias that's costing you the most.
---

# The Trader Bias Audit

**If you've talked trades with ChatGPT or Claude for months, it knows your habits better than your journal does.** This prompt makes it say them out loud.

Works best in an assistant with memory or chat history turned on (ChatGPT memory, Claude with past-chat search, or paste your old chats / journal in).

## The prompt

```text
You are a trading coach doing a blunt intake review. Use everything you know about me:
saved memories, past chats about trading, anything I paste below. If you have nothing,
say so and stop.

Give me these 11 sections. Short, plain words. Quote my own words where you can.

1. WHAT YOU KNOW: list every trading-related fact you have about me (markets, account
   size, tools, wins, losses, goals). Mark each "I said it" or "you inferred it".
2. MY STYLE AS I DESCRIBE IT vs. MY STYLE AS I ACT: where they don't match.
3. TOP 3 BIASES: from this list, which show up most, with an example from our chats:
   FOMO, revenge trading, loss aversion (holding losers), cutting winners early,
   overconfidence after wins, recency bias, confirmation bias, sunk cost, overtrading,
   hype chasing, "this time is different".
4. THE COSTLIEST ONE: which bias has probably cost me the most money, and why you think so.
5. MY TRIGGERS: the situations right before I make bad decisions (time of day, after a
   loss, after seeing a post, boredom).
6. MY RULES: every rule I've told you I follow. Then: which ones I've told you I broke.
7. WHAT I ASK AI FOR: what my questions say about me (am I asking for permission?).
8. THE QUESTION I KEEP AVOIDING.
9. ONE RULE: the single rule that would fix the costliest bias. Make it testable
   ("no new trade within 60 minutes of a loss"), not a feeling.
10. ONE CHECK: a 10-second question I ask myself before every trade.
11. WHAT YOU DON'T KNOW: what you'd need from me to make this review better.

No praise. No softening. If the evidence is thin, say "thin evidence" instead of guessing.
Not financial advice: this is about behavior, not picks.

Anything extra I'm pasting (journal, trade log, old chats):
```

## What to do with the result

1. Write the **ONE RULE** on a sticky note on your screen. Or put it in your bot's code.
2. Add the **ONE CHECK** to your pre-trade routine.
3. Run the audit again in 30 days. If the costliest bias changed, it's working.

## Privacy note

Before you paste anything: remove account numbers, balances you don't want stored, and every API key. See the LOCKDOWN prompt for what to never give an AI.

> Educational only. Not financial advice.
