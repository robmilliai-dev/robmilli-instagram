---
id: equity-video
title: The Equity Curve Video skill
category: content
summary: Equity curve CSV into a 12-second animated MP4: hook, the curve draws itself, the worst drop marked in red, final stats. Reel, square and wide presets.
---

# EQUITY VIDEO

Everyone posts the screenshot. Nobody shows the worst drop. A curve that draws itself, with the drop marked in red, gets watched to the end and trusted.

## SETUP (once, about 2 minutes)

```bash
bash scripts/setup.sh equity-video     # copies template + npm install (Node 18+)
```

Rendering needs Chrome/Chromium. Remotion downloads one automatically; if it can't, pass `--browser-executable=/path/to/chrome`.

## MAKE A VIDEO

1. **Get a curve CSV.** Any CSV with a date column and an equity column. Sources: `/account-stats --format json`, a backtest export, a broker export. Optional second column for buy-and-hold.
2. **Write the hook.** Max 7 words, lands in under 1.5 seconds. Good: "10 years. One rule. Every drop shown." / "I rebuilt the viral bot. Here's the truth." Bad: anything with a promise of future profit.
3. **Convert:**
   ```bash
   python scripts/csv_to_props.py curve.csv --col equity --bench-col buyhold \
     --title "Trend rule on SPY" --hook "10 years. Every drop shown." \
     --subtitle "Backtest 2015 to 2025 · costs included" --out equity-video/data.json
   ```
4. **Render:**
   ```bash
   cd equity-video && npm run render            # → out/equity.mp4 (reel, 12s)
   npx remotion render src/index.ts EquityCurve-square out/square.mp4 --props=./data.json
   npx remotion studio src/index.ts             # live preview in the browser
   ```

## TIMELINE (12 seconds, 30 fps)

| Time | What happens |
|---|---|
| 0.0 to 1.5s | Hook slides in. This is the scroll-stopper. |
| 1.5 to 8.0s | Curve draws left to right, return counter ticks live. Benchmark dashes behind it. |
| when it gets there | Worst drop gets a red dot, a dashed line and the number |
| 8.0 to 12s | Stats land: Total, Worst drop, Benchmark |

## CHANGING THE LOOK

Edit `src/EquityCurve.tsx`: `BG`, `INK`, `MUTED`, `RED` constants at the top; `accent` comes from props (`--accent "#ffb020"`). Change length in `Root.tsx` (`durationInFrames`) and the `[45, 240]` draw window together.

## REMOTION RULES THAT BITE

- Everything animates off `useCurrentFrame()`. No `setTimeout`, no CSS transitions. They won't render.
- `--props` **merges** over `defaultProps`. Any field you don't pass comes from the sample. The converter sets `benchmark: null` on purpose.
- Use `interpolate(..., { extrapolateLeft: "clamp", extrapolateRight: "clamp" })` or values overshoot.
- Fonts: system fonts render everywhere. A web font must be loaded with `@remotion/google-fonts` or it falls back silently.

## HARD RULES

- **The worst drop is always shown.** Don't remove it. It's the reason people trust the video.
- **Label it.** Backtest says "Backtest". Live says "Live account". Footer says "Not financial advice."
- **No cherry-picked window.** Use the full test period. If you shorten it, say why on screen.

## If you can't run scripts here
This playbook uses helper scripts. In a chat app, do the steps by hand with the user (ask them to paste data), or point them to the downloadable skill at milli-ai.com/free (keyword REPLAY).
