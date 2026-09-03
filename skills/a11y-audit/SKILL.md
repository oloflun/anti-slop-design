---
name: a11y-audit
user-invocable: true
description: Runs a full accessibility audit of an interface — a mechanical script pass, WCAG 2.2 AA (POUR), cognitive load (COGA), content, adaptive behaviour, interaction, and a persona walkthrough — and closes with a findings report, a legal-compliance map, and an accessibility-debt ledger. Invoked by `Skill(design)` Step 5 and the `audit` verb, and directly whenever the request is an accessibility audit, tillgänglighet, WCAG, a11y, screen reader, skärmläsare, keyboard, kontrast, EAA, "is this accessible", or "är det tillgängligt".
---

# Accessibility audit

Eight passes over the target, in order. Each pass produces evidence; the report in pass 8 is only as good as what was actually inspected. `references/principles.md` holds the full principle catalog this procedure draws on, tagged by source. `references/report-template.md` holds the exact report skeleton.

## 0 · Scope + coverage

State what you're auditing (URL, files, or a static screenshot set) and what that lets you verify. A static screenshot verifies visual and content findings only — keyboard, screen-reader, and focus-order findings are **inferred, never verified**, and the report must say so.

| Input | Verified | Inferred |
| --- | --- | --- |
| Live URL / running build | Mechanical scripts, keyboard, focus, contrast, reflow, motion | — |
| Static screenshot(s) | Visual contrast (against the pixels shown), content, layout | Keyboard path, screen-reader announcement, focus order, states not shown |
| Source files, no runtime | Semantics in markup, ARIA, labels-in-code | Rendered contrast, computed focus styles, actual tab order |

Never claim coverage you didn't inspect. Say "inferred from static image" or "not verified — no browser" rather than silently upgrading a guess to a finding.

## 1 · Mechanical pass

Run the scripts and read every JSON field before writing findings from them.

```bash
python <S>/scripts/a11y_scan.py <url>     # <S> = this skill's own directory
python <S>/scripts/tab_walk.py <url> [--max 200]
python <S>/scripts/reflow.py <url>
python ~/.agents/skills/design/scripts/contrast.py <url>
python ~/.agents/skills/design/scripts/contrast_over_media.py <url>
```

- **`a11y_scan.py`** — axe-core at desktop (1440×900) and mobile (390×844), merged. Returns `{url, violations: [{id, impact, description, help, viewports, nodes}], passes, incomplete}`. Each violation carries the WCAG tags axe matched it to.
- **`tab_walk.py`** — walks the page with real `Tab` presses. Returns `{stops, issues}` where each issue is `empty_name`, `offscreen`, `order_mismatch`, `no_focus_indicator`, `positive_tabindex`, `focus_trap`, or `unreachable_interactive` (a click handler with no keyboard path).
- **`reflow.py`** — three checks: overflow at 320px width, overflow at 200% zoom emulation, and elements still `opacity: 0` under `prefers-reduced-motion: reduce` at three scroll depths (a reveal system that never fires without JS scroll events). Returns `{overflow320, overflowZoom200, hiddenUnderReducedMotion, hiddenSelectors}`.
- **`contrast.py`** / **`contrast_over_media.py`** — rendered-pixel contrast, the second for text over photo or video (worst-case patch, not the mean).

**CARL rule.** Once per project, before trusting a clean pass from any of these five scripts, run them against `~/anti-slop-design/tests/a11y/broken.html` (absolute; the fixture lives in the design-system repo, not in the audited project) (a fixture with a known violation of each kind: missing label, no focus ring, un-reachable click handler, 320px overflow, failing contrast pair) and confirm every script actually reports it. A verifier that passes a broken page is worse than no verifier — it produces false confidence. If that file is missing, say so and create an equivalent fixture before relying on any script's silence as a clean bill. Hash-routed or multi-state pages: run the scripts once per state (`…/index.html#dashboard`, with the modal open) — the scripts only see the DOM they load.

## 2 · POUR pass

Walk Perceivable / Operable / Understandable / Robust. Cite the WCAG 2.2 AA success-criterion number on every finding (`compliance-mapping` tables in `references/principles.md` map design decisions to criteria — use them rather than guessing a number). Cross-reference `a11y_scan.py`'s violations here; each axe rule maps to one or more SC numbers axe already reports.

## 3 · Cognitive pass (COGA)

For each screen or step, rate the three loads — **intrinsic** (inherent to the task, reduce by chunking not by removing function), **extraneous** (added by the design, eliminate ruthlessly), **germane** (the user's actual engagement, protect it by removing the other two). Then check wayfinding's three questions hold at every point: **where am I, where can I go, how do I get back** — each answerable in under a second, without memory. Verify focus (one primary action per screen, interruptions controllable), error recovery (undo, confirmation on destructive actions, preserved input), and memory load (nothing the user must carry in their head between steps that the interface could show instead).

## 4 · Content pass

Reading age 12–14 (grade 6–8; grade 4–6 for buttons, labels, and errors) — flag anything denser. Heading hierarchy: one H1, no skipped levels, headings that alone tell the page's story. Labels: every input has a visible, programmatic label; placeholders are never labels. Alt text by the decision table: decorative → `alt=""`; functional → the action; informative → the meaning; complex → short alt plus an extended description nearby; never "image of…". Link text stands alone out of context — no "click here" or "read more". Error messages follow **what happened + why + what to do**, in plain language, never blaming the user. Tables carry a caption and scoped headers, never used for layout. Multimedia: accurate synced captions (never unreviewed auto-captions), transcripts for audio, audio description for meaningful visual content, no autoplay.

## 5 · Adaptive pass

Respect every system preference automatically, never ask the user to reconfigure what the OS already knows: `prefers-color-scheme` (real dark mode — dark grey not pure black, off-white not pure white), `prefers-contrast`, `prefers-reduced-motion` (**gentler, not zero** — essential motion like loading and state-change feedback survives, simplified; decorative motion, parallax, and autoplay are removed entirely), `prefers-reduced-transparency` (solid surfaces, no backdrop blur), `forced-colors`. Text in `rem`, never `px`; layout survives 200% zoom and reflows at 320px with no horizontal scroll; density has at least a comfortable default and never drops below 44×44 touch targets or 1.5 line-height at any level. Colour independence: every colour-carried meaning has a second encoding (icon, text, pattern, shape), and the interface passes the **greyscale test** — convert it to greyscale and confirm status, errors, charts, and links are all still legible.

## 6 · Interaction pass

Native element first, ARIA last — `<button>` for actions, `<a href>` for navigation, never `<div onClick>`; no ARIA beats bad ARIA. Focus-visible ring at least 2px solid with 3:1 contrast against every adjacent colour it crosses, never bare `outline: none`. Hit areas: 24×24 CSS px is the WCAG 2.5.8 AA floor, 44×44 the touch target, 40×40 a reasonable desktop target; extend with a pseudo-element on the label or button, never overlapping another target. Every gesture (swipe, pinch, drag, long-press, shake) has a button-based alternative — gestures are shortcuts, never gatekeepers. Skip link is the first focusable element on any page with repeated navigation. Composite widgets (tabs, menus, toolbars) use roving tabindex — one Tab stop, active item `0`, the rest `-1`, arrow keys move both. Modals set `inert` on the background, trap focus inside, and return it to the trigger on close. Never a positive `tabindex` anywhere. Paste is never blocked in any field — password managers and 2FA autofill depend on it — and every field about the user carries a meaningful `autocomplete`.

## 7 · Persona walkthrough

Build 4–6 personas spanning permanent, temporary, and situational conditions (not four permanent-disability personas and nothing else — a broken arm and a parent holding a baby belong in the set too). For each persona, walk every key task from the brief and record whether it **works**, **works with friction**, **works with workaround**, or **fails**. Compile into a barrier matrix: task × persona, one cell per combination. A task that fails for any persona is a finding regardless of how it looks for the rest.

## 8 · Report

Assemble in `references/report-template.md`'s exact shape:

- **Coverage table** from Step 0 — what was verified vs. inferred, restated with what actually got inspected.
- **Findings table** — `Severity | Location | Before | After | Why | WCAG | Who`. One row per root cause; list every location a systemic issue reaches. `Who` names the affected persona(s) or user group, not just "users".
- **Escalation triggers** — always `HIGH` the moment confirmed, never averaged down: no accessible name on an interactive control; a keyboard-reachable control with no visible focus indicator; a control reachable by pointer but not keyboard; motion or autoplay ignoring `prefers-reduced-motion`; content or a control clipped or unreachable at 320px width or 200% zoom; a contrast pair that fails its required ratio; state or meaning carried by colour alone; a destructive action with no confirmation or undo; truncated content with no way to reach the full value; content reachable only past a scroll edge or disclosure with no visible cue; an error that names no way to recover; a semantic colour used against its meaning.
- **Verdict** — `Block` when any `HIGH` remains, `Approve` otherwise. Never `Approve` coverage you did not inspect.
- **Legal map** — which of EAA/EN 301 549, ADA, Section 508, and WCAG 2.2 AA each finding touches. Most organisations target WCAG 2.2 AA; EAA (in effect since June 2025) and EN 301 549 align with it; ADA and Section 508 case law references it.
- **SEO flag** — mark findings on headings, alt text, `lang`, link text, or reflow as SEO-relevant; the same structural signals search crawlers and screen readers both depend on.
- **Deferred items** append to `.impeccable/a11y-debt.md` in the audited project — never dropped silently. Each entry: issue, severity, who's affected, WCAG criterion, why deferred, remediation deadline (critical: this sprint, major: 30 days, minor: 90 days). Accepting accessibility debt requires the user's explicit acknowledgement in the conversation, not an assumed sign-off.

## Cheapest fix ladder

When more than one fix would work, propose the earliest step that does:

1. **Delete** — the decorative layer eating clicks, the ARIA a native element makes redundant, the ramp nothing needs.
2. **Use the platform** — the native element or control instead of a custom rebuild.
3. **Reuse what the project has** — an existing token, focus style, or spacing step.
4. **Correct the value** — the exact contrast pair, hit-area size, or WCAG-conformant markup.
5. **Add** — a new token, wrapper, or ARIA attribute only the platform truly cannot supply.

A fix proposed at step 5 where step 1 was available is itself a finding.

## Never Approve coverage you did not inspect

If the target was a screenshot, say keyboard and screen-reader findings are inferred. If a script failed to run, say so and mark that check `Not verified` — never let a tool failure silently read as a pass.

## The 30/50/20 testing pyramid

Automated tools (axe, this skill's scripts) catch roughly 30% of real barriers — the mechanical ones. Manual expert testing (tab-through, screen-reader pass, zoom, plain-language read) catches another 50%. The remaining 20% — real-world usability barriers, unexpected workarounds, cognitive and emotional friction — surfaces only in testing with actual disabled users. This skill covers the first two layers rigorously; recommend the third to the user rather than claiming it was done.

## Before you finish

| Mistake | Fix |
| --- | --- |
| Claiming a script pass without running it against `tests/a11y/broken.html` first | Run the CARL check once per project before trusting any clean result |
| Reporting a keyboard or screen-reader finding from a static screenshot | Mark it inferred, not verified — say so in the coverage table |
| Averaging an escalation-trigger finding down because the surface is minor | Escalation triggers are `HIGH` on sight, never re-scored |
| A finding with no WCAG criterion cited | Look it up in `compliance-mapping`'s tables before writing the row |
| Silently dropping a Minor finding not in this fix round | Append it to `.impeccable/a11y-debt.md` with severity, owner, and deadline |
| Fixing contrast by changing hue | Change lightness — it's the channel contrast responds to; remeasure after |
| Reporting "not accessible" with no persona named | Name who specifically is blocked and what they were trying to do |
| Treating four personas with the same permanent disability as full persona coverage | Span permanent, temporary, and situational — 4–6 personas, not a single category |
| Proposing a step-5 fix (new ARIA, new token) where step 1–4 would work | Walk the cheapest-fix ladder before proposing an addition |
| A colour-only status indicator passed because the label happened to be nearby | Run the greyscale test explicitly and report the result |
| `Approve` issued on a domain never actually inspected | Mark that domain `Not reviewed` in the coverage table instead |
| An accessibility-debt item deferred with no deadline or owner | Every debt entry needs severity, WCAG criterion, remediation deadline, and explicit user acknowledgement |
