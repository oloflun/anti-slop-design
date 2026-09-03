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
"""
import argparse
import functools
import http.server
import json
import os
import sys
import threading
import webbrowser
from pathlib import Path

SUBMIT_EVENT = threading.Event()

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Bake-off board</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>[hidden]{display:none!important}body{margin:0;background:#e9e9e9;color:#1a1a1a;font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif}#topbar{display:flex;align-items:center;gap:16px;padding:10px 16px;background:#1a1a1a;color:#eee;font:12px/1.3 ui-monospace,Menlo,Consolas,monospace}#topbar .brief{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;opacity:.85}#hint{opacity:.6;flex:none}#tabs{display:flex;gap:4px;padding:8px 16px;background:#d8d8d8;border-bottom:1px solid #bbb;flex-wrap:wrap}#tabs button{font:12px ui-monospace,Menlo,Consolas,monospace;padding:6px 10px;border:1px solid #999;background:#fff;color:#333;cursor:pointer;border-radius:3px}#tabs button[aria-selected="true"]{background:#1a1a1a;color:#fff;border-color:#1a1a1a}button:focus-visible,select:focus-visible,textarea:focus-visible,input:focus-visible{outline:3px solid #2a78d6;outline-offset:1px}#stage{display:flex;gap:1px;background:#bbb}.pane{flex:1;min-width:0;display:flex;flex-direction:column;background:#f4f4f2}.pane-head{padding:6px 10px;background:#ccc;font:11px ui-monospace,Menlo,Consolas,monospace;color:#333}.pane-frame-wrap{position:relative;height:58vh;border-bottom:1px solid #bbb;background:#fff}.pane-frame-wrap iframe{width:100%;height:100%;border:0;display:block}.notbuilt{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:12px ui-monospace,Menlo,Consolas,monospace;color:#888;background:#f4f4f2}.pane-controls{padding:10px;display:flex;flex-direction:column;gap:8px;font:12px system-ui,sans-serif}fieldset{border:1px solid #ccc;padding:6px 8px;display:flex;gap:8px;align-items:center;margin:0}legend{font:11px ui-monospace,Menlo,Consolas,monospace;padding:0 4px}textarea{width:100%;min-height:46px;font:12px system-ui,sans-serif;box-sizing:border-box}.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}button.action{font:12px ui-monospace,Menlo,Consolas,monospace;padding:5px 9px;border:1px solid #888;background:#fff;cursor:pointer;border-radius:3px}#submitbar{display:flex;gap:12px;align-items:flex-start;padding:14px 16px;background:#1a1a1a;color:#eee}#submitbar label{flex:1;font:12px ui-monospace,Menlo,Consolas,monospace}#submitbar textarea{flex:1}#submitbtn{font:13px ui-monospace,Menlo,Consolas,monospace;padding:8px 16px;background:#2a78d6;color:#fff;border:0;border-radius:3px;cursor:pointer}#status{font:11px ui-monospace,Menlo,Consolas,monospace;color:#9c9;align-self:center}@media (prefers-reduced-motion:no-preference){#tabs button{transition:background .1s}}</style>
</head><body>
<div id="topbar"><span class="brief" id="brief"></span><span id="hint">keys: 1-5 direction &middot; &larr;/&rarr; engine pair</span></div>
<div id="tabs" role="tablist" aria-label="Directions"></div>
<div id="stage">
<div class="pane" id="pane-0"><div class="pane-head"><span class="engname" id="engname-0"></span></div><div class="pane-frame-wrap"><iframe id="frame-0" title="left engine"></iframe><div class="notbuilt" id="notbuilt-0" hidden>not built</div></div><div class="pane-controls" id="controls-0"></div></div>
<div class="pane" id="pane-1"><div class="pane-head"><span class="engname" id="engname-1"></span></div><div class="pane-frame-wrap"><iframe id="frame-1" title="right engine"></iframe><div class="notbuilt" id="notbuilt-1" hidden>not built</div></div><div class="pane-controls" id="controls-1"></div></div>
</div>
<div id="submitbar"><label>overall notes<br><textarea id="overall" rows="2"></textarea></label><button type="button" id="submitbtn">submit</button><span id="status"></span></div>
<script>
(function(){
'use strict';
var STATE={board:null,cellsExist:{},active:null,winStart:0,ratings:{},comments:{},remix:{},preferred:null};
function $(s){return document.querySelector(s)}
function ck(d,e){return d+'-'+e}
function esc(s){return (s||'').replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function post(payload){return fetch('/api/feedback',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})}
fetch('/api/state').then(function(r){return r.json()}).then(init);
function init(data){
  STATE.board=data.board; STATE.cellsExist=data.cellsExist; STATE.active=data.board.directions[0].id;
  $('#brief').textContent=(data.board.brief||'').slice(0,140); render();
  document.addEventListener('keydown', onKey); $('#submitbtn').addEventListener('click', submitFeedback);
}
function renderTabs(){
  var tabs=$('#tabs'); tabs.innerHTML='';
  STATE.board.directions.slice(0,5).forEach(function(d,i){
    var b=document.createElement('button');
    b.type='button'; b.setAttribute('role','tab'); b.setAttribute('aria-selected', String(d.id===STATE.active));
    b.textContent=(i+1)+' '+d.name+(d.lane?' — '+d.lane:'');
    b.addEventListener('click', function(){STATE.active=d.id; render()});
    tabs.appendChild(b);
  });
}
function engPair(){
  var eng=STATE.board.engines, n=eng.length, a=STATE.winStart%n, b=(STATE.winStart+1)%n;
  if(n<2) b=a;
  return [eng[a], eng[b]];
}
function render(){ renderTabs(); var pair=engPair(); renderPane(0, pair[0]); renderPane(1, pair[1]); }
function renderPane(idx, eng){
  var key=ck(STATE.active, eng.id);
  $('#engname-'+idx).textContent=eng.name+' · '+STATE.active;
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
  return '<fieldset><legend>rating</legend>'+stars+'</fieldset>'+
    '<label>comment<br><textarea class="cmt" rows="2">'+esc(c)+'</textarea></label>'+
    '<div class="row"><label><input type="radio" name="preferred" value="'+key+'" '+(STATE.preferred===key?'checked':'')+'> prefer this</label>'+
    '<button type="button" class="action morelike">more like this</button></div>'+
    '<div class="row">remix &mdash; layout <select class="rmx-l">'+opts+'</select> colour <select class="rmx-c">'+opts+'</select> <button type="button" class="action remix">remix</button></div>';
}
function wireControls(idx, key){
  var pane=$('#pane-'+idx);
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
  var n=parseInt(e.key,10), maxN=Math.min(5,STATE.board.directions.length);
  if(n>=1 && n<=maxN){STATE.active=STATE.board.directions[n-1].id; render(); return}
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

def make_handler(session_dir: Path):
    class Handler(http.server.SimpleHTTPRequestHandler):
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
                self._json(200, {"board": board, "cellsExist": cells_exist(session_dir, board)})
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
    args = ap.parse_args()
    session_dir = Path(args.session_dir).resolve()
    load_board(session_dir)  # fail fast if board.json is missing/invalid
    (session_dir / "board.html").write_text(TEMPLATE, encoding="utf-8")
    handler = functools.partial(make_handler(session_dir), directory=str(session_dir))
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
