# `design review`

Review orchestrator: one ranked table from four audits.

This file routes to the four things that already judge a page — the slop audit,
the accessibility audit, the pixel critique, and the six Interfaces domain
checklists — and consolidates their output into one table a reviewer can act on.
Almost nothing here is a new rule; the exceptions are the checks in § 3(f)–(j),
which no owning skill holds, and the scoring in § 6, which exists so two rounds
can be compared rather than only judged. Structure ported from
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

**Write the inferred brief before you judge.** The four audits below all
evaluate *against* something. On a review of work this session did not build,
that something does not exist yet, so reconstruct a minimal one — three
questions, not a discovery session (designpowers `design-review` § 2):

1. **What is this, and what is the main thing a person is trying to do here?**
   (the key task)
2. **Who is it for?** (audience and ability spectrum; if unknown, *"assume the
   full spectrum: permanent, temporary, situational"*)
3. **What is the quality bar, and what prompted the review?** (shipping
   prototype vs flagship; *"it feels off"* vs *"failed an audit"* vs *"low
   conversion"*)

Record it in the report, **clearly marked as inferred** — reconstructed for
review, not authored up front. Without this step every craft finding is scored
against the reviewer's own taste, which is exactly what this file exists to
prevent.

**Classify the surface before applying rules**, because the rule set diverges:
**MARKETING/LANDING** (hero-driven, brand-forward, conversion-focused) ·
**APP UI** (workspace-driven, data-dense, task-focused: dashboards, admin,
settings) · **HYBRID** (marketing shell with app-like sections — landing rules
for the hero and marketing sections, app rules for the functional ones). Name
the classification in the scope block.

## 3 · Run the audits, in this order

Foundational failures first, so structural and accessibility problems aren't
hidden by polish notes. **(a) to (e) are the four audits plus the domain
checklists — routing, no new rules. (f) to (j) are the checks no owning skill
holds**: the trunk test, the hard rejections and litmus checks, performance and
implementation integrity, and the cognitive walkthrough. They are scored here
because there is nowhere else for them, and each one names its source.

**(a) [`verbs/audit.md`](audit.md)** — the Hallmark slop audit, gates 1–98:
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

**(f) The trunk test**, on every page in scope. Imagine being dropped on this
page with no context. Can you immediately answer:

1. What site is this? (site ID visible and identifiable)
2. What page am I on? (page name prominent, matching what was clicked)
3. What are the major sections? (primary nav visible and clear)
4. What are my options at this level? (local nav or content choices obvious)
5. Where am I in the scheme of things? ("you are here", breadcrumbs)
6. How can I search? (search box findable without hunting)

Score `PASS` (all six clear) / `PARTIAL` (four to five) / `FAIL` (three or
fewer). **A FAIL is a HIGH finding regardless of how polished the visual design
is** — it sits alongside the escalation triggers below, not under polish.

**(g) Seven hard rejections**, instant-fail patterns; flag if any apply:
generic SaaS card grid as the first impression · beautiful image with weak brand
· strong headline with no clear action · busy imagery behind text · sections
repeating the same mood statement · carousel with no narrative purpose · app UI
made of stacked cards instead of layout.

**(h) Seven litmus checks**, answered YES/NO so two reviewers can be compared:
brand or product unmistakable in the first screen? · one strong visual anchor
present? · page understandable by scanning headlines only? · each section has one
job? · are cards actually necessary? · does motion improve hierarchy or
atmosphere? · would the design feel premium with all decorative shadows removed?

**(i) Two dimensions the four audits above do not own**, from impeccable
`audit.md`, scored 0–4:

- **Performance** — layout thrashing (reading and writing layout properties in
  loops) · expensive animation (*"casual layout-property animation, unbounded
  blur/filter/shadow effects, or effects that visibly drop frames"*) · missing
  optimisation (unlazy images, unoptimised assets) · **`will-change` overuse**
  (*"applied broadly or left on at rest — it is a targeted hint for known
  expensive animations, not a baseline requirement"*) · bundle size · render
  performance. `0` severe, `2` partial with gaps remaining, `4` fast, lean,
  well-optimised. The numbers behind the grade come from `perf_probe.py` and
  the budget in `performance.md`; this dimension is where they enter the table.
- **Implementation integrity (critical)** — *"Run the bundled detector and
  verify each finding in context. Look for repeated implementation shortcuts,
  design-system drift, misleading or decorative content, and structure that is
  interchangeable with an unrelated product. Keep deterministic findings
  separate from visual judgment and call out false positives."* `0` systemic
  drift, `2` several verified issues, `4` coherent and intentional.

The **integrity verdict opens the report**, before the findings table: pass or
fail on one question — *does the implementation express a coherent
product-specific system?* — citing verified evidence and detector findings. A
page can clear every domain checklist and still fail here, and that is the
result worth reading first.

**(j) Cognitive walkthrough** of the key task from the inferred brief. Step
through every step and answer four questions (designpowers
`agents/heuristic-evaluator`):

1. Will the user try to achieve the right effect? (do they understand what this
   step is for?)
2. Will the user notice that the correct action is available? (is the control
   visible and recognisable?)
3. Will the user associate the correct action with the desired effect? (does the
   label or icon communicate what will happen?)
4. If the correct action is performed, will the user see that progress is being
   made?

*"If the answer to any question is 'no' or 'uncertain,' that's a finding."* Cite
the heuristic it violates by number — H1 system status, H3 user control and
freedom (undo, cancel, escape), H5 error prevention, H6 recognition over recall,
H9 error recovery. *"Violates H3 (User Control)"* is actionable in a way that
"the back button is confusing" is not.

### Verification rules that bind all of the above

**Never claim a check passed without running it.** *"NEVER claim work is
complete, fixed, passing, or ready without running verification and confirming
the output. 'I believe this works' is not verification. 'I ran these checks and
here are the results' is."* Two specifics that get eyeballed most often:
**contrast ratios are verified with a tool, not by eye**, and **touch targets
are measured, not estimated**.

**Never guess a URL.** When the target is a live site, discover real URLs before
fetching sub-pages — *"never infer or guess a URL from a nav label, button text,
or any other interface element. Guessed URLs produce false 404 findings and
damage the credibility of the evaluation."* In order: (1) extract every `href`
from the page source, grouped by nav section, and use only those; (2) try
`/sitemap.xml`, then `/sitemap_index.xml`; (3) check `/robots.txt` for a
`Sitemap:` directive; (4) **accept the limit** — state *"sub-page structure
could not be verified — evaluation is based on homepage content only."* That is
an honest finding, not a failure, and a site with no discoverable URL structure
may itself be worth reporting under H1/H10. Hash hrefs are not sub-pages;
`javascript:void(0)` navigation is flagged as an SEO and accessibility issue
rather than fetched.

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

**Escalation of deferred findings.** A `LOW` or `MEDIUM` finding that survives
between rounds is not automatically still `LOW`. Promote it, and say which
trigger fired (designpowers `design-debt-tracker` § 3):

| Trigger | What it looks like |
|---|---|
| **Age** | The item has been open for 3+ iterations without resolution |
| **Accumulation** | Several open items affect the same persona or the same screen |
| **Context change** | A new persona or use case makes the issue more impactful |
| **User complaint** | The user raises the issue independently |
| **Compound effect** | Two Minor items together create a Major experience gap |

Age and accumulation are the two that a per-round review structurally cannot
see, which is why they are written down: a finding deferred three rounds running
is evidence the round is wrong, not that the finding is small. Accessibility
debt is the one class that needs explicit user acknowledgement to accept rather
than being silently carried.

## 5 · Output

Format is [`review-format.md`](../upstream/interfaces/skills/better-interface/review-format.md):

1. **Scope and coverage** — exact scope, stack, conventions found, review
   boundary, then a coverage table (`Domain | Evidence inspected | Result`).
   `Result` is a findings count, `Clear` (inspected, nothing actionable), or
   `Not reviewed: <reason>` — missing skill, out of scope, or (in a change
   review) `no evidence in the change scope`.
2. **Integrity verdict** — the one-question pass/fail from § 3(i), first, with
   its evidence.
3. **Findings table**, ordered by severity then reach: `Severity | Domain |
   Location | Before | After | Why`. In a change review, add `Status`
   (`Introduced` / `Regression`) — `Pre-existing` gets its own section below
   the cap, at most three, highest severity first. **For every `HIGH` and
   `MEDIUM`, name who it affects and why it matters** — the persona or the
   situation, not just the defect. A finding with no named sufferer is a
   preference wearing a severity label.
4. **What works well** — a required section, not a courtesy. *"Review is not
   only problems."* Two or three genuine strengths, specific about *why* they
   work. Its absence is how a review stops being read; its presence is also
   what stops a fix pass from deleting the one thing the page had.
5. **Scores** — two headline grades plus the per-category table (below).
6. **Verification** — every check actually run, the exact command or
   interaction, and its result. Anything not run is `Not verified`, never
   silently assumed to have passed.
7. **Verdict** — `Block` when any `HIGH` finding remains (every trigger,
   plus any `Regression` against one). `Approve` otherwise, with remaining
   `MEDIUM`/`LOW` findings left in the table as work to do.
8. **Recommendation** — one line: ship as-is / fix criticals first / rethink,
   and the single most important next move. The review proposes; it does not
   auto-fix without direction.

**Never `Approve` coverage you did not inspect.** A domain you skipped is
`Not reviewed`, not an assumed pass folded into the verdict.

---

## 6 · The number that survives the round

A verdict tells the builder whether to ship. A **score** tells them whether the
next round was an improvement, which is the thing a per-round review otherwise
cannot say. Ported from the gstack `design-review` skill.

**Two headline grades, A–F:** a **Design Score** (weighted average of the ten
categories) and an **AI Slop Score** (standalone, with a one-line verdict).

**Per-category grade meanings** — these are the words, not a curve:

- **A** — intentional, polished, delightful. Shows design thinking.
- **B** — solid fundamentals, minor inconsistencies. Looks professional.
- **C** — functional but generic. No major problems, no design point of view.
- **D** — noticeable problems. Feels unfinished or careless.
- **F** — actively hurting user experience. Needs significant rework.

**Computation.** Every category starts at **A**. Each `HIGH` finding drops a
full letter grade; each `MEDIUM` drops half a letter; `LOW` findings are noted
and do not move the grade. Minimum is F.

| Category | Weight |
|---|---|
| Visual hierarchy | 15 % |
| Typography | 15 % |
| Spacing and layout | 15 % |
| Colour and contrast | 10 % |
| Interaction states | 10 % |
| Responsive | 10 % |
| Content quality | 10 % |
| AI slop | 5 % |
| Motion | 5 % |
| Performance feel | 5 % |

AI slop is 5 % of the Design Score *and* a headline metric in its own right,
because a page can be craft-clean and still read as generated.

**Baseline and regression.** Write `design-baseline.json` at the end of the
review — date, target, both scores, per-category grades, and the findings list
with id, title, impact and category. On the next review, load it and append a
regression table: per-category deltas, new findings, resolved findings. **Say so
plainly when the final score is worse than the baseline** — a fix round that
lowers the score is the outcome this whole apparatus exists to catch.

The ten categories here and the seven dimensions in
[`critique.md`](critique.md) are not two competing lists: critique scores the
seven on pixels and hands its findings up; this file grades the ten because it
also holds accessibility, responsive, motion and performance, which critique
does not judge.

---

## How readers actually behave

Nothing below is a finding on its own. It is the frame the findings are ranked
in, and it settles the arguments a severity scale cannot. From the usability
canon the gstack `design-review` skill carries.

**Three laws.** *"Don't make me think"* — every page is self-evident; if the
reader stops to ask "what do I click?" the design has failed. *"Clicks don't
matter, thinking does"* — three mindless unambiguous clicks beat one that
requires thought; each step should feel like an obvious choice, not a puzzle.
*"Omit, then omit again"* — cut half the words on each page, then half of what
is left; happy talk and instructions die first.

**Four behaviours.** Readers **scan, they don't read** — *"we're designing
billboards going by at 60 mph, not product brochures people will study."*
Readers **satisfice** — they pick the first reasonable option, not the best, so
make the right choice the most visible one. Readers **muddle through** — *"if
they accomplish their goal by accident, they won't seek the 'right' way"*, and
once something works they keep doing it. Readers **don't read instructions** —
guidance must be brief, timely and unavoidable, or it is not seen.

**Two rules that decide findings.** Start from the assumption that everything on
the page is visual noise, **guilty until proven innocent** — that is the default
posture for the density and decoration findings. And **clarity trumps
consistency**: *"if making something significantly clearer requires making it
slightly inconsistent, choose clarity every time."* When a consistency finding
and a clarity finding collide at the same location, this sentence decides it,
and the reconciliation rule in § 4 records which step did.

---

## Maps to our verbs

[`verbs/audit.md`](audit.md) alone covers the gates-only slop audit — reach
for it when the ask is narrowly "does this pass the gates." **This file is
what the `audit` verb graduates to** when the ask is a full cross-discipline
review. The consolidated table this file produces is what the `polish` verb
receives as its worklist: `review` never edits, `polish` does the fixing.
