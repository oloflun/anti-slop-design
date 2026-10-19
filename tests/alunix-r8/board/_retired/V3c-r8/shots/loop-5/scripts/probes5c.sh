#!/bin/bash
# Loop-5 follow-up C: (1) interleaved A/B of the .panel-thesis window, as built (R10) vs the
# two removed declarations re-injected before the wheel (the R9 condition) - is the window's
# p95 regression 042's price paint or loop 4's single-run noise? (2) the Calyx latch probed
# from before its trigger (2600), so the probe's own settle plateau is outside the ramp.
set -u
cd "C:/Users/Anton L/anti-slop-design"
export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
MPAB="$S/motion_probe_ab.py"
MP="$S/motion_probe_dir.py"
URL="http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html"
CTRL="http://127.0.0.1:3301/tests/motion/smooth.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-5/probe"
LOG="$OUT/probe-log-c.txt"
: > "$LOG"
R9='(function(){var s=document.createElement("style");s.textContent=".price{content-visibility:auto!important;contain-intrinsic-size:auto 760px!important;}";document.head.appendChild(s);})()'
for i in 1 2 3; do
  echo "=== ctrl-$i" | tee -a "$LOG"
  python "$MP" --url "$CTRL" --track "#act:--sc-ps" --cpu 1 --wheel 100:60 --ticks 30 --out "$OUT/ctrl-c-$i" | tee -a "$LOG"
  echo "=== ab-thesis-r10-$i" | tee -a "$LOG"
  python "$MPAB" --url "$URL" --track ".panel-thesis:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 2322 --out "$OUT/ab/thesis-r10-$i" | tee -a "$LOG"
  echo "=== ab-thesis-r9-$i" | tee -a "$LOG"
  python "$MPAB" --url "$URL" --track ".panel-thesis:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 2322 --pre "$R9" --out "$OUT/ab/thesis-r9-$i" | tee -a "$LOG"
done
echo "=== calyx from before trigger" | tee -a "$LOG"
python "$MP" --url "$URL" --track ".calyx-wrap:--rv" --cpu 1 --wheel 100:60 --ticks 24 --start 2600 --out "$OUT/c-calyx-rv-2600" | tee -a "$LOG"
python "$MP" --url "$URL" --track ".calyx-wrap:--rv" --cpu 1 --wheel 100:60 --ticks 24 --start 2600 --out "$OUT/c-calyx-rv-2600b" | tee -a "$LOG"
echo PROBES-C-DONE | tee -a "$LOG"
