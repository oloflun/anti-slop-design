#!/bin/bash
# Loop-5 follow-up: the two windows whose p95 moved against loop 4 (hero cpu4 down,
# .panel-thesis cpu1) measured three times each, interleaved with the control; the footer
# re-run with loop-4-comparable travel (1482 px, not 682); the two --rv latches re-run
# with a start before the reveal so the probe's own settle plateau is outside the sample.
set -u
cd "C:/Users/Anton L/anti-slop-design"
export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
MP="$S/motion_probe_dir.py"
URL="http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html"
CTRL="http://127.0.0.1:3301/tests/motion/smooth.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-5/probe"
LOG="$OUT/probe-log-b.txt"
: > "$LOG"
run() {
  echo "=== $1" | tee -a "$LOG"
  if [ -n "$5" ]; then S2=(--start "$5"); else S2=(); fi
  python "$MP" --url "$URL" --track "$6" --cpu "$2" --wheel "$3" --ticks "$4" "${S2[@]}" --out "$OUT/$1" | tee -a "$LOG"
}
ctrl() { echo "=== ctrl $1" | tee -a "$LOG"; python "$MP" --url "$CTRL" --track "#act:--sc-ps,#card:transform" --cpu "$2" --wheel 100:60 --ticks 30 --out "$OUT/ctrl-b-$1" | tee -a "$LOG"; }
HERO="section.hero:--sc-ps,.plate-card:transform"
for i in 1 2 3; do
  ctrl "c4-$i" 4
  run "b-hero-down-100-$i" 4 100:60 40 "" "$HERO"
  run "b-thesis-cpu1-$i" 1 100:60 18 2322 ".panel-thesis:--sc-ps"
done
ctrl "c1" 1
run b-footer-cpu1-travel 1 100:60 18 8200 "footer.close:--sc-ps"
run b-calyx-rv-cpu1 1 100:60 24 3000 ".calyx-wrap:--rv"
run b-horai-rv-cpu1 1 100:60 24 3600 ".horai-wrap:--rv"
run b-hero-up-100-1 4 -100:60 40 3200 "$HERO"
echo PROBES-B-DONE | tee -a "$LOG"
