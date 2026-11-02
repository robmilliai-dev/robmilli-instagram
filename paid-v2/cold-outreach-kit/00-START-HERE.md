# Start here: cold emails that get replies (and don't land in spam)

**What this does:** You email businesses that don't know you yet, and they write back. You get a list of the right people, emails built to get replies, a safe sending setup that protects your main inbox, and a tool that sends a 3-email follow-up for you.

For freelancers, agencies, consultants and B2B services. Not for mass spam.

**What you'll have in 30 minutes:**

- ✅ 10 real emails sent, from your normal inbox, to 10 businesses you picked on purpose
- ✅ A first line in each one that could only be for that business
- ✅ All 10 tracked, so you follow up on day 3

**What you need:** Your normal email and a free [Claude](https://claude.ai) account. No tools, no new domain yet.

## Your 30-minute first win

Open [Chapter 01](01-first-10-emails-in-30-minutes.md). Use [the personal first-line prompt](prompts/outreach-prompts.md) and the 3-part email from [chapter 04](04-write-emails-that-get-replies.md). Log each one in [the leads file](templates/leads.csv).

10 emails you write by hand teach you more than 1,000 automatic ones. Only automate once you know what gets replies.

## The order you'll work in

| Step | Chapter | What you leave with |
|---|---|---|
| 1 | [01 First 10 emails in 30 minutes](01-first-10-emails-in-30-minutes.md) | Ten real emails sent, tracked for follow-up |
| 2 | [02 Rules and deliverability](02-rules-and-deliverability.md) | A legal footer, a separate sending domain, DNS records and a safe ramp-up |
| 3 | [03 Build the list](03-build-the-list.md) | 50–200 well-chosen prospects with verified emails |
| 4 | [04 Write emails that get replies](04-write-emails-that-get-replies.md) | A tested three-email sequence |
| 5 | [05 Run the machine](05-run-the-machine.md) | The outreach tool personalizing, previewing and sending on a daily schedule |
| 6 | [06 Replies to booked calls](06-replies-to-booked-calls.md) | Reply handling, call booking, and the numbers to watch |
| 7 | [07 Troubleshooting](07-troubleshooting.md) | Fixes for spam folders, bounces, zero replies and angry replies |

You keep [the prompts](prompts/outreach-prompts.md), [the leads file](templates/leads.csv), [the outreach tool](code/outreach.py), [the email template](code/email-template.txt) and [the config file](code/.env.example).

## When to use cold email, and when not to

Use it when:

- You can name a specific type of business with a specific problem you solve.
- The value of one new client is high enough to justify personal, researched emails (usually anything above a few hundred dollars).
- Your offer can be explained in two sentences.

Don't use it when:

- You're selling to consumers at home addresses. Rules for emailing individuals are much stricter in most countries (often consent-based), and it rarely works anyway.
- You're targeting a country with consent-first rules for business email (Canada's anti-spam law is the common example) without checking how they apply to you.
- You can't say who you're emailing or why them. "Everyone with a website" is not a list.
- Your offer is regulated (financial advice, health claims) or depends on guarantees you can't keep.

## What it costs

| Item | Typical cost | Notes |
|---|---|---|
| A separate sending domain | ~$10–20/year | Protects your main domain's reputation |
| A mailbox on that domain | ~$6–8/user/month | Google Workspace or Microsoft 365; check current prices |
| Email verification | Free tiers to a few dollars per hundred | For checking addresses before sending |
| Claude API for personalization | Usually cents per hundred leads | Optional; the tool also runs offline |
| Python | Free | Python 3.9 or newer |

Nothing here requires a paid "outreach platform". Those can help at higher volume, and [chapter 05](05-run-the-machine.md) says when one is worth it.

## Four rules the whole kit runs on

1. **Relevance before volume.** Thirty emails to the right people beat three thousand to the wrong ones, on replies and on deliverability.
2. **Every email is honest.** Real name, real company, a subject line that matches the body, a postal address, and an easy way to say no. These are legal requirements in many places, not just good manners.
3. **Stop when they say stop.** Anyone who asks not to be contacted goes on the suppression list the same day and never hears from you again.
4. **Protect the domain.** Send from a separate domain, ramp up slowly, keep bounces and complaints near zero. A burned main domain hurts your regular business email too.

This kit explains the rules in plain language, but it isn't legal advice. If you send at volume or into several countries, have someone qualified check your setup.

Start with [chapter 01](01-first-10-emails-in-30-minutes.md).

Stuck? Email support@milli-ai.com. If it doesn't work for you in 7 days, you get every dollar back, and you keep the files.
