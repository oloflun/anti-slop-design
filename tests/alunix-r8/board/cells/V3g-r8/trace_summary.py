"""Summarize a CDP trace from click_scroll_probe.py --trace: every main-thread
task over 50 ms from 2 s before the click to 3 s after, with its biggest
child events (script by URL, parse, layout, decode, paint).

    python trace_summary.py TRACE.json
"""
import json, sys
from collections import defaultdict

ev = json.load(open(sys.argv[1], encoding="utf-8"))
ev = ev["traceEvents"] if isinstance(ev, dict) else ev
names = {(e["pid"], e["tid"]): e["args"]["name"] for e in ev if e.get("name") == "thread_name"}
click = next(e["ts"] for e in ev if e.get("name") == "probe-click")
main = [(pid, tid) for (pid, tid), n in names.items() if n == "CrRendererMain"]
KEEP = {"EvaluateScript", "FunctionCall", "ParseHTML", "Layout", "UpdateLayoutTree", "Paint", "Decode Image",
        "ImageDecodeTask", "ParseAuthorStyleSheet", "TimerFire", "FireAnimationFrame", "EventDispatch",
        "v8.compile", "V8.CompileCode", "PrePaint", "Commit", "UpdateLayerTree", "RasterTask", "HitTest",
        "ScheduleStyleRecalculation", "FireIdleCallback", "v8.run", "CompileScript", "XHRLoad"}


def label(e):
    d = e.get("args", {}).get("data", {}) or e.get("args", {}).get("beginData", {}) or {}
    x = d.get("url") or d.get("type") or d.get("functionName") or ""
    return e["name"] + (" " + x.split("/")[-1][:60] if x else "")


for pid, tid in main:
    th = [e for e in ev if e.get("pid") == pid and e.get("tid") == tid and e.get("ph") == "X" and "dur" in e]
    tasks = [e for e in th if e["name"] in ("RunTask", "ThreadControllerImpl::RunTask") and e["dur"] > 50000
             and -2e6 < e["ts"] - click < 3e6]
    if not tasks:
        continue
    print("== main thread pid %s tid %s: %d tasks > 50 ms" % (pid, tid, len(tasks)))
    for t in tasks:
        kids = defaultdict(float)
        for e in th:
            if e["name"] in KEEP and t["ts"] <= e["ts"] < t["ts"] + t["dur"]:
                kids[label(e)] += e["dur"] / 1000
        top = sorted(kids.items(), key=lambda kv: -kv[1])[:7]
        print("  t=%+6d ms  %4d ms  " % ((t["ts"] - click) / 1000, t["dur"] / 1000) + "; ".join("%s %.0f" % kv for kv in top))
