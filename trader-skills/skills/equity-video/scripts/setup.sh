#!/usr/bin/env bash
# Copies the template into ./equity-video and installs Remotion. Run once.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-equity-video}"
[ -d "$DEST" ] && { echo "$DEST already exists"; exit 1; }
cp -r "$HERE/template" "$DEST"
cd "$DEST" && npm install --no-audit --no-fund
mkdir -p out
echo "Ready. Next: put data.json in $DEST, then: cd $DEST && npm run render"
