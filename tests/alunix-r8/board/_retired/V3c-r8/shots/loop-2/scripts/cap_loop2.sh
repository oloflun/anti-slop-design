#!/bin/bash
# Loop-2 capture: slices, previews, flip frames, process frames. Port 3090 (R7 state).
set -u
cd "C:/Users/Anton L/anti-slop-design"
export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
URL="http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-2"
mkdir -p "$OUT"
LOG="$OUT/capture-log.txt"
: > "$LOG"
python "$S/slices.py"   "$OUT/slices-1440" "$URL" v3c-1440 1440 900 16 | tee -a "$LOG"
python "$S/slices.py"   "$OUT/slices-390"  "$URL" v3c-390  390  844 16 | tee -a "$LOG"
python "$S/previews.py" "$OUT/preview" "$URL" | tee -a "$LOG"
python "$S/frames.py" flip "$OUT/flip-1440" "$URL" v3c-1440 1440 900 12 | tee -a "$LOG"
python "$S/frames.py" flip "$OUT/flip-390"  "$URL" v3c-390  390  844 12 | tee -a "$LOG"
python "$S/frames.py" life "$OUT/process-1440" "$URL" v3c-1440 1440 900 12 "#process" | tee -a "$LOG"
python "$S/frames.py" life "$OUT/process-390"  "$URL" v3c-390  390  844 12 "#process" | tee -a "$LOG"
echo CAPTURE-DONE | tee -a "$LOG"
