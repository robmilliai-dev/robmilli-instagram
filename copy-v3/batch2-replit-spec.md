# Batch 2 copy swap (text only)

Scope: ONLY these files in artifacts/milliai/src: pages/custom-build.tsx (the CustomBuildPage sales page only, not the intake page), pages/desk-live.tsx (DeskLiveSalesPage), pages/partners.tsx (PartnersPage only, not the dashboard or owner section), pages/free.tsx, and the BlackFridayStack component in components/offer.tsx.

Rules:
- Text changes only. Do not change layout, logic, routes, tracking, test ids, prices, counts, dates, Black Friday timing or counters, checkout/email gates, SEO tags, or anything from other recent builds.
- Use the NEW text below word for word. Do not reword, shorten or "improve" it.
- Tokens in [SQUARE BRACKETS] are NOT literal text. Keep using the existing dynamic expression already in that spot:
  [SLOTS_LINE] = the existing availability text, [N_GUIDES] = guides count, [BONUS] = bonusCount, [REMAINING_LINE] = the existing "X of 5 free custom bots left / All 5 claimed" text, [COUNTDOWN] = formatPriceCountdown(countdown).
- Where one paragraph becomes several, render them as separate <p> elements in the same container with the same styling.
- Keep every legal line that is not listed here exactly as it is (renewal note, "Never promises profits. Educational only, not financial advice.", the partner rules list, the custom page fine print list).

## 1. custom-build.tsx (CustomBuildPage)

Eyebrow: DONE-FOR-YOU CUSTOM BOTS · ONLY 5 A MONTH
H1: Tell Me Your Trading Idea in Plain English. In 7 Days I Hand You a Working AI Bot That Does It. If It Doesn't Run, You Don't Pay a Cent.

Replace the custom-subhead paragraph with these paragraphs (same class on each):
You've had the idea for months.
"If only something watched the charts and pinged me when..."
You know exactly how that sentence ends. You just can't code it.
So don't. Tell me what you want in plain English. I write the code. I test it. I pack it up so one command installs it. Then I hand it over.
You never touch a line of code.

Buy buttons (both): Claim 1 of 5 build slots, $997 →   (keep the "Opening secure checkout…" pending text)

Guarantee box: <strong>The Runs-or-Refund Guarantee.</strong> Your bot lands within 7 days of your order form and runs on your machine. If it doesn't, you get every cent back. All the risk is mine.

Problem section eyebrow: WHY YOUR BOT IS STILL JUST AN IDEA (unchanged)
Problem H2: There are three ways to get a custom bot. All three stink.
problemPoints (3 items, in order):
Hire a freelancer. Quotes for a custom trading bot often run $2,000 to $10,000. It takes weeks. And nobody promises it will ever work.
Learn to code. That's months of tutorials before your first alert fires.
Ask ChatGPT. You paste the code. It errors. You paste the error back. It breaks something else. Sound familiar?
Problem close line: Meanwhile, you're still staring at charts by hand.

Value list item labels (keep the dollar values and the "all 50 systems" count as they are now):
Your custom bot, built to your exact rules
One-command install. Copy, paste, running in minutes.
Tested before you ever see it, with a written test report
2 rounds of changes within 14 days of delivery
30 days of direct email support
Free bonus: AI Desk Pro, all 50 systems
Total line: Total value: $3,985. You pay $997, once. There's no subscription. You own the code for good.

Comparison third row: Me: $997 · 7 days · it runs or you get a refund

Timeline (4 items):
Day 0: You buy. It takes 2 minutes.
Day 0: You tell me what you want in plain English. It takes 5 minutes.
Days 1 to 6: I build it and test it.
Day 7: Your bot, the installer and the guide land in your inbox.

"Why only 5 a month" paragraph: Because I build and test every bot to order, and I won't rush yours. When this month's 5 slots are gone, they're gone. The next opening is the 1st.
(The fine print list stays as it is.)

FAQ answers (questions unchanged):
Do I need to code? -> No. If you can copy and paste, you can install it.
What do I need? -> A computer, and the accounts your bot connects to. I'll tell you exactly which ones before I build.
What if it doesn't work? -> Then you don't pay. You get a full refund, with no hoops.
Is this financial advice? -> No. These are research and alert tools. You make every decision.

Bottom CTA H2: Only two things can happen. Your bot runs, or you get your money back.
Bottom line: Every week you wait is one more week of watching charts by hand.

Waitlist success text: You're on the waitlist. I'll email you when a build slot opens.

## 2. desk-live.tsx (DeskLiveSalesPage)

H1: One New Finished Trading Bot Lands in Your Account Every Month. $29. Cancel in One Click.

Replace the live-intro paragraph with these paragraphs (same class):
Here's the deal, and it's a simple one.
Every month I build a new trading bot. I test it. I finish it. Then I drop it in your account, ready to run.
Every month I also take one real stock and run it past the six-analyst committee. You get the whole argument in writing: what the analysts liked, what they hated, and where they disagreed.
You get a bonus bot the day you join. And you can quit in one click, any time.

Benefit ticks (4):
A new finished bot every month
A six-analyst breakdown of a real stock every month
A bonus bot on day one
Cancel in one click

Buy button idle text: Start my membership

Middle section H2: One useful drop.<br/><em>Every month.</em>
Middle paragraphs (replace the two paragraphs, keep the member workspace link after them):
The day you join, you get the index dip-buying bot for SPY, QQQ and DIA.
November's drop is a prop-challenge practice bot with guard rails built in. It comes with a full six-analyst breakdown of NVDA.
Six roles look at the same stock. They argue. They tell you where they disagree. You end up with research you can read and judge for yourself. Nobody is telling you what the market will do next.

Bottom H2: A new bot every month<br/>for less than a dollar a day.
Bottom button: Start {selectedPlan === 'annual' ? 'annual' : 'monthly'} (i.e. "Start monthly" / "Start annual")

## 3. partners.tsx (PartnersPage only)

H1: I'll Pay You $80 Every Time One of Your Followers Buys.

Replace the first paragraph under the H1 with these paragraphs (same style):
This is simple.
You get a link. You share it. Somebody buys through it. You keep 40%.
On the $199 AI Desk, that's $79.60 to you. You also earn 40% on Pro and on every other product people buy by themselves, right down to the $7 starter. The only thing left out is the $997 custom build.
You don't even have to make the content. I've already made the Reels, the posts, the captions and the Story texts. Your link is already inside them. Download, post, done.

Second paragraph (keep the condition): And your own AI Desk unlocks free once your link brings in its first sale. / And your own AI Desk unlocks free once your link brings in its first real lead.

Tracking box title: How you get paid
Tracking box text: Your link remembers a visitor for 60 days. If they buy in that time, the sale is yours. I pay out 14 days after each sale, as long as it wasn't refunded or disputed.

Form heading: Get your link in two minutes
(Button text unchanged. Partner rules unchanged.)

## 4. free.tsx

FreeIndex:
H1: I Tested the Viral Trading Bots.<br/>Here's How Each One Really Works. Free.
(Keep the eyebrow and the "I test viral AI trading bots so you don't have to." line.)
Loaded-state paragraph: These aren't teasers. Every one of these [N_GUIDES] guides is a real system from the paid desk, with the full prompts and the exact steps. Pick the one that fits you. Read it here or have it emailed. It costs nothing.
Card button: Run this one free → (unchanged)

FreeGuidePage sign-up panel:
Eyebrow: Your complete first run / $0 (unchanged)
H2: Tell me where to send it and you can be running this in 15 minutes.
LeadForm here: pass finePrint = You get the full guide by email. Then a few short emails from me on what to do next. One click and they stop. The guide is yours either way.
Delivered status line: Done. It's in your inbox. Do yourself a favor and start step one right now, before life gets in the way.

FreeGuidePage offer card (after delivery):
Eyebrow: Everything done for you / one payment (unchanged)
H2: You just built one by hand. Want the other 10, already finished?
Replace the single paragraph with these paragraphs:
You've now seen how one of these works. Good. That was the hard way.
Here's the easy way. I built all 11 bots. I tested them. I wrote every step.
You follow a 60-minute setup. Copy. Paste. Done. Most of them run on a schedule and ping your phone when something is worth a look.
You make every call.
You also get [BONUS] AI business systems, the Never-Blow-Up Kit, and every new bot I release for the next 12 months.
Button: Yes, give me all 11 finished bots →

## 5. components/offer.tsx: BlackFridayStack only

Eyebrow: Black Friday: everything I sell, $249
First line: <strong>AI Desk Pro</strong> (normally $497). Every system I sell, plus every system I ever build.
List items:
3 months of Desk Live. A new finished bot every month.
Setup Fast-Track ($37). The checklist and fix-it prompts that get you running in under an hour. Free.
First 5 buyers only: a custom AI bot, built for you ($997). [REMAINING_LINE]
Running in 7 days, or I set it up with you. Still not running? Full refund, and you keep the files.
Counter paragraph unchanged ([REMAINING_LINE]).
Countdown line: Ends Monday at midnight Eastern. I won't extend it. [COUNTDOWN] left.

## 6. After the change

Run the type check and the existing tests; update any test that asserts old wording so it asserts the new wording. Do not publish. Reply with: files changed, test results, and the exact new H1 of the custom, Desk Live, partners and free index pages as they now appear.
