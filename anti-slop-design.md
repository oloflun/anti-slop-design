---
title: Anti-Slop Design
type: project
status: active
project_slug: anti-slop-design
repo: C:\\Users\\Anton L\\anti-slop-design
updated: 2026-08-01
---

# Anti-Slop Design

Canonical project hub. Read this first to orient; every section points at the document that carries the detail.

## What it is

A Claude Code **design system**. It writes no visual rules of its own beyond one addition — it sequences other people's work (impeccable, Hallmark, taste-skill, Anthropic's Claude Design prompt, copywriting, humanizer) and enforces that they do not overwrite the client's brand on the way through.

**The one rule everything serves:**

> **Brand derives direction. Skills supply craft. Themes are the last resort.**

Every failure this system was built to fix came from inverting that — a specialist skill set the visual direction and the brand got repainted in the skill author's palette.

## 2026-08-01 rework: registers replace the house style, exit bar goes mechanical

Full rationale: [`plans/2026-07-31-what-actually-made-the-difference.md`](plans/2026-07-31-what-actually-made-the-difference.md).

Archaeology across three prior sessions established that the 2026-07-28 v2 rework
(below) fixed v1's mechanical failures — hooks not firing reliably, specialist skills
repainting brands — but never asked why v1's *output* had been good. Craft that lived
resident in one dense context became 120 on-demand reference files; the step that named
an aesthetic lane before writing code disappeared; every quality gate stayed negative,
so a flat, on-palette, thoroughly generic page passed all 88 of them untouched.

- **`SKILL.md` "The craft floor"** — a resident (not routed) section: name the lane
  before code; a **register table** — editorial print / cinematic dark / illustrated
  dark / modern clean / warm photographic / historical art — picked from the business,
  not from which example happens to exist on disk; house physics with exact values;
  a composition contract; an apparatus budget; "a muted tone needs a value per
  ground"; "reduced motion removes motion, not content."
- **[`house-physics.md`](skills/design/references/house-physics.md)** (new) —
  structural invariants true in every register, then a per-register inventory with
  exact values pulled from real page source, not memory.
- **[`sites/`](sites/)** — six worked examples now, not three: `calyx.html` /
  `horai.html` / `hyperborea.html` (editorial print / cinematic dark / illustrated
  dark, from the original v1 build) plus `tidvatten.html` (modern clean),
  `vintergatan.html` (editorial print, a second exemplar), `vinterspelen.html`
  (historical art — built with **no worked example on disk to copy**, the hardest
  test of whether the register table teaches derivation rather than imitation), and
  `klova/` (warm photographic, vendored from a real client project — its README
  explains why it correctly breaks nearly every "invariant" the earlier system
  would have forced on it).
- **`design-stop.py`** — the Stop hook now **blocks** ending a design session when UI
  edits exist that no rendered image was Read afterward (capped at 2 blocks/session,
  then degrades to advisory). This is the mechanical version of the instruction that
  made the difference in the Snajp session — "iterate until you honestly beat the
  references, verified on pixels" — previously only enforced when a user retyped it
  as an explicit goal.
- **`design-session-start.py`**, **`design-vision-track.py`** (new hooks) — session
  state that never cleared before now clears on `SessionStart`; a `PostToolUse` hook
  on `Read` logs when a render actually enters context, feeding the block above.
- **`design-verify-gate.py`** — inverted from "prefer read_page over screenshot, two
  rounds max" to "judge from pixels, iterate until a full pass finds nothing."
- **[`scripts/contrast.py`](skills/design/scripts/contrast.py) /
  [`contrast_over_media.py`](skills/design/scripts/contrast_over_media.py)** (new) —
  both were wrong on their first real run, in ways that would have passed a broken
  page: one only parsed `rgb()` against Tailwind 4's `oklch()` output, the other
  measured text-over-photo against the page background instead of the rendered
  plate with the text hidden.

Verified with three blind one-shot builds from fresh subagents — no iteration, no
dialogue — all of which the author judged to clear the reference bar on the first
attempt. `verify-design-system.py` 80/80. Applied to `alunix-site` (a new scroll-driven
set-piece) and `klova-hamnkrog` (a design audit, 8 fixes, both committed).

**Not yet done:** `install.mjs`/`upgrade.mjs` in `super-intelligence` don't wire the
two new hooks into `settings.json` for existing installs yet — `deployTemplate()`/`wf()`
skip writes when the destination already exists, so this needs an explicit additive
merge. `super-intelligence` 0.4.5 has the file sync committed locally, not pushed.

## 2026-07-28 rework (superseded above, kept for history)

## How it decides — four layers, in order

| Layer | Question | Detail |
|---|---|---|
| **1. Verb** | What kind of job is this? | 8 verbs (EN + SV): build · redesign · audit · polish · study · explore · system · verify. Re-fires when the verb *changes*, not once per session. → [`skill-orchestration.md`](skills/design/references/skill-orchestration.md) §2 |
| **2. Gate** | Where does direction come from? | Tier 0-locked / 0-prose / 1-derive / 2-reference / 3-invent. First tier with evidence wins. → [`brand-derivation.md`](skills/design/references/brand-derivation.md), [`invention.md`](skills/design/references/invention.md) |
| **3. Mode** | Marketing or product? | Persuade/Read/Experience use the marketing stack; Operate (dashboards, admin, tables, editors) uses a different register on the *same tokens*. → [`product-surfaces.md`](skills/design/references/product-surfaces.md) |
| **4. Component** | Which craft skill for this file? | Signal-matched routing table, parsed by the hooks. → [`component-routing.md`](skills/design/references/component-routing.md) |

## The hook chain

Enforcement lives at **edit boundaries**, not turn boundaries — the original system injected guidance once per prompt and drifted across a sixty-tool-call build turn.

```
UserPromptSubmit    design-intent.py        verb + tier + this project's locked tokens
PreToolUse  write   design-gate.py          DENY contract violations before they land
PreToolUse  browser design-verify-gate.py   inspection discipline before the first look
PostToolUse write   design-route.py         name the right skill for what was written
PostToolUse Skill   design-telemetry.py     attribute every skill call to its component
Stop                design-stop.py          deep detector pass + session report
```

Source: [`.claude/hooks/`](.claude/hooks/) (vendored) · live at `~/.claude/hooks/` · shipped in `super-intelligence/hooks/`.

**The load-bearing limitation:** hooks inject text and deny writes. They **cannot load a skill** — only the model calls `Skill()`. Every route is therefore a *suggestion*, which is why the route-vs-invocation gap is measured rather than assumed. `design-gate.py` is the one hard enforcement point.

## Invariants that bite if broken

- **Only write `DESIGN.md` through `impeccable document` or `brand-system`.** Five skills write a file by that name in three incompatible formats. A prose-only one used to make the system announce *"TIER 0 — LOCKED"* while enforcing nothing (`#FF00FF` + Comic Sans passed silently). Now reported honestly as `0-prose`.
- **`minimalist-ui`, `industrial-brutalist-ui`, `high-end-visual-design` may never set direction** — each hardcodes a full palette. Gate 60 treats their hex in a Tier 0–2 build as a contract violation, logged as a `trap` event.
- **Redesign needs all three procedures, in order:** mode detection → tier gate → page shape. Mode beats tier beats page shape.
- **Marketing references do not load on product surfaces** — hero enrichment, macrostructures, the six-axis fingerprint, gates 66–88.
- **A local addition inherits its surface.** It never re-runs the gate and never starts a second identity (gate 65).
- **Don't mix pipelines.** gstack and Stitch are complete parallel workflows that write their own `DESIGN.md`; pick one lane per project.

## Document map

**Entry points**
- [`skills/design/SKILL.md`](skills/design/SKILL.md) — the front door. Dispatcher only; ~240 lines.
- [`ROUTER.md`](ROUTER.md) — plain-English explainer of the architecture.
- [`README.md`](README.md) — public-facing, includes the v1→v2 rebuild rationale and demo sites.

**Foundation**
- [`skill-orchestration.md`](skills/design/references/skill-orchestration.md) — **the foundation doc.** 7 phases, verb routing, full skill catalog with each skill's role and boundary, 9 known collisions and their resolutions, the parallel pipelines. Read for any job larger than one component.
- [`product-surfaces.md`](skills/design/references/product-surfaces.md) — Operate mode.

**The gate**
- [`brand-derivation.md`](skills/design/references/brand-derivation.md) — Tier 1. VISUAL/CONTENT FOUNDATIONS interrogations, logo safety, the exact-values rule.
- [`invention.md`](skills/design/references/invention.md) — Tier 3, plus the four AI palette-calibration clusters.
- [`study.md`](skills/design/references/study.md) — Tier 2.

**Rules**
- [`gates.md`](skills/design/references/gates.md) — index. 1–57 Hallmark · 58–65 ours · 66–88 production tells · mechanical detector mapping.
- [`slop-test.md`](skills/design/references/slop-test.md) — gates 1–57, ported verbatim.
- [`production-tells.md`](skills/design/references/production-tells.md) — gates 66–88, micro-decoration signatures.
- [`scope-discipline.md`](skills/design/references/scope-discipline.md) — targeted-change rule, inheritance checklist, **redesign protocol**.

**Process**
- [`process.md`](skills/design/references/process.md) — working method, question calibration, intensity dials, official-design-system map.
- [`copy-gate.md`](skills/design/references/copy-gate.md) — copywriting → humanizer, every language.
- [`options.md`](skills/design/references/options.md) · [`wireframe.md`](skills/design/references/wireframe.md) · [`handoff.md`](skills/design/references/handoff.md)

**Sibling skills**
- `skills/design-verify/` — batched browser inspection.
- `skills/brand-system/` — builds a full system, emits `{brand}-design` as an installable skill.

**Meta**
- [`attribution/UPSTREAMS.md`](attribution/UPSTREAMS.md) — every upstream, what it provides, what we changed.
- [`verify-design-system.py`](verify-design-system.py) — 79 mechanical checks. Run after any change.
- [`AUDIT.md`](AUDIT.md) — **stale.** The pre-rebuild 32-skill audit; superseded by `skill-orchestration.md`. Kept for history.

## Verification

```bash
python verify-design-system.py
```

79 checks: install, settings wiring, routing table, reference fidelity against upstream, contract enforcement, verb routing, prose-only false-lock, product-vs-marketing routing, false positives, kill switch.

Not covered — model behaviour, provable only by a real build's telemetry report: gate-order judgment, inheritance, the targeted-change rule, copy quality.

## Status

Design system rebuilt 2026-08-01 (registers + mechanical exit bar), verified with three
blind one-shot builds, shipped to `super-intelligence` 0.4.5 (local commit, not yet pushed).

**Open:** `install.mjs`/`upgrade.mjs` need an additive merge for the two new hooks to
reach existing installs. The `hallmark` skill still competes with `design` for
auto-invocation while its 105 references are already ported here; `polish` carries a
stale `/teach-impeccable` dependency (v3 naming).

## Related

- [[super-intelligence]] — the installer that distributes this
- Session logs: `session-logs/` · Plans: `plans/`
