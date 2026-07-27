# Session Log — 2026-07-27

## Session Summary

Rebuilt the `design` skill from a 161-line pointer-router into a brand-derivation gate backed by a 6-hook enforcement chain, fixing three root causes: it fired once per *turn* (not per file write), it was a table of contents rather than a procedure, and the specialist skills it routed to overwrite any project's brand with their own hardcoded palettes. Then propagated the whole system into the `super-intelligence` installer as v0.4.0 so other users get it, which surfaced and fixed a privacy leak (a project-private CARL domain and project-specific rules were shipping in shared always-on config). Both repos are committed on `design-system-v2` branches, unpushed. Snajp rebuild deliberately not started — it is the first real end-to-end test of the new system.

## What Changed

### Files Created

**anti-slop-design** (`skills/design/references/` — 10 new alongside 105 ported byte-identical from Hallmark):
- `brand-derivation.md` — Tier 1 procedure, ported from Anthropic's Claude Design "Create design system": VISUAL FOUNDATIONS + CONTENT FUNDAMENTALS interrogations, logo-safety rules, the exact-values rule ("if the kit says 5px, write 5px, not 4px")
- `invention.md` — Tier 3, "Frontend design" ported verbatim + calibration against the three AI aesthetic clusters
- `process.md` — 5-step method, context mandate, question-calibration table
- `scope-discipline.md` — targeted-change rule, 8-axis inheritance checklist, content guidelines
- `component-routing.md` — signal→skill table; carries the canonical JSON block `design-route.py` parses (single source of truth)
- `gates.md` — index of gates 1–57 (Hallmark, in `slop-test.md`) + new 58–65 + detector rule mapping
- `copy-gate.md`, `wireframe.md`, `options.md`, `handoff.md`
- `skills/design-verify/SKILL.md` — batched browser inspection procedure
- `skills/brand-system/SKILL.md` — full design-system builder, emits `{brand}-design` as an installable skill
- `verify-design-system.py` — 60 mechanical checks
- `.claude/hooks/*.py` — 7 vendored hook files

**~/.claude/hooks/** (live): `design_hook_lib.py`, `design-gate.py`, `design-route.py`, `design-telemetry.py`, `design-verify-gate.py`, `design-stop.py`, `design-intent.py`

**super-intelligence**: `hooks/` (new package dir, 7 files); `skills/design-verify/`, `skills/brand-system/`, `skills/humanizer/`

### Files Modified

- `anti-slop-design/skills/design/SKILL.md` — rebuilt as 208-line dispatcher on Hallmark's spine
- `anti-slop-design/ROUTER.md`, `README.md`, `attribution/UPSTREAMS.md` — rewritten for v2
- `~/.agents/skills/impeccable/` — 3.x → 4.0.2
- `~/.agents/skills/humanizer/` — newly installed from blader/humanizer
- `~/.claude/settings.json` — +6 hook registrations (CARL and gstack hooks verified intact)
- `~/.carl/carl.json` — DESIGN domain updated to v2 content, `design-002` decision added, new GLOBAL governance rule. `HAAJP_DESIGN` **kept** (private config, never shipped)
- `super-intelligence/install.mjs` — `withDesignHooks` flag, `step_design_hooks` (Step 3c), `mergeDesignHooksIntoSettings()`, skills count 141→211
- `super-intelligence/upgrade.mjs` — hooks sync + same additive settings merge
- `super-intelligence/templates/.claude-settings.json` — all 6 hook registrations for fresh installs
- `super-intelligence/carl/carl.json` — `HAAJP_DESIGN` **removed**, DESIGN generalized, governance rule added
- `super-intelligence/docs/design-workflow.md` — rewritten for the gate + hook chain
- `super-intelligence/package.json` — v0.4.0, **`files[]` was missing `hooks/`** (npm publish would have silently dropped the entire hook chain)
- `super-intelligence/VERSION` → 0.4.0, `CHANGELOG.md` → full 0.4.0 entry
- `super-intelligence/README.md` — 141→211 skills, private project name in an example replaced

### Files Moved/Deleted

- `~/.agents/skills/impeccable` v3 → backed up to `~/.agents/backups/impeccable-v3-backup-20260727/` (moved out of `skills/` immediately — it had registered itself as a loadable skill)
- v3 impeccable files deleted as part of the v4 replace; **OneDrive has since restored 22 of them** — see Open Threads

## Decisions Made

- **Brand derives direction; skills supply craft; themes are last resort.** The inversion this whole rebuild implements. Verified by reading the skills: `minimalist-ui` hardcodes Notion's palette, `industrial-brutalist-ui` declares `#E61919` "the ONLY accent color", `high-end-visual-design` ships 3 fixed archetypes. Routing to them as direction-setters is the mechanism behind the drift.
- **Enforcement at edit boundaries, not turn boundaries.** Root cause of "the skill fires once then drifts": CARL is `UserPromptSubmit`-only, but a build turn is 60 tool calls. Hooks fire per write.
- **Upgrade impeccable to v4.0.2 with the dice disabled.** v4 states the thesis natively ("The brief wins... Redirecting a clear brief toward your taste is failure"). Its `concept-seed.mjs` catalog "does not ship with the skill" (paid API), so it degrades to assignment-only anyway; disabled outside the explicit no-reference lane.
- **Reuse impeccable's detector rather than reimplementing contract checks.** Its 68 rules include `design-system-color/font/font-size/radius` which parse `DESIGN.md` directly. `design-gate.py` shells out to it — the contract is enforced by the upstream's own parser.
- **Add a sibling `design-intent.py` instead of editing `carl-hook.py`.** Claude Code runs every hook registered for an event, so a 60-line sibling achieves the same injection with zero regression risk to a 921-line load-bearing file. Deviation from the approved plan, made for safety.
- **Ship the contract gate advisory-first.** `DESIGN_GATE_BLOCKING=1` promotes it. False denials stalling a long session cost more than the drift they prevent, until there's a clean run on record.
- **Drop the `--design-gate-blocking` installer flag.** It would only have changed printed text (can't portably set a persistent env var from a one-shot installer) — misleading UX.
- **Keep `HAAJP_DESIGN` locally, remove it from the package.** It's the user's own private config where it's legitimate; it was never legitimate in shared always-on config shipped to every installer user.
- **References are ported verbatim and are the source of truth.** Commentary supplies direction only. The front door stays light by *splitting* (dispatcher + per-branch references), never by cutting. Enforced by a fidelity diff on every verification run.

## Context & Discussion

- The user's core insight, which reframed the whole task: a design skill's own house style is a contaminant. impeccable.style v4 marks its *own previous landing page* as a slop example — that's an author's current aesthetic promoted to a universal rule, not taste evolving. Hallmark's 20-theme catalog is the same failure in a different shape: rotation between templates is variety-across-outputs, not design-derived-from-brand.
- HAAJP is the reference case for Tier 1: `#F27722` + Afacad uppercase + black surfaces + asymmetric rhombus derives from the mark and the product. No catalogue produces it. It works *because* it isn't black-and-white minimalism.
- The user corrected an early over-compression: I had dismissed `claude-design.md` as ~90% unusable runtime specifics and taken "four things". It actually contains the Tier 1 derivation procedure in full. Re-read properly and ported at fidelity. Lesson: the user's steer to "not skip anything unless you can motivate it" was right and produced materially better references.
- The user also rejected a "trim to 350 lines" framing for the front door. Correct answer was the dispatcher/reference split — nothing gets trimmed.
- Anthropic's own design product validates the gate order: its "Frontend design" guidance is scoped to work *"NOT governed by an existing brand or design system"*, and Hi-fi design calls building from scratch *"a LAST RESORT"*.
- **Mid-turn correction from the user:** private project references must be excluded from the public package. This surfaced that `HAAJP_DESIGN` and Alunix-specific rules had been shipping in `carl/carl.json` since v0.2.0. Fixed, plus a governance rule so it can't recur silently.
- The design hooks were **not active during this session** — `settings.json` registrations load at session start, and they were added mid-session. First live exercise is the Snajp build.

## Open Threads

- **[HYGIENE — needs approval] 22 v3 impeccable files restored by OneDrive.** `rm -rf` + replace deleted them, the commit recorded the deletions, but OneDrive sync restored them to disk in both `~/.agents/skills/impeccable/` and `super-intelligence/skills/impeccable/`. **Impact: cosmetic, not functional** — v4's `SKILL.md` and all v4 references are clean; the only cross-reference is leftover→leftover (`typography.md` → `brand.md`), so they form a disconnected island of dead files. `verify-design-system.py` passes 60/60 with them present. Per the conclude destructive-action guard, **nothing was deleted.** Exact-path manifest below, awaiting explicit approval:
  - `skills/impeccable/reference/`: `brand.md`, `product.md`, `typography.md`, `codex.md`, `cognitive-load.md`, `color-and-contrast.md`, `heuristics-scoring.md`, `interaction-design.md`, `motion-design.md`, `personas.md`, `responsive-design.md`, `spatial-design.md`, `teach.md`, `ux-writing.md`
  - `skills/impeccable/scripts/`: `cleanup-deprecated.mjs`, `design-parser.mjs`, `impeccable-paths.mjs`, `is-generated.mjs`, `live-completion.mjs`, `live-session-store.mjs`, `load-context.mjs`
  - `skills/impeccable/agents/impeccable-asset-producer.md`
  - (same relative paths under both `~/.agents/skills/` and `super-intelligence/skills/`)
- **Snajp rebuild not started** — the actual test. Full brief in the plan file.
- **Two hook systems may both fire.** impeccable v4 installs its own PostToolUse detector manifest into a project's `.claude/settings.local.json`; ours is global. If a project runs `npx impeccable install`, the detector could run twice per write. Not yet hit in practice. Resolve by measurement when it occurs.
- **Neither repo pushed.** Both on `design-system-v2`.
- **Model-behaviour checks unverified.** Gate-order judgment, inheritance, targeted-change rule, copy-gate output, inspection quality — none provable by hook tests. The telemetry report from the Snajp build is how they get verified.
- Pre-existing untracked strays in `super-intelligence` (not mine, not committed): `.agent-chorus/messages/*.conflict.1781166719`, `scripts/update-registry-0711.py`.

## Cross-Project Handoffs

- **super-intelligence** — received the full propagation this session (installer v0.4.0). Done inline, no separate handoff doc needed.
- **snipe-leads (Snajp)** — next session's target. Brief captured in `plans/2026-07-27-snajp-rebuild.md`. Deliberately did **not** read that repo's docs this session; reading them now would bias the router's design toward one project.

## Current State After This Session

The design system is built, verified (60/60 mechanical checks), and committed in both repos on `design-system-v2` branches, unpushed. The live install is fully upgraded and the hooks are wired, but **they take effect at the next session start** — `settings.json` registrations are read once at launch. The next session should start fresh, then run the Snajp rebuild as the first genuine end-to-end test: the metric that matters is the route-vs-invocation gap in `.impeccable/design-report-<date>.md`, which must be zero. A build that looks right but ships a gap-heavy ledger has not passed. Before that build, decide on the v3-leftover deletion manifest above.

<!-- session-state
date: 2026-07-27
type: infrastructure-rebuild
files_created:
  - skills/design/references/brand-derivation.md
  - skills/design/references/invention.md
  - skills/design/references/process.md
  - skills/design/references/scope-discipline.md
  - skills/design/references/component-routing.md
  - skills/design/references/gates.md
  - skills/design/references/copy-gate.md
  - skills/design/references/wireframe.md
  - skills/design/references/options.md
  - skills/design/references/handoff.md
  - skills/design-verify/SKILL.md
  - skills/brand-system/SKILL.md
  - verify-design-system.py
  - .claude/hooks/design_hook_lib.py
  - .claude/hooks/design-gate.py
  - .claude/hooks/design-route.py
  - .claude/hooks/design-telemetry.py
  - .claude/hooks/design-verify-gate.py
  - .claude/hooks/design-stop.py
  - .claude/hooks/design-intent.py
  - plans/2026-07-27-snajp-rebuild.md
files_modified:
  - skills/design/SKILL.md
  - ROUTER.md
  - README.md
  - attribution/UPSTREAMS.md
  - ../super-intelligence/install.mjs
  - ../super-intelligence/upgrade.mjs
  - ../super-intelligence/package.json
  - ../super-intelligence/VERSION
  - ../super-intelligence/CHANGELOG.md
  - ../super-intelligence/README.md
  - ../super-intelligence/carl/carl.json
  - ../super-intelligence/docs/design-workflow.md
  - ../super-intelligence/templates/.claude-settings.json
  - ~/.carl/carl.json
  - ~/.claude/settings.json
decisions_made: 9
open_threads: 6
handoffs_pending:
  - target: snipe-leads
    topic: Snajp rebuild — first end-to-end test of the design system + telemetry
priority_changes: true
status_updated: true
next_session_focus: "Snajp rebuild in snipe-leads — first real test of the brand-derivation gate and the route-vs-invocation telemetry"
session-state -->
