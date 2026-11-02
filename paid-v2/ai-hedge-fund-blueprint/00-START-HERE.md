# Start here: your AI Hedge Fund Committee

**What you'll have in about 30 minutes:** six AI experts in one Claude Project who argue about any stock before you buy it. You get the strongest case **against** the idea, a clear call (**PASS**, **WATCH** or **CANDIDATE**), and a note of what would change it.

Big funds never let one person buy alone. Now you won't either.

> Educational only, not financial advice. Six AI roles are still one AI, so check every fact yourself.

## What you need

- A [Claude](https://claude.ai/) account. **Projects** make it easier, but a normal chat works too.
- One stock you're thinking about.
- 30 minutes.

No code. No installs.

## Step 1: Build the committee (5 minutes)

1. In Claude, click **Projects → Create project**. Name it **Investment Committee**.
2. Open [prompts/committee-charter.md](prompts/committee-charter.md). Copy the whole prompt inside the grey box.
3. Paste it into the Project's **instructions** and save.

That's your committee. It remembers the rules every time you open a new chat in this Project.

**No Projects on your plan?** Paste the charter as the first message of a new chat each time.

## Step 2: Find one real fact (10 minutes)

The committee is only as good as the facts you give it.

1. Go to [SEC EDGAR](https://www.sec.gov/edgar/search/) and search for the company.
2. Open its latest **10-Q** (quarterly report) or **10-K** (yearly report).
3. Copy 1 or 2 numbers you can see on the page, like revenue or debt. Write down the date of the report and the page.

Example: *"MSFT 10-Q filed Oct 2026, page 4: revenue up 15% from last year."*

## Step 3: Run the committee (10 minutes)

Open a **new chat inside the Project** and send this, filled in:

```text
Stock: [TICKER, e.g. MSFT]
Today's date: [DATE]
My idea in one line: [e.g. "Cloud growth is faster than people expect"]
Fact 1: [number, report name, date, page]
Fact 2: [number, report name, date, page, or "none"]
Price chart: [attach a screenshot, or "none"]

Run the full committee.
```

Want more detail and more fields? Use the full round prompt in [prompts/six-role-round.md](prompts/six-role-round.md).

## Step 4: Read it the smart way (5 minutes)

1. **Read the Devil's Advocate first.** Can you answer its argument? If not, your call is WATCH.
2. **Check the numbers.** Every number should come from your facts. If one didn't, reply: *"Which of my facts supports that? If none, remove it."*
3. **Look at the PM's call.** PASS or WATCH is the most common answer. That's the committee saving you from a weak idea.

## Step 5: Write it down (2 minutes)

Copy the call into the [journal](templates/trading-journal.md): the date, the call, the #1 reason against, and a date to look again.

## ✅ You're live when

You have one saved committee memo with all six roles, a call, the strongest case against it, and a date to review it.

## Make it a habit

- **Every week:** run your top idea through the committee. [Chapter 05](05-weekly-meeting-and-review.md) gives you a 20-minute weekly routine.
- **Before you buy anything:** use the [sizing worksheet](templates/position-sizing-worksheet.md) so one loss can't hurt you. [Chapter 04](04-position-sizing-and-risk.md) explains it simply.
- **Want a sharper committee?** [Chapter 02](02-project-setup-and-evidence.md) shows how to give it better evidence.

## If something goes wrong

| What you see | What to do |
|---|---|
| No Projects option | Paste the charter as the first message of a normal chat each time. |
| All six roles agree | Give it more real facts, and ask the Devil's Advocate to "try harder." |
| It quotes a price or number you didn't give it | Ask where it came from. If it can't say, delete it. |
| It won't size a position | Correct. It needs a price, a stop and your account size first. Use the [worksheet](templates/position-sizing-worksheet.md). |
| Anything else | See [chapter 06](06-troubleshooting-and-sources.md). |

**Not working for you after 7 days?** Email support@milli-ai.com. You get every dollar back, and you keep the files.
