# Start here: find local businesses that need what you sell

**What this does:** You find local businesses that have a real problem you can fix. You note the proof. AI helps you write a short, personal message. No buying junk lists. No spam.

**What you'll have in 30 minutes:**

- ✅ 3 real local businesses checked by hand
- ✅ One clear reason to reach out to each
- ✅ A score that tells you who to contact first
- ✅ A first message, drafted and ready for you to review

**What you need:** [Google Maps](https://www.google.com/maps), a spreadsheet, and [Claude](https://claude.ai). No API key. No code.

## Step 1: Pick one city, one business type, one offer

Good: "Website fixes for independent roofers in Madison."
Too broad: "Anyone who needs AI."

## Step 2: Find 3 businesses (15 minutes)

1. Open Google Maps. Search your niche and city, like "independent roofers Madison WI".
2. Open 3 listings.
3. For each one, click through to **their own website**.
4. Look for one problem your offer fixes. For example: no way to book online, a broken contact form, or no phone number on the mobile site.
5. Write what you found in your copy of [the tracker](templates/lead-tracker.csv), with the web address and today's date.

No website? Write "check by hand". Don't assume they don't have one.

## Step 3: Score and draft (15 minutes)

1. Score each business using the simple rules in [qualify](03-qualify-and-enrich.md).
2. Paste [the outreach prompt](prompts/outreach-drafter.md) into Claude with your notes.
3. Read the draft. Make sure every fact in it is true. **Then** decide to send.

✅ **You're done when** one row has: the web address, the date, a score, and your next step. That beats 200 names you never checked.

## What's inside

1. [First win](01-first-win.md): the steps above, with a full example.
2. [Find more, faster](02-collect-with-places.md): the optional Google tool and the included script, for when you're doing this every week.
3. [Score them](03-qualify-and-enrich.md): the scoring rules, so AI can't make stuff up.
4. [Reach out](04-outreach-and-law.md): a short message plan and the US rules to follow.
5. [Weekly routine](05-weekly-operations.md): keep it running in a few hours a week.

**Ready-to-use files:** the [score prompt](prompts/qualification-analyst.md), [outreach prompt](prompts/outreach-drafter.md), [tracker](templates/lead-tracker.csv), [research checklist](templates/research-checklist.md), and an optional [script](code/places_ids.py) with its [settings file](code/.env.example).

## Rules that keep you out of trouble

- Don't use "scraper" tools to copy Google Maps. Google doesn't allow it.
- Get business details from the business's own website, not from Google.
- In the US, sales emails must follow CAN-SPAM (your real name, address, and an easy way to opt out). Calls and texts have stricter rules (TCPA). [Reach out](04-outreach-and-law.md) explains both in plain words.
- The optional Google tool needs a billing account and can cost money. Set a budget alert first.

Stuck? Email support@milli-ai.com. If this doesn't help you in 7 days, you get every dollar back, and you keep the files.
