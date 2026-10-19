#!/bin/bash
# Loop-5 motion/scroll probes on the R10 state (md5 d3491b4a), port 3301, control protocol.
# Starts adjusted to R10 geometry (#process 5340-9136, footer 9682, docH 10582).
set -u
cd "C:/Users/Anton L/anti-slop-design"
export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
MP="$S/motion_probe_dir.py"
SV="C:/Users/Anton L/.claude/skills/design/scripts/scroll_verify.py"
URL="http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html"
CTRL="http://127.0.0.1:3301/tests/motion/smooth.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-5/probe"
mkdir -p "$OUT"
LOG="$OUT/probe-log.txt"
: > "$LOG"

control() {
  for attempt in 1 2; do
    python "$MP" --url "$CTRL" --track "#act:--sc-ps,#card:transform" --cpu "$1" --wheel 100:60 --ticks 30 --out "$OUT/ctrl-$2-$attempt" | tee -a "$LOG"
    if python - "$OUT/ctrl-$2-$attempt/motion_probe.json" <<'EOF'
import json,sys
d=json.load(open(sys.argv[1]))
sys.exit(0 if all(t.get("frames_over_33ms",99)==0 for t in d["tracks"]) else 1)
EOF
    then echo "control $2 clean (attempt $attempt)" | tee -a "$LOG"; return 0; fi
    echo "control $2 noisy (attempt $attempt), waiting 60 s" | tee -a "$LOG"; sleep 60
  done
  echo "control $2 STILL NOISY after 2 attempts, measuring anyway (reported)" | tee -a "$LOG"
}

run() {
  echo "=== $1" | tee -a "$LOG"
  if [ -n "$5" ]; then S2=(--start "$5"); else S2=(); fi
  python "$MP" --url "$URL" --track "$6" --cpu "$2" --wheel "$3" --ticks "$4" "${S2[@]}" --out "$OUT/$1" | tee -a "$LOG"
}

HERO="section.hero:--sc-ps,.plate-card:transform"
PROC="#process:--sc-ps"

control 4 c4a
run hero-down-100 4 100:60 40 "" "$HERO"
run hero-up-100   4 -100:60 40 3200 "$HERO"
control 4 c4b
run hero-down-20  4 20:120 160 "" "$HERO"
run hero-up-20    4 -20:120 160 3200 "$HERO"
control 4 c4c
run proc-down-100 4 100:60 45 4700 "$PROC"
run proc-up-100   4 -100:60 45 9100 "$PROC"
control 4 c4d
run proc-down-20  4 20:120 200 4700 "$PROC"
run proc-up-20    4 -20:120 200 8800 "$PROC"
run giant-down-100 4 100:60 28 2700 "#giant-section:--sc-ps"
run price-down-100 4 100:60 18 3873 ".price:--sc-ps"
control 1 c1a
run hero-down-100-cpu1 1 100:60 40 "" "$HERO"
run hero-up-100-cpu1   1 -100:60 40 3200 "$HERO"
run proc-down-100-cpu1 1 100:60 45 4700 "$PROC"
run proc-up-100-cpu1   1 -100:60 45 9100 "$PROC"
run giant-down-100-cpu1 1 100:60 28 2700 "#giant-section:--sc-ps"
run price-down-100-cpu1 1 100:60 18 3873 ".price:--sc-ps"
run thesis-down-100-cpu1 1 100:60 18 2322 ".panel-thesis:--sc-ps"
run footer-down-100-cpu1 1 100:60 18 9000 "footer.close:--sc-ps"
run calyx-rv-cpu1 1 100:60 24 3200 ".calyx-wrap:--rv,.calyx-wrap .rv:transform"
run horai-rv-cpu1 1 100:60 24 3873 ".horai-wrap:--rv,.horai-wrap .rv:transform"
run hero-down-100-cpu1-b 1 100:60 40 "" "$HERO"
run hero-down-100-cpu1-c 1 100:60 40 "" "$HERO"
control 1 c1b
echo "=== scroll_verify 1440" | tee -a "$LOG"
python "$SV" "$URL" --width 1440 --height 900 --out "$OUT/sv-1440" > "$OUT/scroll-verify-1440.txt" 2>&1; tail -c 2500 "$OUT/scroll-verify-1440.txt" | tee -a "$LOG"
echo "=== scroll_verify 390" | tee -a "$LOG"
python "$SV" "$URL" --width 390 --height 844 --out "$OUT/sv-390" > "$OUT/scroll-verify-390.txt" 2>&1; tail -c 2500 "$OUT/scroll-verify-390.txt" | tee -a "$LOG"
echo PROBES-DONE | tee -a "$LOG"
