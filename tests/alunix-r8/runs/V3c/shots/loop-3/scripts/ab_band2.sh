#!/bin/bash
# A/B round 2: the Horai iris (circle clip-path over a LIVE iframe) is the cost. Which cheap variant keeps the iris?
cd "C:/Users/Anton L/anti-slop-design"; export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
URL="http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-3/probe/ab"
MOUNT='document.querySelectorAll("iframe[data-src]").forEach(f=>{if(!f.src){f.src=f.getAttribute("data-src");}})'
CSS='(function(c){var s=document.createElement("style");s.textContent=c;document.head.appendChild(s);})'
WC="$CSS('.horai-wrap{will-change:clip-path}')"
INSET="$CSS('.horai-wrap{clip-path:inset(calc((1 - var(--rv)) * 50%) calc((1 - var(--rv)) * 50%))}')"
PAINT="$CSS('.horai-wrap{contain:paint}')"
MASK="$CSS('.horai-wrap{clip-path:none;mask-image:radial-gradient(circle at 50% 50%, black calc(var(--rv) * 78%), transparent calc(var(--rv) * 78% + 1px))}')"
for rep in 1 2; do
python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$MOUNT;$WC" --out "$OUT/mount-willchange-$rep" | grep -E "price" | head -1
python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$MOUNT;$INSET" --out "$OUT/mount-inset-$rep" | grep -E "price" | head -1
python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$MOUNT;$PAINT" --out "$OUT/mount-containpaint-$rep" | grep -E "price" | head -1
python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$MOUNT;$MASK" --out "$OUT/mount-mask-$rep" | grep -E "price" | head -1
done
echo AB2-DONE
