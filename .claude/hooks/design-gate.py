#!/usr/bin/env python
"""PreToolUse on Write|Edit|MultiEdit — contract enforcement.

Denies a write that violates the locked design system, so the agent sees the
correction *before* the bad value lands rather than after.

Scope is deliberately narrow. It only fires when:
  * the project has a DESIGN.md (no lock, no contract, no opinion), AND
  * the target is a UI file, AND
  * the incoming content trips a contract rule.

Everything softer — taste, rhythm, structure — is advisory and belongs to
design-route.py. A gate that denies on judgment calls stalls long sessions,
which costs more than the drift it prevents.

Two enforcement modes:
  advisory (default)  warn in context, allow the write
  blocking            deny the write
Promote with DESIGN_GATE_BLOCKING=1 once a clean run is on record.
Kill entirely with DESIGN_HOOKS_DISABLED=1.
"""

import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import design_hook_lib as L
except Exception:
    sys.exit(0)


WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit", "apply_patch"}

# Contract rules only. These read DESIGN.md directly and are unambiguous.
CONTRACT_RULES = {
    "design-system-color",
    "design-system-font",
    "design-system-font-size",
    "design-system-radius",
}

HEX_RE = re.compile(r"#[0-9a-fA-F]{6}\b")


def blocking() -> bool:
    return os.environ.get("DESIGN_GATE_BLOCKING", "").strip() not in ("", "0", "false")


# --------------------------------------------------------------------------
# Reference floor — the r6 failure this closes: builders loaded Skill(design)
# and wrote real UI without ever reading TASTE.md, a catalogue example, or
# (when the brief was scroll-choreographed) the scroll references. Loading
# the skill is not the same as having actually looked at anything it points
# to. This runs only in the UNLOCKED (no DESIGN.md) branch of main() — a
# locked project's contract enforcement above is unrelated and unaffected.
# --------------------------------------------------------------------------

def _check_reference_floor(root: Path) -> None:
    if os.environ.get("DESIGN_REF_FLOOR", "").strip().lower() == "off":
        return
    if L.disabled():
        return
    if not L.armed(root):
        return

    rows = L.scope_to_session(L.all_rows(root))
    ref_reads = [r for r in rows if r.get("event") == "ref-read"]

    cat_roots = L.catalogue_roots(root)
    cat_root = cat_roots[0] if cat_roots else (root / "design-catalogue")
    skill_roots = L.design_skill_roots()
    skill_root = skill_roots[0] if skill_roots else (L.HOME / ".agents" / "skills" / "design")

    missing = []

    # Loading the skill is the floor's first rung: the r7 probe (2026-09-06)
    # read every reference and still never invoked Skill(design), so the
    # procedure (Steps 0-6) was never in context. A skill-read of the
    # skill's own SKILL.md counts the same as the Skill tool.
    skill_loaded = any(
        (r.get("event") == "skill" and str(r.get("skill", "")).split()[0] == "design")
        or (r.get("event") == "skill-read" and r.get("skill") == "design"
            and Path(r.get("file", "")).name == "SKILL.md")
        for r in rows
    )
    if not skill_loaded:
        missing.append("Du har inte laddat Skill(design) — kedjans procedur (Steps 0–6) krävs innan första UI-filen.")

    if not any(r.get("cat") == "taste" for r in ref_reads):
        taste_path = (cat_root / "TASTE.md").as_posix()
        missing.append(f"Du har inte läst {taste_path} — smakreferensen krävs innan första UI-filen.")

    feedback_path_p = cat_root / "FEEDBACK.md"
    if feedback_path_p.exists() and not any(r.get("cat") == "feedback" for r in ref_reads):
        missing.append(f"Du har inte läst {feedback_path_p.as_posix()} — återkopplingen krävs innan första UI-filen.")

    if not any(r.get("cat") == "catalogue" for r in ref_reads):
        entries_path = (cat_root / "entries").as_posix()
        missing.append(f"Du har inte läst någon post under {entries_path} — minst ett katalogexempel krävs innan första UI-filen.")

    has_lock = any(
        r.get("cat") == "references" and Path(r.get("file", "")).name == "reference-lock.md"
        for r in ref_reads
    )
    if not has_lock:
        lock_path = (skill_root / "references" / "reference-lock.md").as_posix()
        missing.append(f"Du har inte läst {lock_path} — referenslåset krävs innan första UI-filen.")

    intent_rows = [r for r in rows if r.get("event") == "intent"]
    latest_scroll = bool(intent_rows) and intent_rows[-1].get("scroll") == 1
    route_scroll = any(
        r.get("event") == "route" and r.get("skill") == "design" and r.get("signal") == "scroll"
        for r in rows
    )
    if latest_scroll or route_scroll:
        scroll_basenames = {
            Path(r.get("file", "")).name for r in ref_reads if r.get("sub") == "scroll"
        }
        for fname in ("devices.md", "feel-and-fingerprint.md"):
            if fname not in scroll_basenames:
                p = (skill_root / "references" / "scroll" / fname).as_posix()
                missing.append(f"Du har inte läst {p} — scrollkoreografins referens krävs innan första UI-filen.")

    if not missing:
        return

    msg = "[design-gate · referensgolv]\n" + "\n".join(missing)
    L.deny(msg)


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()
    if L.tool_name(event) not in WRITE_TOOLS:
        return

    path = L.target_file(event)
    if not path or not L.is_ui_file(path):
        return

    root = L.project_root(event)
    if not L.design_md(root):
        _check_reference_floor(root)
        return  # no locked system — nothing to enforce against

    content = L.written_content(event)
    if not content.strip():
        return

    violations = []

    # Gate 60 — demoted-skill palette. Pattern-matched, no detector needed.
    for skill, hx in L.trap_hits(content):
        violations.append((
            "gate-60",
            f"{hx} is {skill}'s hardcoded palette. This project has a locked "
            f"DESIGN.md — use its token instead."
        ))
        L.log(root, event="trap", file=path, component=L.component_of(path),
              skill=skill, detail=hx, signal="pre" if blocking() else "post")

    # Contract rules — run the real detector against a shadow copy of the
    # incoming content so we check what is about to land, not what is on disk.
    # Runs even when gate 60 already fired: one denial should name everything
    # wrong with the write, or the agent burns a round trip per violation.
    if True:
        shadow = None
        try:
            sd = L.state_dir(root) / "shadow"
            sd.mkdir(parents=True, exist_ok=True)
            shadow = sd / Path(path).name
            shadow.write_text(content, encoding="utf-8")
            findings = L.detect([str(shadow)], root, timeout=20)
            # Hand the full result to design-route.py so the detector runs once
            # per write instead of once per hook.
            L.cache_detect(root, content, findings)
            for f in findings:
                rid = f.get("antipattern", "")
                if rid in CONTRACT_RULES:
                    violations.append((rid, f.get("snippet") or f.get("name") or rid))
        except Exception:
            pass
        finally:
            try:
                if shadow and shadow.exists():
                    shadow.unlink()
            except Exception:
                pass

    if not violations:
        L.log(root, event="gate-pass", file=path,
              component=L.component_of(path), tier=L.tier(root))
        return

    tokens = L.design_tokens(root)
    hint_parts = []
    if tokens.get("colors"):
        hint_parts.append("colors: " + ", ".join(
            f"{k}={v}" for k, v in list(tokens["colors"].items())[:8]))
    if tokens.get("fonts"):
        hint_parts.append("fonts: " + ", ".join(tokens["fonts"][:4]))
    if tokens.get("radii"):
        hint_parts.append("radii: " + ", ".join(tokens["radii"][:6]))

    body = [f"DESIGN.md contract violation in {Path(path).name}:"]
    for rid, detail in violations[:6]:
        body.append(f"  · [{rid}] {detail}")
    if hint_parts:
        body.append("Locked tokens — " + " | ".join(hint_parts))
    body.append(
        "Use the locked token. If the value is genuinely new, add it to "
        "DESIGN.md first, then reference it — do not inline it."
    )
    msg = "\n".join(body)

    for rid, detail in violations[:6]:
        L.log(root, event="gate-deny", file=path, component=L.component_of(path),
              signal=rid, detail=str(detail)[:160], tier=L.tier(root))

    if blocking():
        L.deny(msg)
    else:
        L.emit("PreToolUse", "[design-gate · advisory] " + msg +
               "\n(Set DESIGN_GATE_BLOCKING=1 to make this a hard denial.)")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
