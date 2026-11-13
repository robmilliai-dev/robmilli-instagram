# Batch 1 copy swap (text only)

Scope: ONLY these files in artifacts/milliai/src: pages/home.tsx, pages/checkout.tsx, pages/starter-checkout.tsx, components/offer.tsx, lib/headline-variant.ts.

Rules:
- Text changes only. Do not change layout, logic, routes, tracking, test ids, prices, counts, dates, Black Friday behaviour, the 2-step email checkout, the TestedProof box, usePageSeo, or anything from other recent builds.
- Use the NEW text below word for word. Do not reword, shorten or "improve" it.
- Tokens in [SQUARE BRACKETS] are NOT literal text. Keep using the existing dynamic expression that is already in that spot:
  [PRICE] = current Standard price (money(p.current) / headlinePrice / money(currentPriceCents))
  [FUTURE] = future price (money(stack.futurePriceCents))
  [RISE_DATE] = p.date
  [EXTRA] = future price minus current price
  [TOTAL] = Standard total listed value
  [BONUS] = standardBonusCount
  [STD] = standardSystemCount / displayItemCount
  [PRO_ONLY] = stack.pro.proOnlyCount
  [BOT] = systemName / starterSystem.name
  [BOT_PRICE] = money(normalPriceCents)
  [N_GUIDES] = freeGuides count
- Keep existing fallbacks for when data is still loading.
- Where one paragraph becomes several, render them as separate <p> elements in the same container with the same styling.

## 1. Headline test (home.tsx + lib/headline-variant.ts + checkout.tsx)

Start a NEW 50/50 homepage headline test. Keep the variant values 'A' and 'B' and all tracking as is, but change the storage key from 'milli-hl' to 'milli-hl2' so every visitor is assigned fresh.

Variant A H1 (keep the <em> on the second sentence onward):
Most Viral AI Trading Bots Are Junk. <em>I Rip Them Apart, Rebuild the Few Worth Having, and Hand You 11 Finished Ones Tonight.</em>

Variant B H1:
Wall Street Has a Team Behind Every Trade. You Have a Hunch and a Chatbot That Says Yes to Everything. <em>Fix That Tonight for [PRICE].</em>

Remove the variant-B-only paragraph that starts "Its creator says it turned $150 into $279,053" (the new B headline makes no such claim). KEEP the line "I test viral AI trading bots so you don't have to." under the H1 for both variants.

checkout.tsx non-package H1, for BOTH variants:
You're One Click From 11 AI Trading Bots on Your Own Laptop.

## 2. home.tsx

2.1 Hero kicker (after the live dot):
Read this before your next trade. It takes four minutes and it may save you from a bad one.

2.2 Replace the single long hero-intro paragraph (starts "The AI Desk is 11 finished, tested AI trading bots") with these paragraphs:
Dear trader,
You've seen the posts. "This bot turned $150 into $279,053."
Maybe it did. Maybe it didn't. You can't check. Neither can I.
So here's what I do instead. I take the viral bots apart. I rebuild them. I test them. Then I hand you the finished ones.
That's the AI Desk. 11 finished AI trading bots that run on your own laptop.
One watches the market around the clock and pings your phone. One reads your chart and tells you what it sees. Six of them sit down like a research team and argue about your trade. One of the six, the Risk Manager, can kill the idea on the spot.
One command installs them. You can be live in about 60 minutes.
And not one of them ever places a trade. They watch, they dig, they argue. You make every call.
Last paragraph when the founding price is active: [PRICE] once, until [RISE_DATE]. After that it's [FUTURE] for the same files.
Last paragraph otherwise: [PRICE] once.

2.3 Hero primary button: Yes, send me my 11 bots for [PRICE] →
(secondary button unchanged)

2.4 hero-guarantee line:
My promise: follow the steps. If they aren't running on your machine in 7 days, email support@milli-ai.com and I'll set it up with you. Still not running? I send back every dollar. You keep the files anyway.

2.5 hero-side: "One payment. Yours for good." then the price, then (founding): It goes to [FUTURE] on [RISE_DATE]. Same files. The only thing that changes is what you pay.

2.6 Offer section eyebrow: Here's the whole deal, in plain sight.
Offer section H2: [TOTAL] of AI trading systems. [PRICE]. I'll explain why in a second.
Add one new paragraph directly under that H2 (above TestedProof), styled like section-lede:
Why so cheap? Simple. I'm new, and you have no reason to trust me yet. So I priced it so low that trying me costs less than one bad trade.
(When the founding price is active, append: On [RISE_DATE] the price goes to [FUTURE].)

2.7 Never-Blow-Up status box (keep the bold title):
<strong>The Never-Blow-Up-Your-Account Kit.</strong> Here's a secret most beginners learn the hard way. They don't go broke picking the wrong stock. They go broke betting too big on it. So before you click buy, you type in four numbers: your account size, your entry, your exit, and the most you're willing to lose. The calculator tells you exactly how much to buy. You also get a watchlist, a trade journal and a daily checklist. It all works offline.

2.8 Eyebrow "02 / The AI Side-Hustle Vault: ..." becomes: 02 / The bonus vault: [BONUS] more AI systems, $0 extra
Paragraph under the bonus chips:
You came for the trading bots. You leave with [BONUS] more AI systems for content, business, client work and coding. I could sell these one at a time. I'd rather you feel like you robbed me.

2.9 Eyebrow "03 / Two guarantees. All the risk is on us." becomes: 03 / Two guarantees. If anyone gets burned here, it's me.

2.10 "The ugly truth" section. manifesto-copy: You're trading against Wall Street. <span>Alone.</span>
manifesto-note paragraphs:
Think about how a hedge fund makes a trade. Nobody there acts on a hunch.
One person checks the big picture. One checks the numbers. One checks the chart. And one person's whole job is to say "no."
Now think about how you make a trade. You've got a chart, a gut feeling, and a chatbot that agrees with anything you type.
That's not a fair fight.
The AI Desk gives you the team. Six roles argue about your idea. The Risk Manager can veto it. Then you get a verdict in writing: PASS, WATCH or CANDIDATE. All before you risk a dollar.
Serial strip: "One chatbot that agrees with you" / "A team that argues back" (keep the icon)

2.11 Bonus vault section (id="inside"). Eyebrow: The bonus vault / included free
H2: I couldn't stop at the trading desk. So here are [BONUS] more.
Lede: Once your bots are running, put AI to work on the rest of your life. Content. A business idea. Client work. Coding. All [BONUS] are yours with the desk. Don't take my word for any of it. Chapter one of every system is free to read, right here, right now.

2.12 Pro-only section. H2: [PRO_ONLY] flagship systems you can only get one way.
Lede: These [PRO_ONLY] aren't sold on their own. They aren't in Standard. The only door in is Pro. With Pro you also get every system I ever build from here on, the day it comes out.

2.13 "What changes the day you buy". H3 unchanged. Paragraphs:
Typing "is NVDA a good buy?" into ChatGPT isn't research. It's asking a stranger at a bus stop for a stock tip.
Here's what you get instead. An alert that watches the market while you sleep. A chart read that tells you what's really on the chart and what it's only guessing. And a committee that goes looking for the reasons you're wrong.
Every word is already written for you. Follow the steps. Run it on your own stock. Read the verdict. Then you decide.

2.14 Dark panel. H2: Your next trade deserves a second opinion. I'm giving you six.
Lede: 11 bots, the Never-Blow-Up Kit and all [BONUS] bonuses for [PRICE], once. My promise: follow the steps. If it isn't running in 7 days, email support@milli-ai.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files.
Button: Send me my AI Desk →

2.15 How it works. H2: One stock. Sixty minutes. Your first written verdict.
Lede: Pick a stock you're itching to buy. Then do three things.
Step 1 h3 "Pick your stock." p: Chapter one is free, so you can see exactly what the bot does before you spend a cent.
Step 2 h3 "Copy. Paste. Run." p: The prompt, the template and a worked example are already written. You never face a blank page.
Step 3 h3 "Read the verdict. Make the call." p: PASS, WATCH or CANDIDATE, with the case against your idea in writing. Whether you trade, and how much, is up to you.

2.16 Guarantee section. Eyebrow: 06 / I take the risk.
H2: I take the risk. You keep the files.
(manifesto-copy unchanged.) Replace the "Our promise: ..." paragraph after <Guarantee/> with these paragraphs:
I'm not asking you to trust me. I'm asking you to test me.
Read chapter one free. Buy it. Follow the 60-minute setup. If it isn't running in 7 days, email me and I'll set it up with you. Still not running? Every dollar comes back, and you keep everything you downloaded.
And if any system doesn't do what its page says, tell me within 14 days. Full refund.
So either it works, and you have a research team for life for less than a nice dinner. Or it doesn't, and you got it all free.
Button: Ask me anything before you buy →

2.17 FAQ. Eyebrow: 07 / Every question I get
H2: Still looking for the catch? Fair. Here's every question I get.
Replace the 9 question/answer pairs, same order:
Q: "Can't I just write these prompts myself?"
A: You can. Block out a few weekends. Write six analyst roles, a veto rule, a sizing calculator, a journal, the alert code and the fix-it notes. Then test all of it. Or pay [PRICE] and run your first verdict tonight.
Q: What exactly am I buying?
A: 11 finished trading bots. Each one has tested code, a one-command install, phone alerts, setup steps, copy-paste prompts and a worked example. You also get the Never-Blow-Up Kit, [BONUS] bonus systems, every free guide and every setup path. Every file is listed on its page before you pay.
Q: Will I be billed again?
A: No. The AI Desk is one payment of [PRICE]. Desk Live is a separate monthly or annual membership. It's optional and you can cancel it any time.
Q: How fast do I get it?
A: The second your payment clears. There are no 40 videos to sit through. Open the files, follow the 60-minute setup, and you're running the same day.
Q: "I already have ChatGPT and Claude."
A: Good. You'll need one of them. Owning a hammer doesn't mean you have a house. The desk is the blueprint. It turns the AI you already pay for into a team with roles, rules and a veto.
Q: Do updates cost extra?
A: No. When an AI model changes and a chapter needs a rewrite, the new version lands in your account. Free.
Q: Will this make me money?
A: I won't promise that, and you should run from anyone who does. Here's what I can tell you. I tested the rules behind three of these bots on 43 markets, from 2010 to October 2026. These are hypothetical backtests, not real trades. The Desk 24/7 rules came out ahead on 36 of the 43. The gains were small. None of them beat simply holding the S&P 500. What they did well was keep the worst drops small, around 7% to 9%. The bots give you a process: watch, read the chart, argue the idea, size the bet. What you make or lose is down to you and the market. Educational only, not financial advice.
Q: "What if it doesn't work for me?"
A: Follow the steps. If it isn't running in 7 days, email support@milli-ai.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files. And if a system doesn't do what its page says, you have 14 days for a full refund.
Q: Does it buy or sell for me?
A: No. Not one of the 11 bots ever places a trade. They watch, research and alert. You place every order.

2.18 Final CTA. H2 unchanged. Replace the paragraph with these paragraphs:
You have two choices.
One. Close this page. Keep doing what you're doing. A chart, a hunch, and a chatbot that says yes to everything.
Two. Pay [PRICE] once. Have 11 bots and a six-analyst team on your laptop tonight. If they aren't running in 7 days, I set it up with you. Still not running? You get every dollar back and keep the files.
(Only when the founding price is active:) On [RISE_DATE] the same files cost [FUTURE]. Buy now, or explain to yourself later why you paid [EXTRA] more.
Button: Send me my AI Desk for [PRICE] →

2.19 Free guides capture. Eyebrow: 09 / Not ready? Then take one free.
H2: Steal one of my bots' playbooks. Free.
Loaded-state paragraph: All [N_GUIDES] free guides are the real prompts from the paid desk, not teasers. Pick one. Run it tonight. See for yourself.
LeadForm cta: Send me the free guides

2.20 MobileBuyBar label: Get my 11 bots, [PRICE] →

## 3. checkout.tsx (non-package / bundle view only; leave package view text alone)

3.1 Paragraph under the H1:
11 finished AI trading bots, with a one-command install and phone alerts. The Never-Blow-Up Kit, [BONUS] bonus systems, every free guide and every setup path come along. [PRICE], once. My promise: follow the steps. If they aren't running in 7 days, email support@milli-ai.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files.

3.2 Left column H2: I did the hard part. You just turn it on.
Paragraphs:
Every bot is built. Every bot is tested. All that's left is the easy part, and that part is yours.
Follow the 60-minute setup. Copy. Paste. Done. The bots start watching the market for you. Most run on a schedule and ping your phone when something is worth a look.
You make every call. You pay once. You keep it all.

3.3 Order rows:
"Subscription?" value: None. You pay once.
"Future systems" Standard value: Free updates to all [STD] for life. Every new system too, with Pro.
"Future systems" Pro value: Every system I ever build (Pro)
("Your protection" row unchanged.)

3.4 status-content box:
<strong>Don't let this turn into one more download you never open.</strong> The second you pay, open your files. Pick the stock that's on your mind right now. Follow the 60-minute setup. You'll have your first written verdict tonight.

3.5 Tier descriptions.
Standard: 11 trading bots, the Never-Blow-Up Kit, [BONUS] bonus systems, every free guide and every setup path. You pay once.
Pro: Everything in Standard. Plus the [PRO_ONLY] Pro-only flagships you can't get any other way. Plus every system I build after today, the day it comes out, for good.

3.6 Setup Fast-Track label:
<strong>Yes, get me running faster for $37.</strong> Add the step-by-step checklist for every bot, copy-paste fixes for any install error, and 30 days of email alerts whenever a bot gets an update. Built to get you live in under an hour.

3.7 Main button (non-package): Yes, send me my AI Desk for [displayed price] →  (Pro: Yes, send me AI Desk Pro for [displayed price] →)

3.8 mini-faq:
Is this a subscription? No. You pay once. Desk Live is a separate monthly or annual membership, and it's optional.
What if it doesn't work? Follow the steps. If it isn't running in 7 days, email support@milli-ai.com and I'll set it up with you. Still not running? You get every dollar back, and you keep the files.
How fast do I get it? The second your payment clears.

3.9 GuestCheckoutSuccess H1: You're in. Your AI Desk is ready.

## 4. components/offer.tsx

4.1 Guarantee component, first block (keep title and email link):
My promise: follow the steps. If it isn't running in 7 days, email {SUPPORT_EMAIL} and I'll set it up with you. Still not running? You get every dollar back, and you keep the files.
Second block: change "tell us" to "tell me". Rest unchanged.

4.2 PriceLine founding text: change "The only difference is whether you were early or late." to "The only thing that changes is what you pay."

4.3 StarterLeadOffer.
Eyebrow: Wait. Before you start building...
H2 with a bot: You could build the [BOT] yourself this weekend. Or take the finished one for $7.
H2 without a bot: Most traders don't blow up on a bad pick. They blow up on a bet that was too big.

4.4 StarterOfferDetails WITH a bot. Replace the first paragraph with these paragraphs:
You just saw how the [BOT] works. You can build it from the guide. It's all in there.
Or you can take the lazy way.
I already built it. I already tested it. It's sitting here finished.
(only when a normal price is known:) On its own it sells for [BOT_PRICE].
Today it's $7.
Why so cheap? Because I'd rather you watch one of my bots run on your own laptop than take my word for anything.
Bullets:
The finished [BOT], tested and ready to run
Setup steps from start to finish. Copy, paste, done.
A bonus: the Never-Blow-Up Calculator, so one bad trade can't sink you
Help if you get stuck. Email support@milli-ai.com and I'll get you running.
Closing paragraph: $7. One time. If it doesn't do what I say, email me within 14 days and I'll send your $7 back.

4.5 StarterOfferDetails WITHOUT a bot. Paragraphs:
The Never-Blow-Up Calculator fixes that in two minutes.
Type in your account size and where your stop goes. It tells you exactly how many shares to buy. Now one bad trade can't sink you. It works for stocks, crypto and futures.
Bullets:
The Never-Blow-Up Calculator. It's a spreadsheet, so there's nothing to install.
The "Rules That Keep You Alive" cheat sheet: how much to risk, and when to stop for the day
The AI Size-Check prompt: Claude checks your plan before you click buy
Help if you get stuck. Email support@milli-ai.com.
Closing paragraph: $7. One time. If it doesn't do what I say, you get a full refund within 14 days.

4.6 Buttons in StarterLeadOffer: "Yes, give me the finished [BOT] for $7 →" and "Yes, I want it for $7 →"

## 5. starter-checkout.tsx

H1 with a bot: The finished [BOT] is yours for $7.
H1 without a bot: Most traders don't blow up on a bad pick. They blow up on a bet that was too big.
Buttons: "Yes, give me the finished [BOT] for $7 →" and "Yes, I want it for $7 →"

## 6. After the change

Run the type check and the existing tests; update any test that asserts the old wording so it asserts the new wording. Do not publish. Reply with: the list of files changed, test results, and the exact new text of both homepage H1 variants as they now appear in home.tsx.
