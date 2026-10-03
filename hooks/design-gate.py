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
SHELL_TOOLS = {"Bash", "PowerShell"}

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

def _motion_floor(cat_root: Path, slug: str) -> int:
    """motion_floor from entries/<slug>/entry.md frontmatter, -1 when absent."""
    try:
        head = (cat_root / "entries" / slug / "entry.md").read_text(encoding="utf-8", errors="replace")[:3000]
    except Exception:
        return -1
    m = re.search(r"^motion_floor:\s*(\d)", head, re.M)
    return int(m.group(1)) if m else -1


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

    # Catalogue evidence (T3, 2026-09-08). The old rule accepted ANY file
    # under entries/<slug>/ — one fold.webp cleared a floor whose prose asks
    # for 2-4 entries read as pixels and as text. r7 (2026-09-06/07) passed
    # that bar and still never ran Skill(design-catalog): the selection was
    # the orchestrator's memory, not the catalogue. Three rungs now:
    #   1. a catalogue-select row, written by scripts/catalogue/select.py,
    #      naming >= 2 slugs -- mechanical proof the choice came out of the
    #      whole catalogue rather than recall;
    #   2. per selected slug: entry.md AND its fold read, plus the extract's
    #      DESIGN.md when one exists on disk (missing extracts are a known
    #      catalogue gap, not the builder's fault);
    #   3. the fingerprint registry on a scroll brief (below).
    entries_path = (cat_root / "entries").as_posix()
    cat_reads = [r for r in ref_reads if r.get("cat") == "catalogue"]
    select_rows = [r for r in rows if r.get("event") == "catalogue-select"]
    # The LATEST selection is the lock. r8 R1 (2026-09-10): the V3c builder ran
    # select.py once against the unfilled skeleton (zero scores, alphabetical
    # top four) and once against the real draft; a union of both rows would
    # have denied R2 for four slugs that were never the lock. Re-running
    # select.py supersedes, it does not accumulate.
    selected: list[str] = []
    if select_rows:
        for slug in (select_rows[-1].get("slugs") or []):
            if slug and slug not in selected:
                selected.append(slug)

    if not select_rows:
        missing.append(
            "Ingen katalogvalsrad i sessionen — kör "
            "`python scripts/catalogue/select.py --brief <fil> --k 4` "
            "(eller Skill(design-catalog)) så att urvalet görs ur hela katalogen, "
            "inte ur minnet.")
    elif len(selected) < 2:
        missing.append(
            f"Katalogvalet gav {len(selected)} post — kedjan kräver minst två "
            f"(SKILL.md Step 1b: läs 2–4 poster). Kör select.py med --k 2 eller mer.")
    else:
        by_slug: dict[str, set] = {}
        for r in cat_reads:
            by_slug.setdefault(r.get("slug", ""), set()).add(r.get("kind", "other"))
        for slug in selected:
            kinds = by_slug.get(slug, set())
            want = []
            if "entry-md" not in kinds:
                want.append(f"{entries_path}/{slug}/entry.md")
            if "fold" not in kinds and "slice" not in kinds and "shot" not in kinds:
                want.append(f"{entries_path}/{slug}/fold.webp (som bild, inte som text)")
            if "design-md" not in kinds:
                try:
                    ex = cat_root / "entries" / slug / "extract"
                    if ex.is_dir() and any(ex.glob("*-design-language.md")):
                        want.append(f"{entries_path}/{slug}/extract/*-design-language.md")
                except Exception:
                    pass
            if want:
                missing.append(
                    f"Vald katalogpost `{slug}` är inte läst färdigt — saknas: "
                    + ", ".join(want))

    if not cat_reads:
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
        # The fingerprint gate is >= 4-of-6 against EVERY row of the registry.
        # A concept cannot clear a gate whose rows were never read, and the
        # registry is the only place earlier builds are written down.
        if not any(r.get("cat") == "registry" for r in ref_reads):
            missing.append(
                "Du har inte läst fingerprint-registret "
                "(wiki/projects/_index/design-fingerprints.md) — fingerprint-gaten "
                "(≥ 4/6 mot varje rad) kan inte hållas mot rader du inte sett.")
        # The showcase floor (Anton 2026-10-03: the chain must CALL the GSAP/Lenis
        # mechanisms, not only list them). showcase-floor.md § 1 asks for two
        # motion_floor-2 sheets read as pixels and the Era journey before the first
        # line of motion code; the GSAP/Lenis skills hold the API the page is built in.
        for fname in ("showcase-floor.md", "era-residence.md"):
            if fname not in scroll_basenames:
                sub = "journeys/" if fname == "era-residence.md" else ""
                p = (skill_root / "references" / "scroll" / f"{sub}{fname}").as_posix()
                missing.append(f"Du har inte läst {p} — showcase-golvet krävs innan första UI-filen.")
        sheets = {r.get("slug") for r in cat_reads if r.get("kind") == "motion-sheet"}
        floor2 = sorted(s for s in sheets if s and _motion_floor(cat_root, s) == 2)
        if len(floor2) < 2:
            missing.append(
                f"Du har läst {len(floor2)} rörelseark med motion_floor: 2 — golvet kräver två "
                f"({entries_path}/<slug>/motion/sheet.webp som bild; välj med "
                "`grep -l \"motion_floor: 2\" design-catalogue/entries/*/entry.md`). "
                "Namnge intro, övergångar och signaturobjekt du lånar i beslutsloggen.")
        loaded = {str(r.get("skill", "")).split()[0].split(":")[-1]
                  for r in rows if r.get("event") in ("skill", "skill-read")}
        for sk in ("lenis", "gsap-core", "gsap-scrolltrigger"):
            if sk not in loaded:
                missing.append(f"Du har inte laddat Skill({sk}) — rörelsemotorns API krävs innan första UI-filen (devices.md § Skills to load).")

    if not missing:
        return

    msg = "[design-gate · referensgolv]\n" + "\n".join(missing)
    L.deny(msg)


def _check_generation(event, root) -> None:
    """Two conditions before anything is queued at a paid backend.

    1. A `generation budget: N credits` line in a BRIEF.md under this root.
       r7 ran to a ceiling Anton set out loud and the log reconciles because of
       it; without a written ceiling there is nothing to reconcile against.
    2. A `get_cost` preflight earlier in the session. The cost is readable
       without queueing a job, so spending without reading it is a choice, not
       a constraint.

    Advisory by default, like the rest of this hook: it denies, and
    DESIGN_GEN_GATE=off turns it off for a session that knows what it is doing.
    """
    if os.environ.get("DESIGN_GEN_GATE", "").strip().lower() == "off":
        return
    rows = L.scope_to_session(L.all_rows(root))

    budget = None
    for brief in list(root.glob("**/BRIEF.md"))[:40]:
        try:
            m = re.search(r"generation budget:\s*([0-9]+(?:[.,][0-9]+)?)",
                          brief.read_text(encoding="utf-8", errors="replace"), re.I)
        except Exception:
            continue
        if m:
            budget = m.group(1)
            break

    missing = []
    if budget is None:
        missing.append("Ingen `generation budget: N credits`-rad i nagon BRIEF.md under "
                       "projektet. Skriv taket innan du koar ett betalt jobb "
                       "(references/generation.md § Kreditgrinden).")
    if not any(r.get("event") == "generation" and r.get("preflight") for r in rows):
        missing.append("Ingen `get_cost`-preflight i sessionen. Kor samma anrop med "
                       "`get_cost: true` forst och las kostnaden.")
    if missing:
        L.deny("[design-gate · genereringsgrind]\n" + "\n".join(missing))


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()

    if L.is_generation_tool(L.tool_name(event)):
        fields = L.generation_fields(event)
        if not fields.get("preflight"):
            _check_generation(event, L.project_root({"cwd": event.get("cwd")}))
        return

    # Shell authoring of a UI file bypasses every check below (r8 probe,
    # 2026-09-09: `cat > B.html <<'EOF'` sailed past the reference floor and
    # left no ledger row). Deny it in an armed session and point at Write/Edit,
    # where the floor and the contract can actually read the content.
    if L.tool_name(event) in SHELL_TOOLS:
        cmd = str(L.tool_input(event).get("command") or "")
        targets = L.shell_ui_write_targets(cmd)
        if not targets:
            return
        root = L.project_root({"cwd": event.get("cwd")})
        msg = ("[design-gate · skalskrivning]\n"
               "UI-filer författas bara med Write eller Edit, så att referensgolvet och "
               "kontraktet kan granska innehållet. Skalvägen kringgår båda: "
               + ", ".join(targets) +
               "\nKopiera (cp, mv, Copy-Item) är tillåtet. Omdirigering, heredoc, tee, "
               "sed -i, Set-Content/Out-File och inline-skript som skriver filen är det inte.")
        if L.armed(root):
            L.log(root, event="gate-deny", file=targets[0],
                  component=L.component_of(targets[0]), signal="shell-write",
                  detail=cmd[:160], tier=L.tier(root))
            L.deny(msg)
        else:
            L.emit("PreToolUse", msg + "\n(Sessionen är inte armad, så detta är en varning, inte ett nej.)")
        return

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
