#!/usr/bin/env bash
# Usage: bash apply_guides_v3.sh <free-guides-dir> <systems-dir>
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
python3 "$here/guides_v3.py" "$1"
python3 "$here/paid_v3.py" "$2"
