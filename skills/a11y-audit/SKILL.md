---
name: a11y-audit
user-invocable: true
description: Runs a full accessibility audit of an interface — a mechanical script pass, WCAG 2.2 AA (POUR), cognitive load (COGA), content, adaptive behaviour, interaction, and a persona walkthrough — and closes with a findings report, a legal-compliance map, and an accessibility-debt ledger. Invoked by `Skill(design)` Step 5 and the `audit` verb, and directly whenever the request is an accessibility audit, tillgänglighet, WCAG, a11y, screen reader, skärmläsare, keyboard, kontrast, EAA, "is this accessible", or "är det tillgängligt".
---

# Accessibility audit

Eight passes over the target, in order. Each pass produces evidence; the report in pass 8 is only as good as what was actually inspected. `references/principles.md` holds the full principle catalog this procedure draws on, tagged by source. `references/report-template.md` holds the exact report skeleton.

**Standing override — F-011 (Anton, 2026-09-07, permanent, global — applies to every audit this skill runs, not just one project):** motion always plays. Do not raise a finding, escalation, or debt-ledger item for an animation, autoplay, or scroll set-piece that ignores `prefers-reduced-motion` or any other browser/OS motion-accessibility signal — that is intentional in every design system this skill audits, not a defect. This is a deliberate, informed trade against real accessibility guidance (vestibular-disorder / motion-sensitivity users lose their opt-out); it is not an oversight, so do not "helpfully" flag it anyway. Every other WCAG check still applies in full, including the hard, preference-independent seizure-safety limit (no content flashing more than three times per second, WCAG 2.3.1) — that one is not a preference, it stays enforced regardless.

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
- **`reflow.py`** — three checks: overflow at 320px width, overflow at 200% zoom emulation, and **unrevealed content**: elements still `opacity: 0` at three scroll depths (a reveal system that never fires). Returns `{overflow320, overflowZoom200, unrevealed, unrevealedSelectors}`. Under F-011 there is no reduced-motion branch left to isolate, so check (c) is read purely as an unrevealed-content count — the AB09 failure where a page shipped empty below the fold.
- **`contrast.py`** / **`contrast_over_media.py`** — rendered-pixel contrast, the second for text over photo or video (worst-case patch, not the mean).

**CARL rule.** Once per project, before trusting a clean pass from any of these five scripts, run them against `~/anti-slop-design/tests/a11y/broken.html` (absolute; the fixture lives in the design-system repo, not in the audited project) (a fixture with a known violation of each kind: missing label, no focus ring, un-reachable click handler, 320px overflow, failing contrast pair) and confirm every script actually reports it. A verifier that passes a broken page is worse than no verifier — it produces false confidence. If that file is missing, say so and create an equivalent fixture before relying on any script's silence as a clean bill. Hash-routed or multi-state pages: run the scripts once per state (`…/index.html#dashboard`, with the modal open) — the scripts only see the DOM they load.

## 2 · POUR pass

Walk Perceivable / Operable / Understandable / Robust. Cite the WCAG 2.2 AA success-criterion number on every finding (`compliance-mapping` tables in `references/principles.md` map design decisions to criteria — use them rather than guessing a number). Cross-reference `a11y_scan.py`'s violations here; each axe rule maps to one or more SC numbers axe already reports.

## 3 · Cognitive pass (COGA)

For each screen or step, rate the three loads — **intrinsic** (inherent to the task, reduce by chunking not by removing function), **extraneous** (added by the design, eliminate ruthlessly), **germane** (the user's actual engagement, protect it by removing the other two). Then check wayfinding's three questions hold at every point: **where am I, where can I go, how do I get back** — each answerable in under a second, without memory. Verify focus (one primary action per screen, interruptions controllable), error recovery (undo, confirmation on destructive actions, preserved input), and memory load (nothing the user must carry in their head between steps that the interface could show instead).

Then rate every screen or step on six dimensions, with the thresholds — this is what turns "feels complex" into a finding:

| Dimension | Low (good) | Medium (review) | High (redesign) |
| --- | --- | --- | --- |
| Decisions required | 0–1 | 2–3 | 4+ |
| Items to remember | none | 1–2 | 3+ |
| New concepts to learn | none | 1 | 2+ |
| Steps to complete | 1–2 | 3–5 | 6+ |
| Reading complexity | plain language | some jargon | dense / technical |
| Visual complexity | clean, focused | moderate | cluttered |

**If any single dimension rates High, that screen needs redesign before launch** — the rating is not averaged across the six, exactly as an escalation trigger is never averaged down. Walk the flow as a user who is tired, stressed and unfamiliar; where you pause, re-read, or feel uncertain is a load spike, and the next question is whether the difficulty is intrinsic (chunk it) or extraneous (delete it). Report as a screen-by-screen table with the ratings, then recommendations sorted by impact.

## 4 · Content pass

Reading age 12–14 (grade 6–8; grade 4–6 for buttons, labels, and errors) — flag anything denser. Heading hierarchy: one H1, no skipped levels, headings that alone tell the page's story, and **depth never past H4** — a page reaching H5 has a structure problem, not a markup problem. Labels: every input has a visible, programmatic label; placeholders are never labels. Alt text by the decision table: decorative → `alt=""`; functional → the action; informative → the meaning; complex → short alt plus an extended description nearby; never "image of…". Link text stands alone out of context — no "click here" or "read more". Error messages follow **what happened + why + what to do**, in plain language, never blaming the user. Tables carry a caption and scoped headers, never used for layout. Multimedia: accurate synced captions (never unreviewed auto-captions), transcripts for audio, audio description for meaningful visual content, keyboard-accessible play / pause / stop / volume / seek controls.

**Autoplay — the explicit ruling.** F-011 removes the *preference gate*, not the *control*. Two different things sit under the word "autoplay" and only one of them is overridden:

| Case | Verdict |
| --- | --- |
| A silent, decorative video or scroll set-piece that starts on its own and ignores `prefers-reduced-motion` | **Not a finding.** F-011, by design. |
| **Audio** that starts on its own | **Finding, HIGH.** Audio is not motion; it collides with a screen reader and with whatever the person is listening to. WCAG 1.4.2 stands untouched. |
| Any autoplaying media with **no reachable pause / stop control** | **Finding.** The user must be able to stop it once it is running, and that control must be keyboard-reachable and labelled. Removing the preference gate did not remove the user's ability to act. |
| Content flashing more than three times per second | **Finding, HIGH.** Seizure safety, not a preference (WCAG 2.3.1). |

## 5 · Adaptive pass

Respect every system preference automatically, never ask the user to reconfigure what the OS already knows: `prefers-color-scheme` (real dark mode — dark grey not pure black, off-white not pure white), `prefers-contrast`, `prefers-reduced-transparency` (solid surfaces, no backdrop blur), `forced-colors`. `prefers-reduced-motion` is the one preference this skill does not audit — see the F-011 standing override above; everything else in this list is audited in full. Text in `rem`, never `px`; layout survives 200% zoom and reflows at 320px with no horizontal scroll; density has at least a comfortable default and never drops below 44×44 touch targets or 1.5 line-height at any level. Colour independence: every colour-carried meaning has a second encoding (icon, text, pattern, shape), and the interface passes the **greyscale test**. **In running prose, the underline is the accessible indicator and colour is the enhancement** — an inline link distinguished by colour alone fails colour independence no matter how strong the contrast; the design system's own styling clause on this is gate 61, and a link that drops the underline needs a second non-colour channel in its place (weight, a background, a marker), not a stronger hue. Run the greyscale test explicitly — convert the interface to greyscale and confirm status, errors, charts, and links are all still legible — and report the result rather than assuming it.

## 6 · Interaction pass

Native element first, ARIA last — `<button>` for actions, `<a href>` for navigation, never `<div onClick>`; no ARIA beats bad ARIA. Focus-visible ring at least 2px solid with 3:1 contrast against every adjacent colour it crosses, never bare `outline: none`. Hit areas: 24×24 CSS px is the WCAG 2.5.8 AA floor, 44×44 the touch target, 40×40 a reasonable desktop target; extend with a pseudo-element on the label or button, never overlapping another target. Every gesture (swipe, pinch, drag, long-press, shake) has a button-based alternative — gestures are shortcuts, never gatekeepers. Skip link is the first focusable element on any page with repeated navigation. Composite widgets (tabs, menus, toolbars) use roving tabindex — one Tab stop, active item `0`, the rest `-1`, arrow keys move both. Modals set `inert` on the background, trap focus inside, and return it to the trigger on close. **Landmarks: `banner`, `navigation`, `main`, `contentinfo` are the minimum on every page** — screen-reader users navigate by region before they navigate by heading, and a page with no regions is one undifferentiated run. Prefer the native elements (`<header>`, `<nav>`, `<main>`, `<footer>`) over explicit `role=`; where a landmark type repeats (two navs, several significant forms), each instance carries a distinguishing `aria-label`. **Every `<iframe>` carries a `title`** — an untitled frame announces as "frame" and nothing more, and on a page embedding a map, a video, a preview or a live demo this is the single most likely automated finding. Both checks are cheap and both are routinely missing, because no build reference mentions them; `tab_walk.py` will not catch either, so check the markup. Never a positive `tabindex` anywhere. Paste is never blocked in any field — password managers and 2FA autofill depend on it — and every field about the user carries a meaningful `autocomplete`.

## 7 · Persona walkthrough

Build 4–6 personas spanning permanent, temporary, and situational conditions (not four permanent-disability personas and nothing else — a broken arm and a parent holding a baby belong in the set too). For each persona, walk every key task from the brief and record whether it **works**, **works with friction**, **works with workaround**, or **fails**. Compile into a barrier matrix: task × persona, one cell per combination. A task that fails for any persona is a finding regardless of how it looks for the rest.

**Name the technology, not the disability.** "A blind user" produces a guess; "JAWS on Windows Firefox, navigating by headings" produces a walkthrough. Cover at minimum: one screen-reader user, one keyboard-only user, one low-vision user using magnification, one user with a cognitive difference, and one user in a situational-impairment context.

The inventory to pick from:

| Sense | Technologies, and what each one changes |
| --- | --- |
| Vision | **Screen reader** (JAWS, NVDA, VoiceOver, TalkBack) — reads aloud, navigates by headings, links and landmarks. **Magnifier** (ZoomText, OS zoom) — sees only a fraction of the screen at a time. **Braille display** — text to braille in real time, alongside a screen reader. **High-contrast mode** — system-level colour override. |
| Motor | **Switch device** — one or two buttons scanning through options; *much slower than a keyboard, and every extra step counts*. **Voice control** (Dragon, Voice Access) — spoken commands. **Head pointer / eye tracking** — limited precision. **Mouth stick / stylus**. |
| Hearing | Captions, visual alerts replacing audio ones, hearing loop / Bluetooth to hearing aids. |
| Cognitive | **Text-to-speech** (not a screen reader — the person sees the screen but processes better by hearing), reading ruler, simplified view, password managers as memory relief. |

**The switch device is the worst case for anything long and pinned.** A page whose primary content is a several-screen scroll sequence with pinned acts costs a switch user one scan cycle per step, and there is no "skip to the end of the act" unless the build provides one. Walk that case explicitly rather than inferring it from the keyboard walkthrough.

**Scenario template — eight fields**, and a scenario is not done until all eight are filled:

```
Name:            [name]
Role/context:    [who they are beyond their disability]
Technology:      [devices, AT, browser, settings]
Environment:     [where, when, what else is happening]
Task:            [what they are trying to accomplish]
Steps:           [how they interact, step by step, using their AT]
Pain points:     [where the design fails or creates friction]
Success:         [what a good outcome looks like for this person]
```

The scenario's job is to surface a specific failure a developer could fix — not to describe a goal. If it does not name a step where the design breaks, it hasn't been walked.

Two source lists worth pulling from rather than inventing: `situational-impairment-mapping`'s permanent / temporary / situational split per sense (bright sunlight, a noisy train, gloves, one hand holding a child are the same barriers as their permanent counterparts), and `edge-case-identification`'s content cases — long hyphenated names, non-Latin scripts on a Swedish/English page, a single character, an empty value (`references/principles.md` carries both, tagged by source).

## 8 · Report

Assemble in `references/report-template.md`'s exact shape:

- **Coverage table** from Step 0 — what was verified vs. inferred, restated with what actually got inspected.
- **Findings table** — `Severity | Location | Before | After | Why | WCAG | Who`. One row per root cause; list every location a systemic issue reaches. `Who` names the affected persona(s) or user group, not just "users".
- **Escalation triggers** — always `HIGH` the moment confirmed, never averaged down: no accessible name on an interactive control; a keyboard-reachable control with no visible focus indicator; a control reachable by pointer but not keyboard; content flashing more than three times per second (WCAG 2.3.1 — the one motion check that stays, preference-independent); content or a control clipped or unreachable at 320px width or 200% zoom; a contrast pair that fails its required ratio; state or meaning carried by colour alone; a destructive action with no confirmation or undo; truncated content with no way to reach the full value; content reachable only past a scroll edge or disclosure with no visible cue; an error that names no way to recover; a semantic colour used against its meaning.
- **Verdict** — `Block` when any `HIGH` remains, `Approve` otherwise. Never `Approve` coverage you did not inspect.
- **Legal map** — which of EAA/EN 301 549, ADA, Section 508, and WCAG 2.2 AA each finding touches. Most organisations target WCAG 2.2 AA; EAA (in effect since June 2025) and EN 301 549 align with it; ADA and Section 508 case law references it.
- **SEO flag** — mark findings on headings, alt text, `lang`, link text, or reflow as SEO-relevant; the same structural signals search crawlers and screen readers both depend on.
- **Deferred items** append to `.impeccable/a11y-debt.md` in the audited project — never dropped silently. Accepting accessibility debt requires the user's explicit acknowledgement in the conversation, not an assumed sign-off.

### The debt-entry format — an eight-field ADR

A one-line "deferred: contrast on the footer" is how a decision gets silently reversed two redesigns later by someone who wasn't in the room. Write each entry as a decision record (`inclusive/decision-documentation`):

| Field | What goes in it |
| --- | --- |
| **Title** | Clear and searchable — "Form validation: inline errors instead of summary banner", not "form fix". |
| **Date and author** | When, and by whom. |
| **Context** | The situation and the constraints that produced the decision. |
| **Decision** | What was decided, specifically enough to implement. |
| **Alternatives considered** | What else was evaluated and why it was rejected. |
| **Accessibility impact** | Who benefits and how — named groups, not "users". |
| **Risks and tradeoffs** | What was sacrificed, and why that was acceptable. |
| **Evidence** | The testing, research, or WCAG criterion supporting it. |

Plus the four deferral fields this skill requires on top: severity, **who is excluded** (named groups), **severity of exclusion** — blocked or friction — and a **remediation deadline** (critical: this sprint · major: 30 days · minor: 90 days) with a **review date**.

Store it alongside the code where it travels with the implementation. *Never only in someone's head or in a chat thread* — documentation is the immune system that protects a good decision from being undone by someone who doesn't know why it was made.

## Folding a HIGH: mandatory tradeoff analysis

A `HIGH` finding is never quietly downgraded. If one is going to be accepted rather than fixed, it is folded **by name**, through this analysis, and the result goes in the debt ledger in the format above (`inclusive/tradeoff-analysis`). Six questions:

1. **Who benefits from option A?** Which groups gain, roughly how many, and how severe the barrier is without it.
2. **Who benefits from option B?** The same analysis for the alternative.
3. **Who is harmed by each?** Which groups lose access or degrade, how badly, and whether the harm is permanent or temporary.
4. **What is the severity asymmetry?** **Blocked beats friction** — a user who *cannot* complete the task is more severely affected than one for whom it is *harder*, and blockers get removed before friction gets reduced. Permanent conditions outrank situational ones, because a situational user has other options and a permanent user may not.
5. **What is the reversibility?** Reversible → take the faster option and schedule the improvement. Irreversible → take the more inclusive option and accept the delay.
6. **What is the precedent?** A shortcut taken once becomes the standard unless it is documented as an exception.

**Red lines — tradeoffs that are never made:** never ship a feature that is entirely inaccessible by keyboard; never deprioritise a fix that blocks task completion; never treat "we'll fix it later" as acceptable without a tracked item and a date.

**The one crossed red line, and why it does not generalise.** Upstream's fourth red line is *"never remove existing accessibility to meet a deadline"*, and **F-011 crossed it deliberately** — motion-sensitivity users lost an opt-out they previously had. It is exempt not because the rule is wrong but because it was crossed the way this section demands: analysed, named, attested by the decision owner in writing, permanent rather than a deadline expedient, and recorded with its cost stated (`design-catalogue/FEEDBACK.md` F-011). That is the bar. **An attested override is a decision; an unattested one is the red line.** Nothing else in this skill inherits the exemption, and F-011 does not widen by analogy to any other preference.

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
| An accessibility-debt item deferred with no deadline or owner | Every debt entry needs severity, WCAG criterion, remediation deadline, and explicit user acknowledgement — written in the eight-field ADR shape, not as a one-liner |
| A `HIGH` accepted rather than fixed, with no analysis behind it | Run the six tradeoff questions, name who is excluded and whether they are blocked or merely slowed, and record it with a review date |
| Landmarks and `<iframe title>` never checked because no script reports them | Read the markup: four landmarks minimum, a title on every frame. `a11y_scan.py` catches `region` and `landmark-one-main`; the frame title and the label on a repeated landmark it does not |
