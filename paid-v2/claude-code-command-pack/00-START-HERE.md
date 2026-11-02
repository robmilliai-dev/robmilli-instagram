# Start here: 14 shortcuts that make Claude Code do your boring dev work

**What this does:** You type one short command like `/review` and Claude Code checks your code, finds missing tests, writes your PR description, and more. No more typing the same long request every day.

**What you'll have in 30 minutes:**

- ✅ Your first command working in your own project
- ✅ All 14 ready-made commands, copied in and ready
- ✅ The know-how to write your own

**What you need:** [Claude Code](https://code.claude.com/docs/en/overview) installed, and a project folder that uses git.

## Try it now: your first command (5 minutes)

1. Open your project in a terminal.
2. Make a folder called `.claude/commands/` in the top of your project.
3. Make a file in it called `change-map.md`. Paste this in exactly:

```text
---
description: Summarize changed files and identify the riskiest change
argument-hint: [optional area]
---
Inspect the current git diff and relevant surrounding code. If $ARGUMENTS names an area, prioritize it. Do not edit files. Report: changed files grouped by purpose; the most likely regression with file/line evidence; one cheap test to run; and anything you could not verify. If there is no diff, say so and ask for a branch or commit range. Never claim a test passed unless you ran it.
```

4. Type `claude` in the same folder to start Claude Code.
5. Type `/change-map` and press Enter.

✅ **It works when** you see a short summary of your changes and the riskiest one. It won't change any code.

**Command not found?** Make sure you started `claude` from the top of your project, the file name is right, and restart Claude Code.

## Add all 14 commands

1. Save your work first: commit it, or check `git status --short` is clean.
2. Copy the command files you want from `code/.claude/commands/` into your project's `.claude/commands/` folder.
3. Start Claude Code in that folder. Type `/` to see your commands.
4. Try one: `/explain src/path/to/file`.

**The 14 commands:** review, test gaps, explain, safe refactor, debug, security, docs, migration, PR description, commit message, dependency check, API contract, release check, incident notes.

Commands that change files always ask you first.

## What's inside

1. [Pick your commands](01-install-and-choose.md): which ones you need.
2. [The 30-minute walkthrough](02-first-win.md): step by step.
3. [Write your own](03-write-your-own.md): make new shortcuts.
4. [Fix problems](04-troubleshooting.md): when a command misbehaves.

A starter `CLAUDE.md` is included too. It tells Claude the rules for your project.

## Good to know

- Always check Claude's review against your real code and tests before you merge.
- Never paste passwords or secret keys into a command.
- Big changes use more of your Claude plan. Point commands at one folder to keep it small.
- Newer Claude Code versions also support "skills". Your commands still work. See the [skills docs](https://code.claude.com/docs/en/skills).

Stuck? Email support@milli-ai.com. If it's not working in 7 days, you get every dollar back, and you keep the files.
