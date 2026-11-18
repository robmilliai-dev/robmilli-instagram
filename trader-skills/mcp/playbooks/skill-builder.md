---
id: skill-builder
title: The Skill Builder
category: build
summary: Turn anything you repeat as a trader into a reusable skill: intake, process, rules with reasons, output contract, self-check, stop-and-show. Tested on your real example.
---

# SKILL BUILDER

If you've typed the same instructions into an AI three times, it should be a skill.

## INTAKE (one message)

1. What's the task? Describe the last time you did it, step by step.
2. How often? (Daily, weekly, every trade)
3. What goes in? (Files, a ticker, a CSV, nothing)
4. What comes out? Paste the best version you've ever produced, if you have one.
5. What has gone wrong before when you or an AI did it?
6. Can it touch anything risky? (Orders, money, sending messages, deleting files)

## BUILD

Write `SKILL.md` with these parts, in this order:

1. **Frontmatter:** `name` (kebab-case), `description` (what it does + when to use it, one or two sentences: this is what makes Claude pick it), `argument-hint`.
2. **One-line purpose** under the title.
3. **READ FIRST:** files or context it must load before acting (rules.md, watchlist, last week's output).
4. **INTAKE:** questions to ask if inputs are missing, all in one message.
5. **PROCESS:** numbered steps. Each step produces something checkable.
6. **HARD RULES:** each one with "because …". Rules without reasons get ignored or over-applied.
7. **OUTPUT CONTRACT:** exact file names, format, sections. Same every time.
8. **SELF-CHECK:** 3 to 5 checks before it shows the result.
9. **STOP AND SHOW:** where it must pause for the human (anything risky from intake question 6 always gets one).

If it needs a script (math, API calls, file parsing), write it in `scripts/` and have the skill call it. **Models are bad at arithmetic; scripts aren't.**

## TEST BEFORE SHIPPING

1. Run the skill on the user's real last example.
2. Compare with their best version. List differences.
3. Run it on one bad input (missing file, weird data). It should ask or stop, not guess.
4. Fix and re-run. Call it done only after both pass.

## INSTALL

```
.claude/skills/<name>/SKILL.md        # this project
~/.claude/skills/<name>/SKILL.md      # every project
```

For ChatGPT or Claude Projects without Claude Code: paste the same content as project instructions.

## HARD RULES

- **One skill, one job.** If the description needs "and also", make two skills.
- **Never let a skill place trades or send messages without a stop-and-show step,** because the cost of one wrong run is real money or a burned contact.
- **Fill every [bracket] with the user's real constants** (their risk %, their broker, their watchlist). A skill with someone else's numbers is worse than none.
