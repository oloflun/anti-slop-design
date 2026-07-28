---
title: Anti-Slop Design
type: project
status: active
project_slug: anti-slop-design
repo: C:\\Users\\Anton L\\anti-slop-design
updated: 2026-07-28
---

# Anti-Slop Design

Canonical project hub. Read this first to orient; every section points at the document that carries the detail.

## What it is

A Claude Code **design router**. It writes no visual rules of its own — it sequences other people's work (impeccable, Hallmark, taste-skill, Anthropic's Claude Design prompt, copywriting, humanizer) and enforces that they do not overwrite the client's brand on the way through.

**The one rule everything serves:**

> **Brand derives direction. Skills supply craft. Themes are the last resort.**

Every failure this system was built to fix came from inverting that — a specialist skill set the visual direction and the brand got repainted in the skill author's palette.

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

Design system v2 complete and verified. Shipped to other users via the `super-intelligence` installer (v0.4.3+).

**Open:** the Snajp rebuild in `snipe-leads` is the first end-to-end test — read that repo's product docs first, and the route-vs-invocation gap in `.impeccable/design-report-*.md` must be zero. Then promote `design-gate.py` from advisory to blocking (`DESIGN_GATE_BLOCKING=1`).

**Decisions left open:** the installed `hallmark` skill competes with `design` for auto-invocation while its 105 references are already ported here; `polish` carries a stale `/teach-impeccable` dependency (v3 naming).

## Related

- [[super-intelligence]] — the installer that distributes this
- Session logs: `session-logs/` · Plans: `plans/`
