#!/bin/bash
# A/B round 3, three reps each, median: is it the clip over a LIVE iframe? (hidden iframe under the same clip = poster emulation)
cd "C:/Users/Anton L/anti-slop-design"; export PYTHONIOENCODING=utf-8
S="C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac/scratchpad"
URL="http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUT="tests/alunix-r8/runs/V3c/shots/loop-3/probe/ab"
MOUNT='document.querySelectorAll("iframe[data-src]").forEach(f=>{if(!f.src){f.src=f.getAttribute("data-src");}})'
CSS='(function(c){var s=document.createElement("style");s.textContent=c;document.head.appendChild(s);})'
MASK="$CSS('.horai-wrap{clip-path:none;mask-image:radial-gradient(circle at 50% 50%, black calc(var(--rv) * 78%), transparent calc(var(--rv) * 78% + 1px))}')"
HIDDEN="$CSS('.horai-wrap iframe{visibility:hidden}.horai-wrap{background:var(--c-graphite,#333)}')"
NOCLIP='document.querySelectorAll(".frame-wrap").forEach(w=>{w.style.setProperty("--rv","1")})'
for rep in 1 2 3; do
for v in clip mask hidden noclip; do
  case $v in clip) PRE="$MOUNT";; mask) PRE="$MOUNT;$MASK";; hidden) PRE="$MOUNT;$HIDDEN";; noclip) PRE="$MOUNT;$NOCLIP";; esac
  echo -n "$v-$rep "; python "$S/motion_probe_ab.py" --url "$URL" --track ".price:--sc-ps" --cpu 1 --wheel 100:60 --ticks 18 --start 3873 --pre "$PRE" --out "$OUT/r3-$v-$rep" | grep -E "price" | head -1
done; done
echo AB3-DONE
