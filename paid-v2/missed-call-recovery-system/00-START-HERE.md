# Start here: text back every missed call, automatically

**What this does:** A customer calls. Nobody picks up. Seconds later, they get one friendly text: "Sorry we missed you! Here's how to book, or reply and we'll call you back." The lead doesn't go to your competitor.

**What you'll have in 30 minutes:**

- ✅ A test phone number that rings your real phone first
- ✅ If nobody answers, one text goes out to the caller
- ✅ Tested on your own phone, so you know it works

**What you need:**

- A [Twilio](https://www.twilio.com/) account with a number that can call and text
- A phone you can test with
- The text you want to send (we give you templates)

## How it works

1. Someone calls your Twilio number.
2. It rings your staff phone first.
3. If nobody answers (or the line is busy), the caller gets **one** text.
4. If someone answers, no text is sent.

It sends one text, not a spam drip.

## Your 30-minute first win

Follow [02-first-win](02-first-win.md) step by step. You'll:

1. Write your text (business name + "sorry we missed you" + how to book + "Reply STOP to opt out")
2. Set up a test number in Twilio Studio (drag and drop, no code)
3. Call it, don't answer, and check the text arrives on your phone

✅ **It works when** you call, let it ring out, and **one** text lands on your phone within a minute.

**No text arrived?** In the US you must finish Twilio's text-message registration (called "A2P 10DLC") before texts go out. That's normal. Finish it, then test again.

## Pick your setup

| Option | Pick it if | Guide |
|---|---|---|
| **Studio (no code)** | You want the fastest setup. **Most people pick this.** | [Studio setup](03-studio-setup.md) |
| **Functions (code)** | You want different texts for open and closed hours | [Functions setup](04-functions-setup.md), with ready [code](code/missed-call.js) |

Use only **one** of them on a number, not both.

## One thing to watch: voicemail

If your staff phone has voicemail on, Twilio thinks the call was "answered", so no text goes out. Turn off voicemail on the staff phone, or forward it to a phone without voicemail.

## Before you go live

Get the business owner to OK:

- The exact text message
- Business hours
- Who calls people back
- How people opt out

Then read [compliance](05-compliance.md) and [operations](06-operations.md). Texting rules differ by place, so have someone check them for your area.

## What it costs

Twilio charges for the phone number, call minutes, texts, and US text registration. Check [US SMS prices](https://www.twilio.com/en-us/sms/pricing/us) and [number prices](https://www.twilio.com/en-us/phone-numbers).

## How to know it's paying off

A text sent isn't a sale. Count it as a win only when the caller replies and books, or your team calls back and helps them. Track it in the [results sheet](templates/roi-worksheet.md) with your real numbers.

## If something goes wrong

| Problem | Fix |
|---|---|
| A text goes out even when you answer | Check the Studio split looks for `no-answer` or `busy` only. See [Studio setup](03-studio-setup.md). |
| No text ever goes out | Finish US text registration, and turn off voicemail on the staff phone. |
| Two texts go out | You have both Studio and Functions on one number. Remove one. |

Stuck? Email support@milli-ai.com. If it's not sending texts in 7 days, you get every dollar back, and you keep the files.
