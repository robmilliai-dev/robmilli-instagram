#!/usr/bin/env python3
"""Score and rank a filled saved.csv.  python rank.py saved.csv [--top 10]
Columns used: testable (0-3), data_free (0-2), claimed_result (text), rule (text).
score = testable*3 + data_free*2 + (2 if a rule is written) + (1 if a claimed result exists)."""
import argparse, csv
ap = argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--top", type=int, default=10); a = ap.parse_args()
rows = list(csv.DictReader(open(a.csv, newline="", encoding="utf-8")))
def num(x):
    try: return float(x)
    except (TypeError, ValueError): return 0.0
for r in rows:
    s = num(r.get("testable")) * 3 + num(r.get("data_free")) * 2 + (2 if (r.get("rule") or "").strip() else 0) + (1 if (r.get("claimed_result") or "").strip() else 0)
    r["score"] = f"{s:.0f}"
    if not r.get("verdict"):
        r["verdict"] = "TEST NEXT" if s >= 12 else "MAYBE" if s >= 7 else "SKIP"
rows.sort(key=lambda r: -num(r["score"]))
with open(a.csv, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
with open("SHORTLIST.md", "w") as f:
    f.write("# Strategies worth testing (ranked)\n\n| # | Score | Verdict | Claim | Rule | Market | Post |\n|---|---|---|---|---|---|---|\n")
    for i, r in enumerate(rows[: a.top], 1):
        f.write(f"| {i} | {r['score']} | {r['verdict']} | {r.get('claim','')} | {r.get('rule','')} | {r.get('market','')} | {r['url']} |\n")
print(f"Ranked {len(rows)} → SHORTLIST.md (top {min(a.top, len(rows))})")
