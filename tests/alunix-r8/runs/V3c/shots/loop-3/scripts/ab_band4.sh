#!/bin/bash
# A/B round 4: iris as a transform (border-radius circle scaled, iframe counter-scaled) instead of clip-path; and rounded clip without counter-scale.
cd "C:/Users/Anton L/anti-slop-design"; export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
URL="http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-3/probe/ab"
MOUNT='document.querySelectorAll("iframe[data-src]").forEach(f=>{if(!f.src){f.src=f.getAttribute("data-src");}})'
CSS='(function(c){var s=document.createElement("style");s.textContent=c;document.head.appendChild(s);})'
WRAP='(function(){var w=document.querySelector(".horai-wrap"),f=w.querySelector("iframe"),d=document.createElement("div");d.className="iris";w.insertBefore(d,f);d.appendChild(f);})()'
IRIS="$CSS('.horai-wrap{clip-path:none!important;--t:clamp(0.05,calc((var(--sc-ps) - 0.10) / 0.45),1)}.horai-wrap .iris{position:absolute;inset:0;border-radius:50%;overflow:clip;transform:scale(var(--t))}.horai-wrap .iris iframe{transform:scale(calc(1 / var(--t)));transform-origin:50% 50%}')"
IRISNOSCALE="$CSS('.horai-wrap{clip-path:none!important;--t:clamp(0.05,calc((var(--sc-ps) - 0.10) / 0.45),1)}.horai-wrap .iris{position:absolute;inset:0;border-radius:50%;overflow:clip;transform:scale(var(--t))}')"
INSETTX="$CSS('.horai-wrap{clip-path:none!important;--t:clamp(0,calc((var(--sc-ps) - 0.10) / 0.45),1)}.horai-wrap .iris{position:absolute;inset:0;transform:translateY(calc((1 - var(--t)) * 100%))}')"
for rep in 1 2; do
for v in iris irisnoscale insettx; do
  case $v in iris) PRE="$MOUNT;$WRAP;$IRIS";; irisnoscale) PRE="$MOUNT;$WRAP;$IRISNOSCALE";; insettx) PRE="$MOUNT;$WRAP;$INSETTX";; esac
  echo -n "$v-$rep "; python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$PRE" --out "$OUT/r4-$v-$rep" | grep -E "price" | head -1
done; done
echo AB4-DONE
