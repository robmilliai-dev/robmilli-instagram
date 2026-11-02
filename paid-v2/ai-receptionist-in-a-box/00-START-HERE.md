# Start here: never miss a customer call again

**What this does:** When you're busy and the phone rings, an AI answers. It greets the caller, finds out what they need, sends them your booking link, and passes you a short message. No more calls going to voicemail and never calling back.

**What you'll have in 30 minutes:**

- ✅ An AI receptionist you can talk to and test, before you buy a phone number
- ✅ It knows your business name, hours, services and booking link
- ✅ It hands hard calls to a real person

**What you need:**

- A free [Vapi](https://vapi.ai/) account (the AI voice)
- A [Twilio](https://www.twilio.com/) account (the phone number), only when you're ready to go live
- 5 facts about the business (below)

## Step 1: Get your 5 facts ready

1. The exact business name
2. Time zone and open hours
3. Services and the area you serve
4. Your booking link (from [Cal.com](https://cal.com/) or [Calendly](https://calendly.com/))
5. The name and number of the real person who handles anything tricky

Write them in the [intake sheet](templates/business-intake.md). If you don't know one, leave it blank. The AI is told never to guess.

## Step 2: Build and test it (about 30 minutes)

Open [02-first-working-call](02-first-working-call.md) and follow it step by step. You'll paste in the [receptionist prompt](prompts/receptionist-system-prompt.md) and talk to your AI right in the Vapi dashboard. No phone number needed yet.

## Step 3: Run the test calls

Use the [test call script](templates/test-call-script.md). Call it like a real customer would. Try a normal question, a booking, and something weird.

✅ **It's working when** every test call ends with a correct summary, an honest next step, no made-up times, and a hand-off to a human when it isn't sure.

## Step 4: Go live

Only after the tests pass:

| Your situation | Do this |
|---|---|
| You want to hear it before touching your main number | Buy a new Twilio number and point it at your AI. |
| You must keep your current number | Forward only after-hours or missed calls to the AI. Test that you can switch it back. |
| You already use a Twilio number | Write down its current settings first, then import it into Vapi. |

**Never point a real number at an AI you haven't tested.**

## Important rules (keep these)

- The AI tells callers it's an AI assistant.
- It only says "you're booked" if a real booking was made. Otherwise it says: "Here's the link to pick a time."
- Check your local rules before recording calls.
- Don't use it for emergencies, medical or legal advice. For those, it just takes a message.

## What it costs

Vapi and Twilio charge by the minute, plus a small monthly fee for the phone number. Check [Vapi pricing](https://vapi.ai/pricing) and [Twilio pricing](https://www.twilio.com/voice/pricing). Testing in the dashboard may use a few free credits. Plan for minutes used, not just a monthly fee.

## After launch

Listen to 5 real calls (with permission). Fix any wrong answers in your facts or the prompt, then test again. Want to understand how all the pieces connect? Read [how it fits together](01-system-map.md). Setting it up for a client? Use the [client handoff](templates/client-handoff.md).

## If something goes wrong

| Problem | Fix |
|---|---|
| It makes up open times | Add your hours to the facts and tell it: "Never offer times. Only send the booking link." |
| Calls don't reach the AI | Check the Twilio number is assigned to your assistant in Vapi. |
| It gives wrong info | Turn the number off, fix the facts, test again. |

Stuck? Email support@milli-ai.com. If it's not answering calls in 7 days, you get every dollar back, and you keep the files.
