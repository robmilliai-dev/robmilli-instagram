# Start here: one page that shows how your business is really doing

**What this does:** You drop in the files you already have (sales, leads, expenses). You get one clear page that shows revenue, orders, new customers, expenses, profit and leads, compared to last week or last month. With charts. And a short AI summary of what changed, if you want it.

No more waiting months for your accountant to tell you how it's going.

**What you'll have in 30 minutes:**

- ✅ A sample dashboard running in 5 minutes
- ✅ Your own last 6 months of sales on one page, in your browser
- ✅ (Later) It rebuilt and emailed to you every Monday, automatically

**What you need:** Python (free, often already on Mac) and a sales export (CSV) from your shop or payment tool. No database, no subscription, no developer.

## Your 30-minute first win

Open [Chapter 01](01-first-dashboard-in-30-minutes.md). It runs the dashboard on the included sample data first, so you see it work. Then you swap in your own sales file.

✅ **You're done when** a dashboard of your own sales is open in your browser.

## The order you'll work in

| Step | Chapter | What you leave with |
|---|---|---|
| 1 | [01 First dashboard in 30 minutes](01-first-dashboard-in-30-minutes.md) | The sample dashboard, then one built from your real sales |
| 2 | [02 Pick the numbers that matter](02-pick-the-numbers-that-matter.md) | Five to eight numbers you'll actually act on, and targets |
| 3 | [03 Get your data in](03-get-your-data-in.md) | Clean exports from your sales, lead and expense tools |
| 4 | [04 Set up your config](04-set-up-your-config.md) | A settings file that maps your columns, period and targets |
| 5 | [05 Automate the weekly update](05-automate-the-weekly-update.md) | The dashboard rebuilt and emailed to you on a schedule |
| 6 | [06 The weekly review with AI](06-the-weekly-review-with-ai.md) | A 20-minute weekly review that ends in decisions |
| 7 | [07 Troubleshooting](07-troubleshooting.md) | Fixes for wrong numbers, date problems and errors |

You keep [the dashboard script](code/dashboard.py), [the example config](code/dashboard-config.json), [the sample data](code/sample-data/sales.csv), [the prompts](prompts/dashboard-prompts.md), [the KPI definitions sheet](templates/kpi-definitions.md) and [the weekly review template](templates/weekly-review.md).

## What it costs

| Item | Cost | Notes |
|---|---|---|
| Python 3.9+ | Free | python.org; often already on Mac and Linux |
| Your existing tools' CSV exports | Free | Almost every sales, CRM and accounting tool can export CSV |
| AI summary (optional) | Usually a fraction of a cent per run | Claude API key; the dashboard works fully without it |
| Emailing the dashboard (optional) | Free | Uses your existing email account |

## What this is and isn't

It is a clear weekly or monthly picture of your business from the data you have, so you notice changes early and make decisions with numbers instead of gut feel.

It isn't accounting software, and the "profit" it shows is simply revenue minus the expenses in your file, before tax and any costs you didn't include. Use your accountant's figures for tax and official reports. The dashboard is only as accurate as the exports you give it; [chapter 03](03-get-your-data-in.md) shows how to keep them clean.

Your data stays on your computer. The script reads your files and writes an HTML file next to them. The only time anything leaves your computer is if you switch on the AI summary (which sends the summary numbers, not your customer list, to the Claude API) or email the dashboard to yourself.

Start with [chapter 01](01-first-dashboard-in-30-minutes.md).

Stuck? Email support@milli-ai.com. If it doesn't work for you in 7 days, you get every dollar back, and you keep the files.
