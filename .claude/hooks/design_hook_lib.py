"""Shared helpers for the design hook chain.

Used by design-route.py, design-gate.py, design-telemetry.py,
design-verify-gate.py and design-stop.py.

Design rules for everything in here:
  * Never raise into the harness. A broken hook must never block the user's
    work, so every public function swallows its own errors and degrades to a
    no-op. Callers still wrap in try/except as a second net.
  * Never do slow work on the hot path. The routing table is parsed once and
    cached; DESIGN.md is read at most once per invocation.
  * The routing table is NOT duplicated here. It is parsed out of
    skills/design/references/component-routing.md so that file stays the
    single source of truth.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HOME = Path(os.path.expanduser("~"))
ROUTING_DOC = HOME / ".agents" / "skills" / "design" / "references" / "component-routing.md"
IMPECCABLE = HOME / ".agents" / "skills" / "impeccable"

KILL_SWITCH = "DESIGN_HOOKS_DISABLED"
UNIVERSAL_KILL_SWITCH = "CLAUDE_HOOKS_DISABLED"  # Fas 6 assistant-bench arm B: all hooks off
STATE_DIR_NAME = ".impeccable"
LEDGER_NAME = "design-session.jsonl"
PREV_LEDGER_NAME = "design-session.prev.jsonl"
PREV_LEDGER_CAP = 4000  # max lines kept in the prev ledger after rotation

# Markers that make a project root. Closest match wins, so DESIGN.md is listed
# first on purpose: a design system nested inside a larger monorepo defines its
# own boundary, and resolving past it would read the wrong contract.
ROOT_MARKERS = ("DESIGN.md", "design.md", ".impeccable", ".git",
                "package.json", "pyproject.toml")


def disabled() -> bool:
    if os.environ.get(UNIVERSAL_KILL_SWITCH, "").strip() not in ("", "0", "false"):
        return True
    return os.environ.get(KILL_SWITCH, "").strip() not in ("", "0", "false")


def read_event() -> dict:
    """Parse the hook event from stdin. Returns {} on anything unexpected.

    Side effect, deliberate: the harness does not reliably export
    CLAUDE_CODE_SESSION_ID to the hook process, but every event carries
    `session_id`. Without this, scope_to_session() falls back to "all rows"
    and a Stop report counts another session's edits (CHAIN-AUDIT 2026-09-07
    saw 213 edits reported for a session with 2). Seeding the env from the
    event makes session scoping work for every hook in the chain.
    """
    try:
        raw = sys.stdin.read()
        event = json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}
    try:
        sid = event.get("session_id")
        if sid:
            # The event's id WINS over an inherited env var. A hook process
            # spawned inside a nested session (the r6/r7 harness runs
            # `claude -p` children that inherit the parent's environment)
            # would otherwise be told it is the parent session and scope the
            # ledger to the wrong rows -- the exact shape of the 213-edits
            # report in CHAIN-AUDIT 2026-09-07. Measured 2026-09-08: with
            # "only if unset", a child hook silently read zero of its own
            # rows because the parent id was already exported.
            os.environ["CLAUDE_CODE_SESSION_ID"] = str(sid)
    except Exception:
        pass
    return event


def emit(event_name: str, context: str) -> None:
    """Push text into the agent's context and exit cleanly."""
    if not context:
        return
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": context,
        }
    }))


def deny(reason: str) -> None:
    """Block a PreToolUse call. The agent sees `reason` and can self-correct."""
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))


# --------------------------------------------------------------------------
# Event shape
# --------------------------------------------------------------------------

def tool_name(event: dict) -> str:
    return event.get("tool_name") or event.get("toolName") or ""


def tool_input(event: dict) -> dict:
    ti = event.get("tool_input") or event.get("toolInput") or {}
    return ti if isinstance(ti, dict) else {}


def target_file(event: dict) -> str:
    """The path a Write/Edit/MultiEdit is aimed at, or ''."""
    ti = tool_input(event)
    for key in ("file_path", "filePath", "path", "notebook_path"):
        v = ti.get(key)
        if isinstance(v, str) and v:
            return v
    return ""


def written_content(event: dict) -> str:
    """Best-effort text a Write/Edit is about to introduce.

    Only the *incoming* side matters: we are checking what the agent is adding,
    not re-flagging what the file already contained.
    """
    ti = tool_input(event)
    parts = []
    for key in ("content", "new_string", "newString"):
        v = ti.get(key)
        if isinstance(v, str):
            parts.append(v)
    edits = ti.get("edits")
    if isinstance(edits, list):
        for e in edits:
            if isinstance(e, dict):
                v = e.get("new_string") or e.get("newString")
                if isinstance(v, str):
                    parts.append(v)
    return "\n".join(parts)


# --------------------------------------------------------------------------
# Project state
# --------------------------------------------------------------------------

def project_root(event: dict) -> Path:
    start = event.get("cwd") or os.getcwd()
    tf = target_file(event)
    if tf:
        try:
            start = str(Path(tf).parent)
        except Exception:
            pass
    try:
        cur = Path(start).resolve()
    except Exception:
        return Path(os.getcwd())
    for candidate in [cur, *cur.parents]:
        for marker in ROOT_MARKERS:
            if (candidate / marker).exists():
                return candidate
    return cur


def state_dir(root: Path) -> Path:
    d = root / STATE_DIR_NAME
    try:
        d.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass
    return d


def design_md(root: Path) -> Path | None:
    for name in ("DESIGN.md", "design.md", "Design.md"):
        p = root / name
        if p.exists():
            return p
    return None


def tier(root: Path) -> str:
    """Coarse tier signal for the ledger and the injected reminder.

    Three states, not two. The middle one exists because five different skills
    write a file called DESIGN.md in three incompatible formats:

      0-locked  DESIGN.md with parseable token frontmatter (impeccable/Stitch
                schema). Full mechanical enforcement.
      0-prose   DESIGN.md exists but carries no parseable tokens — what
                `design-md`, gstack's `design-consultation`, and hand-written
                files produce. Authority WITHOUT enforcement.
      ungated   No DESIGN.md. The model runs the tier gate.

    Collapsing 0-prose into 0-locked was a real bug: the system announced
    "TIER 0 - LOCKED, inherit the system" while design-gate.py enforced
    nothing, so an off-brand write passed silently. That is strictly worse
    than 'ungated', where the model at least performs the derivation.

    Distinguishing tiers 1/2/3 stays a model judgment; only tier 0 is
    mechanically decidable.
    """
    if not design_md(root):
        return "ungated"
    t = design_tokens(root)
    has_tokens = bool(t.get("colors") or t.get("fonts") or t.get("radii"))
    return "0-locked" if has_tokens else "0-prose"


def design_tokens(root: Path) -> dict:
    """Parse the DESIGN.md frontmatter maps we care about.

    Deliberately small: enough to name the right token in a denial message.
    The authoritative check is impeccable's detector, which parses the full
    schema plus the .impeccable/design.json sidecar.
    """
    out = {"colors": {}, "fonts": [], "radii": []}
    p = design_md(root)
    if not p:
        return out
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return out
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return out
    fm = m.group(1)

    section = None
    for line in fm.splitlines():
        if re.match(r"^\w+:", line):
            section = line.split(":", 1)[0].strip()
            continue
        if section == "colors":
            km = re.match(r"^\s+([\w-]+):\s*[\"']?(#[0-9a-fA-F]{3,8}|oklch\([^)]*\))", line)
            if km:
                out["colors"][km.group(1)] = km.group(2).lower()
        elif section == "typography":
            fmatch = re.search(r"fontFamily:\s*[\"']([^\"']+)", line)
            if fmatch:
                out["fonts"].append(fmatch.group(1).strip())
        elif section == "rounded":
            rm = re.match(r"^\s+([\w-]+):\s*[\"']?([\d.]+(?:px|rem|em))", line)
            if rm:
                out["radii"].append(rm.group(2))
    return out


# --------------------------------------------------------------------------
# Arm / disarm — a design session must be armed before per-edit hooks act
#
# The chain used to treat every prompt that brushed a design keyword as a
# live design session. "investigate the design hooks" is not a design task;
# neither is a stray ".ts" edit in a repo that happens to have a DESIGN.md.
# classify() below decides how strong the signal is; arm()/armed() decide
# whether the per-edit hooks (route/verify-gate) and the Stop report treat
# the session as one actually doing UI work. design-gate.py is exempt: it is
# the one hard contract enforcement and stays unconditional.
# --------------------------------------------------------------------------

ARMED_NAME = ".armed"
FORCE_ARM_ENV = "DESIGN_HOOKS_FORCE_ARM"


def session_file(root: Path, base: str) -> Path:
    """Per-session variant of a shared state file name (2026-09-06).

    An orchestrator session and headless builder sessions share one project
    root at once; a bare `.armed`/`.design-verb`/`.stop-blocks`/`.linked-roots`
    is shared mutable state that a sibling's SessionStart used to clear from
    under a running build. Suffixing with this session's id keeps sessions
    apart; no session id collapses onto a shared "nosession" bucket.
    """
    sid = current_session_id()
    sid8 = sid[:8] if sid else "nosession"
    return state_dir(root) / f"{base}-{sid8}"


def arm(root: Path, source: str, detail: str = "") -> None:
    """Mark this project root as a live design session.

    Cleared by design-session-start.py on source=startup/clear, so it is
    scoped to one Claude Code session the same way the ledger is.
    """
    try:
        rec = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "source": source,
            "detail": detail,
            "session": current_session_id(),
        }
        session_file(root, ARMED_NAME).write_text(
            json.dumps(rec, ensure_ascii=False), encoding="utf-8")
    except Exception:
        pass


def armed(root: Path) -> bool:
    if os.environ.get(FORCE_ARM_ENV, "").strip() not in ("", "0", "false"):
        return True
    try:
        return session_file(root, ARMED_NAME).exists()
    except Exception:
        return False


def disarm(root: Path) -> None:
    try:
        p = session_file(root, ARMED_NAME)
        if p.exists():
            p.unlink()
    except Exception:
        pass


# --------------------------------------------------------------------------
# Intent classification — how strong is the signal that this prompt is a
# UI task, as opposed to prose that merely mentions a design word?
#
# Three tiers:
#   high    verb + object, unambiguous UI task. Arms the session.
#   medium  a UI object (or the bare word design/ui) with no verb, or a
#           question about the design. One-line nudge, does not arm.
#   none    no design signal at all, or the prompt is ABOUT the hook chain,
#           the repo's tooling, or unrelated engineering work — the negative
#           guard below wins over any keyword coincidence.
#
# The corpus this was tuned against lives at
# anti-slop-design/tests/intent_corpus.jsonl and is run by
# verify-design-system.py. Tuning notes, not spec drift:
#   * "diagnose" was DROPPED from the negative guard. It is a legitimate
#     bare-bug-report verb ("diagnose why the modal state is undefined") and
#     the corpus has a medium-tier row that proves it must not force "none".
#     "investigate"/"undersök"/"felsök" stayed — nothing in the corpus needs
#     them to fire on non-tooling prose.
#   * The guard drops the trailing \b so Swedish suffixed forms still hit —
#     "design-hookarna" (hooks + -arna), "design-skillen" (skill + -en).
#     Checked against every high/medium row for accidental prefix collisions
#     (carl/regex/skill/commit/... do not appear as prefixes there).
#   * OBJECTS keeps its trailing \b (unlike the guard) specifically so a
#     file path like "components/settings/actions.ts" does NOT read as the
#     word "component" — dropping it there let path fragments leak into
#     object detection. Two Swedish suffixes needed explicit extra literals
#     instead: "landningssida(n)?" and "scroll ?animation(er)?".
#   * One narrow verb phrase, "update the color tokens", was added for the
#     "update the color tokens in tailwind.config" row. A bare "update" verb
#     was tried first and rejected: it also lit up "update the README layout
#     section..." (expected medium — a docs edit, not UI) once paired with
#     "layout"/"section" as objects. The narrow phrase avoids that collision.
#   * "color" (bare) was added to OBJECTS for "the color of the log output
#     is wrong in the CLI" (expected medium) — only "color tokens" existed
#     before and nothing else in that prompt is UI-object shaped.
# --------------------------------------------------------------------------

_SLASH_DESIGN_RE = re.compile(r"^/design\b", re.I)

# Leading \b only — see the Swedish-suffix note above.
NEGATIVE_GUARD = re.compile(
    r"\b(?:hook|hooks|hookkedjan|design-gate|design-intent|design-stop|design-route|"
    r"carl|regex|skill|skills|skill-routing|routing|plugin|anti-slop-design|"
    r"verify-design-system|route gap|detect\.mjs|impeccable live|design-shotgun|"
    r"conclude|session log|sessionslogg|migration|supabase|database|databas|"
    r"git push|commit|pull request|test(?:s|er)?\b.*?\bfail|analysera repot|"
    r"sammanfatta|explain how|förklara hur|varför fyrar|why does .* fire|"
    r"investigate|undersök|felsök|write a plan|skriv en plan)",
    re.I,
)

VERBS_RE = re.compile(
    r"\b(?:build|bygg|create|skapa|make|g(?:ö|o)r|design|designa|redesign|"
    r"g(?:ö|o)r om|omdesign|rebuild|bygg om|polish|polera|finputsa|style|styla|"
    r"restyle|improve the look|make it (?:look|feel)|premium|"
    r"audit the (?:ui|design|page|flow)|granska (?:ui|design|sidan)|"
    r"implement|implementera|add|l(?:ä|a)gg till|animate|animera|refresh|"
    r"modernise|modernize|overhaul|tighten|"
    r"fix the (?:spacing|alignment|typography|contrast)|"
    r"update the color tokens)\b",
    re.I,
)

OBJECTS_RE = re.compile(
    r"\b(?:landing ?page|landningssida(?:n)?|start ?sida|startsidan|page|sida|sidan|"
    r"site|sajt|sajten|webbplats|hero|heron|nav|navigation|navigationen|"
    r"header|footer|sidebar|dashboard|admin|settings page|checkout|pricing|"
    r"prislista|form|formul(?:ä|a)r|modal|drawer|toast|tooltip|carousel|karusell|"
    r"button|knapp|cta|card|kort|component|komponent|layout|typography|"
    r"typografi|font|typsnitt|palette|palett|color tokens|color|f(?:ä|a)rg|"
    r"dark mode|theme|tema|ui|frontend|hero section|"
    r"scroll ?animation(?:er)?|scrollanimation(?:er)?|"
    r"imagery|bilder|section|sektion|grid|banner|tokens|tailwind\.config)\b",
    re.I,
)

_DESIGN_WORD_RE = re.compile(r"\bdesign\b", re.I)
_QUESTION_RE = re.compile(r"\b(?:vad tycker du om|what do you think of)\b", re.I)

_UI_EVIDENCE_EXTS = (".html", ".css", ".tsx", ".jsx", ".vue", ".svelte", ".astro")
_UI_EVIDENCE_SKIP_DIRS = {"node_modules", ".git"}
_UI_EVIDENCE_PKG_RE = re.compile(r"\b(?:react|next|vue|svelte|astro|tailwind)\b", re.I)


def _scan_ui_evidence(root: Path) -> bool:
    try:
        pkg = root / "package.json"
        if pkg.exists():
            txt = pkg.read_text(encoding="utf-8", errors="replace")
            if _UI_EVIDENCE_PKG_RE.search(txt):
                return True
    except Exception:
        pass

    def walk(d: Path, depth: int) -> bool:
        try:
            entries = list(d.iterdir())
        except Exception:
            return False
        for entry in entries:
            try:
                if entry.is_dir():
                    if entry.name in _UI_EVIDENCE_SKIP_DIRS:
                        continue
                    if depth < 2 and walk(entry, depth + 1):
                        return True
                elif entry.is_file():
                    if entry.suffix.lower() in _UI_EVIDENCE_EXTS:
                        return True
            except Exception:
                continue
        return False

    try:
        return walk(root, 0)
    except Exception:
        return False


def _has_ui_evidence(root: Path) -> bool:
    """Cached (10 min) scan for UI evidence in the project root.

    Keeps classify()'s hot path fast: most turns hit the cache, not the
    filesystem walk.
    """
    cache_file = state_dir(root) / ".ui-evidence"
    now = time.time()
    try:
        if cache_file.exists():
            data = json.loads(cache_file.read_text(encoding="utf-8"))
            if now - float(data.get("ts", 0)) < 600:
                return bool(data.get("value"))
    except Exception:
        pass
    value = _scan_ui_evidence(root)
    try:
        cache_file.write_text(json.dumps({"ts": now, "value": value}), encoding="utf-8")
    except Exception:
        pass
    return value


SCROLL_RE = re.compile(
    r"\b(?:scroll|scrolla|scroll ?animation(?:s|er)?|scroll[- ]?driven|"
    r"scrub(?:b(?:ning|ed|ing))?|parallax|pin(?:ned)?|set-piece|set piece|"
    r"signaturr(?:ö|o)relse|koreograf(?:i|era))\b",
    re.I,
)


def scroll_signal(prompt: str) -> bool:
    """True when the prompt names scroll choreography specifically.

    Separate from classify() on purpose: classify()'s corpus (42 rows in
    tests/intent_corpus.jsonl) is tuned against exact verb/object/guard
    interactions, and folding another concept into it risks silently
    shifting an existing row's tier. This is an independent, additive
    signal design-intent.py layers on top of whatever classify() decided.
    """
    if not prompt:
        return False
    return bool(SCROLL_RE.search(prompt))


def classify(prompt: str, root: Path) -> str:
    """"high" | "medium" | "none" — how strong is this prompt's UI signal?"""
    if not prompt:
        return "none"
    p = prompt.strip()
    if _SLASH_DESIGN_RE.match(p):
        return "high"
    has_verb = bool(VERBS_RE.search(p))
    has_object = bool(OBJECTS_RE.search(p))
    has_design_word = bool(_DESIGN_WORD_RE.search(p))
    is_question = bool(_QUESTION_RE.search(p))

    # The negative guard decides ambiguous prompts only. A brief that names a UI
    # verb AND a UI object is design work even when it also says "ingen commit"
    # or "vilka skills du laddade" (r6, 2026-09-06: one such word anywhere in a
    # 110-line build brief silenced the gate for every arm-B cell).
    if NEGATIVE_GUARD.search(p) and not (has_verb and has_object):
        return "none"

    if has_verb and has_object:
        return "high" if _has_ui_evidence(root) else "medium"
    if has_object or has_design_word or is_question:
        return "medium"
    return "none"


# --------------------------------------------------------------------------
# Reference-floor roots — where the taste/feedback/catalogue/scroll
# references actually live on disk, deduped so a junction (both
# ~/.agents/skills/design and ~/.claude/skills/design point at the same
# physical vault folder) is not counted twice.
# --------------------------------------------------------------------------

_DESIGN_SKILL_DIRS = (
    HOME / ".agents" / "skills" / "design",
    HOME / ".claude" / "skills" / "design",
    # The plugin's own copy (repo checkout or installed dist/plugin): same files, kept
    # identical by sync-from-live --check. A builder working in the repo reads these, and
    # r37 V4 (2026-10-03) was denied for references it had read here.
    Path(__file__).resolve().parent.parent / "skills" / "design",
)


def design_skill_roots() -> list[Path]:
    seen: list[Path] = []
    for p in _DESIGN_SKILL_DIRS:
        try:
            rp = p.resolve()
        except Exception:
            continue
        if rp not in seen:
            seen.append(rp)
    return seen


def catalogue_roots(root: Path) -> list[Path]:
    candidates = [root / "design-catalogue", HOME / "anti-slop-design" / "design-catalogue"]
    seen: list[Path] = []
    for p in candidates:
        try:
            rp = p.resolve()
        except Exception:
            continue
        if rp not in seen:
            seen.append(rp)
    return seen


# --------------------------------------------------------------------------
# Routing table — parsed from the reference, never duplicated
# --------------------------------------------------------------------------

_ROUTING_CACHE: dict | None = None


def routing_table() -> dict:
    global _ROUTING_CACHE
    if _ROUTING_CACHE is not None:
        return _ROUTING_CACHE
    table = {"rules": [], "ui_extensions": [], "trap_hexes": {}}
    try:
        text = ROUTING_DOC.read_text(encoding="utf-8", errors="replace")
        for block in re.findall(r"```json\s*\n(.*?)\n```", text, re.S):
            try:
                parsed = json.loads(block)
            except Exception:
                continue
            if isinstance(parsed, dict) and "rules" in parsed:
                table = parsed
                break
    except Exception:
        pass
    _ROUTING_CACHE = table
    return table


# Extensions that are UI by definition — markup, styles, or a component format
# where the file cannot be anything else.
_UNAMBIGUOUS_UI_EXTS = (
    ".tsx", ".jsx", ".vue", ".svelte", ".astro",
    ".html", ".htm", ".css", ".scss", ".sass", ".less",
)

# Extensions that are usually NOT UI. A .ts file is as likely to be a schema, a
# parser, or a migration script as a component, so routing on extension alone
# produced a permanent route-gap on backend-only work — which then masks a
# genuine miss on a real component. These require a content signal.
_AMBIGUOUS_UI_EXTS = (".ts", ".js", ".mjs", ".cjs")

_UI_CONTENT_SIGNALS = (
    # JSX, detected by a CLOSING tag only. An opening tag is unusable here:
    # `NodeTree<BaseNode>` is a TypeScript generic, not markup, and the two are
    # not reliably distinguishable. Generics never produce `</Foo>`.
    re.compile(r"</[A-Za-z][\w.]*\s*>|<\s*/\s*>"),
    re.compile(r"\bclassName\s*=|\bstyle\s*=\s*\{\{"),           # React styling
    re.compile(r"""from\s+['"](react|react-dom|preact|solid-js|vue|svelte)"""),
    re.compile(r"\bdocument\.(getElement|querySelector|createElement)|\bwindow\."),
    # `(?<![\w.])` so prose like "the published `framework.css`" does not read
    # as a css`` tagged template — the backtick there belongs to the next token.
    re.compile(r"styled\.[a-z]|(?<![\w.])css`|createGlobalStyle|@emotion"),
    re.compile(r"^\s*[.#][\w-]+\s*\{", re.MULTILINE),            # raw CSS rules
)

_OPEN_TAG_LETTER_RE = re.compile(r"<[A-Za-z]")


def is_substantive_ui_write(content: str) -> bool:
    """A real markup/style write, not a stray angle bracket or a generic.

    Reuses the same signals as `_UI_CONTENT_SIGNALS` (closing tag, className/
    style, raw CSS rule) and adds one more: an opening tag followed by a
    letter, which those three intentionally skip (see the comment above them
    on why an opening tag alone is unreliable for a `.ts` generics false
    positive). Used to decide whether an edit is "substantive" enough to
    auto-arm a locked project on a strong code-route — a stray `<div` in a
    comment should not.
    """
    if not content:
        return False
    if _UI_CONTENT_SIGNALS[0].search(content):   # closing tag
        return True
    if _UI_CONTENT_SIGNALS[1].search(content):   # className= / style=
        return True
    if _UI_CONTENT_SIGNALS[5].search(content):   # raw CSS rule
        return True
    return bool(_OPEN_TAG_LETTER_RE.search(content))


def is_ui_file(path: str, content: str | None = None) -> bool:
    """Whether this write is a design decision.

    Extension alone is not enough: `.ts`/`.js` cover schemas, parsers and build
    scripts as often as components. When content is available those are checked
    for a real UI signal. Without content the previous extension-only behaviour
    is kept, so any caller that cannot supply it is unaffected.
    """
    if not path:
        return False
    exts = routing_table().get("ui_extensions") or []
    low = path.lower()
    if not any(low.endswith(e) for e in exts):
        return False
    if low.endswith(_UNAMBIGUOUS_UI_EXTS):
        return True
    if low.endswith(_AMBIGUOUS_UI_EXTS):
        if content is None:
            return True  # unchanged behaviour when the caller has no content
        return any(rx.search(content) for rx in _UI_CONTENT_SIGNALS)
    return True


# The shell bypass (r8 probe, 2026-09-09): a headless Opus builder wrote its
# UI file with `cat > x.html <<'EOF'`. Every gate in this chain keys on the
# Write/Edit tools, so the reference floor, the contract check and the route
# ledger all saw nothing. These patterns name the shell constructs that
# AUTHOR a file; copying (cp, mv, Copy-Item) is deliberately not among them,
# because vendoring the scroll engine into runs/<cell>/scroll/ is a copy.
_UI_EXT_RX = r"(?:html?|css|scss|sass|less|jsx?|tsx?|vue|svelte|astro)"
_SHELL_PATH = r"""["']?([^\s"'|;&<>]+\.""" + _UI_EXT_RX + r""")["']?(?=[\s;&|)]|$)"""
_SHELL_AUTHORING = [
    re.compile(r"(?<!<)>{1,2}\s*" + _SHELL_PATH),                                   # cat > x.html, echo >> x.css
    re.compile(r"\btee\b(?:\s+-\w+)*\s+" + _SHELL_PATH),                            # tee x.html
    re.compile(r"\b(?:Set-Content|Out-File|Add-Content)\b[^|;\n]*?" + _SHELL_PATH, re.I),
    re.compile(r"\bsed\b[^|;\n]*?\s-i\S*[^|;\n]*?\s" + _SHELL_PATH),                # sed -i ... x.html
    re.compile(r"open\(\s*[\"']([^\"']+\." + _UI_EXT_RX + r")[\"']\s*,\s*[\"'][wa]"),  # python open(x,'w')
    re.compile(r"writeFile(?:Sync)?\(\s*[\"']([^\"']+\." + _UI_EXT_RX + r")[\"']"),   # node fs.writeFile
]


def shell_ui_write_targets(command: str) -> list[str]:
    """UI files a shell command would AUTHOR (not copy). Empty = nothing to gate."""
    if not command:
        return []
    found: list[str] = []
    for rx in _SHELL_AUTHORING:
        for m in rx.finditer(command):
            p = m.group(1).strip()
            if p and is_ui_file(p) and p not in found:
                found.append(p)
    return found


# Skills whose route is about the surrounding framework, not the component
# being crafted — react-components and next-best-practices route on generic
# structural signals ("export function", "app/") that fire on almost every
# file in a React/Next project. Counting them in the Stop report's gap is
# what produced a "must be zero" alarm on every session: the router named
# them constantly and nothing ever "invokes" a framework-conventions skill
# the way it invokes emil-design-eng for a drawer. Hardcoded rather than
# read from component-routing.md so the reference stays free of a concept
# (framework vs craft) that only the Stop report needs.
FRAMEWORK_SKILLS = {"react-components", "next-best-practices", "vercel-react-best-practices"}


def skill_class(skill_name: str) -> str:
    """"framework" | "craft" — see FRAMEWORK_SKILLS above."""
    name = (skill_name or "").split(":")[-1].strip()
    return "framework" if name in FRAMEWORK_SKILLS else "craft"


def match_routes(path: str, content: str) -> list[dict]:
    """Which routing rules fire for this write. Most specific first.

    Each returned dict is a COPY of the cached rule with one extra key,
    `_matched_on`: "path" | "code" | "fallback" — which fragment kind fired.
    Copies so the cached table (shared across every call) is never mutated.
    """
    table = routing_table()
    low_path = (path or "").replace("\\", "/").lower()
    hits, fallback = [], None

    for rule in table.get("rules", []):
        if rule.get("fallback"):
            fallback = rule
            continue
        # `not_path` suppresses a rule for paths it must never claim. The
        # imagery rule used to fire on every `<img` in the project, including
        # material already sourced and vendored under assets/ — 90+ routes,
        # zero of them actionable, and a permanent false gap in the Stop
        # report (2026-09-08).
        if any(frag.lower() in low_path for frag in rule.get("not_path", [])):
            continue
        matched_on = None
        for frag in rule.get("path", []):
            if frag.lower() in low_path:
                matched_on = "path"
                break
        if not matched_on:
            use_regex = bool(rule.get("regex"))
            for frag in rule.get("code", []):
                try:
                    if use_regex:
                        if re.search(frag, content):
                            matched_on = "code"
                            break
                    elif frag in content:
                        matched_on = "code"
                        break
                except re.error:
                    continue
        if matched_on:
            hit = dict(rule)
            hit["_matched_on"] = matched_on
            hits.append(hit)

    if not [h for h in hits if h.get("id") != "copy"] and fallback:
        fb = dict(fallback)
        fb["_matched_on"] = "fallback"
        hits.append(fb)
    return hits


def strong_route(rule: dict, path: str, content: str) -> bool:
    """True only when `rule` (from match_routes) matched on CODE, not path.

    A path-only match ("components/" in the file path) is weak — it fires on
    every file in a folder regardless of what is actually written. A code
    match means the written bytes themselves carried the signal (an actual
    `<nav`, a real `useGesture()` call). Only strong, code-matched routes to
    a craft skill auto-arm an otherwise-unarmed 0-locked session, and only
    strong routes count against the route gap in the Stop report.
    """
    return bool(rule) and rule.get("_matched_on") == "code"


def trap_hits(content: str) -> list[tuple[str, str]]:
    """(skill, hex) for every demoted-skill palette value in the content.

    This is gate 60, the flag under test.
    """
    out = []
    if not content:
        return out
    low = content.lower()
    for skill, hexes in (routing_table().get("trap_hexes") or {}).items():
        for hx in hexes:
            if hx.lower() in low:
                out.append((skill, hx))
    return out


# --------------------------------------------------------------------------
# Ledger
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Generated material
#
# The generation backend is reached through an MCP whose server segment is a
# UUID in this install, so the tool name is matched on the OPERATION, not on
# the provider: mcp__<anything>__generate_image and friends. That keeps the
# ledger honest if the connector is renamed or a second provider is added.
# --------------------------------------------------------------------------

GEN_TOOL = re.compile(
    r"^mcp__.+__(generate_(image|video|audio|3d)(_batch)?|upscale_(image|video)"
    r"|reframe|remove_background|outpaint_image|motion_control)$")

COST_TOOL_HINT = "get_cost"


def is_generation_tool(name: str) -> bool:
    return bool(GEN_TOOL.match(name or ""))


def generation_fields(event: dict) -> dict:
    """Model, cost-preflight flag and job id, dug out of an MCP call."""
    ti = tool_input(event) or {}
    params = ti.get("params")
    if isinstance(params, str):
        try:
            params = json.loads(params)
        except Exception:
            params = {}
    if not isinstance(params, dict):
        params = {}
    out = {"tool": tool_name(event), "model": params.get("model", "")}
    if params.get(COST_TOOL_HINT):
        out["preflight"] = 1
    if params.get("count"):
        out["count"] = params.get("count")
    resp = event.get("tool_response") or event.get("tool_result") or {}
    if isinstance(resp, str):
        m = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", resp)
        if m:
            out["job"] = m.group(0)
        m = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*credit", resp, re.I)
        if m:
            out["credits"] = float(m.group(1))
    elif isinstance(resp, dict):
        for k in ("job_id", "id", "jobId"):
            if resp.get(k):
                out["job"] = str(resp[k]); break
        for k in ("cost", "credits", "price"):
            if isinstance(resp.get(k), (int, float)):
                out["credits"] = resp[k]; break
    return {k: v for k, v in out.items() if v not in (None, "")}


def _skill_dir(name: str):
    """Where an installed skill lives, or None. First word only: routes name
    commands like "impeccable layout", and the skill is `impeccable`."""
    base = (name or "").strip().split()[0] if (name or "").strip() else ""
    if not base:
        return None
    for root in (HOME / ".agents" / "skills", HOME / ".claude" / "skills"):
        d = root / base
        try:
            if (d / "SKILL.md").exists():
                return d
        except Exception:
            continue
    return None


def skill_status(name: str) -> str:
    """How a routed skill can be reached: 'ok', 'user-only', or 'missing'.

    The route-vs-invocation gap is only meaningful for skills the model could
    have loaded and did not. Two other cases were being counted in the same
    bucket and made the number untrustworthy (2026-09-08):

      user-only  the skill sets `disable-model-invocation`, so ONLY the user
                 can run it (/review-animations). An agent cannot close this
                 gap no matter what it does.
      missing    the route names something that is not an installed skill at
                 all. That is a bug in component-routing.md, not a skipped
                 step - the fallback rule shipped as "impeccable layout" for
                 months and could never load once.
    """
    d = _skill_dir(name)
    if d is None:
        return "missing"
    try:
        head = (d / "SKILL.md").read_text(encoding="utf-8", errors="replace")[:1200]
        if "disable-model-invocation: true" in head:
            return "user-only"
    except Exception:
        pass
    return "ok"


def current_session_id() -> str:
    """The running Claude Code session's id. Hooks inherit it via env."""
    return os.environ.get("CLAUDE_CODE_SESSION_ID", "")


def log(root: Path, **fields) -> None:
    """Append one event to the session ledger. Silent on failure.

    Every row is stamped with the session id so consumers can scope to the
    CURRENT session. Before this stamp, design-stop.py counted every row ever
    written in the root — "31 UI edits this session" in a session with zero
    edits (idea-2ao, verified 2026-08-25).
    """
    try:
        rec = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        sid = current_session_id()
        if sid:
            rec["session"] = sid
        rec.update({k: v for k, v in fields.items() if v not in (None, "")})
        path = state_dir(root) / LEDGER_NAME
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception:
        pass


def read_ledger(root: Path, name: str = LEDGER_NAME) -> list[dict]:
    try:
        path = state_dir(root) / name
        if not path.exists():
            return []
        rows = []
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                continue
        return rows
    except Exception:
        return []


def all_rows(root: Path) -> list[dict]:
    """The cwd root's ledger plus every linked root's (cross-project builds).

    Promoted out of design-stop.py so design-gate.py's reference floor can
    see the same session history the Stop report does — a cross-project
    build (site scaffold, worktree) that read the taste reference from the
    cwd root must not look empty from the file root's ledger, or vice versa.
    """
    rows = read_ledger(root) + read_ledger(root, PREV_LEDGER_NAME)
    try:
        reg = session_file(root, ".linked-roots")
        if reg.exists():
            for line in reg.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line:
                    rows.extend(read_ledger(Path(line)))
                    rows.extend(read_ledger(Path(line), PREV_LEDGER_NAME))
        rows.sort(key=lambda r: r.get("ts", ""))
    except Exception:
        pass
    return rows


def scope_to_session(rows: list[dict]) -> list[dict]:
    """Keep only this session's rows (plus any row too old to carry a `session`
    field — backward compatible with a ledger written before that stamp)."""
    sid = current_session_id()
    if not sid:
        return rows
    return [r for r in rows if "session" not in r or r.get("session") == sid]


def component_of(path: str) -> str:
    """Human label for the thing being edited — the file stem is enough."""
    try:
        return Path(path).stem or Path(path).name
    except Exception:
        return path or "?"


def once_per_session(root: Path, key: str) -> bool:
    """True the first time this key is seen, False after. Used to keep
    session-level reminders from repeating on every single tool call."""
    try:
        flag = state_dir(root) / f".once-{re.sub(r'[^a-z0-9]+', '-', key.lower())}"
        if flag.exists():
            return False
        flag.write_text("1", encoding="utf-8")
        return True
    except Exception:
        return False


def _cache_path(root: Path) -> Path:
    return state_dir(root) / ".detect-cache.json"


def cache_detect(root: Path, content: str, findings: list[dict]) -> None:
    """Stash detector findings keyed by content hash.

    design-gate.py (PreToolUse) and design-route.py (PostToolUse) both want the
    detector's verdict on the same bytes. Without this the detector runs twice
    per UI write, which is the single largest cost in the chain.
    """
    try:
        import hashlib
        key = hashlib.sha1(content.encode("utf-8", "replace")).hexdigest()
        p = _cache_path(root)
        data = {}
        if p.exists():
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                data = {}
        data[key] = findings
        # keep it small — this is a hot-path read
        if len(data) > 20:
            data = dict(list(data.items())[-20:])
        p.write_text(json.dumps(data), encoding="utf-8")
    except Exception:
        pass


def cached_detect(root: Path, content: str):
    """Findings for these exact bytes, or None if not cached."""
    try:
        import hashlib
        key = hashlib.sha1(content.encode("utf-8", "replace")).hexdigest()
        p = _cache_path(root)
        if not p.exists():
            return None
        return json.loads(p.read_text(encoding="utf-8")).get(key)
    except Exception:
        return None


def detect(files: list[str], root: Path, timeout: int = 25) -> list[dict]:
    """Run impeccable's deterministic detector. [] if unavailable.

    NOTE: the detector exits 0 even when it has findings, so the JSON is the
    only signal. Never branch on returncode here.
    """
    script = IMPECCABLE / "scripts" / "detect.mjs"
    if not script.exists() or not files:
        return []
    try:
        import subprocess
        proc = subprocess.run(
            ["node", str(script), "--json", *files],
            capture_output=True, text=True, timeout=timeout, cwd=str(root),
        )
        out = (proc.stdout or "").strip()
        if not out:
            return []
        start = out.find("[")
        if start < 0:
            return []
        data = json.loads(out[start:])
        return data if isinstance(data, list) else []
    except Exception:
        return []
