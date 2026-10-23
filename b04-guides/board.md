---
title: The AI Board Blueprint
promise: Five AIs, five jobs, one vote. How a 5-AI trading board works (Perplexity, Grok, Gemini, ChatGPT and Claude), how to build it, and 5 free prompts you can paste into each AI today. Works with just Claude, too.
minutes: 15
nextSystemSlug: ai-board
---

# The AI Board Blueprint

In Nof1's Alpha Arena (Season 1, October to November 2025), six AI models each traded real money on their own, and four of them lost it (Nof1's reported results, not mine). The ones that lost traded too often, chased hype and skipped their stops.

One AI alone has blind spots. So I built a board: **five AIs, each with one job, and a vote.** The AI that's best at a job does that job, and none of them can push a trade through alone.

| Seat | AI | Its one job | When it votes SKIP |
|---|---|---|---|
| Sources | Perplexity | Find recent news and filings, each with a link and a date | Fewer than 2 linked, dated sources, or a red flag |
| Sentiment | Grok | Read what traders on X are saying | Hype alert: chatter far above normal or driven by rumors |
| Charts | Gemini | Map the setup: entry, stop, target | No clean setup |
| Thesis | ChatGPT | Build the case, then attack it | The case doesn't survive its own attack |
| Risk | Claude | Check what's missing and what could go wrong | Anything a careful trader would walk away from. **Claude can veto.** |

**A trade only reaches you if 4 of 5 vote TAKE, Claude doesn't veto, and the hard rules pass.** Then you decide. It never places an order.

Educational only, not financial advice. AI can be wrong.

## Try it today: 5 free prompts

Open each AI in its own tab and run the prompts in order, pasting each answer into the next. Don't have all five? Run every prompt in Claude. That works too.

**1. Perplexity (Sources)**
```text
You are SOURCES on a 5-AI trading board. Find news from the last 14 days that matters for [TICKER]:
earnings, filings, guidance, analyst moves, macro. List each item as: claim · source · date · link.
Any item without a link and a date doesn't count. Then list red flags.
End with VOTE: TAKE or SKIP (SKIP if fewer than 2 solid items or any red flag).
```

**2. Grok (Sentiment)**
```text
You are SENTIMENT on a 5-AI trading board. What are traders on X saying about [TICKER] right now?
Give: % bullish, % bearish, a one-line summary, and HYPE ALERT yes/no (yes if chatter is far above
normal or driven by memes, influencers or rumors). Hype is a warning, not a signal.
End with VOTE: TAKE or SKIP (always SKIP on a hype alert).
```

**3. Gemini (Charts)**: paste a daily chart screenshot, or the price, 20/50/200 EMAs, RSI and ATR.
```text
You are CHARTS on a 5-AI trading board. Using only what I give you, map the setup for [TICKER]:
direction (LONG / SHORT / NONE), entry, stop (where the setup is clearly wrong, about 1-2 ATR away),
target (at least 1.5x the stop distance), and confidence 0-100. No clean setup = NONE.
End with VOTE: TAKE or SKIP. Never invent prices.
```

**4. ChatGPT (Thesis)**: paste the first three answers.
```text
You are THESIS on a 5-AI trading board. Using the reports below, write the best case for this trade,
then argue the other side as hard as you can. Give the one event that would kill the trade,
and a confidence 0-100. Vote TAKE only if the case survives your own attack.
End with VOTE: TAKE or SKIP.
[paste reports 1-3]
```

**5. Claude (Risk)**: paste all four answers.
```text
You are RISK on a 5-AI trading board, and you can veto. Review the four reports below. List missing
data, stale or weak sources, hype, a stop in the wrong place, and anything the team glossed over.
Then: VETO yes/no and VOTE: TAKE or SKIP.
Finally count the votes. If 4 of 5 say TAKE and there's no veto, size it so hitting the stop loses
1% of a $[ACCOUNT] account, and show the ticket. Otherwise say "NO TRADE" and why.
End with: "Nothing has been placed. You make the final call."
[paste reports 1-4]
```

**NO TRADE will be the most common answer.** That's the board doing its job.

## How to build the automated version (the blueprint)

**Data (no AI).** Pull a year of daily prices for each ticker (the free `yfinance` Python library works) and calculate the 20/50/200 EMAs, 14-day RSI, 14-day ATR and the 20-day high and low. The chart seat gets these numbers, so it can't invent prices.

**One function per AI.** Each provider has a simple HTTP API:
- **Perplexity:** `POST https://api.perplexity.ai/chat/completions` (its models search the web by default).
- **Grok (xAI):** `POST https://api.x.ai/v1/chat/completions`.
- **Gemini:** `POST https://generativelanguage.googleapis.com/v1beta/models/<model>:generateContent`, with JSON output turned on.
- **ChatGPT:** `POST https://api.openai.com/v1/chat/completions`, with JSON mode.
- **Claude:** the official `anthropic` Python SDK, with structured outputs for the Risk seat and the web search tool when it fills the Sources or Sentiment seat.

Ask every seat for **one JSON object** that ends in `"vote": "TAKE"` or `"SKIP"`.

**Fallback.** If you don't have a key for a seat, send that seat's prompt to Claude instead. If an AI errors or times out, that seat votes SKIP. One broken AI must never crash the board, and must never count as a yes.

**Rules in plain code (the AIs can't overrule these):**

| Check | Default |
|---|---|
| Votes | at least 4 of 5 TAKE |
| Claude veto | none |
| Sources | at least 2 with a link and a date (code drops the rest) |
| Hype alert | forces Sentiment to SKIP |
| Stop | on the correct side, 0.5-3 ATR away |
| Reward : risk | at least 1.5 |
| Entry | within 2% of the current price |
| Size | lose at most 1% of the account at the stop |

**Ticket + log.** Send one message to Telegram with every vote (and which AI cast it), the chart setup, the bull case, the bear case, the kill rule, Claude's concerns and, only if everything passed, the size and max loss. Log each run to a CSV. After a month, check whether the trades the board passed beat the ones it blocked.

## Want the finished bot?

If you'd rather not build it, the finished, tested AI Board is in the **AI Desk**: all 5 seats wired up, Claude fallback for any seat you don't have a key for, one-command install, Telegram tickets and the vote log, with step-by-step instructions from zero to your first ticket.

Every free guide we release, including this one, is also included as a bonus inside the AI Desk.
