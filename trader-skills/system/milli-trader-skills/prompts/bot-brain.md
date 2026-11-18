---
title: The Bot Brain Meta-Prompt
keyword: BRAIN
promise: The 9-part pattern behind every serious AI product's instructions, and one prompt that writes a pro-grade system prompt for your trading bot.
---

# The Bot Brain

**The difference between a toy AI bot and one you'd trust near money isn't the model. It's the instructions.** Serious AI products (coding agents, support bots, research tools) share the same structure in their system prompts. Here it is, applied to trading.

## The 9 parts every strong system prompt has

| # | Part | What it does | Trading bot example |
|---|---|---|---|
| 1 | **Identity + job** | One line: who it is, one job | "You are a risk-first market scanner for US large caps." |
| 2 | **Context to read first** | What it must load before acting | "Read rules.md, today's watchlist, open positions." |
| 3 | **Inputs it gets** | Exact shape of what comes in | "A JSON of OHLCV bars per symbol, last 250 days." |
| 4 | **The process** | Numbered steps, in order | "1. check data freshness 2. compute signals 3. apply risk rules…" |
| 5 | **Hard rules with reasons** | Never/always, each with a why | "Never size above 1% risk: one bad fill must not hurt the week." |
| 6 | **Output contract** | Exact format, every time | "Return JSON {symbol, action, size, stop, reason}." |
| 7 | **Refusals and stops** | When to do nothing | "If data is older than 1 bar, return NO_ACTION with reason STALE." |
| 8 | **Quality check** | Self-check before answering | "Before output, verify stop < entry for longs." |
| 9 | **Tone + examples** | 1 good and 1 bad example | A sample correct output, and a sample rejected one |

Most home-made bot prompts have parts 1 and 4. The missing 2, 5, 6 and 7 are where bots blow up.

## The meta-prompt (paste into Claude or ChatGPT)

```text
You are a prompt engineer who writes system prompts for AI agents that touch money.

Interview me first, in ONE message, with these questions:
1. What should the agent do, in one sentence?
2. What data does it get, and in what format?
3. What can it do: just suggest, send alerts, or place orders?
4. My risk rules (risk per trade, max daily loss, max positions, markets allowed).
5. What should it NEVER do?
6. What does a perfect output look like? (paste an example if you have one)

Then write the system prompt with exactly these 9 sections:
IDENTITY & JOB, READ FIRST, INPUTS, PROCESS (numbered), HARD RULES (each with
"because ..."), OUTPUT CONTRACT (exact JSON or text format), WHEN TO DO NOTHING,
SELF-CHECK BEFORE OUTPUT, EXAMPLES (one good, one rejected with why).

Rules for what you write:
- Risk rules come before signal rules.
- Every rule is testable by reading the output.
- Default to "do nothing" when anything is missing, stale or unclear.
- If the agent can place orders, add a KILL check as step 1 of the process.
- No hype words. No promises of profit.
After the prompt, list 5 test inputs I should run it on, including 2 that should
make it refuse.
```

## Then test it

Run the 5 test inputs. If any "should refuse" input gets a trade, add a rule and run again. A prompt you haven't tried to break isn't finished.

> Educational only. Not financial advice.
