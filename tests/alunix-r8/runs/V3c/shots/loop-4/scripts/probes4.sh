#!/bin/bash
# Loop-4 motion/scroll probes on the R9 state with the control protocol. One run at a time.
# Contract step 1: hero + process tracks, cpu 4, 100:60 and 20:120, both directions;
# plus the loop-3 cpu 1 set (hero, process, giant, price, footer) for H-22 and the
# 036/041 windows.
set -u
cd "C:/Users/Anton L/anti-slop-design"
export PYTHONIOENCODING=utf-8
MP="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad/motion_probe_dir.py"
SV="C:/Users/Anton L/.claude/skills/design/scripts/scroll_verify.py"
URL="http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CTRL="http://localhost:3090/tests/motion/smooth.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-4/probe"
mkdir -p "$OUT"
LOG="$OUT/probe-log.txt"
: > "$LOG"

control() {  # $1 = cpu, $2 = name; retries once after 60 s if any frame > 33 ms
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

run() {  # name cpu wheel ticks start track
  echo "=== $1" | tee -a "$LOG"
  if [ -n "$5" ]; then S=(--start "$5"); else S=(); fi
  python "$MP" --url "$URL" --track "$6" --cpu "$2" --wheel "$3" --ticks "$4" "${S[@]}" --out "$OUT/$1" | tee -a "$LOG"
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
run proc-up-100   4 -100:60 45 9400 "$PROC"
control 4 c4d
run proc-down-20  4 20:120 200 4700 "$PROC"
run proc-up-20    4 -20:120 200 9000 "$PROC"
run giant-down-100 4 100:60 28 2700 "#giant-section:--sc-ps"
run price-down-100 4 100:60 18 3873 ".price:--sc-ps"
control 1 c1a
run hero-down-100-cpu1 1 100:60 40 "" "$HERO"
run hero-up-100-cpu1   1 -100:60 40 3200 "$HERO"
run proc-down-100-cpu1 1 100:60 45 4700 "$PROC"
run proc-up-100-cpu1   1 -100:60 45 9400 "$PROC"
run giant-down-100-cpu1 1 100:60 28 2700 "#giant-section:--sc-ps"
run price-down-100-cpu1 1 100:60 18 3873 ".price:--sc-ps"
run thesis-down-100-cpu1 1 100:60 18 2322 ".panel-thesis:--sc-ps"
run footer-down-100-cpu1 1 100:60 18 8500 "footer.close:--sc-ps"
run horai-rv-cpu1 1 100:60 24 3873 ".horai-wrap:--rv,.horai-wrap .rv:transform"
run hero-down-100-cpu1-b 1 100:60 40 "" "$HERO"
run hero-down-100-cpu1-c 1 100:60 40 "" "$HERO"
echo "=== scroll_verify 1440" | tee -a "$LOG"
python "$SV" "$URL" --width 1440 --height 900 --out "$OUT/sv-1440" | tee "$OUT/scroll-verify-1440.txt" | tail -c 3000 | tee -a "$LOG"
echo "=== scroll_verify 390" | tee -a "$LOG"
python "$SV" "$URL" --width 390 --height 844 --out "$OUT/sv-390" | tee "$OUT/scroll-verify-390.txt" | tail -c 3000 | tee -a "$LOG"

# --- A/B for the .price content-visibility reservation (loop 4 finding): as built vs the
# two declarations neutralised after load + 5 s (so the 297 px relayout happens before the wheel)
MPAB="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad/motion_probe_ab.py"
PRICEFIX='(function(){var s=document.createElement("style");s.textContent=".price{content-visibility:visible!important;contain-intrinsic-size:none!important;}";document.head.appendChild(s);})()'
for i in 1 2 3; do
  echo "=== ab-price-asbuilt-$i" | tee -a "$LOG"
  python "$MPAB" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --out "$OUT/ab/price-asbuilt-$i" | tee -a "$LOG"
  echo "=== ab-price-fix-$i" | tee -a "$LOG"
  python "$MPAB" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$PRICEFIX" --out "$OUT/ab/price-fix-$i" | tee -a "$LOG"
  echo "=== ab-giant-asbuilt-$i" | tee -a "$LOG"
  python "$MPAB" --url "$URL" --track "#giant-section:--sc-ps" --cpu 1 --wheel 100:60 --ticks 28 --start 2700 --out "$OUT/ab/giant-asbuilt-$i" | tee -a "$LOG"
  echo "=== ab-giant-fix-$i" | tee -a "$LOG"
  python "$MPAB" --url "$URL" --track "#giant-section:--sc-ps" --cpu 1 --wheel 100:60 --ticks 28 --start 2700 --pre "$PRICEFIX" --out "$OUT/ab/giant-fix-$i" | tee -a "$LOG"
done
echo AB-DONE | tee -a "$LOG"
echo PROBES-DONE | tee -a "$LOG"
