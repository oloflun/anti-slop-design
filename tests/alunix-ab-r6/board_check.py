"""Screenshot the r6 board: default (pair) view, then fullscreen via key x. Stdlib + Playwright."""
import sys, time, json, urllib.request, pathlib
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
out = pathlib.Path(__file__).resolve().parent / "review" / "board"
out.mkdir(parents=True, exist_ok=True)
url = "http://127.0.0.1:4624/board.html"
for _ in range(20):
    try:
        state = json.load(urllib.request.urlopen("http://127.0.0.1:4624/api/state", timeout=2)); break
    except Exception:
        time.sleep(1)
else:
    sys.exit("board server not up")
print("cellsExist:", state.get("cellsExist"))
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1600, "height": 900})
    pg.goto(url); pg.wait_for_timeout(4000)
    pg.screenshot(path=str(out / "board-pair.png"))
    pg.keyboard.press("2"); pg.wait_for_timeout(3000)
    pg.screenshot(path=str(out / "board-k2-pair.png"))
    pg.mouse.move(400, 500); pg.keyboard.press("x"); pg.wait_for_timeout(1500)
    pg.screenshot(path=str(out / "board-fullscreen.png"))
    pg.keyboard.press("Escape"); pg.wait_for_timeout(500)
    print("topbar hidden in fullscreen:", pg.evaluate("document.body.classList.contains('fs')"), "(after Esc should be False)")
    b.close()
print("ok", out)
