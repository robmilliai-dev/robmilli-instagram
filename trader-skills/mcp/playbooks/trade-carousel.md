---
id: trade-carousel
title: The Trade Carousel skill
category: content
summary: Carousel about a trade or backtest: giant-number hook slide, content slides, keyword CTA, caption. HTML to 1080x1350 PNGs plus a PDF DM asset. Dark and light.
---

# TRADE CAROUSEL

A carousel is a 7-second sales letter. Slide 1 is the headline, the last slide is the ask, everything between earns the swipe.

## SETUP (once)

```bash
npm i playwright && npx playwright install chromium   # or set CHROME_PATH to your Chrome
```

## WORKFLOW

1. **Get the proof.** One real number or result: a backtest, `/account-stats`, a verified third-party claim (credited). No proof, ask for one before writing.
2. **Write slide 1 (the hook) first.** One giant number + under 10 words that make the number mean something.
   - "2 trades in 6 years. That's not a strategy."
   - "27 wins out of 33. One free indicator."
   - "$150 → $279k. Their bot. I rebuilt it." (credit, and never phrase it as a promise)
3. **Outline the middle (3 to 6 slides).** Each slide = one idea, max 25 words, one visual (stat card, list, chart screenshot, before/after). Orders that work: Claim → Test → Result → Catch → Fix. Or: Mistake → Cost → Rule → Tool.
4. **One slide is the honest one.** Worst drop, trade count, or what didn't work. Non-negotiable.
5. **Last slide = CTA.** "Comment <KEYWORD> and I'll DM you <exact thing>." Keyword in a big colored box.
6. **Copy `templates/carousel.html`**, replace the sections, keep the classes. Use `class="light"` on `<body>` for the light style. Mix styles across posts: don't run every post on one template.
7. **Render:**
   ```bash
   CHROME_PATH=/path/to/chrome node scripts/render.mjs my-carousel.html --out out/my-carousel --pdf
   ```
   You get `slide-01.png` … and `carousel.pdf`.
8. **Check every slide at phone size** (open a PNG at 30% zoom). If you can't read it, the font is too small. Body text minimum 40px.
9. **Write the caption:** first line restates the hook another way; 3 short lines; keyword CTA; honesty line; 3 to 5 hashtags.

## DESIGN RULES

- One giant number on slide 1, 250px+. It's the thumbnail.
- Max 2 colors plus neutrals. Green for gains, red only for losses/drawdown.
- 88px side margins. Nothing important in the bottom 120px (the app covers it).
- Handle and page number on every slide (`.foot`).
- Real charts beat drawn ones. Screenshot TradingView, crop tight, drop it in an `<img>`.

## THE DM ASSET

The PDF doubles as the lead magnet: the same slides plus one extra "How to do it yourself" slide with the steps. Send it when someone comments the keyword.

## HARD RULES

- **Every number is real** and matches its source. Never round in your favor.
- **No "giveaway", no "$X into $Y" promises** in slides or caption (Instagram link restrictions).
- Credit third-party results by name. Never present them as your own.
- Last slide footer: "Educational only. Not financial advice."

## If you can't run scripts here
This playbook uses helper scripts. In a chat app, do the steps by hand with the user (ask them to paste data), or point them to the downloadable skill at milli-ai.com/free (keyword CAROUSEL).
