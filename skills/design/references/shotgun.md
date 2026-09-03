# Step 2b · Shotgun / bake-off

**Load right after Step 2 (the gate), before Step 3, whenever Step 0 landed on page or
surface scope inside the `build` or `redesign` verbs.** Mandatory there — skippable
only on an explicit **"skip variants"** from the user. Component scope never loads this
file: route instead to `Skill(prototype)`, or the Interfaces `variant` method
([`upstream/interfaces/skills/variant/SKILL.md`](upstream/interfaces/skills/variant/SKILL.md)
+ [`picker.md`](upstream/interfaces/skills/variant/picker.md)) for a single component's
candidates. Where `options.md` and `wireframe.md` present rough directions on one page
for discussion, shotgun builds **real fold-depth HTML** per direction and serves it on
a live comparison board — describing three roads versus driving down each far enough
to feel the surface.

| | |
|---|---|
| **Reads** | Step 1b's reference lock, the register from `SKILL.md`'s table, the design catalog families, [`structure.md`](structure.md)'s six axes, [`house-physics.md`](house-physics.md)'s per-register inventories, the vault fingerprint registry (`wiki/projects/_index/design-fingerprints.md`, if present). |
| **Does** | Names 3–5 structural DIRECTIONS that differ on one primary axis; runs every pair through the fingerprint gate; builds one fold-depth cell per direction × engine with a fresh subagent per cell; serves the set on `scripts/board.py`; reads every cell as a screenshot itself; writes the tradeoff table. |
| **Writes** | `<session-dir>/board.json` + `cells/<dir>-<eng>/index.html` (working files, not shipped code); on human submit, `<session-dir>/approved.json`; an append to `.impeccable/shotgun/results.jsonl`; one line in the vault's bake-off log, when that section already exists. |
| **Human checks** | The board itself decides which direction and engine wins — never a favourite named in the tradeoff table. |

## 1 · Name the directions

From the register (`SKILL.md`'s table), the Step 1b reference lock, and the catalog
families, name **3 (up to 5) DIRECTIONS** that differ on **one** primary axis —
register, grammar, or colour world, never two or three at once, or the set stops being
a controlled comparison and starts being noise. Each direction states a one-phrase
**lane** (e.g. "print-tech paper", "dark-navy illustrated") and a **register** +
**grammar**, in the vocabulary `house-physics.md` and `structure.md` already use.

**Fingerprint gate.** Run every pairwise combination of directions through
`structure.md`'s six axes (heading placement, body composition, divider language,
button voice, image treatment, reveal pattern). Two directions must differ on **at
least 3 of the 6** — `structure.md`'s own anti-repetition rule ("no two should share
more than three of the six axes") applied here as a hard gate. A pair sharing 4 or
more axes is one direction wearing two names; merge them or push one further out.

**Vault registry check.** Cross-check each direction against
`wiki/projects/_index/design-fingerprints.md` if it exists — confirm no new direction
repeats one already logged there. Owned by another agent: read it, never edit it
beyond the Step 5 bake-off log append. **If it does not exist yet, skip this check and
say so out loud** rather than inventing its contents.

## 2 · Pick the engines

Default ENGINES = `{our chain, impeccable only}` — two build paths run against the same
brief, so the board measures the pipeline too. Add on request: `taste-skill v2`,
`frontend-design`, `scroll-craft`.

## 3 · Build each cell

One **fresh Sonnet subagent per cell** (directions × engines — 3 directions × 2
engines = 6 subagents, run in parallel). Fresh means it reads *only* that engine's own
skill files, the brief, and the locked tokens — never the other engine's files, never
another cell, never the board.

**Budget.** Three fold-depth cells run roughly **1 full build** in agent-time. Five
directions × two engines is closer to 3–4 full builds — spend it deliberately, default
to 3 directions, go to 5 only when the brief genuinely spans that much space.

**Subagent prompt template** (fill every `{…}`):

```
Build ONE fold-depth cell for a design bake-off. This is a single candidate on a
comparison board, not the final build. Work fast; do not iterate.

Direction: {direction_name} — {lane}
Register: {register}
Grammar: {grammar}
Engine: {engine_name}

Read ONLY:
{engine_skill_files}

Do not read any other engine's skill files, any other direction's cell, or the
board itself.

Brief: {brief}

Locked tokens (from Step 1b / DESIGN.md — do not re-derive, do not invent a new
palette or type stack):
{locked_tokens}

Build:
- The fold plus the first section only, roughly 150 lines of real HTML/CSS, one
  self-contained file.
- Real copy for this business, in this direction's voice — no lorem ipsum, no
  placeholder headline.
- Real tokens: the palette and type above, applied at this direction's register.
- No screenshots. No iteration. One pass, then stop.

Write the result to: {output_path}  (cells/{direction_id}-{engine_id}/index.html)

Report exactly one of: DONE {output_path} <line count>  ·  FAILED <reason>
```

## 4 · Serve and read it yourself

```bash
python "$HOME/.agents/skills/design/scripts/board.py" <session-dir> --port 4620 --open
```

`board.py` writes `board.html` into `<session-dir>` and serves the whole directory —
tabs for each direction (keys 1–5), two panes side by side (keys ←/→ swap the engine
pair), synced scroll, and a rating/comment/remix control under each cell. A missing
cell renders as "not built" rather than a broken frame.

Then, **yourself, never delegated to a subagent** — screenshot every built cell:

```bash
python "$HOME/.agents/skills/design/scripts/shoot.py" <session-dir>/.shots \
  <session-dir>/cells/A-chain/index.html <session-dir>/cells/A-impeccable/index.html ...
```

Read every screenshot, then write the tradeoff table:

| Direction | Axis position | Right when | Costs |
|---|---|---|---|
| [name] | [where it sits on the primary axis] | [the case that favours it] | [what it gives up] |

**Never mark a favourite in this table.** State costs and conditions; the human picks.

**Anti-convergence test.** Swap the headline between two cells. If nobody would notice
the swap, one of them failed the gate in Step 1 — fold it back into naming directions
and re-run with a wider gap on the primary axis, don't ship it as-is.

## 5 · The human chooses

The board is the chooser, not a question asked in chat. Wait for `feedback.json` with
`submit: true`, then write:

```json
{"direction": "A", "engine": "chain", "lane": "...", "register": "...", "grammar": "...", "feedback": {"...": "..."}, "date": "2026-09-03"}
```

to `<session-dir>/approved.json`. Log the engine bake-off result — which engine won,
on which family — as one appended line in `.impeccable/shotgun/results.jsonl`. Then
append one line to the vault's `wiki/projects/_index/design-fingerprints.md`, under
its "bake-off log" section (create that section if the file exists but the section
doesn't; never touch any other part of the file — another agent owns it). **If the
file does not exist yet, do not create it** — write the log line to
`.impeccable/shotgun/results.jsonl` only, and say plainly that the vault log was
skipped for that reason.

## 6 · Hand off

The chosen cell becomes **Step 4's** starting point in the main flow — its markup,
locked tokens, and structural fingerprint carry forward. The full build (every
section, all 8 states, imagery, the copy gate) proceeds from there, not a second cold
start.

## 7 · After the full build

Once the chosen direction ships as a complete page, element-level variation — three
variants *within* the same identity, a button weight, a card density, a hero crop — is
`impeccable live`'s job, not another bake-off round:
[`~/.agents/skills/impeccable/reference/live.md`](../../impeccable/reference/live.md).
Shotgun picks the identity; `live` tunes the knobs inside it. The whole procedure exists
to make the Step 4 anti-convergence swap noticeable every time — passing it with
headlines swapped freely means the budget bought nothing.
