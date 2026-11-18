#!/usr/bin/env bash
# Milli.ai Trader Skills installer: puts all 17 skills in ~/.claude/skills and the prompt kits in ~/.claude/milli-prompts.
# Read before you run: it only downloads one zip from milli-ai.com and copies folders. No sudo, nothing else.
set -euo pipefail
URL="${MILLI_SKILLS_URL:-https://milli-ai.com/api/downloads/trader-skills/milli-trader-skills.zip}"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
command -v unzip >/dev/null || { echo "Please install unzip first."; exit 1; }
echo "Downloading Milli trader skills..."
curl -fsSL "$URL" -o "$TMP/skills.zip"
unzip -q "$TMP/skills.zip" -d "$TMP"
mkdir -p "$DEST" "$HOME/.claude/milli-prompts"
n=0
for d in "$TMP"/milli-trader-skills/*/; do
  name="$(basename "$d")"
  [ "$name" = "prompts" ] && continue
  if [ -d "$DEST/$name" ]; then echo "  skip $name (already installed; delete it to update)"; continue; fi
  cp -r "$d" "$DEST/$name"; n=$((n+1)); echo "  + $name"
done
cp "$TMP"/milli-trader-skills/prompts/*.md "$HOME/.claude/milli-prompts/" 2>/dev/null || true
echo "Installed $n skills into $DEST. Open Claude Code and type / to see them."
echo "Prompt kits are in ~/.claude/milli-prompts. Educational only. Not financial advice."
