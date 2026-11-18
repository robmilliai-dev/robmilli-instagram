---
name: saved-posts-sorter
description: Turn the hundreds of trading reels you saved on Instagram or TikTok into a ranked shortlist of strategies actually worth testing. Parses your data export into a sheet, pulls the claim and the exact rule out of each post, scores how testable it is, and ranks them. The top ones go straight to a backtest. Starter kit included.
argument-hint: "[path to your Instagram/TikTok export, or a list of links]"
---

# SAVED POSTS SORTER

You saved 300 "this strategy prints" reels. You tested zero. This turns the pile into a queue.

## STEP 1: GET YOUR SAVED POSTS (5 minutes, then wait for the email)

- **Instagram:** Settings → Accounts Center → Your information and permissions → Download your information → pick your Instagram account → "Some of your information" → **Saved** → format **JSON** → date range "All time". Instagram emails a zip (minutes to a few hours). Unzip it.
- **TikTok:** Settings → Account → Download your data → JSON. Favorites are inside `user_data.json`.
- **No export?** Paste links into a `links.txt`, one per line. That works too.

## STEP 2: PARSE

```bash
python scripts/parse_saved.py ~/Downloads/instagram-export --out saved.csv
```

Finds every saved post link in any export layout, dedupes, writes `saved.csv` with empty columns to fill: claim, rule, market, testable, data_free, claimed_result.

## STEP 3: FILL THE SHEET (Claude does this)

For each row, get the post's caption or transcript. Ways, in order: the user pastes it; the user screen-records and you read the frames; a browser tool the user has connected opens the link. **Never log into the user's Instagram yourself.** If you can't see a post, leave it and say how many you skipped.

Fill per row:
- **claim:** what the post promises, in 10 words ("RSI 30 bounce wins 80%")
- **rule:** the exact rule if one exists ("buy close < lower Bollinger band, sell at middle band"). Blank if vague.
- **market:** what it's for (SPY, BTC, forex, any)
- **testable (0 to 3):** 0 = vibes, 1 = partly defined, 2 = defined but needs one assumption, 3 = exact rule a computer can run
- **data_free (0 to 2):** 2 = daily data on Yahoo is enough, 1 = needs intraday or paid data, 0 = needs data nobody sells (order flow from a private Discord)
- **claimed_result:** the number they show, with their name ("@user says +300% in 2024")

Go in batches of 20. Save after each batch.

## STEP 4: RANK

```bash
python scripts/rank.py saved.csv --top 10
```

Score = testable×3 + data_free×2 + 2 if a rule is written + 1 if there's a claimed result. Verdicts: **TEST NEXT** (12+), **MAYBE** (7 to 11), **SKIP**. Writes `SHORTLIST.md`.

## STEP 5: SHIP IT

- Put the shortlist on a URL so you can check it on your phone: any static host, a GitHub Gist, or the `/trading-dashboard-app` build.
- Take the #1 row and test it this week (the TEST guide or the Backtest Any Idea kit).
- Rows with the same rule from different accounts: merge them and note "seen 4 times". Popular isn't proof, but it's what your audience wants tested.

## HARD RULES

- **A claim is not a result.** Always write who said it.
- **Never invent the rule** a post didn't give. Blank means "not testable as posted", which is a finding.
- Never download or repost someone else's video. Link to it.
- Educational only. Not financial advice.
