#!/usr/bin/env bash
# Återuppta den headless Opus-leaden för Alunix r8 med en ny instruktion.
#   bash tests/alunix-r8/lead-resume.sh <tagg> <promptfil> [budget-usd]
# Skriver logs/lead/<tagg>.jsonl / .stderr.txt / .meta.txt och skriver ut result-raden.
# Miljö: PYTHONUTF8=1 (carl-hook och andra hookar utan encoding=), väntetaket för
# bakgrundsagenter avstängt (harnesset dödade annars subagenter efter 600 s).
set -u
cd "$(dirname "$0")/../.." || exit 2
TAG="${1:?tagg}"; PROMPT_FILE="${2:?promptfil}"; BUDGET="${3:-40}"
SID="$(cat tests/alunix-r8/logs/lead/SESSION_ID)"
CLAUDE="$HOME/AppData/Roaming/npm/node_modules/@anthropic-ai/claude-code/bin/claude.exe"
export SCROLLCRAFT_CHROME="C:/Program Files/Google/Chrome/Application/chrome.exe"
export PYTHONIOENCODING=utf-8 PYTHONUTF8=1 CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0
LOG="tests/alunix-r8/logs/lead/$TAG"
echo "start $(date -u +%FT%TZ) sid=$SID prompt=$PROMPT_FILE budget=$BUDGET" >> "$LOG.meta.txt"
"$CLAUDE" -p "$(cat "$PROMPT_FILE")" --resume "$SID" \
  --model claude-opus-5 --effort high \
  --output-format stream-json --verbose --include-hook-events \
  --dangerously-skip-permissions --no-chrome --max-budget-usd "$BUDGET" \
  < /dev/null > "$LOG.jsonl" 2> "$LOG.stderr.txt"
EC=$?
echo "exit=$EC $(date -u +%FT%TZ)" >> "$LOG.meta.txt"
python - "$LOG.jsonl" <<'PY'
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
seen = False
for line in open(sys.argv[1], encoding="utf-8", errors="replace"):
    try: e = json.loads(line)
    except Exception: continue
    if e.get("type") == "assistant": seen = True
    if e.get("type") == "result" and seen:
        print(f"result: {e.get('subtype')} | turns {e.get('num_turns')} | ${(e.get('total_cost_usd') or 0):.2f} | {e.get('duration_ms')} ms")
        print((e.get("result") or "")[:4000])
PY
echo "lead $TAG exit=$EC"
