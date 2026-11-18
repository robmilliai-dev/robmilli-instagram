#!/usr/bin/env python3
"""Turn an equity-curve CSV into data.json props for the Remotion template.
  python csv_to_props.py curve.csv --col equity [--bench-col buyhold] --title "..." --hook "..." --out template/data.json
Downsamples to 120 points so the animation stays smooth."""
import argparse, csv, json
ap = argparse.ArgumentParser()
ap.add_argument("csv"); ap.add_argument("--col", default="equity"); ap.add_argument("--bench-col")
ap.add_argument("--date-col", default="date"); ap.add_argument("--title", required=True); ap.add_argument("--hook", required=True)
ap.add_argument("--subtitle", default="Backtest · costs included"); ap.add_argument("--bench-label", default="Buy and hold")
ap.add_argument("--preset", default="reel", choices=["reel", "square", "wide"]); ap.add_argument("--accent", default="#22d3a6")
ap.add_argument("--footer", default="Backtest, not live results. Not financial advice.")
ap.add_argument("--points", type=int, default=120); ap.add_argument("--out", default="data.json")
a = ap.parse_args()
rows = [r for r in csv.DictReader(open(a.csv, newline="", encoding="utf-8-sig")) if r.get(a.col) not in (None, "")]
if len(rows) < 2:
    raise SystemExit(f"Need at least 2 rows with a '{a.col}' value. Columns: {list(rows[0].keys()) if rows else 'none'}")
step = max(1, len(rows) // a.points)
pick = rows[::step]
if pick[-1] is not rows[-1]:
    pick.append(rows[-1])
props = {
    "title": a.title, "subtitle": a.subtitle, "hook": a.hook,
    "points": [float(r[a.col]) for r in pick],
    "startLabel": pick[0].get(a.date_col, "")[:4], "endLabel": pick[-1].get(a.date_col, "")[:4],
    "footer": a.footer, "preset": a.preset, "accent": a.accent,
}
props["benchmark"] = None  # explicit, so the template's sample data never leaks in
if a.bench_col:
    props["benchmark"] = [float(r[a.bench_col]) for r in pick]
    props["benchmarkLabel"] = a.bench_label
json.dump(props, open(a.out, "w"), indent=1)
print(f"Wrote {a.out}: {len(props['points'])} points")
