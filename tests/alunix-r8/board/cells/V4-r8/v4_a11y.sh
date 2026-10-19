#!/usr/bin/env bash
# Runs a11y-audit's three scripts plus contrast.py on the known-broken fixture first (CARL rule),
# then on V4. Call through tests/alunix-r8/browser_lock.py so only one browser runs at a time.
S="$HOME/.claude/skills/a11y-audit/scripts"
C="$HOME/.claude/skills/design/scripts"
O="tests/alunix-r8/runs/V4/shots/a11y"
mkdir -p "$O"
for name in broken v4; do
  if [ "$name" = broken ]; then U="http://127.0.0.1:3308/tests/a11y/broken.html"; else U="http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"; fi
  python "$S/a11y_scan.py" "$U" > "$O/$name-scan.json" 2> "$O/$name-scan.err"
  python "$S/tab_walk.py" "$U" --max 120 > "$O/$name-tab.json" 2> "$O/$name-tab.err"
  python "$S/reflow.py" "$U" > "$O/$name-reflow.json" 2> "$O/$name-reflow.err"
  python "$C/contrast.py" "$U" > "$O/$name-contrast.txt" 2>&1
done
echo done
