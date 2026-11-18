---
name: reel-prompts
description: Write prompts for AI video models (Seedance, Kling, Veo, Higgsfield, Runway, Sora-class) that make scroll-stopping B-roll and ads for trading content. Twelve two-second opening hooks built for trading, a master prompt template, shot-by-shot plans for five trading video types, a credit estimate before anything is generated, and an assembly guide.
argument-hint: "[what the video is for]"
---

# REEL PROMPTS

Stock footage of a guy pointing at a candle chart is dead. This writes the shots that make a trader stop.

## INTAKE

1. What's the video for? (Reel B-roll, an ad for a product, a story, a thumbnail loop)
2. Which model do you have credits on? (Defaults to a generic prompt that works on most)
3. Vertical 9:16 or square?
4. Any real asset to include (screen recording, chart, logo)? Real screens beat generated ones for proof.

## THE MASTER PROMPT TEMPLATE

```
[SHOT TYPE], [SUBJECT doing ONE action], [SETTING], [LIGHTING], [CAMERA MOVE],
[STYLE / LENS], [MOOD], [DURATION]s, 9:16, no text, no logos, no watermarks
```

Rules that matter on every model:
- **One action per shot.** Two actions = mush.
- **No text in the generation.** Models misspell. Add text in the editor.
- **No real brands, logos, tickers or people's faces.** Use "a trading app", not a broker's name.
- **Name the camera move** (slow push-in, orbit, handheld, top-down). Unnamed = random.
- **Say "photoreal" or the exact look.** Otherwise you get a style lottery.

## 12 TWO-SECOND HOOKS (trading-tuned)

1. **The 3am glow:** close-up, face lit only by green monitor light, eyes snap open as a notification chimes. Slow push-in.
2. **The robot hand:** a sleek robotic hand taps "execute" on a glass touchscreen showing a rising line. Macro, shallow focus.
3. **Desk of screens wakes up:** six dark monitors turn on one after another in sequence, dark room. Static wide.
4. **The candle that grows:** a single giant green candlestick rises from a reflective black floor like a skyscraper. Low-angle orbit.
5. **Coffee and chaos:** top-down, hands around a coffee cup, phone beside it buzzing with alerts. Calm vs. chaos.
6. **The red wall:** a wall of red numbers flickers, then one by one turns green. Rack focus.
7. **Server room heartbeat:** blinking server rack, a single amber light pulses like a heartbeat. Slow dolly.
8. **Paper burning into code:** a printed chart curls and burns, the ash becomes glowing lines of code. Macro.
9. **The empty chair:** an office chair spins slowly in front of a trading setup still running at night. "The bot works while you sleep."
10. **Glass brain:** a translucent glass head with tiny glowing candlesticks moving inside it. Studio light, slow orbit.
11. **Phone in the pocket:** a hand slides a phone into a jacket pocket and walks away; screen still shows a running bot. Handheld follow.
12. **The scale:** an old brass balance scale; one side gold coins, the other a small glowing chip that outweighs it. Static, museum light.

## SHOT PLANS (5 video types)

| Type | Shots (2 to 3s each) |
|---|---|
| **"I tested the viral bot"** | Hook 8 → real screen recording of the backtest → Hook 6 → your face/voice verdict → CTA card |
| **"Bot works while you sleep"** | Hook 9 → Hook 7 → real phone alert screenshot → Hook 1 → CTA |
| **Product ad** | Hook 3 → real product screens (3 shots) → Hook 12 → offer card → CTA |
| **Story / hot take** | Hook 10 → talking head → Hook 4 → CTA |
| **Thumbnail loop (3s)** | Hook 4 or 12, seamless loop: same start and end frame |

## CREDIT ESTIMATE (always, before generating)

List every generated shot with its duration, multiply by the model's per-second cost (ask the user or check their plan page), add 50% for retries. Show: "8 shots × 3s = 24s ≈ N credits + retries ≈ M credits." Wait for OK.

## ASSEMBLY GUIDE

1. Generate each shot 2 to 3 times. Keep the best.
2. Cut on action. Every shot change on a beat.
3. Add all text in CapCut/Premiere/DaVinci: big, high contrast, 2 lines max, inside the safe zone (top 15% and bottom 25% get covered by app UI).
4. Real proof (screens, charts) goes in the middle, never cut for an AI shot.
5. Captions burned in. 80% watch muted.
6. End card: keyword + "Not financial advice."

## HARD RULES

- **Never generate a fake broker statement, P&L screenshot or testimonial.** Ever. AI B-roll is mood; proof must be real.
- **Never generate a real person's face** (including famous traders).
- Mark AI-generated footage if the platform asks (most now do).
