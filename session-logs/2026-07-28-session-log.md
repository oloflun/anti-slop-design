# Session Log — 2026-07-28

Continuation of the 2026-07-27 design-system rebuild (see `2026-07-27-session-log.md`). That session ended with the system built and propagated; this one closed two gaps in it.

## Session Summary

Synced Anton's own live `~/.carl/carl.json` to the v2 DESIGN content that had already shipped to the package the day before, and added the domain-governance rule to his personal config too. Then audited the upstream `Leonxlnx/taste-skill` v2 release, found that only one of its seven skills had actually changed, and absorbed that skill's genuinely-new content into the design references as gates 66–88 plus a redesign protocol, a fourth palette-calibration cluster, and an official-design-system map. Reversed the Snajp handoff instruction per Anton: the next session now reads the product docs first rather than deferring them.

## What Changed

### Files Created
- `skills/design/references/production-tells.md` — gates 66–88. About twenty empirically-derived micro-decoration signatures from taste-skill v2 §9.F, each annotated with what impeccable's detector already catches mechanically and what does not.
- `session-logs/2026-07-28-session-log.md` — this file.

### Files Modified

**anti-slop-design** (committed `3eb763f`)
- `skills/design/SKILL.md` — `production-tells.md` added to the binding-while-building list, the reference index, and the exit bar (including an explicit zero-em-dash line)
- `skills/design/references/gates.md` — 66–88 range indexed, with a note on why it is separate from 1–57
- `skills/design/references/scope-discipline.md` — redesign protocol added: mode detection, audit-before-touching, preservation rules, modernisation levers, never-change-silently list
- `skills/design/references/invention.md` — fourth calibration cluster (premium-consumer beige+brass+oxblood+espresso) with concrete banned hex families; serif discipline
- `skills/design/references/process.md` — the one-line design read, the three intensity dials, the brief→official-design-system map, the out-of-scope boundary
- `skills/design/references/component-routing.md` — `design-taste-frontend` now routed for page-scope landing/marketing/portfolio surfaces
- `attribution/UPSTREAMS.md` — documented the v2 upgrade, which skills changed, and where each ported section landed
- `session-logs/2026-07-27-session-log.md` — handoff line 88 superseded (see Decisions)
- `plans/2026-07-27-snajp-rebuild.md` — scope note reversed; "read the docs" moved to the top of the Next Steps checklist

**super-intelligence** (committed `d59202e`, v0.4.1)
- `skills/design-taste-frontend/SKILL.md` — v1 → v2 (226 → 1206 lines)
- `skills/design/` — full re-sync of SKILL.md + 116 references
- `VERSION`, `package.json`, `CHANGELOG.md` — 0.4.0 → 0.4.1

**Live config**
- `~/.carl/carl.json` — `DESIGN` domain synced to the same v2 content shipped to the package (5 rules, decisions `design-001` + `design-002`); new GLOBAL rule 9 (ask before creating a domain / adding project-identifying content to an always-on one). **`HAAJP_DESIGN` deliberately kept.**
- `~/.agents/skills/design-taste-frontend/SKILL.md`, `~/.agents/skills/design/` — synced

### Files Moved/Deleted
- None. Backup written to `%TEMP%/claude/carl.json.pre-sync-backup` before the live CARL edit.

## Decisions Made

- **`HAAJP_DESIGN` stays in the live config, stays out of the package.** The 07-27 privacy fix was about what ships to other users. On Anton's own machine a project-private domain is exactly what CARL domains are for. Only the *package* copy needed scrubbing.
- **Port taste-skill v2's content; do not adopt the skill wholesale.** Its 1206-line SKILL.md carries a competing end-to-end methodology (its own brief inference, dials, tells, pre-flight check) that would fight the front door. Deduplicated against Hallmark's 57 gates and impeccable's 68 detector rules first, then ported only what was genuinely uncovered.
- **Gates 66–88 live in their own file, not inline in `gates.md`.** They are a coherent set from one source with a distinct character — micro-decoration rather than structure — and inlining twenty more gates would turn the index into a document. Matches how `slop-test.md` already holds 1–57.
- **Gate 75 (em-dash) is zero-tolerance and wins.** Three rules in this system now touch em-dashes: impeccable's `em-dash-overuse` (threshold-based), `humanizer`'s style ban (copy gate), and gate 75. Upstream's argument is persuasive — "use sparingly" has been ignored in every prior round, so the phrasing has to be binary.
- **The intensity dials are orthogonal to the tier gate.** The tier decides *where direction comes from*; the dials decide *how loud the execution is*. A Tier-0 locked brand can legitimately build at variance 9 or variance 4. Recorded explicitly so a future session does not treat them as competing systems.
- **`design-taste-frontend` is routed but palette-locked.** It was installed and never reachable before. Now it fires on page-scope marketing surfaces — for craft and structure only, under the same Tier 0–2 rule as every other specialist: it may not pick the palette.
- **Snajp handoff reversed (Anton).** The original defer-reading instruction existed to keep the design-system plan's context clean while that system was being designed. That system is now built, so the reason is spent. The next session reads the product docs first. Noted as *superseded*, not silently rewritten, so the original reasoning stays legible.

## Context & Discussion

- **Anton's prompt was the right instinct.** I had audited only the *installed* copies of the taste-skill family and never checked upstream for version drift. Five of the seven skills turned out byte-identical between v1 and v2, so the audit conclusions from 07-27 (the hardcoded palettes in `minimalist-ui`, `industrial-brutalist-ui`, `high-end-visual-design`) all still hold. But `design-taste-frontend` had been rewritten wholesale, and it was the one skill the rebuilt router never referenced — so the gap was real.
- **Upstream restructured directory names.** v2 moved each skill into its own renamed folder (`taste-skill`, `brutalist-skill`, `minimalist-skill`, `gpt-tasteskill`, `soft-skill`, `redesign-skill`, `output-skill`) while keeping the same `name:` in frontmatter. v1 is preserved as `taste-skill-v1` / `design-taste-frontend-v1`. Anything syncing by directory name will silently miss the update.
- **A tool call ran twice.** After a "Tool result missing due to internal error", the `design-taste-frontend` sync script executed twice, so its "before" reading showed the post-copy line count. Git history confirmed the repo copy was genuinely still v1 (226 lines) and the end state is correct. The task list was also wiped by the same error and had to be rebuilt.
- **Most of v2's Section 9 was already covered**, which is the point of deduplicating first: purple gradients, Inter-as-default, 3-column card rows, gradient text, Jane Doe / Acme placeholder content, custom cursors, `numbered-section-labels`, `cream-palette`, `em-dash-overuse` all had existing coverage in Hallmark's anti-patterns or impeccable's detector. Roughly twenty items did not.

## Open Threads

Carried forward from 2026-07-27, all still open:
- **Snajp rebuild** — the first genuine end-to-end test. Route-vs-invocation gap must be zero.
- **Promote `design-gate.py` to blocking** after one clean Snajp run.
- **Dual-hook-system question** — impeccable v4's project-level PostToolUse manifest vs. our global one. Only bites if `npx impeccable install` runs inside a project.
- **Model-behaviour checks unverified** — gate-order judgment, inheritance, targeted-change rule, copy-gate output. Not provable by hook tests.
- **Neither repo pushed.** Both on `design-system-v2`.
- **v3-leftover deletion manifest** in `super-intelligence` — ~22 untracked `skills/impeccable/` files orphaned by the v4 upgrade. Listed, not deleted, per the destructive-action guard. Needs an explicit exact-path manifest and Anton's approval.

New this session:
- **`MEMORY.md` is over cap** — 2358 / 2200 chars before this session's additions. Audited and offloaded below.

## Cross-Project Handoffs

**→ snipe-leads (Snajp rebuild)** — unchanged in substance from the 07-27 log and `plans/2026-07-27-snajp-rebuild.md`, with one revision:

> **First action: read `snipe-leads`' project documentation.** Understand the product properly — the existing leads agent *and* the newer dedicated support agent, and how the two relate as a single offering — before touching the site. (Revised 2026-07-28 by Anton; the original instruction deferred this to avoid diluting the design-system plan's context, and that reason is now spent.)

Everything else holds: rename to Snajp, merge the two offerings, big wordmark with a clickable Leads/Support toggle that swaps page content, surface the orphaned `/snajp-support`, present it uniformly with the email studio and improve both, keep the large type, drop the corner editorial text, Nordic SaaS register. It is a **redesign · preserve** (partial rebrand), not greenfield — the newly-ported redesign protocol in `scope-discipline.md` now covers exactly this case. Named traps: Nordic SaaS is not `minimalist-ui`'s Notion palette; "large fonts, drop the fine print" is not `industrial-brutalist-ui`'s hazard-red grid.

## Current State After This Session

The design system is complete, verified at 60/60 mechanical checks, and committed in both repos on `design-system-v2` — anti-slop-design at `3eb763f`, super-intelligence at `d59202e` (v0.4.1). Neither is pushed. Anton's live config now matches what ships. The upstream taste-skill drift is closed and documented, so a future audit can tell at a glance which of those seven skills are pinned and which move. What remains unproven is still everything that depends on model judgment rather than mechanism; the Snajp rebuild is the next session and the telemetry report is the evidence.


---

## Addendum — orchestration foundation, product surfaces, vault hub doc

Continued after the initial conclude. Three further pieces of work.

### Skill orchestration foundation (commit `5f8a465` / `79f7811`, v0.4.2)

Anton asked which redesign procedure is prioritised — Hallmark's `verbs/redesign.md` or the taste-skill protocol. The answer was **neither, nothing prioritised them**, which opened a full audit of all ~40 design-capable skills.

- **Root gap:** the system routed by *component* but never by *task type*. Build / redesign / audit / polish / study all got identical treatment.
- **Resolved the redesign collision:** three procedures, complementary only when sequenced — mode detection (`scope-discipline.md`) → tier gate → page shape (`verbs/redesign.md`). Mode beats tier beats page shape. `redesign-existing-projects` drops out as redundant.
- **Found a high-severity bug.** `tier()` reported `0-locked` on `DESIGN.md` *existence alone*, but five skills write that filename in three incompatible formats — `design-md` and gstack's `design-consultation` emit prose only. A prose file made the system announce *"TIER 0 — LOCKED, inherit the system"* while `design-gate.py` enforced nothing; verified empirically that `#FF00FF` + Comic Sans passed silently. Strictly worse than ungated, since the model skips derivation *and* gets no enforcement. Now `0-locked` / `0-prose` / `ungated`, with `0-prose` stating plainly that the gate is blind.
- **Found two undocumented parallel pipelines** — gstack (`design-consultation` → `design-shotgun` → `design-html` → `design-review`) and Stitch. Both write their own `DESIGN.md`. Now documented with lane boundaries.
- New `references/skill-orchestration.md`: 7 phases, verb routing, full skill catalog with role/boundary per skill, 9 collisions with resolutions.
- `design-intent.py`: 8-verb detection (EN + SV), re-firing on verb *change* rather than once per session.

### Product surfaces as Operate mode (commit `b7c4a02` / `4b84507`, v0.4.3)

Dashboards, admin, settings, tables and editors were listed as out of scope. Wrong for real work — they sit inside corporate sites constantly. The boundary is a **mode**, not an exclusion.

Audited the stack before proposing imports: **nothing new needed**. `impeccable` v4 already ships an Operate mode with `reference/operate.md`, never wired into the router. `shadcn-ui`, `dataviz`, `ui-ux-pro-max`, `web-design-guidelines`, `impeccable harden`/`onboard` covered the rest.

The gate does **not** change (same brand tokens, gate 65 across the seam); the **register** does — one font family, fixed rem scale, Restrained colour floor, 150–250ms state-only motion, density over expression. Marketing references (hero-enrichment, macrostructures, six-axis fingerprint, gates 66–88) do not load there. Detection is automatic via a new `product` routing rule.

### Vault hub doc + permanent /conclude rules

- **Created `anti-slop-design.md`** at the repo root — the project hub doc, surfacing in the vault through the junction. Searched first and confirmed no existing one (only the junction dir, unrelated skill files, and git refs matched). Carries the four decision layers, the hook chain, invariants that bite, a full document map, verification, and status. `AUDIT.md` marked stale in the map rather than deleted.
- **Three permanent `/conclude` rules added** to both the skill (Steps 3d, 8b, and a strengthened 3c) and the CARL `CONCLUDE` domain: the vault hub doc is mandatory for infra work and must be searched-for before writing; installer sync is **unconditional** for infra work rather than gated on `upstream.json`; and `qmd update` + `gbrain sync` must run before the session closes.

`verify-design-system.py`: 60 → 74 → 79 checks, all passing.

<!-- session-state
date: 2026-07-28
type: infrastructure-followup
files_created:
  - skills/design/references/production-tells.md
  - session-logs/2026-07-28-session-log.md
files_modified:
  - skills/design/SKILL.md
  - skills/design/references/gates.md
  - skills/design/references/scope-discipline.md
  - skills/design/references/invention.md
  - skills/design/references/process.md
  - skills/design/references/component-routing.md
  - attribution/UPSTREAMS.md
  - session-logs/2026-07-27-session-log.md
  - plans/2026-07-27-snajp-rebuild.md
  - super-intelligence/skills/design-taste-frontend/SKILL.md
  - super-intelligence/skills/design/
  - super-intelligence/VERSION
  - super-intelligence/package.json
  - super-intelligence/CHANGELOG.md
  - ~/.carl/carl.json
  - ~/.agents/skills/design-taste-frontend/SKILL.md
  - ~/.agents/skills/design/
decisions_made: 13
open_threads: 8
handoffs_pending:
  - target: snipe-leads
    topic: "Snajp rebuild — READ THE PRODUCT DOCS FIRST (leads agent + new support agent), then Tier-1 redesign-preserve; first end-to-end telemetry test"
priority_changes: false
status_updated: true
next_session_focus: "Snajp rebuild in snipe-leads: read product docs, then redesign-preserve with route-gap-zero telemetry"
session-state -->
