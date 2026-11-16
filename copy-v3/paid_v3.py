#!/usr/bin/env python3
"""Add a short I-voice opener under the H1 of each paid 00-START-HERE.md, and a plain sign-off.
Nothing else in the file changes: steps, commands, tables, prompts and safety notes stay as they are."""
import sys, pathlib, re

D = pathlib.Path(sys.argv[1])

O = {
"agency-ops-in-a-box": "Most agency owners don't have a client problem. They have a chaos problem. Files go missing. Reports get written from memory at 11pm. Clients ask \"where are we?\" and you don't know either.\n\nThis fixes that. Start with one client today. You'll feel the difference by Friday.",
"ai-agent-failure-field-guide": "Read this one before you trust an AI agent with anything that matters.\n\nIt takes 30 minutes. After that, you'll never take \"Done!\" at face value again.",
"ai-app-builder": "You've had an app idea for a while. Maybe a booking tool. Maybe a calculator for your customers. You never built it because you can't code.\n\nGood news. You don't need to anymore. Do the first win below and you'll have a real link on your phone in 30 minutes.",
"ai-content-machine": "Staring at a blank screen is the worst part of posting. So let's skip it.\n\nYou bring one real idea. This turns it into six posts. Do the 2-minute test first and you'll see what I mean.",
"ai-creator-os": "Most creators work hard and still feel stuck. Not because they're bad. Because nobody handed them a plan.\n\nThis is the plan. Do the 30-minute first win today and you'll know exactly what to post for the next 4 weeks.",
"ai-employee-pack": "Thanks for grabbing this. Here's my advice: don't hire all 8 at once.\n\nHire one today. Give it one real job. Once it's earning its keep, add the next.",
"ai-executive-council": "Big companies never make a big decision alone. They put it in front of a room full of people who poke holes in it.\n\nNow you have that room. Bring the decision that's been keeping you up at night.",
"ai-hedge-fund-blueprint": "You've got the committee now. Six experts who argue about a stock before you spend a dollar on it.\n\nExpect a lot of PASS and WATCH. That's not the system failing. That's the system saving you money.",
"ai-local-marketing-kit": "When someone near you searches for what you do, one of two things happens. They find you, or they find the other guy.\n\nThis kit makes sure it's you. The first win takes 30 minutes, and you can do most of it from your phone.",
"ai-money-systems-vault": "There are a hundred ways to make money with AI. Trying all of them is how people end up with nothing.\n\nSo pick one. This vault helps you choose the right one in 30 minutes, with the real math in front of you.",
"ai-receptionist-in-a-box": "Every missed call is a customer calling your competitor next. That's not a guess. That's how people shop.\n\nThis puts an AI on your phone that picks up when you can't. You'll test it yourself before you spend a cent on a phone number.",
"ai-saas-builder-os": "Most people build the app first and look for buyers second. That's backwards, and it's why most apps make $0.\n\nThis flips it. You prove people will pay before you build a thing.",
"ai-sales-pack": "The best salespeople aren't smoother than you. They're more prepared.\n\nThis kit does your homework before every call. Use it on the next real call you have coming up.",
"ai-startup-in-a-box": "Most business ideas die after months of work and money. Yours doesn't have to.\n\nGive it 7 days. By the end, you'll know whether to keep going, change it or walk away, and you won't have built a thing.",
"ai-trader-starter-prompt": "This is the simplest thing in the whole desk, and that's the point. Start here if you're new.\n\nIt doesn't trade. It thinks with you, and it keeps your notes honest.",
"ai-trading-desk-247": "You've got it. Now let's get it running.\n\nFollow the steps in order and don't skip step 3. That's where you check it's reading real prices.",
"ai-youtube-studio": "Most YouTube videos fail before anyone hits record. The idea was weak, or the title lied.\n\nThis is your writers' room. Run the 3-minute idea test first. It'll save you a whole weekend.",
"billion-dollar-solo-operator-playbook": "You don't need more hours. You need to stop doing the same work twice.\n\nThis finds the step that wastes the most of your time and fixes it first. One step. Today.",
"business-dashboard-kit": "Most small business owners find out how last month went... three months later.\n\nThis gives you one page that shows it right now. The sample runs in 5 minutes.",
"business-prompt-vault": "Generic prompts give you generic answers. That's the problem with most prompt packs.\n\nThis one is different, because of one sheet you fill in once. Do that first. Every prompt after it gets better.",
"carousel-that-converts-system": "Most \"tips\" carousels get a scroll and nothing else.\n\nThis builds a carousel around one real question your customers ask, with one clear next step at the end. Your first one takes 30 minutes.",
"claude-code-business-builder": "Claude Code sounds like it's for programmers. It isn't. Not the way you'll use it.\n\nYou're going to use it to run the boring parts of your business. Your first proposal will be drafted in about 30 minutes.",
"claude-code-command-pack": "You type the same long requests to Claude Code every day. Stop.\n\nOne short command, the same careful result every time. Try the first one in 5 minutes.",
"claude-code-skills-vault": "Telling an AI how to do the same job over and over gets old fast.\n\nA skill tells it once. You're getting 35 of them. Install 3 today and see how it feels.",
"claude-code-zero-to-first-deploy": "In the next 30 minutes, you'll have a real website with a real link you can text to anyone.\n\nNo coding. No domain to buy. Just follow the steps in order.",
"cold-outreach-kit": "Cold email works. Spam doesn't. The difference is about ten minutes of homework per email.\n\nThis kit shows you the homework. Send your first 10 today, from your normal inbox.",
"creator-prompt-library": "\"What do I post today?\" If you ask yourself that every morning, this is for you.\n\nSet up your voice first. It takes 3 minutes, and it's why the rest won't sound like a robot.",
"creator-storefront-kit": "Most creators have something worth selling. What stops them is the boring part: where does the money go, and how does the file get delivered?\n\nThis handles the boring part. Once it's set up, a sale can come in while you sleep.",
"free-bloomberg-terminal-setup": "A Bloomberg Terminal costs about $30,000 a year. You're about to get the useful part for free.\n\nFollow the steps in order, and check one number yourself at the end. That's how you know it's real.",
"github-to-income-repo-shortlist": "Thousands of businesses need free software set up. They don't know how. With AI's help, you do.\n\nThis gives you 10 tools and the buyers for each. Pick one today.",
"industry-blueprint-collection": "AI can help almost any small business. The trick is knowing exactly where to start.\n\nThis tells you, for 10 kinds of business. Pick one job and set it up this week.",
"local-lead-finder": "Buying a list of 10,000 leads feels productive. It isn't. Three businesses with a real problem you can fix beat all of them.\n\nThat's what you'll find in the next 30 minutes.",
"mcp-quickstart-kit": "MCP sounds technical. It's not, once you've seen it work.\n\nYou'll do it in a safe test folder, so nothing important can break. Thirty minutes.",
"missed-call-recovery-system": "A customer calls. Nobody picks up. They call the next business on the list.\n\nThis stops that. One friendly text goes out seconds after every missed call. Test it on your own phone first.",
"one-person-ai-business-roadmap": "You don't need a big idea. You need one offer people already want, and a plan to get it in front of them.\n\nThis is 10 weeks, one step at a time. Start with step 1 today.",
"repo-to-revenue-shortlist": "Free software on GitHub is one of the best-kept secrets in business. Lots of people would pay you to set it up.\n\nBut some projects are duds. This check takes 30 minutes and saves you a wasted weekend.",
"tradingview-claude-chart-analyst": "You've got it. Start with Part 1. It takes 10 minutes and needs no code.\n\nOnce Claude is reading your charts the way you like, Part 2 puts it on your phone.",
"viral-reel-builder": "Nobody can promise you a viral video. Anyone who does is lying.\n\nWhat I can do is take away the two things that stop most people: editing time, and not knowing what makes someone stop scrolling.",
}

SIGNOFF = "\n\n---\n\nStuck on a step? Email support@milli-ai.com and tell me which one. I'll help you get it running.\n\nRob\n"

def apply(slug):
    p = D / slug / "00-START-HERE.md"
    s = p.read_text()
    if "Stuck on a step? Email support@milli-ai.com" in s:
        return "skip"
    m = re.match(r"(# [^\n]*\n\n)", s)
    assert m, slug
    s = m.group(1) + O[slug] + "\n\n" + s[m.end():]
    s = s.rstrip("\n") + SIGNOFF
    p.write_text(s)
    return "ok"

dirs = sorted(x.name for x in D.iterdir() if x.is_dir())
missing = [d for d in dirs if d not in O]
assert not missing, missing
print({d: apply(d) for d in dirs})
