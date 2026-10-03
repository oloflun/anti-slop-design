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
# broken. The design hooks moved out of super-intelligence and into this
# repo (2026-09-04) — this repo's own hooks/ IS the plugin checkout now,
# not a mirror of an external source, so HOOKS points here directly.
PLUGIN_ROOT = Path(__file__).resolve().parent
HOOKS = PLUGIN_ROOT / "hooks"
SKILLS = Path.home() / ".agents" / "skills"
os.environ.setdefault("CLAUDE_CODE_SESSION_ID", "verify-session-0001")
SID8 = os.environ["CLAUDE_CODE_SESSION_ID"][:8]
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
        # 2026-09-27: "." made `claude plugin update` copy the whole repo
        # (3.4 GB per version) into the plugin cache; the slim build is ~11 MB.
        check("marketplace.json plugin source is './dist/plugin'",
              bool(plugins) and plugins[0].get("source") == "./dist/plugin")
        import subprocess
        fresh = subprocess.run([sys.executable, str(PLUGIN_ROOT / "scripts" / "build-plugin.py"), "--check"],
                               capture_output=True, text=True)
        check("dist/plugin is built from the current skills/hooks/agents", fresh.returncode == 0,
              fresh.stdout.strip()[:200])
    except Exception as e:
        check("marketplace.json parses", False, str(e))

    plugin_hooks_dir = PLUGIN_ROOT / "hooks"
    try:
        ph = json.loads((plugin_hooks_dir / "hooks.json").read_text(encoding="utf-8"))
        entries = [h for arr in ph.get("hooks", {}).values()
                   for b in arr for h in b.get("hooks", [])]
        # 10 since T12 (2026-09-08): the two generation matchers, one on
        # PreToolUse for the credit gate and one on PostToolUse for the ledger.
        # The count is asserted rather than bounded so a hook added by accident
        # still shows up as a failure.
        # 11 since 2026-09-09: the Bash|PowerShell matcher on PreToolUse, after
        # the r8 probe authored its UI file through a heredoc and bypassed
        # every Write/Edit-keyed gate (tests/hooks/test_shell_write_gate.py).
        check("plugin hooks.json has exactly 12 entries", len(entries) == 12,  # +1 2026-09-25: mcp__inspo__|mcp__ui-skills__ ledger matcher
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

    # hooks/ here IS the canonical source now (design hooks moved out of
    # super-intelligence 2026-09-04) — nothing external to byte-compare it
    # against any more. Every hook file existing is already covered by the
    # "hook present" checks in -- install -- above (HOOKS == plugin_hooks_dir)
    # and by the hooks.json entry check just above.

    print("\n-- mirror --")
    sync_script = Path(__file__).resolve().parent / "scripts" / "sync-from-live.py"
    p = subprocess.run([sys.executable, str(sync_script), "--check"],
                        capture_output=True, text=True, encoding="utf-8", env=ENV)
    first_line = next((l for l in p.stdout.splitlines() if l.strip()), "")
    check("repo == live (scripts/sync-from-live.py --check)", p.returncode == 0, first_line)

    print("\n-- settings wiring --")
    # The plugin's own hooks.json (HOOKS/hooks.json) is self-contained — just
    # the 8 design-hook registrations, loaded into a session via
    # ${CLAUDE_PLUGIN_ROOT}. It never carries carl-hook.py or the gstack
    # hooks, so those are no longer checked against it.
    try:
        st = json.loads((HOOKS / "hooks.json").read_text(encoding="utf-8"))
        cmds = [h.get("command", "") for arr in st.get("hooks", {}).values()
                for b in arr for h in b.get("hooks", [])]
        for want in ("design-gate.py", "design-route.py", "design-telemetry.py",
                     "design-verify-gate.py", "design-stop.py", "design-intent.py"):
            check(f"wired: {want}", any(want in c for c in cmds))
    except Exception as e:
        check("plugin hooks.json parses (wiring)", False, str(e))

    # The other half of the split: super-intelligence's own hooks.json must
    # have lost every design-* reference while keeping CARL and the gstack
    # hooks intact. Skipped (not failed) if that checkout isn't present —
    # this machine-specific path isn't guaranteed to exist for every runner.
    si_hooks = Path.home() / "super-intelligence" / "hooks" / "hooks.json"
    if si_hooks.exists():
        try:
            st = json.loads(si_hooks.read_text(encoding="utf-8"))
            cmds = [h.get("command", "") for arr in st.get("hooks", {}).values()
                    for b in arr for h in b.get("hooks", [])]
            check("super-intelligence hooks.json has no design-* entries",
                  not any("design-" in c or "design_" in c for c in cmds),
                  "; ".join(c for c in cmds if "design-" in c or "design_" in c))
            check("super-intelligence: CARL preserved", any("carl-hook.py" in c for c in cmds))
            check("super-intelligence: gstack hooks preserved",
                  sum("gstack" in c for c in cmds) >= 3)
        except Exception as e:
            check("super-intelligence hooks.json parses", False, str(e))

    print("\n-- routing table --")
    sys.path.insert(0, str(HOOKS))
    import design_hook_lib as L  # noqa: E402
    t = L.routing_table()
    check("routing table parsed from reference", len(t.get("rules", [])) >= 10,
          f"{len(t.get('rules', []))} rules")
    check("ui extensions loaded", len(t.get("ui_extensions", [])) >= 10)
    check("trap palettes loaded", len(t.get("trap_hexes", {})) == 3)

    print("\n-- canonical DESIGN.md writer --")
    # T11. Five skills write a file called DESIGN.md in three incompatible
    # formats, and design-gate.py reads it to enforce the token contract. The
    # ambiguity is only safe while exactly one writer is named canonical, so
    # that claim gets a mechanical check rather than living in prose alone.
    orch = (SKILLS / "design" / "references" / "skill-orchestration.md").read_text(encoding="utf-8")
    canon = [ln for ln in orch.splitlines()
             if ln.startswith("|") and "canonical form" in ln]
    check("exactly one DESIGN.md writer is canonical", len(canon) == 1,
          f"{len(canon)} rows claim it")
    check("the canonical writer is `impeccable document`",
          bool(canon) and "impeccable document" in canon[0])
    check("design-md is demoted to Stitch-import", "Stitch-import" in orch)

    print("\n-- reviewer contract --")
    # T10. The quartet's five-section contract is only worth writing down if
    # something rejects a report that breaks it. design-stop.py cannot: it reads
    # ledger rows and a reviewer's text never lands there. The report is a file
    # the lead reads, so the gate is a file gate (scripts/check_reviewer_report.py).
    sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))
    from check_reviewer_report import check as _rc  # noqa: E402
    _good = ("fix\n\n## persistence\nRead this run.\n\n## fidelity\ns1 matches.\n\n"
             "## ceiling\n- garden-eight: slår. Silence is longer than ours.\n\n"
             "## material_fixes\n- Plate offset 40 -> 0 px.\n\n## keep\nThe single accent.\n")
    check("well-formed reviewer report passes", not _rc(_good))
    check("report without a disposition word is rejected",
          bool(_rc(_good.replace("fix\n", "Here is my review.\n", 1))))
    check("report missing a contract section is rejected",
          bool(_rc(_good.replace("## ceiling", "## celing"))))
    check("report with a sixth section is rejected",
          bool(_rc(_good + "\n## recommendations\nWarmer paper.\n")))
    check("reviewer raising reduced motion is rejected (F-011)",
          bool(_rc(_good + "\nAdd a prefers-reduced-motion fallback.\n")))

    print("\n-- shell write gate --")
    # r8 probe (2026-09-09): a builder wrote its UI file with `cat > x.html`
    # and the whole Write/Edit-keyed chain saw nothing. The gate now covers
    # Bash|PowerShell; both directions, because a gate that also fires on
    # copying the scroll engine would block a legitimate step in every round.
    _heredoc = "cat > runs/K3/index.html <<'EOF'\n<h1>x</h1>\nEOF"
    check("heredoc into .html is detected as shell authoring",
          L.shell_ui_write_targets(_heredoc) == ["runs/K3/index.html"])
    check("cp of the engine css is not (copy, not authoring)",
          L.shell_ui_write_targets("cp scripts/scroll/scrollcraft.css runs/K3/scroll/") == [])
    check("redirect into a .txt is not a UI write",
          L.shell_ui_write_targets("echo hi > NOTES.txt") == [])
    _td = tempfile.mkdtemp(prefix="shellgate-verify-")
    _ev = {"cwd": _td, "tool_name": "Bash", "tool_input": {"command": _heredoc}}
    hso, _ = run_hook("design-gate.py", _ev, env={"DESIGN_HOOKS_FORCE_ARM": "1"})
    check("armed session: shell UI write is denied",
          bool(hso) and hso.get("permissionDecision") == "deny"
          and "skalskrivning" in hso.get("permissionDecisionReason", ""))
    hso, _ = run_hook("design-gate.py", _ev, env={"DESIGN_HOOKS_FORCE_ARM": ""})
    check("unarmed session: shell UI write only warns",
          bool(hso) and hso.get("permissionDecision") != "deny"
          and "skalskrivning" in hso.get("additionalContext", ""))
    check("Bash|PowerShell matcher is wired in hooks.json",
          any(e.get("matcher") == "Bash|PowerShell"
              for e in json.loads((HOOKS / "hooks.json").read_text(encoding="utf-8"))["hooks"]["PreToolUse"]))

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

            # Deliberate divergences from upstream hallmark. The chain is a
            # fork with an owner's overrides on it, so "byte-identical" is the
            # wrong bar; "identical except where we wrote down why" is the
            # right one. A file may diverge only if it is named here AND the
            # local copy actually carries the marker that explains it, so a
            # future accidental edit to one of these files still fails.
            ALLOWED_DIVERGENCE = {
                # F-011 (2026-09-07): motion always plays. Every
                # prefers-reduced-motion mandate and code block was struck.
                "assets.md": "F-011", "custom-craft.md": "F-011",
                "custom-theme.md": "F-011", "hero-enrichment.md": "F-011",
                "microinteractions.md": "F-011", "motion.md": "F-011",
                "preview-examples.md": "F-011", "slop-test.md": "F-011",
                "ft8-marquee-scroll.md": "F-011", "n8-terminal-command.md": "F-011",
                "h7-demo-video-clipped-by-viewport-edge.md": "F-011",
                "playful.md": "F-011", "carnival.md": "F-011", "cobalt.md": "F-011",
                "hum.md": "F-011", "lumen.md": "F-011",
                # Pre-existing drift, corrected 2026-09-08: the local line
                # said the nav archetypes were N1-N9 while components/ has
                # shipped n1..n13 (plus n1b) for some time. Upstream says
                # N1a-N13; the chain names its own files.
                "macrostructures.md": "N1–N13",
                # T6 (2026-09-09): the v4 plan's port lists, sections 2.1-2.5,
                # moved material out of impeccable, taste-skill, emilkowalski,
                # refero, interfaces, inclusive and designpowers into these
                # files. Upstream Hallmark stopped being the bar for them the
                # moment that happened, so each carries a note saying so and
                # naming the winner wherever a port collided with a rule
                # already there.
                "color.md": "T6 port", "copy.md": "T6 port",
                "interaction-and-states.md": "T6 port",
                "layout-and-space.md": "T6 port",
                "responsive.md": "T6 port", "typography.md": "T6 port",
                "redesign.md": "T6 port",
                # F-016/F-018 (2026-09-19/20): descriptive microtext and the page
                # narrating itself, appended as owner rules.
                "anti-patterns.md": "F-016",
            }
            unexplained = []
            for line in differ:
                name = Path(line.split(" and ")[0].replace("Files ", "").strip().strip("'\"")).name
                marker = ALLOWED_DIVERGENCE.get(name)
                if not marker:
                    unexplained.append(f"{name} (no recorded reason)")
                    continue
                try:
                    body = (Path(dst) / name).read_text(encoding="utf-8", errors="replace")
                except Exception:
                    body = ""
                    for cand in Path(dst).rglob(name):
                        body = cand.read_text(encoding="utf-8", errors="replace"); break
                if marker not in body:
                    unexplained.append(f"{name} (diverges but carries no {marker} note)")
            check(f"{label}: ported refs identical except recorded divergences",
                  not unexplained,
                  "; ".join(unexplained[:6]))
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
            armed_now = (Path(td) / ".impeccable" / f".armed-{SID8}").exists()

            name = f"intent corpus [{expect}]: {prompt[:50]}"
            if expect == "high":
                ok = bool(ctx) and "<design-gate>" in ctx and armed_now
            elif expect == "medium":
                ok = (bool(ctx) and "Skill(design)" in ctx
                      and "<design-gate>" not in ctx and not armed_now)
            else:  # none
                ok = hso is None and not armed_now
            if row.get("scroll"):
                ok = ok and "SCROLL —" in ctx
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
              not (Path(td) / ".impeccable" / f".armed-{SID8}").exists())

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
        # A motion contact sheet is its own kind, so the showcase floor can count it.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        sheet = Path(td) / "design-catalogue" / "entries" / "acme" / "motion" / "sheet.webp"
        sheet.parent.mkdir(parents=True)
        sheet.write_bytes(b"RIFF")
        L.arm(Path(td), "verify")
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read", "tool_input": {"file_path": str(sheet)}})
        rows = [r for r in L.all_rows(Path(td)) if r.get("event") == "ref-read"]
        check("vision-track logs entries/<slug>/motion/sheet.webp as kind motion-sheet",
              any(r.get("kind") == "motion-sheet" and r.get("slug") == "acme" for r in rows))
        # r37 (2026-10-03): a builder in the repo reads the plugin's own skills/design copy.
        repo_devices = PLUGIN_ROOT / "skills" / "design" / "references" / "scroll" / "devices.md"
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read", "tool_input": {"file_path": str(repo_devices)}})
        rows = [r for r in L.all_rows(Path(td)) if r.get("event") == "ref-read"]
        check("a read of the plugin's own skills/design copy counts as a scroll reference",
              any(r.get("sub") == "scroll" and r.get("file", "").endswith("devices.md") for r in rows))

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

    print("\n-- behaviour: reference floor --")
    with tempfile.TemporaryDirectory() as td:
        # (a) armed greenfield project, empty ledger: the gate denies the
        # first UI write and names every required reference.
        (Path(td) / "package.json").write_text(
            '{"dependencies":{"react":"18.2.0"}}', encoding="utf-8")
        cat_dir = Path(td) / "design-catalogue"
        cat_dir.mkdir()
        (cat_dir / "FEEDBACK.md").write_text("# feedback", encoding="utf-8")
        L.arm(Path(td), "verify")

        hso, _ = run_hook("design-gate.py", write_ev(td, "index.html", "<html></html>"))
        reason = (hso or {}).get("permissionDecisionReason", "")
        check("reference floor denies a greenfield write with an empty ledger",
              (hso or {}).get("permissionDecision") == "deny")
        check("floor names TASTE.md", "TASTE.md" in reason)
        check("floor names FEEDBACK.md", "FEEDBACK.md" in reason)
        check("floor names entries (catalogue example)", "entries" in reason)
        check("floor names reference-lock.md", "reference-lock.md" in reason)
        check("floor names Skill(design)", "Skill(design)" in reason)

        # (b) log synthetic ref-read rows for taste, feedback, one catalogue
        # entry, and the reference lock, plus the skill load — the same
        # write is now allowed.
        L.log(Path(td), event="skill", skill="design", tier="ungated")
        skill_roots = L.design_skill_roots()
        lock_file = (skill_roots[0] / "references" / "reference-lock.md") if skill_roots \
            else Path("references/reference-lock.md")
        L.log(Path(td), event="ref-read", cat="taste", file=str(cat_dir / "TASTE.md"))
        L.log(Path(td), event="ref-read", cat="feedback", file=str(cat_dir / "FEEDBACK.md"))
        L.log(Path(td), event="ref-read", cat="references", file=str(lock_file))

        # T3 (2026-09-08): one file under entries/<slug>/ no longer clears the
        # floor. The gate now wants a catalogue-select row naming >= 2 slugs,
        # and for each of them entry.md plus a fold/slice/shot read.
        L.log(Path(td), event="ref-read", cat="catalogue", slug="acme", kind="shot",
              file=str(cat_dir / "entries" / "acme" / "shot.png"))
        hso, _ = run_hook("design-gate.py", write_ev(td, "index.html", "<html></html>"))
        reason = (hso or {}).get("permissionDecisionReason", "")
        check("floor still denies with one catalogue file and no select row",
              (hso or {}).get("permissionDecision") == "deny")
        check("floor names the catalogue selection step", "select.py" in reason)

        L.log(Path(td), event="catalogue-select", slugs=["acme", "beta"], brief="BRIEF.md")
        hso, _ = run_hook("design-gate.py", write_ev(td, "index.html", "<html></html>"))
        reason = (hso or {}).get("permissionDecisionReason", "")
        check("floor denies when a selected slug is not read through",
              (hso or {}).get("permissionDecision") == "deny" and "beta" in reason)

        for slug in ("acme", "beta"):
            L.log(Path(td), event="ref-read", cat="catalogue", slug=slug, kind="entry-md",
                  file=str(cat_dir / "entries" / slug / "entry.md"))
            L.log(Path(td), event="ref-read", cat="catalogue", slug=slug, kind="fold",
                  file=str(cat_dir / "entries" / slug / "fold.webp"))
        hso, _ = run_hook("design-gate.py", write_ev(td, "index.html", "<html></html>"))
        check("reference floor allows the write once the selection is read through", hso is None)

        # (c) a scroll-signalled intent with no scroll ref-reads names the
        # two scroll references specifically.
        L.log(Path(td), event="intent", tier="ungated", signal="build", scroll=1)
        hso, _ = run_hook("design-gate.py", write_ev(td, "other.html", "<html></html>"))
        reason = (hso or {}).get("permissionDecisionReason", "")
        check("scroll intent without scroll reads denies",
              (hso or {}).get("permissionDecision") == "deny")
        check("floor names devices.md", "devices.md" in reason)
        check("floor names feel-and-fingerprint.md", "feel-and-fingerprint.md" in reason)

        if skill_roots:
            L.log(Path(td), event="ref-read", cat="references", sub="scroll",
                  file=str(skill_roots[0] / "references" / "scroll" / "devices.md"))
            L.log(Path(td), event="ref-read", cat="references", sub="scroll",
                  file=str(skill_roots[0] / "references" / "scroll" / "feel-and-fingerprint.md"))
            hso, _ = run_hook("design-gate.py", write_ev(td, "other.html", "<html></html>"))
            reason = (hso or {}).get("permissionDecisionReason", "")
            check("scroll brief also demands the fingerprint registry",
                  (hso or {}).get("permissionDecision") == "deny"
                  and "design-fingerprints.md" in reason)
            L.log(Path(td), event="ref-read", cat="registry",
                  file="design-fingerprints.md")
            # Showcase floor (2026-10-03): the floor doc, the Era journey, two
            # motion_floor-2 sheets read as images, and the GSAP/Lenis skills.
            hso, _ = run_hook("design-gate.py", write_ev(td, "other.html", "<html></html>"))
            reason = (hso or {}).get("permissionDecisionReason", "")
            check("scroll brief demands the showcase floor and the Era journey",
                  (hso or {}).get("permissionDecision") == "deny"
                  and "showcase-floor.md" in reason and "era-residence.md" in reason)
            check("scroll brief demands two motion_floor-2 sheets", "motion_floor: 2" in reason)
            check("scroll brief demands Skill(lenis) and Skill(gsap-core) before the first write",
                  "Skill(lenis)" in reason and "Skill(gsap-core)" in reason
                  and "Skill(gsap-scrolltrigger)" in reason)
            L.log(Path(td), event="ref-read", cat="references", sub="scroll",
                  file=str(skill_roots[0] / "references" / "scroll" / "showcase-floor.md"))
            L.log(Path(td), event="ref-read", cat="references", sub="scroll",
                  file=str(skill_roots[0] / "references" / "scroll" / "journeys" / "era-residence.md"))
            for slug, floor in (("acme", 2), ("beta", 1)):
                (cat_dir / "entries" / slug).mkdir(parents=True, exist_ok=True)
                (cat_dir / "entries" / slug / "entry.md").write_text(
                    f"---\nslug: {slug}\nmotion_floor: {floor}\n---\n", encoding="utf-8")
                L.log(Path(td), event="ref-read", cat="catalogue", slug=slug, kind="motion-sheet",
                      file=str(cat_dir / "entries" / slug / "motion" / "sheet.webp"))
            for sk in ("lenis", "gsap-core", "gsap-scrolltrigger"):
                L.log(Path(td), event="skill", skill=sk, tier="ungated")
            hso, _ = run_hook("design-gate.py", write_ev(td, "other.html", "<html></html>"))
            reason = (hso or {}).get("permissionDecisionReason", "")
            check("a floor-1 sheet does not count as the second floor-2 sheet",
                  (hso or {}).get("permissionDecision") == "deny" and "motion_floor: 2" in reason
                  and "Skill(lenis)" not in reason)
            (cat_dir / "entries" / "gamma").mkdir(parents=True, exist_ok=True)
            (cat_dir / "entries" / "gamma" / "entry.md").write_text(
                "---\nslug: gamma\nmotion_floor: 2\n---\n", encoding="utf-8")
            L.log(Path(td), event="ref-read", cat="catalogue", slug="gamma", kind="motion-sheet",
                  file=str(cat_dir / "entries" / "gamma" / "motion" / "sheet.webp"))
            hso, _ = run_hook("design-gate.py", write_ev(td, "other.html", "<html></html>"))
            check("reference floor allows the write once scroll refs, registry and showcase floor are read",
                  hso is None)

    # T5 (2026-09-08): the route corpus. 90+ writes routed to a fallback whose
    # skill name ("impeccable layout") is not loadable, imagery fired on every
    # <img> including material already vendored, and 17 named skills had no
    # mechanical route at all -- so "route-vs-invocation gap = 0" could not be
    # measured for exactly the skills that were never called. Each case pins
    # one route that must fire and, where it matters, one that must not.
    corpus = PLUGIN_ROOT / "tests" / "route_corpus.jsonl"
    if corpus.exists():
        failures = []
        cases = 0
        for line in corpus.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            c = json.loads(line)
            cases += 1
            ids = {r["id"] for r in L.match_routes(c["path"], c["content"])}
            for want in c.get("expect", []):
                if want not in ids:
                    failures.append(f"{c['path']}: missing {want}")
            for no in c.get("reject", []):
                if no in ids:
                    failures.append(f"{c['path']}: unwanted {no}")
        check(f"route corpus ({cases} cases) routes as specified", not failures,
              "; ".join(failures[:5]))
        fb = [r for r in L.routing_table().get("rules", []) if r.get("fallback")]
        check("fallback route names a loadable skill",
              bool(fb) and fb[0]["skill"] == "impeccable",
              f"fallback={fb[0]['skill'] if fb else 'none'}")
        named = {r["skill"].split()[0] for r in L.routing_table().get("rules", [])}
        for must in ("a11y-audit", "review-animations", "design-catalog"):
            check(f"{must} has a mechanical route", must in named)
    else:
        check("route corpus present", False, "tests/route_corpus.jsonl missing")

    # (d) the scroll route rule fires on scroll-driven markup.
    scroll_routes = L.match_routes("index.html", '<div data-sc-act="scrub">')
    check("scroll route rule matches data-sc- attribute",
          any(r.get("id") == "scroll" for r in scroll_routes))

    with tempfile.TemporaryDirectory() as td:
        # (e) the exit bar's scroll-specific requirement: a reduced-motion
        # capture, Read after the last edit, once ordinary vision already
        # passed. (f) section 8 always renders in the report.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        L.arm(Path(td), "verify")
        run_hook("design-route.py", write_ev(
            td, "components/Hero.tsx",
            'export function Hero(){return <div className="hero">x</div>}'))
        L.log(Path(td), event="intent", tier="ungated", signal="build", scroll=1)
        time.sleep(1.1)
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read",
                  "tool_input": {"file_path": str(Path(td) / "shots" / "fold.png")}})

        p = subprocess.run(
            [sys.executable, str(HOOKS / "design-stop.py")],
            input=json.dumps({"cwd": td}), capture_output=True, text=True,
            encoding="utf-8", env=ENV)
        try:
            blk = json.loads(p.stdout)
        except Exception:
            blk = {}
        # F-011 (2026-09-07): builds no longer branch on prefers-reduced-motion,
        # so there is no second render to verify. The old expectation — that a
        # scroll session is blocked until an rm- capture exists — is inverted:
        # one read capture after the last edit is the whole bar.
        check("scroll session is NOT blocked for a missing reduced-motion shot (F-011)",
              not (blk.get("decision") == "block"
                   and "reduced motion" in blk.get("reason", "").lower()))

        time.sleep(1.1)
        run_hook("design-vision-track.py",
                 {"cwd": td, "tool_name": "Read",
                  "tool_input": {"file_path": str(Path(td) / "shots" / "rm-fold.png")}})
        hso, _ = run_hook("design-stop.py", {"cwd": td})
        check("stop still reports after a second capture (F-011: no rm bar left)",
              hso is not None)

        reports = list((Path(td) / ".impeccable").glob("design-report-*.md"))
        body = reports[-1].read_text(encoding="utf-8") if reports else ""
        check("stop report body contains '## 8. Referensgolv'",
              "## 8. Referensgolv" in body)

    print("\n-- behaviour: concurrent sessions --")
    # An orchestrator session and one or more headless builder sessions can
    # share one project root at once. Before the 2026-09-06 fix, a second
    # session's SessionStart deleted the shared .armed/.design-verb/
    # .stop-blocks/.linked-roots files and RENAMED the ledger over prev,
    # destroying whatever the first session had just written. These fixtures
    # simulate two real sessions (distinct CLAUDE_CODE_SESSION_ID) touching
    # the same root and check the second session's startup leaves the first
    # session's live state and ledger rows intact and still findable.
    import importlib.util

    def _load_hook_module(name: str, filename: str):
        spec = importlib.util.spec_from_file_location(name, HOOKS / filename)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    design_stop_mod = _load_hook_module("design_stop_verify", "design-stop.py")

    SID_A = "aaaaaaaa-0000-0000-0000-000000000000"
    SID_B = "bbbbbbbb-0000-0000-0000-000000000000"

    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "package.json").write_text(
            '{"dependencies":{"react":"18.2.0"}}', encoding="utf-8")
        state_dir = Path(td) / ".impeccable"

        # Session A: a high-confidence prompt arms and logs an intent row
        # under A's own id.
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "redesign the hero"},
                           {"CLAUDE_CODE_SESSION_ID": SID_A})
        check("session A's intent fires", "<design-gate>" in (hso or {}).get("additionalContext", ""))
        armed_a = state_dir / f".armed-{SID_A[:8]}"
        check("session A armed its own per-session file", armed_a.exists())

        # Session B starts (SessionStart, source=startup) on the same root.
        run_hook("design-session-start.py", {"cwd": td, "source": "startup"},
                 {"CLAUDE_CODE_SESSION_ID": SID_B})
        check("B's SessionStart does not delete A's .armed file", armed_a.exists())
        check("B's SessionStart does not create its own .armed file",
              not (state_dir / f".armed-{SID_B[:8]}").exists())

        # A's ledger rows (rotated into prev by B's SessionStart) must still
        # be readable and still scope correctly to session A.
        check("ledger rotated into prev, not deleted",
              (state_dir / "design-session.prev.jsonl").exists()
              and not (state_dir / "design-session.jsonl").exists())
        prev_sid = os.environ.get("CLAUDE_CODE_SESSION_ID")
        os.environ["CLAUDE_CODE_SESSION_ID"] = SID_A
        try:
            # design-stop.py imports the shared lib as L; it has never re-exported
            # these names, so the old call crashed the whole verifier before the
            # remaining checks ran (pre-existing, found 2026-09-08).
            a_rows = design_stop_mod.L.scope_to_session(design_stop_mod.L.all_rows(Path(td)))
        finally:
            os.environ["CLAUDE_CODE_SESSION_ID"] = prev_sid
        check("A's own rows are still readable via all_rows()+scope_to_session() after B's start",
              any(r.get("event") == "intent" for r in a_rows))
        check("scoping to A excludes nothing of B's (B wrote no rows)",
              all(r.get("session", SID_A) == SID_A for r in a_rows))

        # Session B now does its own design work — must not collide with A's
        # per-session files, and A's report must still be gettable afterward.
        hso, _ = run_hook("design-intent.py", {"cwd": td, "prompt": "polish the nav"},
                           {"CLAUDE_CODE_SESSION_ID": SID_B})
        check("session B's intent fires independently",
              "<design-gate>" in (hso or {}).get("additionalContext", ""))
        check("A's .armed file untouched by B's own intent firing", armed_a.exists())

    with tempfile.TemporaryDirectory() as td:
        # prev is capped at PREV_LEDGER_CAP lines — write more than that
        # directly into the live ledger, rotate once, and check the cap held.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        state_dir = Path(td) / ".impeccable"
        state_dir.mkdir(parents=True, exist_ok=True)
        ledger = state_dir / "design-session.jsonl"
        overflow = L.PREV_LEDGER_CAP + 500
        with ledger.open("w", encoding="utf-8") as fh:
            for i in range(overflow):
                fh.write(json.dumps({"ts": f"t{i:06d}", "event": "edit",
                                      "session": "filler"}) + "\n")
        run_hook("design-session-start.py", {"cwd": td, "source": "startup"})
        prev = state_dir / "design-session.prev.jsonl"
        lines = [l for l in prev.read_text(encoding="utf-8").splitlines() if l.strip()] \
            if prev.exists() else []
        check("prev ledger is capped at PREV_LEDGER_CAP lines",
              len(lines) == L.PREV_LEDGER_CAP, f"{len(lines)} lines")
        check("current ledger removed after rotation", not ledger.exists())

    with tempfile.TemporaryDirectory() as td:
        # A fresh (not stale) shared .once-* flag and .stop-signature must
        # survive a sibling session's SessionStart — only age, not another
        # session merely starting, may prune them.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        state_dir = Path(td) / ".impeccable"
        state_dir.mkdir(parents=True, exist_ok=True)
        once_flag = state_dir / ".once-verify-discipline"
        once_flag.write_text("1", encoding="utf-8")
        sig_flag = state_dir / ".stop-signature"
        sig_flag.write_text("deadbeef", encoding="utf-8")
        run_hook("design-session-start.py", {"cwd": td, "source": "startup"},
                 {"CLAUDE_CODE_SESSION_ID": SID_B})
        check("fresh .once-* flag survives a sibling SessionStart", once_flag.exists())
        check("fresh .stop-signature survives a sibling SessionStart", sig_flag.exists())

    with tempfile.TemporaryDirectory() as td:
        # A per-session file (or a .once-* flag) old enough that no session
        # could still legitimately own it DOES get pruned.
        (Path(td) / "package.json").write_text("{}", encoding="utf-8")
        state_dir = Path(td) / ".impeccable"
        state_dir.mkdir(parents=True, exist_ok=True)
        stale_armed = state_dir / ".armed-deadbeef"
        stale_armed.write_text("{}", encoding="utf-8")
        stale_once = state_dir / ".once-old-thing"
        stale_once.write_text("1", encoding="utf-8")
        old = time.time() - 25 * 3600
        os.utime(stale_armed, (old, old))
        os.utime(stale_once, (old, old))
        run_hook("design-session-start.py", {"cwd": td, "source": "startup"})
        check("stale (>24h) per-session .armed-* is pruned", not stale_armed.exists())
        check("stale (>24h) .once-* flag is pruned", not stale_once.exists())

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
