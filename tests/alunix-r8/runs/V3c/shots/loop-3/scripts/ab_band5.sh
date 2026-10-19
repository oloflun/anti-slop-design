#!/bin/bash
# A/B round 5: the transform recipe WITHOUT pre-mount (mount cost inside the window?), price window and giant window (both reveals).
cd "C:/Users/Anton L/anti-slop-design"; export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
URL="http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-3/probe/ab"
CSS='(function(c){var s=document.createElement("style");s.textContent=c;document.head.appendChild(s);})'
WRAP='document.querySelectorAll(".frame-wrap").forEach(function(w){var f=w.querySelector("iframe"),d=document.createElement("div");d.className="rv";w.insertBefore(d,f);d.appendChild(f);})'
RECIPE="$CSS('.frame-wrap{clip-path:none!important}.calyx-wrap{--t:clamp(0,calc((var(--sc-ps) - 0.02) / 0.28),1)}.horai-wrap{--t:clamp(0.05,calc((var(--sc-ps) - 0.10) / 0.45),1)}.frame-wrap .rv{position:absolute;inset:0}.calyx-wrap .rv{transform:translateY(calc((1 - var(--t)) * 100%))}.calyx-wrap .rv iframe{transform:translateY(calc((var(--t) - 1) * 100%))}.horai-wrap .rv{border-radius:50%;overflow:clip;transform:scale(var(--t))}.horai-wrap .rv iframe{transform:scale(calc(1 / var(--t)))}')"
for rep in 1 2; do
  echo -n "price-recipe-nomount-$rep "; python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$WRAP;$RECIPE" --out "$OUT/r5-price-recipe-$rep" | grep -E "price" | head -1
  echo -n "giant-base-$rep "; python "$S/motion_probe_ab.py" --url "$URL" --track "#giant-section:--sc-ps" --cpu 1 --wheel 100:60 --ticks 28 --start 2700 --out "$OUT/r5-giant-base-$rep" | grep -E "giant" | head -1
  echo -n "giant-recipe-nomount-$rep "; python "$S/motion_probe_ab.py" --url "$URL" --track "#giant-section:--sc-ps" --cpu 1 --wheel 100:60 --ticks 28 --start 2700 --pre "$WRAP;$RECIPE" --out "$OUT/r5-giant-recipe-$rep" | grep -E "giant" | head -1
done
echo AB5-DONE
