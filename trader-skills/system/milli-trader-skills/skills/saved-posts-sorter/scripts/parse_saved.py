#!/usr/bin/env python3
"""Turn an Instagram data export (or TikTok favorites, or a plain list of links) into
saved.csv, one row per saved post, ready to be scored.

  python parse_saved.py <export folder or file> [--out saved.csv]

Accepts: Instagram saved_posts.json (any export year's layout), TikTok user_data.json
("Favorite Videos"), or any .txt/.csv/.html containing post links.
"""
import argparse, csv, json, os, re, sys
from datetime import datetime, timezone

LINK = re.compile(r"https?://(?:www\.)?(?:instagram\.com/(?:p|reel|reels|tv)/[A-Za-z0-9_-]+|tiktok\.com/[^\s\"'<>]+|vm\.tiktok\.com/[^\s\"'<>]+|youtube\.com/shorts/[A-Za-z0-9_-]+)")


def ts(v):
    try:
        return datetime.fromtimestamp(int(v), tz=timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return ""


def walk_json(obj, found, owner=""):
    """Collect (url, owner, saved_on) from any nesting of Instagram/TikTok export JSON."""
    if isinstance(obj, dict):
        owner = obj.get("title") or obj.get("Author") or owner
        href = obj.get("href") or obj.get("Link") or obj.get("link")
        if isinstance(href, str) and LINK.search(href):
            found.append((LINK.search(href).group(0), owner if isinstance(owner, str) else "", ts(obj.get("timestamp")) or str(obj.get("Date", ""))[:10]))
        for v in obj.values():
            walk_json(v, found, owner)
    elif isinstance(obj, list):
        for v in obj:
            walk_json(v, found, owner)


def collect(path):
    files = []
    if os.path.isdir(path):
        for root, _, names in os.walk(path):
            for n in names:
                if re.search(r"(saved|favorite|user_data|links)", n, re.I) and n.lower().endswith((".json", ".html", ".txt", ".csv")):
                    files.append(os.path.join(root, n))
    else:
        files = [path]
    found = []
    for f in files:
        text = open(f, encoding="utf-8", errors="ignore").read()
        if f.lower().endswith(".json"):
            try:
                walk_json(json.loads(text), found)
                continue
            except json.JSONDecodeError:
                pass
        for m in LINK.finditer(text):
            found.append((m.group(0), "", ""))
    seen, rows = set(), []
    for url, owner, date in found:
        key = url.rstrip("/").split("?")[0]
        if key not in seen:
            seen.add(key)
            rows.append({"url": key, "account": owner, "saved_on": date})
    return files, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out", default="saved.csv")
    a = ap.parse_args()
    files, rows = collect(a.src)
    if not rows:
        sys.exit(f"No post links found in {len(files)} file(s). Point me at saved_posts.json or a list of links.")
    cols = ["url", "account", "saved_on", "claim", "rule", "market", "testable", "data_free", "claimed_result", "score", "verdict"]
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"{len(rows)} saved posts from {len(files)} file(s) → {a.out}")


if __name__ == "__main__":
    main()
