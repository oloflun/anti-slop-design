#!/usr/bin/env python
"""SessionStart — make session-scoped hook state actually session-scoped.

The chain's dedup flags (.once-*, .design-verb, .stop-signature) were written
once and never cleared, so "once per session" silently meant "once per project,
forever": the inspection floor injected on jul 28 never fired again, and a new
session whose first design verb matched the previous session's last verb got
no intent injection at all. The ledger likewise accumulated across sessions,
turning Stop reports into cross-session mush.

Runs on source=startup and source=clear only — resume and compact continue an
existing conversation, so their state is still live.

Concurrency (2026-09-06): an orchestrator session and one or more headless
builder sessions can share this same project root at once. The original fix
above cleared everything unconditionally on every SessionStart, which solved
"stale forever" by creating a worse bug: session B's SessionStart deleted
session A's live `.armed`/`.design-verb`/`.stop-blocks`/`.linked-roots` out
from under a build in progress, and rotating the ledger by RENAMING it over
`design-session.prev.jsonl` threw away whatever was already in prev — often
session A's own rows, written moments earlier by session A's own SessionStart.
Two changes fix this without giving up the original "actually session-scoped"
property:

  1. `.armed`/`.design-verb`/`.stop-blocks`/`.linked-roots` are now per-session
     files (design_hook_lib.session_file — suffixed with this session's id).
     This session's own copies do not exist yet at startup, so clearing "this
     session's files" is a no-op by construction; what actually needs doing
     is pruning old SESSIONS' leftover copies (a crashed session, a killed
     headless builder) once they are unambiguously stale, never a sibling
     that is merely still running.
  2. The ledger is APPENDED into prev, not renamed over it, and prev is
     capped at PREV_LEDGER_CAP lines. `.linked-roots` is unaffected by this —
     it is handled entirely by the per-session-file change above.
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import design_hook_lib as L
except Exception:
    sys.exit(0)


STALE_SECONDS = 24 * 60 * 60  # a day — long enough no live session is this old

# Base names of files that now live per-session (see session_file()). Globbed
# with a trailing "-*" to catch every session's copy, our own included (which
# will not exist yet, so pruning it is a no-op for us specifically).
PER_SESSION_BASES = (L.ARMED_NAME, ".design-verb", ".stop-blocks", ".linked-roots",
                     ".unarmed-notice")


def clear_root(root: Path) -> None:
    d = root / L.STATE_DIR_NAME
    if not d.is_dir():
        return

    now = time.time()

    def prune_if_stale(p: Path) -> None:
        try:
            if now - p.stat().st_mtime >= STALE_SECONDS:
                p.unlink()
        except Exception:
            pass

    # Per-session files: never delete another session's live copy. Only prune
    # ones old enough that no session could still legitimately be using them.
    for base in PER_SESSION_BASES:
        for flag in d.glob(f"{base}-*"):
            prune_if_stale(flag)

    # .once-* dedup flags are NOT session-suffixed (see design_hook_lib's
    # once_per_session) — they intentionally stay a single shared bucket, so
    # the same stale-age prune applies rather than a hard delete every start.
    for flag in d.glob(".once-*"):
        prune_if_stale(flag)

    # .stop-signature dedups the Stop report across turns of ONE session and
    # is cheap to get wrong (worst case: one repeated report), unlike the
    # per-session files above (worst case: a running build's state vanishes).
    # Same stale-age treatment rather than an unconditional wipe.
    prune_if_stale(d / ".stop-signature")

    # Ledger rotation: APPEND into prev instead of renaming over it, so a
    # sibling session's SessionStart never destroys rows this session already
    # rotated in. Every row carries its own `session` field and is re-scoped
    # by scope_to_session() downstream, so accumulating rows from many
    # sessions into prev is harmless — capped so it cannot grow unbounded.
    ledger = d / L.LEDGER_NAME
    prev = d / L.PREV_LEDGER_NAME
    try:
        if ledger.exists():
            current_lines = [l for l in ledger.read_text(
                encoding="utf-8", errors="replace").splitlines() if l.strip()]
            prev_lines = []
            if prev.exists():
                prev_lines = [l for l in prev.read_text(
                    encoding="utf-8", errors="replace").splitlines() if l.strip()]
            combined = prev_lines + current_lines
            if len(combined) > L.PREV_LEDGER_CAP:
                combined = combined[-L.PREV_LEDGER_CAP:]
            prev.write_text(
                "\n".join(combined) + ("\n" if combined else ""), encoding="utf-8")
            ledger.unlink()
    except Exception:
        pass


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()
    if event.get("source") not in ("startup", "clear"):
        return
    clear_root(L.project_root({"cwd": event.get("cwd")}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
