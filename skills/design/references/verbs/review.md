# `design review`

Review orchestrator: one ranked table from four audits.

Nothing here is a new rule. This file routes to the four things that already
judge a page — the slop audit, the accessibility audit, the pixel critique,
and the six Interfaces domain checklists — and consolidates their output into
one table a reviewer can act on. Structure ported from
[`better-interface/`](../upstream/interfaces/skills/better-interface/) and
[`interface-review/`](../upstream/interfaces/skills/interface-review/).
**Read-only unless the user also asks to implement.**

---

## 1 · Resolve scope first

Infer screen, flow, or repository scope from the request. State it out loud
before inspecting anything.

**A branch, PR, commit range, or uncommitted diff is a change review, not a
screen review.** Resolve it per
[`interface-review/scope-resolution.md`](../upstream/interfaces/skills/interface-review/scope-resolution.md):

- **Blast radius, one hop by default** — changed files plus their direct
  importers/callers. Expand a second hop only for tokens, theme values, and
  shared primitives, where one line reaches the whole product. State how many
  consumers you did not expand.
- **Read the removed lines**, not just the added ones — a regression is
  invisible in the post-change state. Check the `-` side of every hunk.
- **Status every finding**: `Introduced` (the change created it),
  `Regression` (weakened something that worked), or `Pre-existing` (present,
  not caused by this change). `Pre-existing` sits outside the cap and the
  verdict — at most three, named plainly, in its own section.

When the scope is too large to inspect credibly, narrow to one complete flow
and state the boundary and what it excluded. Never imply an uninspected
surface was reviewed.

## 2 · Recon before judgment

Identify the stack, styling system, component library, design tokens, and
supported viewports. Then read what the project has written about its own
interface — `DESIGN.md`, `CONTRIBUTING.md`, `CLAUDE.md`, a design-system doc.
Name what you found, or that there is none.

Read these to find where a finding belongs, not for permission to drop it.
**A documented convention is not evidence the convention is good.** "It's in
the style guide" does not retire a finding — it means report it once against
the guideline, with every affected component as a location.

## 3 · Run the four audits, in this order

Foundational failures first, so structural and accessibility problems aren't
hidden by polish notes.

**(a) [`verbs/audit.md`](audit.md)** — the Hallmark slop audit, gates 1–91:
structural fingerprint, stamp-vs-page, `DESIGN.md` drift. Read-only.

**(b) `Skill(a11y-audit)`** — mechanical checks plus WCAG/COGA judgment:
accessible names, keyboard reachability, focus visibility,
compliance, colour-alone state. Overlaps `better-accessibility`; where both
flag the same symptom, report it once under Accessibility.

**(c) [`verbs/critique.md`](critique.md)** — the seven pixel dimensions
(hierarchy, composition, typography, colour, affordance, density, brand) plus
the squint test and the three-flat-sections check. The only one of the four
that judges *quality*, not just violations — what stops a gate-clean,
accessible page from being flat.

**(d) `Skill(review-animations)`** on any motion in scope — durations,
easings, interruptibility, whether a state
change leaves a static cue when the animation doesn't run.

**(e) The six Interfaces domain checklists**, sources of truth for their
concern — cite the upstream file per finding, not this one:

| Domain | Source | Owns |
|---|---|---|
| Accessibility | [`better-accessibility`](../upstream/interfaces/skills/better-accessibility/SKILL.md) | Native elements, focus, keyboard, ARIA, hit areas |
| Layout | [`better-layout`](../upstream/interfaces/skills/better-layout/SKILL.md) | Grouping, alignment, breakpoints, RTL, growth |
| Writing | [`better-writing`](../upstream/interfaces/skills/better-writing/SKILL.md) | Voice, terminology, error copy, labels |
| Typography | [`better-typography`](../upstream/interfaces/skills/better-typography/SKILL.md) | Scale, measure, line-height, wrapping, tokens |
| Colour | [`better-colors`](../upstream/interfaces/skills/better-colors/SKILL.md) | Ramps, contrast, semantic use, gradients |
| UI polish | [`better-ui`](../upstream/interfaces/skills/better-ui/SKILL.md) | Radius, elevation, icon transitions, press states |

Unavailable owning skill → mark that domain `Not reviewed`, name the missing
skill, continue with the rest. Never recreate its rules from memory.

## 4 · Consolidate

**One root cause, one row.** List every confirmed location in the same row
rather than one row per occurrence. Cap the table at **15 findings**. Never
pad to reach the cap — a short review, or no findings, is a valid result.

**Escalation triggers — always `HIGH`, always listed first**, copied verbatim
from `better-interface`, never averaged down because the surface is minor:

- An interactive control with no accessible name.
- A keyboard-reachable control with no visible focus indicator.
- A control or path reachable by pointer but not by keyboard.
- ~~Motion or auto-playing content that ignores `prefers-reduced-motion`.~~ **F-011 (2026-09-07):** denna trigger utgår; ett bygge utan rm-gren är korrekt här.
- Content or a control clipped, overlapped, or unreachable at 320px width or
  200% zoom.
- Body or control text whose rendered contrast pair fails its required ratio.
- State or meaning carried by colour alone.
- A destructive action with no confirmation, undo, or distinct treatment.
- Truncated content with no way to reach the full value.
- Content or a control reachable only past a scroll edge or behind a
  disclosure that has no visible cue.
- An error that names no way to recover from it.
- A semantic colour used against its meaning (the danger hue on a
  non-destructive action).
- A state change carried by motion alone, with no colour, icon, or label left
  behind when the animation does not run.

When more triggers fire than the cap allows, list them first and say how many
the cap excluded. The cap may shorten a report; it may never be why a blocker
went unreported.

**Cheapest-fix ladder** — propose the earliest step that works: **1. Delete**
(a separator space would carry, an unneeded ARIA attribute, an unused ramp)
· **2. Use the platform** (native element over custom rebuild) · **3. Reuse
what the project has** (existing token, spacing step, motion curve) ·
**4. Correct the value** (the exact value the owning domain gives) ·
**5. Add** (a new token, wrapper, or attribute nothing else supplies). A fix
written at step 5 where step 1 was available is its own finding — report the
deletion instead.

**Severity by user impact**, one shared scale across all four audits:

- `HIGH` — blocks a task, misleads the user, hides content or controls, risks
  data loss, or is a repeated systemic failure. Every escalation trigger.
- `MEDIUM` — meaningfully harms comprehension, efficiency, adaptability, or
  consistency.
- `LOW` — isolated polish with limited task impact.

**Reconciliation rule.** When two audits recommend conflicting fixes for the
same location, resolve in order and say which step decided it:
**accessibility > usability > the brief > named personas > escalate to the
user.** If none of the four settles it, stop and ask rather than pick
silently.

## 5 · Output

Format is [`review-format.md`](../upstream/interfaces/skills/better-interface/review-format.md):

1. **Scope and coverage** — exact scope, stack, conventions found, review
   boundary, then a coverage table (`Domain | Evidence inspected | Result`).
   `Result` is a findings count, `Clear` (inspected, nothing actionable), or
   `Not reviewed: <reason>` — missing skill, out of scope, or (in a change
   review) `no evidence in the change scope`.
2. **Findings table**, ordered by severity then reach: `Severity | Domain |
   Location | Before | After | Why`. In a change review, add `Status`
   (`Introduced` / `Regression`) — `Pre-existing` gets its own section below
   the cap, at most three, highest severity first.
3. **Verification** — every check actually run, the exact command or
   interaction, and its result. Anything not run is `Not verified`, never
   silently assumed to have passed.
4. **Verdict** — `Block` when any `HIGH` finding remains (every trigger,
   plus any `Regression` against one). `Approve` otherwise, with remaining
   `MEDIUM`/`LOW` findings left in the table as work to do.

**Never `Approve` coverage you did not inspect.** A domain you skipped is
`Not reviewed`, not an assumed pass folded into the verdict.

---

## Maps to our verbs

[`verbs/audit.md`](audit.md) alone covers the gates-only slop audit — reach
for it when the ask is narrowly "does this pass the gates." **This file is
what the `audit` verb graduates to** when the ask is a full cross-discipline
review. The consolidated table this file produces is what the `polish` verb
receives as its worklist: `review` never edits, `polish` does the fixing.
