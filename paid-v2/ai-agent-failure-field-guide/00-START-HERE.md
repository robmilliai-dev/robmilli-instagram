# Start here: catch your AI agent when it lies about being done

**The problem:** An AI agent can say "Done! ✅" when nothing actually happened. The tool failed. The file never saved. The email never sent. It *sounds* finished, so you believe it.

**What this guide does:** It shows you how to catch that in minutes, before it costs you money or a client.

**What you'll have in 30 minutes:**

- ✅ A simple 3-question check you can run on any agent
- ✅ Your first agent audited, with proof of what really happened
- ✅ A pre-flight checklist so it doesn't happen again

**What you need:** Any AI agent or tool you already use (Claude, ChatGPT, an automation). No extra software.

## The 3 questions

Ask these after any agent run that matters:

1. **What did I ask for?** Look at your first message, not the agent's summary of it.
2. **What really happened?** Look at the tool result. Did it say "saved", show an ID, or show an error? The agent's chat message is not proof.
3. **What would have caught a mistake?** Write one simple test. Not "be careful". Something like: "Only say done if you got the new record ID back."

**Try it now:** Take your last agent run. Put your request next to its final answer. Find one tool result that proves it worked. Can't find one? Mark it **"not proven"**. Not a fail, not a win. Now you know what to check.

## A 10-minute practice drill

1. Give a test agent a harmless job, like: "Create a draft note called April test."
2. Make the save step fail on purpose (turn off its access, or use a fake folder). **Never do this on real data.**
3. Ask the agent to keep going.

- **Good agent:** "The save didn't work. Here's the error. Want me to try again?"
- **Bad agent:** "Your note is created!" That's called **fake success**. It's one of the 12 problems in [the field patterns](02-field-patterns.md).

## What's inside

1. [Your first audit](01-first-audit.md): the 30-minute check, with a full example.
2. [The 12 field patterns](02-field-patterns.md): each problem, how to spot it, how to fix it, how to test it.
3. [Test and recover](03-test-and-recover.md): what to check before you launch, and what to do when something breaks.
4. Keep these handy: the [pre-flight checklist](templates/preflight.md) and the [incident log](templates/incident-log.md).

## Simple safety rules

- Test on fake or sandbox data first.
- Make the agent ask you before it sends messages, deletes things, buys things, or changes access.
- Remove passwords and private info before pasting logs into any AI.
- Re-running tests can cost a little in AI usage. Set a spending cap in your AI account.

The goal isn't zero mistakes. The goal is that you **see** every mistake before your customers do.

Stuck? Email support@milli-ai.com. If this doesn't help you in 7 days, you get every dollar back, and you keep the files.
