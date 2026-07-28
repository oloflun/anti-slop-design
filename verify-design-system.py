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
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HOOKS = Path.home() / ".claude" / "hooks"
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

    print("\n-- settings wiring --")
    try:
        st = json.loads((Path.home() / ".claude" / "settings.json")
                        .read_text(encoding="utf-8"))
        cmds = [h.get("command", "") for arr in st.get("hooks", {}).values()
                for b in arr for h in b.get("hooks", [])]
        for want in ("design-gate.py", "design-route.py", "design-telemetry.py",
                     "design-verify-gate.py", "design-stop.py", "design-intent.py"):
            check(f"wired: {want}", any(want in c for c in cmds))
        check("CARL preserved", any("carl-hook.py" in c for c in cmds))
        check("gstack hooks preserved",
              sum("gstack" in c for c in cmds) >= 3)
    except Exception as e:
        check("settings.json parses", False, str(e))

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
        hso, _ = run_hook("design-stop.py", {"cwd": td})
        summ = (hso or {}).get("additionalContext", "")
        check("stop renders the ledger report", "design session" in summ)
        check("stop measures the route gap", "gap" in summ.lower())
        reports = list((Path(td) / ".impeccable").glob("design-report-*.md"))
        check("report file written", bool(reports))
        if reports:
            body = reports[0].read_text(encoding="utf-8")
            for sec in ("Component → skills", "Route-vs-invocation gap",
                        "Coverage", "Gate activity", "Trap firings", "Timeline"):
                check(f"report section: {sec}", sec in body)

    print("\n-- behaviour: verb routing --")
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        cases = [
            ("redesign", "redesign the pricing page", "REDESIGN"),
            ("audit", "audit the design", "AUDIT"),
            ("polish", "polish the nav", "POLISH"),
            ("explore", "show me some design options", "EXPLORE"),
            ("system", "create a design system", "SYSTEM"),
            ("build", "build a landing page", "BUILD"),
        ]
        for verb, prompt, marker in cases:
            hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": prompt})
            ctx = (hso or {}).get("additionalContext", "")
            check(f"verb '{verb}' routes correctly", marker in ctx)
        # re-fire on change, silence on repeat
        run_hook("design-intent.py", {"cwd": td, "prompt": "redesign it"})
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "redesign it again"})
        check("same verb twice = silent", hso is None)
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "now audit the design"})
        check("verb change re-fires", "Task type changed" in (hso or {}).get("additionalContext", ""))
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "gör om hela sidan"})
        check("Swedish verb detected", "REDESIGN" in (hso or {}).get("additionalContext", ""))

    print("\n-- behaviour: prose-only DESIGN.md must not false-lock --")
    PROSE = "# Design System\n## Colors\n- Ink #0B0B0C primary\n"
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
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
