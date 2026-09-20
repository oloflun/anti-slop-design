"""Shotgun / bake-off comparison board. Stdlib only.

Serves a session dir holding N design DIRECTIONS x 2 ENGINES of real HTML
fold-builds, side by side, for one human to rate and choose.

Session dir layout (created by the calling agent before this runs):
    board.json  {"brief":"...","directions":[{"id","name","lane","register",
                "grammar"},...],"engines":[{"id","name"},...]}
    cells/<dir>-<eng>/index.html   one fold build per cell (may be missing ->
                board shows "not built")

Writes board.html into the session dir and serves the dir on 127.0.0.1:<port>.
Also answers GET /api/state -> {"board":..., "cellsExist": {"A-chain": true}}
and POST /api/feedback -> JSON body appended to feedback.jsonl; if
body.submit is true, also written to feedback.json (pretty).

    python board.py <session-dir> [--port 4620] [--open] [--until-submit]
                    [--fallback-root .] [--single]

--single serves one cell at a time in full width: the pair toggle is gone and
`p` does nothing. Half-width panes make every cell look worse than it is
(r5, 2026-09-08), so a board meant for a verdict is opened with --single.
"""
import argparse
import functools
import http.server
import json
import mimetypes
import os
import sys
import threading
import webbrowser
from pathlib import Path

mimetypes.add_type("image/webp", ".webp")

SUBMIT_EVENT = threading.Event()

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Bake-off board</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>[hidden]{display:none!important}html,body{height:100%}body{margin:0;background:#111;color:#eee;font:13px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;display:flex;flex-direction:column;overflow:hidden}
#topbar{flex:none;height:32px;display:flex;align-items:center;gap:6px;padding:0 8px;background:#1a1a1a;color:#ddd;font:12px ui-monospace,Menlo,Consolas,monospace}
#tabs{display:flex;gap:4px;flex:1;min-width:0;overflow:hidden}
#tabs button{font:12px ui-monospace,Menlo,Consolas,monospace;padding:3px 9px;border:1px solid #444;background:#222;color:#ccc;cursor:pointer;border-radius:3px;white-space:nowrap}
#tabs button[aria-selected="true"]{background:#eee;color:#111;border-color:#eee}
#topbar .tool{font:12px ui-monospace,Menlo,Consolas,monospace;padding:3px 9px;border:1px solid #444;background:#222;color:#ccc;cursor:pointer;border-radius:3px}
#topbar .tool[aria-pressed="true"]{background:#2a78d6;color:#fff;border-color:#2a78d6}
#hint{opacity:.5;white-space:nowrap}
button:focus-visible,select:focus-visible,textarea:focus-visible,input:focus-visible{outline:3px solid #2a78d6;outline-offset:1px}
#stage{flex:1;min-height:0;display:flex;gap:1px;background:#333}
.pane{flex:1;min-width:0;display:flex;flex-direction:column;background:#fff;position:relative}
.pane-head{position:absolute;left:8px;top:6px;z-index:2;padding:2px 6px;background:rgba(0,0,0,.55);color:#eee;font:10px ui-monospace,Menlo,Consolas,monospace;border-radius:2px;pointer-events:none}
.pane-frame-wrap{flex:1;min-height:0;position:relative;background:#fff}
.pane-frame-wrap iframe{width:100%;height:100%;border:0;display:block}
.notbuilt{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:12px ui-monospace,Menlo,Consolas,monospace;color:#888;background:#f4f4f2}
.pane.fullscreen{position:fixed;inset:0;z-index:50;background:#000}
.pane.fullscreen .pane-frame-wrap{height:100%}
body.fs #topbar{display:none}
#drawer{position:fixed;top:32px;right:0;bottom:0;width:min(380px,100vw);background:#1a1a1a;color:#eee;border-left:1px solid #333;padding:14px;overflow:auto;display:flex;flex-direction:column;gap:14px;z-index:10;box-shadow:-8px 0 24px rgba(0,0,0,.4)}
#drawer h2{margin:0;font:12px ui-monospace,Menlo,Consolas,monospace;color:#9c9}
.pane-controls{display:flex;flex-direction:column;gap:8px;font:12px system-ui,sans-serif;padding-bottom:12px;border-bottom:1px solid #333}
fieldset{border:1px solid #444;padding:6px 8px;display:flex;gap:8px;align-items:center;margin:0}legend{font:11px ui-monospace,Menlo,Consolas,monospace;padding:0 4px;color:#aaa}
textarea{width:100%;min-height:46px;font:12px system-ui,sans-serif;box-sizing:border-box;background:#111;color:#eee;border:1px solid #444}
select{background:#111;color:#eee;border:1px solid #444}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
button.action{font:12px ui-monospace,Menlo,Consolas,monospace;padding:5px 9px;border:1px solid #666;background:#222;color:#eee;cursor:pointer;border-radius:3px}
#submitbar{display:flex;flex-direction:column;gap:8px}#submitbar label{font:12px ui-monospace,Menlo,Consolas,monospace;color:#aaa}
#submitbtn{font:13px ui-monospace,Menlo,Consolas,monospace;padding:8px 16px;background:#2a78d6;color:#fff;border:0;border-radius:3px;cursor:pointer;align-self:flex-start}
#status{font:11px ui-monospace,Menlo,Consolas,monospace;color:#9c9}
#tabs button{transition:background .1s}</style>
</head><body>
<div id="topbar"><div id="tabs" role="tablist" aria-label="Directions"></div><button type="button" class="tool" id="pairbtn" aria-pressed="false" title="visa två motorer sida vid sida (tangent p)">par</button><button type="button" class="tool" id="fsbtn" aria-pressed="false" title="helskärm för aktiv panel (tangent x, Esc avslutar)">helskärm</button><button type="button" class="tool" id="drawerbtn" aria-pressed="false" title="betyg och kommentar (tangent f)">betyg</button><span id="hint">1-9 riktning &middot; f betyg &middot; p par &middot; x helskärm</span></div>
<div id="stage">
<div class="pane" id="pane-0"><div class="pane-head"><span class="engname" id="engname-0"></span></div><div class="pane-frame-wrap"><iframe id="frame-0" title="engine A"></iframe><div class="notbuilt" id="notbuilt-0" hidden>not built</div></div></div>
<div class="pane" id="pane-1" hidden><div class="pane-head"><span class="engname" id="engname-1"></span></div><div class="pane-frame-wrap"><iframe id="frame-1" title="engine B"></iframe><div class="notbuilt" id="notbuilt-1" hidden>not built</div></div></div>
</div>
<div id="drawer" hidden><h2 id="drawer-title"></h2><div class="pane-controls" id="controls-0"></div><div class="pane-controls" id="controls-1" hidden></div>
<div id="submitbar"><label>overall notes<br><textarea id="overall" rows="3"></textarea></label><button type="button" id="submitbtn">submit</button><span id="status"></span></div></div>
<script>
(function(){
'use strict';
var STATE={board:null,cellsExist:{},active:null,winStart:0,ratings:{},comments:{},remix:{},preferred:null,pair:false,single:false,drawer:false,fs:null,hoverPane:null};
function $(s){return document.querySelector(s)}
function ck(d,e){return d+'-'+e}
function esc(s){return (s||'').replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function post(payload){return fetch('/api/feedback',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})}
fetch('/api/state').then(function(r){return r.json()}).then(init);
function init(data){
  STATE.board=data.board; STATE.cellsExist=data.cellsExist; STATE.active=data.board.directions[0].id;
  STATE.single=!!data.single;
  STATE.pair=!STATE.single && data.board.engines.length>1; document.title=(data.board.brief||'Bake-off board').slice(0,80);
  $('#pairbtn').hidden=STATE.single||data.board.engines.length<2;
  if(STATE.single) $('#hint').textContent='1-9 riktning · f betyg · x helskärm';
  render();
  document.addEventListener('keydown', onKey); $('#submitbtn').addEventListener('click', submitFeedback);
  $('#drawerbtn').addEventListener('click', function(){toggleDrawer()});
  $('#pairbtn').addEventListener('click', function(){if(STATE.single) return; STATE.pair=!STATE.pair; render()});
  $('#fsbtn').addEventListener('click', function(){toggleFullscreen()});
  $('#stage').addEventListener('mouseover', function(e){var p=e.target.closest?e.target.closest('.pane'):null; if(p) STATE.hoverPane=paneIdx(p)});
}
function paneIdx(p){return parseInt(p.id.split('-')[1],10)}
function activePaneIdx(){
  var ae=document.activeElement, p=ae&&ae.closest?ae.closest('.pane'):null;
  if(p&&!p.hidden) return paneIdx(p);
  if(STATE.hoverPane!==null){var hp=$('#pane-'+STATE.hoverPane); if(hp&&!hp.hidden) return STATE.hoverPane}
  return 0;
}
function toggleFullscreen(idx){
  if(STATE.fs!==null){
    var cur=$('#pane-'+STATE.fs); if(cur) cur.classList.remove('fullscreen');
    STATE.fs=null; document.body.classList.remove('fs'); $('#fsbtn').setAttribute('aria-pressed','false'); return;
  }
  if(idx===undefined) idx=activePaneIdx();
  var p=$('#pane-'+idx); if(!p||p.hidden) return;
  p.classList.add('fullscreen'); STATE.fs=idx; document.body.classList.add('fs'); $('#fsbtn').setAttribute('aria-pressed','true');
}
function toggleDrawer(){STATE.drawer=!STATE.drawer; $('#drawer').hidden=!STATE.drawer; $('#drawerbtn').setAttribute('aria-pressed',String(STATE.drawer))}
function renderTabs(){
  var tabs=$('#tabs'); tabs.innerHTML='';
  STATE.board.directions.slice(0,9).forEach(function(d,i){
    var b=document.createElement('button');
    b.type='button'; b.setAttribute('role','tab'); b.setAttribute('aria-selected', String(d.id===STATE.active));
    b.textContent=(i+1)+' '+d.name; b.title=d.lane||'';
    b.addEventListener('click', function(){STATE.active=d.id; render()});
    tabs.appendChild(b);
  });
}
function engPair(){
  var eng=STATE.board.engines, n=eng.length, a=STATE.winStart%n, b=(STATE.winStart+1)%n;
  if(n<2) b=a;
  return [eng[a], eng[b]];
}
function render(){
  renderTabs(); var pair=engPair(); var two=!STATE.single && STATE.pair && STATE.board.engines.length>1;
  $('#pairbtn').setAttribute('aria-pressed',String(two));
  $('#pane-1').hidden=!two; $('#controls-1').hidden=!two; document.querySelectorAll('.pane-head').forEach(function(h){h.hidden=!two});
  if(STATE.fs!==null && $('#pane-'+STATE.fs).hidden) toggleFullscreen();
  renderPane(0, pair[0]); if(two) renderPane(1, pair[1]);
  var d=STATE.board.directions.filter(function(x){return x.id===STATE.active})[0];
  $('#drawer-title').textContent=STATE.active+' \u00b7 '+(d?d.name:'');
}
function renderPane(idx, eng){
  var key=ck(STATE.active, eng.id);
  $('#engname-'+idx).textContent=eng.name+' \u00b7 '+STATE.active;
  var frame=$('#frame-'+idx), nb=$('#notbuilt-'+idx);
  if(STATE.cellsExist[key]){
    if(frame.dataset.key!==key){frame.src='cells/'+key+'/index.html'; frame.dataset.key=key; frame.onload=function(){wireScrollSync(frame)}}
    frame.hidden=false; nb.hidden=true;
  } else {
    frame.hidden=true; frame.removeAttribute('src'); frame.dataset.key=''; nb.hidden=false;
  }
  $('#controls-'+idx).innerHTML=controlsHTML(key);
  wireControls(idx, key);
}
function controlsHTML(key){
  var r=STATE.ratings[key]||0, c=STATE.comments[key]||'';
  var stars=[1,2,3,4,5].map(function(n){return '<label><input type="radio" name="r-'+key+'" value="'+n+'" '+(r===n?'checked':'')+'> '+n+'</label>'}).join('');
  var opts=STATE.board.directions.map(function(d){return '<option value="'+d.id+'">'+esc(d.name)+'</option>'}).join('');
  return '<div class="row" style="font:11px ui-monospace,Menlo,Consolas,monospace;color:#aaa">'+esc(key)+'</div><fieldset><legend>rating</legend>'+stars+'</fieldset>'+
    '<label>comment<br><textarea class="cmt" rows="2">'+esc(c)+'</textarea></label>'+
    '<div class="row"><label><input type="radio" name="preferred" value="'+key+'" '+(STATE.preferred===key?'checked':'')+'> prefer this</label>'+
    '<button type="button" class="action morelike">more like this</button></div>'+
    '<div class="row">remix &mdash; layout <select class="rmx-l">'+opts+'</select> colour <select class="rmx-c">'+opts+'</select> <button type="button" class="action remix">remix</button></div>';
}
function wireControls(idx, key){
  var pane=$('#controls-'+idx);
  pane.querySelectorAll('input[name="r-'+key+'"]').forEach(function(el){ el.addEventListener('change', function(){STATE.ratings[key]=+el.value; post({type:'rating',cell:key,value:+el.value,submit:false})}); });
  pane.querySelector('.cmt').addEventListener('change', function(e){STATE.comments[key]=e.target.value});
  pane.querySelectorAll('input[name="preferred"]').forEach(function(el){ el.addEventListener('change', function(){if(el.checked) STATE.preferred=key}); });
  pane.querySelector('.morelike').addEventListener('click', function(){post({type:'more_like_this',cell:key,submit:false})});
  pane.querySelector('.remix').addEventListener('click', function(){
    var l=pane.querySelector('.rmx-l').value, c=pane.querySelector('.rmx-c').value;
    STATE.remix[key]={layout:l,colour:c}; post({type:'remix',cell:key,remix:STATE.remix[key],submit:false});
  });
}
var syncing=false;
function wireScrollSync(frame){
  try{
    var w=frame.contentWindow;
    w.addEventListener('keydown', function(ev){ if(ev.key==='Escape'||ev.key==='x'||ev.key==='X') onKey(ev) });
    w.addEventListener('scroll', function(){
      if(syncing) return; syncing=true;
      document.querySelectorAll('.pane-frame-wrap iframe').forEach(function(other){ if(other!==frame && !other.hidden && other.contentWindow){ try{other.contentWindow.scrollTo(0, w.scrollY)}catch(e){} } });
      syncing=false;
    });
  }catch(e){}
}
function onKey(e){
  var t=e.target; if(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) return;
  if(e.metaKey||e.ctrlKey||e.altKey) return;
  var n=parseInt(e.key,10), maxN=Math.min(9,STATE.board.directions.length);
  if(n>=1 && n<=maxN){STATE.active=STATE.board.directions[n-1].id; render(); return}
  if(e.key==='x'||e.key==='X'){toggleFullscreen(); return}
  if(e.key==='Escape'){if(STATE.fs!==null) toggleFullscreen(); return}
  if(e.key==='f'||e.key==='F'){toggleDrawer(); return}
  if(e.key==='p'||e.key==='P'){if(!STATE.single && STATE.board.engines.length>1){STATE.pair=!STATE.pair; render()} return}
  if(e.key==='ArrowRight'){STATE.winStart=(STATE.winStart+1)%STATE.board.engines.length; render()}
  else if(e.key==='ArrowLeft'){STATE.winStart=(STATE.winStart-1+STATE.board.engines.length)%STATE.board.engines.length; render()}
}
function submitFeedback(){
  var pair=engPair(), preferred=STATE.preferred || ck(STATE.active, pair[0].id);
  var payload={preferred:preferred, ratings:STATE.ratings, comments:STATE.comments, overall:$('#overall').value, remix:STATE.remix, submit:true};
  post(payload).then(function(){$('#status').textContent='submitted'});
}
})();
</script>
</body></html>
"""


def load_board(session_dir: Path) -> dict:
    board_path = session_dir / "board.json"
    if not board_path.is_file():
        sys.exit(f"board.py: no board.json in {session_dir}")
    return json.loads(board_path.read_text(encoding="utf-8"))

def cells_exist(session_dir: Path, board: dict) -> dict:
    out = {}
    for d in board.get("directions", []):
        for e in board.get("engines", []):
            key = f"{d['id']}-{e['id']}"
            out[key] = (session_dir / "cells" / key / "index.html").is_file()
    return out

def make_handler(session_dir: Path, fallback_root: Path | None = None, single: bool = False):
    class Handler(http.server.SimpleHTTPRequestHandler):
        # HTTP/1.0 (the stdlib default) drops WebP responses intermittently
        # under Chromium (net::ERR_CONNECTION_RESET) -- the same bug
        # scripts/serve.py was built to work around for cell builders. The
        # board itself hadn't been patched with the same fix (F-011, 2026-09-07).
        protocol_version = "HTTP/1.1"

        def end_headers(self):
            # Without Cache-Control the stdlib sends only Last-Modified, and
            # browsers then apply HEURISTIC freshness: a cell rebuilt minutes
            # ago is served from cache without revalidating, so the board shows
            # the previous round and the reviewer judges a stale page. Cost us a
            # round on 2026-09-20. The board is a review surface, never a CDN.
            self.send_header("Cache-Control", "no-store, must-revalidate")
            super().end_headers()

        def translate_path(self, path):
            # cells may reference repo-absolute assets (/sites/..., /tests/...): fall back to the repo root
            local = super().translate_path(path)
            if fallback_root and not os.path.exists(local):
                rel = path.split("?", 1)[0].split("#", 1)[0].lstrip("/")
                cand = fallback_root / rel
                if cand.exists():
                    return str(cand)
            return local

        def _json(self, code, obj):
            data = json.dumps(obj).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):  # noqa: N802 (stdlib override)
            if self.path.split("?", 1)[0] == "/api/state":
                board = load_board(session_dir)
                self._json(200, {"board": board, "cellsExist": cells_exist(session_dir, board),
                                 "single": single})
                return
            super().do_GET()

        def do_POST(self):  # noqa: N802 (stdlib override)
            if self.path.split("?", 1)[0] != "/api/feedback":
                self.send_response(404); self.end_headers(); return
            raw = self.rfile.read(int(self.headers.get("Content-Length", 0) or 0))
            try:
                payload = json.loads(raw)
            except ValueError:
                self.send_response(400); self.end_headers(); return
            with open(session_dir / "feedback.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps(payload) + "\n")
            if payload.get("submit"):
                (session_dir / "feedback.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
                SUBMIT_EVENT.set()
            self._json(200, {"ok": True})

        def log_message(self, fmt, *args):
            pass  # keep stdout limited to BOARD_URL

    return Handler

def main():
    ap = argparse.ArgumentParser(description="Serve the shotgun/bake-off comparison board.")
    ap.add_argument("session_dir")
    ap.add_argument("--port", type=int, default=4620)
    ap.add_argument("--open", action="store_true")
    ap.add_argument("--until-submit", action="store_true")
    ap.add_argument("--fallback-root", default=None, help="serve /paths missing in session_dir from this root (repo root)")
    ap.add_argument("--single", action="store_true",
                    help="one cell at a time in full width; no pair toggle (half-width flatters nothing)")
    args = ap.parse_args()
    fallback_root = Path(args.fallback_root).resolve() if args.fallback_root else None
    session_dir = Path(args.session_dir).resolve()
    load_board(session_dir)  # fail fast if board.json is missing/invalid
    (session_dir / "board.html").write_text(TEMPLATE, encoding="utf-8")
    handler = functools.partial(make_handler(session_dir, fallback_root, args.single),
                                directory=str(session_dir))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    url = f"http://127.0.0.1:{args.port}/board.html"
    print(f"BOARD_URL: {url}")
    sys.stdout.flush()
    if args.open:
        try:
            os.startfile(url)  # type: ignore[attr-defined]
        except AttributeError:
            webbrowser.open(url)
    if args.until_submit:
        threading.Thread(target=lambda: (SUBMIT_EVENT.wait(), httpd.shutdown()), daemon=True).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == "__main__":
    main()
