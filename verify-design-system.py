#!/usr/bin/env python
"""Mechanical verification for the design hook chain.

Run after any change to the hooks, the routing table, or the skills:

    python verify-design-system.py

Covers everything that can be checked without a live model in the loop.
Gate-order judgment, inheritance, the targeted-change rule and the copy gate
are model behaviour and are verified by the telemetry report of a real build,
not here.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# The report text below uses non-ASCII (→, —). On Windows the console's
# default codepage is cp1252, not UTF-8, so a bare print() of those
# characters raises UnicodeEncodeError and kills the run partway through —
# this reconfigures OUR OWN stdout/stderr, independent of the utf-8 env
# passed to hook subprocesses below.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# The copy that actually runs is the plugin's own checkout, loaded into the
# session via ${CLAUDE_PLUGIN_ROOT} — not a ~/.claude/hooks mirror. Testing
# the wrong copy is how a fix here can pass while the live chain stays
# broken.
HOOKS = Path.home() / "super-intelligence" / "hooks"
SKILLS = Path.home() / ".agents" / "skills"
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}

PASS, FAIL = [], []


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def run_hook(hook: str, event: dict, env: dict | None = None):
    p = subprocess.run(
        [sys.executable, str(HOOKS / hook)],
        input=json.dumps(event), capture_output=True, text=True,
        encoding="utf-8", env={**ENV, **(env or {})},
    )
    if not p.stdout.strip():
        return None, p.stderr
    try:
        return json.loads(p.stdout)["hookSpecificOutput"], p.stderr
    except Exception:
        return None, p.stderr


def write_ev(root: str, name: str, content: str) -> dict:
    return {"cwd": root, "tool_name": "Write",
            "tool_input": {"file_path": str(Path(root) / name), "content": content}}


DESIGN_MD = """---
name: VerifyFixture
description: fixture
colors:
  ink: "#0B0B0C"
  paper: "#F5F3EF"
  accent: "#F27722"
typography:
  display:
    fontFamily: "Afacad"
    fontSize: "72px"
  body:
    fontFamily: "Source Serif 4"
    fontSize: "17px"
rounded:
  card: "5px"
---
# Design
"""


def main() -> int:
    print("=" * 66)
    print("DESIGN SYSTEM VERIFICATION")
    print("=" * 66)

    print("\n-- install --")
    for f in ("design_hook_lib.py", "design-gate.py", "design-route.py",
              "design-telemetry.py", "design-verify-gate.py",
              "design-stop.py", "design-intent.py"):
        check(f"hook present: {f}", (HOOKS / f).exists())
    for s in ("design", "design-verify", "brand-system", "impeccable",
              "humanizer", "copywriting", "emil-design-eng",
              "animated-navigation"):
        check(f"skill present: {s}", (SKILLS / s / "SKILL.md").exists())

    ver = ""
    try:
        ver = next(l for l in (SKILLS / "impeccable" / "SKILL.md")
                   .read_text(encoding="utf-8").splitlines()
                   if l.startswith("version:"))
    except Exception:
        pass
    check("impeccable is v4", "4." in ver, ver or "no version field")

    print("\n-- plugin --")
    PLUGIN_ROOT = Path(__file__).resolve().parent
    DESIGN_HOOK_FILES = (
        "design-intent.py", "design-gate.py", "design-verify-gate.py",
        "design-route.py", "design-telemetry.py", "design-vision-track.py",
        "design-session-start.py", "design-stop.py",
    )

    try:
        pj = json.loads((PLUGIN_ROOT / ".claude-plugin" / "plugin.json")
                         .read_text(encoding="utf-8"))
        check("plugin.json parses", True)
        check("plugin.json name is anti-slop-design", pj.get("name") == "anti-slop-design")
    except Exception as e:
        check("plugin.json parses", False, str(e))

    try:
        mj = json.loads((PLUGIN_ROOT / ".claude-plugin" / "marketplace.json")
                         .read_text(encoding="utf-8"))
        check("marketplace.json parses", True)
        plugins = mj.get("plugins", [])
        check("marketplace.json has exactly one plugin", len(plugins) == 1,
              f"{len(plugins)} plugins")
        check("marketplace.json plugin source is '.'",
              bool(plugins) and plugins[0].get("source") == ".")
    except Exception as e:
        check("marketplace.json parses", False, str(e))

    plugin_hooks_dir = PLUGIN_ROOT / "hooks"
    try:
        ph = json.loads((plugin_hooks_dir / "hooks.json").read_text(encoding="utf-8"))
        entries = [h for arr in ph.get("hooks", {}).values()
                   for b in arr for h in b.get("hooks", [])]
        check("plugin hooks.json has exactly 8 entries", len(entries) == 8,
              f"{len(entries)} entries")
        missing = []
        for h in entries:
            m = re.search(r'hooks/([\w.-]+\.py)"', h.get("command", ""))
            if not m or not (plugin_hooks_dir / m.group(1)).exists():
                missing.append(h.get("command", "<no command>"))
        check("all plugin hook entries point at files that exist in hooks/",
              not missing, "; ".join(missing))
    except Exception as e:
        check("plugin hooks.json parses", False, str(e))

    # Until the flip lands, hooks/ here is still a byte-identical mirror of
    # the live source at super-intelligence/hooks — not yet canonical itself.
    diffs = []
    for f in DESIGN_HOOK_FILES + ("design_hook_lib.py",):
        live, mirror = HOOKS / f, plugin_hooks_dir / f
        if not live.exists() or not mirror.exists():
            diffs.append(f"missing:{f}")
        elif live.read_bytes() != mirror.read_bytes():
            diffs.append(f"differ:{f}")
    check("plugin hooks byte-identical to super-intelligence/hooks",
          not diffs, "; ".join(diffs))

    print("\n-- mirror --")
    sync_script = Path(__file__).resolve().parent / "scripts" / "sync-from-live.py"
    p = subprocess.run([sys.executable, str(sync_script), "--check"],
                        capture_output=True, text=True, encoding="utf-8", env=ENV)
    first_line = next((l for l in p.stdout.splitlines() if l.strip()), "")
    check("repo == live (scripts/sync-from-live.py --check)", p.returncode == 0, first_line)

    print("\n-- settings wiring --")
    try:
        st = json.loads((HOOKS / "hooks.json").read_text(encoding="utf-8"))
        cmds = [h.get("command", "") for arr in st.get("hooks", {}).values()
                for b in arr for h in b.get("hooks", [])]
        for want in ("design-gate.py", "design-route.py", "design-telemetry.py",
                     "design-verify-gate.py", "design-stop.py", "design-intent.py"):
            check(f"wired: {want}", any(want in c for c in cmds))
        check("CARL preserved", any("carl-hook.py" in c for c in cmds))
        check("gstack hooks preserved",
              sum("gstack" in c for c in cmds) >= 3)
    except Exception as e:
        check("hooks.json parses", False, str(e))

    print("\n-- routing table --")
    sys.path.insert(0, str(HOOKS))
    import design_hook_lib as L  # noqa: E402
    t = L.routing_table()
    check("routing table parsed from reference", len(t.get("rules", [])) >= 10,
          f"{len(t.get('rules', []))} rules")
    check("ui extensions loaded", len(t.get("ui_extensions", [])) >= 10)
    check("trap palettes loaded", len(t.get("trap_hexes", {})) == 3)

    print("\n-- reference fidelity --")
    # Unique dir per run. A fixed path races with Windows file locks left by a
    # previous clone, which shows up as a spurious fidelity failure.
    up = Path(tempfile.mkdtemp(prefix="hallmark-verify-")) / "src"
    cloned = subprocess.run(
        ["git", "clone", "--depth", "1", "-q",
         "https://github.com/Nutlope/hallmark.git", str(up)],
        capture_output=True, text=True).returncode == 0
    if cloned:
        src = up / "skills" / "hallmark" / "references"
        for label, dst in (("repo", Path.home() / "anti-slop-design" / "skills"
                            / "design" / "references"),
                           ("live", SKILLS / "design" / "references")):
            d = subprocess.run(["diff", "-rq", str(src), str(dst)],
                               capture_output=True, text=True).stdout
            differ = [l for l in d.splitlines() if "differ" in l]
            missing = [l for l in d.splitlines() if l.startswith(f"Only in {src}")]
            check(f"{label}: ported refs byte-identical", not differ,
                  f"{len(differ)} differ")
            check(f"{label}: no upstream refs missing", not missing,
                  f"{len(missing)} missing")
        shutil.rmtree(up.parent, ignore_errors=True)
    else:
        check("upstream clone for fidelity diff", False, "network unavailable")

    print("\n-- behaviour: locked project --")
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "DESIGN.md").write_text(DESIGN_MD, encoding="utf-8")
        (Path(td) / "components").mkdir()
        # UI evidence for classify()'s project-signal cap — this fixture's
        # intent-detection call later on needs "designa om hero" to resolve
        # to "high", not capped to "medium" for lack of a real react/html
        # file on disk (the route/gate calls above only simulate a write via
        # a synthetic event; nothing here actually lands on disk).
        (Path(td) / "package.json").write_text(
            '{"dependencies":{"react":"18.2.0"}}', encoding="utf-8")
        # Arm/disarm (idea-2ao follow-up): design-route.py only emits into
        # context when the session is armed. This fixture exercises the
        # router directly (path-matched routes, which never auto-arm — only
        # a strong CODE match does), so arm it explicitly rather than
        # depending on call order.
        L.arm(Path(td), "verify")

        hso, _ = run_hook("design-route.py", write_ev(
            td, "components/Nav.tsx",
            'export function Nav(){return <nav className="topbar">Hem</nav>}'))
        ctx = (hso or {}).get("additionalContext", "")
        check("routes nav -> animated-navigation", "animated-navigation" in ctx)
        check("declares tier 0 in locked project", "tier 0" in ctx)

        hso, _ = run_hook("design-route.py", write_ev(
            td, "components/Drawer.tsx",
            "export function D(){const g=useGesture();return <div onDrag={g}/>}"))
        check("routes drag -> emil-design-eng",
              "emil-design-eng" in (hso or {}).get("additionalContext", ""))

        hso, _ = run_hook("design-gate.py", write_ev(
            td, "components/Bad.tsx",
            'export function B(){return <div style={{background:"#F7F6F3",'
            'fontFamily:"Poppins",borderRadius:"14px"}}/>}'),
            {"DESIGN_GATE_BLOCKING": "1"})
        reason = (hso or {}).get("permissionDecisionReason", "")
        check("gate DENIES contract violation",
              (hso or {}).get("permissionDecision") == "deny")
        check("gate 60 catches demoted-skill hex", "gate-60" in reason)
        check("detector catches undeclared font", "design-system-font" in reason)
        check("detector catches off-scale radius (exact-values)",
              "design-system-radius" in reason)
        check("denial names the locked tokens", "#f27722" in reason.lower())

        hso, _ = run_hook("design-gate.py", write_ev(
            td, "components/Good.tsx",
            'export function G(){return <div style={{background:"var(--paper)",'
            'borderRadius:"5px",fontFamily:"var(--font-body)"}}/>}'),
            {"DESIGN_GATE_BLOCKING": "1"})
        check("gate allows a token-only write", hso is None)

        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "designa om hero"})
        ctx = (hso or {}).get("additionalContext", "")
        check("intent fires on Swedish", "TIER 0" in ctx)
        check("intent injects real token values", "#f27722" in ctx.lower())

        run_hook("design-telemetry.py",
                 {"cwd": td, "tool_name": "Skill",
                  "tool_input": {"skill": "animated-navigation"}})

        # The exit bar: edits with no rendered image Read afterwards must
        # BLOCK the stop. Raw parse — the block is top-level JSON, not
        # hookSpecificOutput.
        p = subprocess.run(
            [sys.executable, str(HOOKS / "design-stop.py")],
            input=json.dumps({"cwd": td}), capture_output=True, text=True,
            encoding="utf-8", env=ENV)
        try:
            blocked = json.loads(p.stdout).get("decision") == "block"
        except Exception:
            blocked = False
        check("stop BLOCKS an unseen build", blocked)

        # Reading a render (any image) satisfies the bar and the stop passes.
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read",
                  "tool_input": {"file_path": str(Path(td) / "shot.png")}})
        hso, _ = run_hook("design-stop.py", {"cwd": td})
        summ = (hso or {}).get("additionalContext", "")
        check("stop renders the ledger report", "design session" in summ)
        check("stop measures the route gap", "gap" in summ.lower())
        reports = list((Path(td) / ".impeccable").glob("design-report-*.md"))
        check("report file written", bool(reports))
        if reports:
            body = reports[0].read_text(encoding="utf-8")
            for sec in ("Component → skills", "Unloaded strong routes",
                        "Coverage", "Gate activity", "Trap firings",
                        "Deep detector pass", "Timeline"):
                check(f"report section: {sec}", sec in body)

    print("\n-- behaviour: verb routing --")
    with tempfile.TemporaryDirectory() as td:
        # A design_hook_lib.classify() "high" needs a verb AND an object AND
        # project UI evidence (see "-- behaviour: arm/disarm --" below for the
        # cap itself) — package.json must actually look like a UI project,
        # and every prompt needs a real object word, not just the bare verb
        # phrase some of these used to rely on ("audit the design" has no
        # OBJECT; "design" alone is a medium-tier signal, not an object).
        (Path(td) / "package.json").write_text(
            '{"dependencies":{"react":"18.2.0"}}', encoding="utf-8")
        cases = [
            ("redesign", "redesign the pricing page", "REDESIGN"),
            ("audit", "audit the design of the page", "AUDIT"),
            ("polish", "polish the nav", "POLISH"),
            ("explore", "show me some design options for the landing page", "EXPLORE"),
            ("system", "create a design system for the landing page", "SYSTEM"),
            ("build", "build a landing page", "BUILD"),
        ]
        for verb, prompt, marker in cases:
            hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": prompt})
            ctx = (hso or {}).get("additionalContext", "")
            check(f"verb '{verb}' routes correctly", marker in ctx)
        # re-fire on change, silence on repeat
        run_hook("design-intent.py", {"cwd": td, "prompt": "redesign the hero"})
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "redesign the hero again"})
        check("same verb twice = silent", hso is None)
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "now audit the page"})
        check("verb change re-fires", "Task type changed" in (hso or {}).get("additionalContext", ""))
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "gör om hela sidan"})
        check("Swedish verb detected", "REDESIGN" in (hso or {}).get("additionalContext", ""))

    print("\n-- behaviour: prose-only DESIGN.md must not false-lock --")
    PROSE = "# Design System\n## Colors\n- Ink #0B0B0C primary\n"
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text(
            '{"dependencies":{"react":"18.2.0"}}', encoding="utf-8")
        (Path(td) / "DESIGN.md").write_text(PROSE, encoding="utf-8")
        (Path(td) / "components").mkdir()
        check("tier() reports 0-prose, not 0-locked", L.tier(Path(td)) == "0-prose")
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "redesign the hero"})
        ctx = (hso or {}).get("additionalContext", "")
        check("injects PROSE ONLY warning", "PROSE ONLY" in ctx)
        check("states the gate is blind", "BLIND" in ctx)
        check("does NOT claim LOCKED", "TIER 0 — LOCKED" not in ctx)

    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        (Path(td) / "DESIGN.md").write_text(DESIGN_MD, encoding="utf-8")
        check("tier() reports 0-locked with frontmatter", L.tier(Path(td)) == "0-locked")

    print("\n-- behaviour: product surface vs marketing --")
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        for sub in ("app/dashboard", "app/settings", "app/marketing"):
            (Path(td) / sub).mkdir(parents=True, exist_ok=True)
        # No DESIGN.md here (tier stays "ungated"), so nothing auto-arms —
        # arm explicitly so design-route.py actually emits.
        L.arm(Path(td), "verify")

        hso, _ = run_hook("design-route.py", write_ev(
            td, "app/dashboard/Users.tsx",
            'export function Users(){const t=useReactTable();return <table aria-sort="asc"/>}'))
        ctx = (hso or {}).get("additionalContext", "")
        check("data table routes to Operate mode", "impeccable operate" in ctx)
        check("data table does NOT route to marketing", "design-taste-frontend" not in ctx)

        hso, _ = run_hook("design-route.py", write_ev(
            td, "app/settings/page.tsx", 'export default function S(){return <Sidebar/>}'))
        check("settings routes to Operate mode",
              "impeccable operate" in (hso or {}).get("additionalContext", ""))

        hso, _ = run_hook("design-route.py", write_ev(
            td, "app/marketing/Home.tsx",
            'export function Home(){return <Hero><Pricing/></Hero>}'))
        ctx = (hso or {}).get("additionalContext", "")
        check("marketing routes to design-taste-frontend", "design-taste-frontend" in ctx)
        check("marketing does NOT route to Operate", "impeccable operate" not in ctx)

    print("\n-- behaviour: intent corpus --")
    corpus_path = Path(__file__).resolve().parent / "tests" / "intent_corpus.jsonl"
    try:
        corpus_rows = [json.loads(l) for l in
                       corpus_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    except Exception as e:
        corpus_rows = []
        check("intent corpus loads", False, str(e))

    for row in corpus_rows:
        prompt, expect = row.get("prompt", ""), row.get("expect", "")
        with tempfile.TemporaryDirectory() as td:
            # UI evidence present in every fixture here so the project-signal
            # cap (see below) never masks what classify() itself decided —
            # that cap gets its own dedicated test.
            (Path(td) / "package.json").write_text(
                '{"dependencies":{"react":"18.2.0"}}', encoding="utf-8")
            (Path(td) / "index.html").write_text("<html></html>", encoding="utf-8")
            hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": prompt})
            ctx = (hso or {}).get("additionalContext", "")
            armed_now = (Path(td) / ".impeccable" / ".armed").exists()

            name = f"intent corpus [{expect}]: {prompt[:50]}"
            if expect == "high":
                ok = bool(ctx) and "<design-gate>" in ctx and armed_now
            elif expect == "medium":
                ok = (bool(ctx) and "Skill(design)" in ctx
                      and "<design-gate>" not in ctx and not armed_now)
            else:  # none
                ok = hso is None and not armed_now
            check(name, ok)

    print("\n-- behaviour: arm/disarm --")

    with tempfile.TemporaryDirectory() as td:
        # An empty package.json anchors project_root() at td itself — without
        # SOME marker here, resolution walks past the temp dir and up to
        # whatever real project root the machine's temp dir happens to sit
        # under, which defeats "no UI evidence" and can write test state into
        # a real project. No react/UI files: this fixture needs the ABSENCE
        # of evidence, not the absence of a root marker.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        # An otherwise-"high" prompt must cap to "medium": the nudge line,
        # no <design-gate>, no arm.
        hso, _ = run_hook("design-intent.py",
                           {"cwd": td, "prompt": "designa om heron på startsidan"})
        ctx = (hso or {}).get("additionalContext", "")
        check("project signal caps at medium (no UI evidence)",
              bool(ctx) and "<design-gate>" not in ctx)
        check("capped session does not arm",
              not (Path(td) / ".impeccable" / ".armed").exists())

    with tempfile.TemporaryDirectory() as td:
        # tier stays "ungated" (no DESIGN.md) so nothing auto-arms.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        hso, _ = run_hook("design-route.py", write_ev(
            td, "components/Nav.tsx",
            'export function Nav(){return <nav className="topbar">Hem</nav>}'))
        check("unarmed session: route silent", hso is None)

        hso, _ = run_hook("design-verify-gate.py",
                           {"cwd": td, "tool_name": "mcp__Claude_Browser__computer",
                            "tool_input": {}})
        check("unarmed session: verify-gate silent", hso is None)

        p = subprocess.run(
            [sys.executable, str(HOOKS / "design-stop.py")],
            input=json.dumps({"cwd": td}), capture_output=True, text=True,
            encoding="utf-8", env=ENV)
        check("unarmed session: stop does not block", '"decision"' not in p.stdout)
        try:
            hso = json.loads(p.stdout)["hookSpecificOutput"]
        except Exception:
            hso = None
        summ = (hso or {}).get("additionalContext", "")
        check("unarmed session: stop is advisory-only", "armad designsession" in summ)
        reports = list((Path(td) / ".impeccable").glob("design-report-*.md"))
        check("unarmed session: no report file written", not reports)

    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        L.arm(Path(td), "verify")
        hso, _ = run_hook("design-route.py", write_ev(
            td, "components/Nav.tsx",
            'export function Nav(){return <nav className="topbar">Hem</nav>}'))
        check("armed session: route emits",
              "animated-navigation" in (hso or {}).get("additionalContext", ""))

    with tempfile.TemporaryDirectory() as td:
        # A 0-locked project with a genuinely strong (code-matched) route
        # auto-arms even without an intent prompt or a Skill() call.
        (Path(td) / "DESIGN.md").write_text(DESIGN_MD, encoding="utf-8")
        (Path(td) / "components").mkdir()
        check("0-locked project starts unarmed", not L.armed(Path(td)))
        hso, _ = run_hook("design-route.py", write_ev(
            td, "components/Foo.tsx",
            'export function Foo(){const g=useGesture();'
            'return <div onDrag={g} className="x"/>}'))
        check("strong code route on 0-locked auto-arms",
              "emil-design-eng" in (hso or {}).get("additionalContext", ""))
        check("auto-arm persisted", L.armed(Path(td)))

    with tempfile.TemporaryDirectory() as td:
        # react-components is a FRAMEWORK skill (routes on generic structure,
        # not craft) — a code-matched route to it must never count against
        # the gap, even with nothing ever invoking or reading it.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        L.arm(Path(td), "verify")
        hso, _ = run_hook("design-route.py", write_ev(
            td, "src/Foo.tsx",
            'export function Foo(){const [x,setX]=useState(0);return <div>{x}</div>;}'))
        check("framework route emits",
              "react-components" in (hso or {}).get("additionalContext", ""))
        # Ledger timestamps are second-resolution; exit_bar_block requires
        # the vision row to be STRICTLY newer than the edit row, so a sub-
        # second gap between the two hook calls above and this one is a race.
        time.sleep(1.1)
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read",
                  "tool_input": {"file_path": str(Path(td) / "shot.png")}})
        hso, _ = run_hook("design-stop.py", {"cwd": td})
        summ = (hso or {}).get("additionalContext", "")
        check("framework route never counts as gap",
              "Route gap (strong, craft only) = 0" in summ)

    with tempfile.TemporaryDirectory() as td:
        # Reading the routed skill's own SKILL.md closes the gap the same
        # way a Skill() invocation does.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        L.arm(Path(td), "verify")
        hso, _ = run_hook("design-route.py", write_ev(
            td, "components/Foo.tsx",
            'export function Foo(){const g=useGesture();'
            'return <div onDrag={g} className="x"/>}'))
        check("interaction route emits",
              "emil-design-eng" in (hso or {}).get("additionalContext", ""))
        skill_md = SKILLS / "emil-design-eng" / "SKILL.md"
        # See the sleep note above — same second-resolution timestamp race.
        time.sleep(1.1)
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read",
                  "tool_input": {"file_path": str(skill_md)}})
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read",
                  "tool_input": {"file_path": str(Path(td) / "shot.png")}})
        hso, _ = run_hook("design-stop.py", {"cwd": td})
        summ = (hso or {}).get("additionalContext", "")
        check("skill-read closes the gap", "Route gap (strong, craft only) = 0" in summ)

    with tempfile.TemporaryDirectory() as td:
        # Section 6 must render even with zero detector findings — a section
        # that only appears when it has findings is indistinguishable from
        # one that never ran.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        L.arm(Path(td), "verify")
        run_hook("design-route.py", write_ev(
            td, "components/Clean.tsx",
            'export function Clean(){return <div className="ok">hi</div>}'))
        # See the sleep note above — same second-resolution timestamp race.
        time.sleep(1.1)
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read",
                  "tool_input": {"file_path": str(Path(td) / "shot.png")}})
        run_hook("design-stop.py", {"cwd": td})
        reports = list((Path(td) / ".impeccable").glob("design-report-*.md"))
        body = reports[0].read_text(encoding="utf-8") if reports else ""
        check("report always has section 6", bool(reports) and "## 6. Deep detector pass" in body)

    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        hso, _ = run_hook("design-route.py", write_ev(
            td, "components/Nav.tsx",
            'export function Nav(){return <nav className="topbar">Hem</nav>}'),
            {"DESIGN_HOOKS_FORCE_ARM": "1"})
        check("FORCE_ARM env arms",
              "animated-navigation" in (hso or {}).get("additionalContext", ""))

    print("\n-- behaviour: false positives --")
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        cases = [
            ("gate silent on unlocked project", "design-gate.py",
             write_ev(td, "page.tsx", 'const c="#7C3AED"')),
            ("gate silent on non-UI file", "design-gate.py",
             write_ev(td, "notes.txt", "#F7F6F3")),
            ("gate silent on Bash", "design-gate.py",
             {"cwd": td, "tool_name": "Bash", "tool_input": {"command": "ls"}}),
            ("gate silent on Read", "design-gate.py",
             {"cwd": td, "tool_name": "Read", "tool_input": {"file_path": "a.tsx"}}),
            ("route silent on markdown", "design-route.py",
             write_ev(td, "README.md", "# x")),
            ("intent silent on backend prompt", "design-intent.py",
             {"cwd": td, "prompt": "refactor the supabase client"}),
            ("stop silent with no design work", "design-stop.py", {"cwd": td}),
        ]
        for label, hook, ev in cases:
            hso, err = run_hook(hook, ev, {"DESIGN_GATE_BLOCKING": "1"})
            check(label, hso is None, (err or "").strip()[:60])

    print("\n-- kill switch --")
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "DESIGN.md").write_text(DESIGN_MD, encoding="utf-8")
        for hook in ("design-gate.py", "design-route.py"):
            hso, _ = run_hook(hook, write_ev(td, "a.tsx", 'x="#F7F6F3"'),
                              {"DESIGN_HOOKS_DISABLED": "1",
                               "DESIGN_GATE_BLOCKING": "1"})
            check(f"DESIGN_HOOKS_DISABLED silences {hook}", hso is None)

    print("\n" + "=" * 66)
    print(f"{len(PASS)} passed, {len(FAIL)} failed")
    if FAIL:
        print("\nFAILED:")
        for f in FAIL:
            print("  -", f)
    print("=" * 66)
    print("\nNot covered here (needs a live build — see the telemetry report):")
    print("  gate-order judgment · inheritance · targeted-change rule")
    print("  copy gate output · design-verify inspection quality")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
