#!/bin/bash
# A/B on the band's frame time (cpu 1, 100:60, 18 ticks from 3873 = .price.top - 900): where do the frames go?
cd "C:/Users/Anton L/anti-slop-design"; export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
URL="http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-3/probe/ab"
MOUNT='document.querySelectorAll("iframe[data-src]").forEach(f=>{if(!f.src){f.src=f.getAttribute("data-src");}})'
NOCLIP='document.querySelectorAll(".frame-wrap").forEach(w=>{w.style.setProperty("--rv","1")})'
NODRIFT='document.querySelectorAll("[data-sc-drift]").forEach(e=>e.removeAttribute("data-sc-drift"))'
for rep in 1 2; do
python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --out "$OUT/base-$rep" | grep -E "price|FAIL" | head -2
python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$MOUNT" --out "$OUT/mount-$rep" | grep -E "price" | head -1
python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$MOUNT;$NOCLIP" --out "$OUT/mount-noclip-$rep" | grep -E "price" | head -1
python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$MOUNT;$NOCLIP;$NODRIFT" --out "$OUT/mount-noclip-nodrift-$rep" | grep -E "price" | head -1
done
# the giant run (2700 -> 5500) with everything pre-mounted, for the band as a whole
python "$S/motion_probe_ab.py" --url "$URL" --track "#giant-section:--sc-ps" --cpu 1 --wheel 100:60 --ticks 28 --start 2700 --pre "$MOUNT" --out "$OUT/giant-mount" | grep -E "giant" | head -1
python "$S/motion_probe_ab.py" --url "$URL" --track "#giant-section:--sc-ps" --cpu 1 --wheel 100:60 --ticks 28 --start 2700 --pre "$MOUNT;$NODRIFT" --out "$OUT/giant-mount-nodrift" | grep -E "giant" | head -1
echo AB-DONE
