# Accessibility principle catalog

One line per principle, deduplicated by meaning, grouped by the eight audit passes in `SKILL.md`. Source tag in brackets after each line. Source index at the end lists every upstream file, relative to `references/upstream` in the design skill.

## Pass 1 — Mechanical

- Most accessibility is free if you use the platform; prefer the platform default over a custom rebuild, and remove ARIA rather than add it. [better-accessibility]
- A screenshot you didn't read doesn't count, and neither does a check whose output you didn't read. [design/SKILL.md]
- CARL rule: before trusting a load-bearing check's clean pass, run it against a version known to be broken and confirm it actually fails. [design/SKILL.md]
- Automated tools catch roughly 30% of real barriers, manual expert testing another 50%, testing with disabled users the remaining 20%. [inclusive/accessibility-testing-strategy]
- Automated tools miss whether alt text is meaningful, whether focus order is logical, and whether interactions actually work — only a human judges those. [inclusive/accessibility-testing-strategy]
- Test priority order: core tasks first, then input and navigation, then content and comprehension, then edge cases and preferences. [inclusive/accessibility-testing-strategy]
- Tab from the browser address bar through the entire page and document unreachable elements, wrong order, invisible focus, and traps. [inclusive/keyboard-review]
- Audit across devices and browsers, in both static and interactive states. [designer-skills/accessibility-audit]
- Believing work is done is not verification; run the check and report the observed result. [designpowers/verification-before-shipping]

## Pass 2 — POUR (WCAG 2.2 AA)

- POUR: every finding maps to Perceivable, Operable, Understandable, or Robust. [designer-skills/accessibility-audit]
- `<button>` for actions, `<a href>` for navigation, never `<div onClick>` — a real link supports Cmd/Ctrl/middle-click. [better-accessibility]
- The five rules of ARIA: prefer native semantics, don't change native semantics needlessly, every ARIA control must be fully keyboard-operable, never hide a focusable element, every interactive element needs an accessible name. [better-accessibility/semantics-and-aria]
- Accessible-name precedence: `aria-labelledby` > `aria-label` > native label/text/`alt` > `title`. [better-accessibility/semantics-and-aria]
- Label in Name (WCAG 2.5.3): the visible label text must appear in the accessible name, or voice-control users saying the visible word can't activate the control. [better-accessibility/semantics-and-aria]
- Multiple landmarks of the same type need distinguishing labels, e.g. `<nav aria-label="Primary">`. [better-accessibility/semantics-and-aria]
- Native `disabled` removes a control from the tab order and blocks activation; `aria-disabled="true"` keeps it focusable and hoverable for a tooltip. Never set both on one element. [better-accessibility/semantics-and-aria]
- Never disable a submit button — keep it enabled, validate on submit, focus the first error. [better-accessibility/semantics-and-aria]
- `.sr-only` needs a 1px box, not zero size, plus `white-space: nowrap` — some screen readers skip zero-sized elements. [better-accessibility/screen-readers]
- Choose the announcement mechanism in order: focus move, then `aria-describedby` tied to a control, then a polite live region (`role="status"`), then `role="alert"` for urgent untied errors only. [better-accessibility/screen-readers]
- A repeated polite live region must be a stable empty region rendered before its text changes, never re-inserted already holding content. [better-accessibility/screen-readers]
- `aria-hidden="true"` removes the whole subtree from assistive tech; never place it on or above a focusable element. [better-accessibility/screen-readers]
- Alt text by purpose: decorative `alt=""`, informative describes the meaning, functional describes the action, image-of-text reproduces the text, complex gets short alt plus a nearby full description. [better-accessibility/screen-readers]
- A missing `alt` is worse than an empty one — screen readers fall back to reading the filename. [better-accessibility/screen-readers]
- `aria-invalid="true"` on the failing field, removed once fixed; `aria-describedby` links the field to its inline error text. [better-accessibility/forms]
- `autocomplete` with a meaningful `name` is a WCAG 1.3.5 requirement for any field about the user. [better-accessibility/forms]
- Never block paste in a field — users paste passwords and one-time codes. [better-accessibility/forms]
- Modals trap and restore focus: `inert` on the background content, focus moves in on open, returns to the trigger on close. [better-accessibility]
- Map every design decision to its WCAG 2.2 success criterion before it ships, not after an audit finds it. [compliance-mapping]
- WCAG 2.2 AA is the global baseline most laws reference; some AAA criteria — especially cognitive ones — are worth adopting even when not required. [compliance-mapping]
- Placeholder text is never a label — it disappears on focus and usually fails contrast. [inclusive/form-labelling]
- Group related fields with `<fieldset>`/`<legend>` — always for radio groups. [inclusive/form-labelling]
- Every table needs `<th scope="col">`/`scope="row"` headers and a `<caption>` describing its content — never "Table 1". [inclusive/table-accessibility]
- Don't use tables for layout; use them only for data with a real row/column relationship. [inclusive/table-accessibility]

## Pass 3 — Cognitive (COGA)

- Three loads: intrinsic (inherent to the task — reduce by chunking, not deletion), extraneous (added by poor design — eliminate ruthlessly), germane (the user's real engagement — maximise by removing the other two). [COGA]
- Users must answer "where am I / where can I go / how do I get back" in under a second, without relying on memory. [inclusive/wayfinding-navigation]
- Important actions reachable in 1–2 clicks; favour breadth over depth in navigation hierarchies. [inclusive/wayfinding-navigation]
- Rate each screen on decisions required, items to remember, new concepts, steps, reading complexity, visual complexity — any dimension rated High means redesign before launch. [inclusive/cognitive-load-assessment]
- Map cognitive load across a whole journey to find load spikes and memory bridges, not just isolated screens. [inclusive/assess-load]
- Working memory holds roughly 4 items; if the system can remember it, the user shouldn't have to. [inclusive/memory-load-reduction]
- Never re-ask information the system already has; pre-fill from earlier steps or sessions. [inclusive/memory-load-reduction]
- Auto-save progress in any flow longer than 3 steps; never require starting over when a session expires. [inclusive/memory-load-reduction]
- One primary action per screen; secondary actions visually de-emphasised. [inclusive/focus-attention-design]
- No autoplaying audio or video, no unsolicited pop-ups; closing a modal never loses the user's work. [inclusive/focus-attention-design]
- Avoid time limits; where unavoidable, warn well before expiry and allow one-click extension. [inclusive/focus-attention-design]
- Accept multiple date and phone formats, auto-format as the user types, trim whitespace automatically. [inclusive/error-prevention-recovery]
- Never clear user input on error — always preserve their work. [inclusive/error-prevention-recovery]
- Every error message answers what happened, why, and what to do now — never blames the user. [inclusive/error-prevention-recovery]
- Undo available for at least 10 seconds after any action; destructive confirmations state the concrete consequence, not a generic "are you sure?". [inclusive/error-prevention-recovery]
- Help must be reachable without leaving the screen the user is stuck on, and never require a reference number to reach a human. [inclusive/contextual-help-design]
- Write help content at grade 4–6 reading level, using the same terminology as the interface. [inclusive/contextual-help-design]

## Pass 4 — Content

- Aim for a reading age of 12–14 (grade 6–8); grade 4–6 for buttons, labels, and errors. [designpowers/accessible-content]
- One idea per sentence, active voice, specific over vague — "Save your changes" not "Submit". [designpowers/accessible-content]
- Error messages follow "what happened + what to do", placed adjacent to the field, announced via live region or focus move. [designpowers/accessible-content]
- People scan before they read — inverted pyramid, most important information first, chunked into short paragraphs. [inclusive/readable-content]
- Maximum 3–4 sentences per paragraph; a new heading every 2–3 paragraphs. [inclusive/readable-content]
- The 5-second test: can someone read a sentence and understand it in 5 seconds? If not, rewrite. [inclusive/plain-language-design]
- Passive voice hides who does what — "Your application has been rejected" hides both the actor and the next step. [inclusive/plain-language-design]
- One H1 per page, no skipped levels, headings describe content rather than serving as visual styling. [inclusive/heading-structure]
- A screen-reader user scanning only headings should understand the page's structure. [inclusive/heading-structure]
- Alt text answers "if this image disappeared, what information would be lost" — not what the image looks like. [inclusive/alt-text-design]
- The same image needs different alt text in different contexts. [inclusive/alt-text-design]
- Every link makes sense read completely on its own, outside any surrounding sentence. [inclusive/link-text-design]
- Same link text must always go to the same destination; different destinations need different text. [inclusive/link-text-design]
- File links state type and size; links that open a new tab warn the user first. [inclusive/link-text-design]
- Auto-generated captions run 80–85% accuracy — always review and correct before shipping. [inclusive/multimedia-accessibility]
- Captions include relevant sound effects and music cues in brackets, not just dialogue. [inclusive/multimedia-accessibility]
- Media players need keyboard-accessible controls and speed adjustment (0.5x–2x) — essential for cognitive accessibility. [inclusive/multimedia-accessibility]
- Prefer simple tables with one header row; avoid merged cells; give a complex table a text summary. [inclusive/table-accessibility]
- Maximum 5–7 columns for comfortable scanning; on small screens convert to a card/list view rather than hiding data. [inclusive/table-accessibility]

## Pass 5 — Adaptive

- APCA Lc thresholds are the better default for design decisions (body ≥75, non-body ≥60, large text ≥45, UI components ≥30); WCAG 2 ratios are required for formal conformance claims. [better-colors]
- Identify the actual rendered background — the nearest ancestor that paints one — before measuring, not the page background. [better-colors]
- Fix a failing contrast pair by moving lightness, holding hue and saturation — hue and saturation barely move the measured value. [better-colors]
- Report a failing pair and its measured value; never repaint without being asked — contrast is a design decision. [better-colors]
- A translucent surface's contrast shifts with whatever scrolls behind it — test against the lightest and darkest content it can sit over. [better-colors]
- Dark mode is a separate design exercise, not an inverted palette — dark grey not pure black, off-white not pure white, elevation logic flips. [designpowers/adaptive-interfaces]
- Detect and respond to system preferences automatically; never make the user reconfigure what the OS already knows. [inclusive/user-preference-respect]
- `forced-colors: active` strips authored colour — borders and outlines must still define interactive elements without it. [inclusive/user-preference-respect]
- 1 in 12 male users has colour vision deficiency; colour can enhance meaning but must never be its only carrier. [inclusive/colour-independence]
- The greyscale test: convert the interface to greyscale and confirm status, charts, errors, and links remain legible. [inclusive/colour-independence]
- Font sizes in `rem`, never `px` — px overrides the user's chosen base size. [inclusive/flexible-typography]
- Body text line-height at least 1.5 (WCAG requirement); layout must survive user-applied letter- and word-spacing overrides. [inclusive/flexible-typography]
- Comfortable is the default density; compact and spacious are options, never the starting point, and every density level keeps 44px touch targets and 1.5 line-height. [inclusive/information-density]
- Content reflows to a single column at 320px width, or 200% zoom on a 1280px viewport, with no horizontal scroll (WCAG 1.4.10); tables, maps, and code blocks may scroll within their own container. [inclusive/responsive-accessibility]
- Never lock orientation unless the function genuinely requires it. [inclusive/responsive-accessibility]
- A simplified view is a focused version containing everything needed for core tasks, not a stripped-down "lite" mode. [inclusive/simplified-views]
- Wrap motion in `@media (prefers-reduced-motion: no-preference)` so it is opt-in; reduced motion means reduced, not eliminated — it targets vestibular triggers (parallax, autoplay, large-scale movement), not functional feedback (loading spinners, hover colour, focus rings). [better-accessibility/motion-and-zoom]
- Flashing content faster than 3 times per second is a seizure risk and a hard WCAG Level A line, never optional. [inclusive/motion-sensitivity]
- Test realistic preference combinations together — dark mode plus high contrast plus reduced motion — not each in isolation. [inclusive/preference-audit]

## Pass 6 — Interaction

- Style `:focus-visible`, never bare `:focus`; prefer the browser's unmodified ring, verified against every adjacent colour it crosses. [better-accessibility/focus-and-keyboard]
- `tabindex="0"` joins the natural tab order, `tabindex="-1"` is for programmatic focus only, positive values are never acceptable — they hijack the whole page's tab order. [better-accessibility/focus-and-keyboard]
- Roving tabindex (a roving `tabindex` pattern) for composite widgets (tabs, menus, toolbars, radio groups): one Tab stop, active item `0`, the rest `-1`, arrow keys move both. [better-accessibility/focus-and-keyboard]
- A skip link is the first focusable element, hidden until focused, targeting `<main id="main">`; anchor targets get `scroll-margin-top` so a sticky header never hides them. [better-accessibility/focus-and-keyboard]
- SPA route changes must update `document.title` and move focus to the new view's heading or `<main>` — client-side routing resets nothing on its own. [better-accessibility/focus-and-keyboard]
- WCAG 2.5.8 AA floor is 24×24 CSS px; 44×44 is the recommended touch target, 40×40 a usable desktop one; the spacing exception allows a smaller target with enough gap around it. [better-accessibility/hit-areas]
- Extend the hit area with a pseudo-element on the wrapping label or button, never on the input itself; two extended hit areas must never overlap. [better-accessibility/hit-areas]
- Decorative layers (glows, scrims, blurred sheens) get `pointer-events: none` so clicks reach the real control beneath. [better-accessibility/hit-areas]
- Every interactive element must be reachable by Tab, in an order matching the visual reading order — no element reachable only by hover or click. [inclusive/keyboard-navigation]
- Drag-and-drop always needs a keyboard alternative — move up/down buttons or arrow-key reordering. [inclusive/keyboard-navigation]
- Trigger actions on touch-up, not touch-down, so a user can slide away to cancel. [inclusive/touch-target-design]
- Separate destructive actions from common ones by distance or visual weight, never adjacent with no gap. [inclusive/touch-target-design]
- Every gesture (swipe, pinch, shake, long-press) needs a visible, single-action button alternative — gestures are shortcuts, never gatekeepers. [inclusive/gesture-alternatives]
- Build the button-based version first, add gesture support as an enhancement on top — that ordering guarantees the alternative always exists. [inclusive/gesture-alternatives]
- Every action must be possible through at least keyboard and pointer; never lock a feature to one input method. [inclusive/multi-modal-input]
- Never disable paste in a text field — password managers and assistive tools depend on it. [inclusive/multi-modal-input]
- Every piece of feedback works through at least two channels (visual plus text, minimum); colour alone is never one of the two. [inclusive/feedback-and-status]
- Transient toasts show for at least 5 seconds and never carry the only path to an action; errors stay until resolved, never auto-dismiss. [inclusive/feedback-and-status]
- Voice is an accelerator, never a gatekeeper — every voice interaction needs a text, touch, or keyboard alternative. [inclusive/voice-interaction]
- Never autoplay content with motion — show a static poster first, and give every moving element a visible pause control. [inclusive/motion-sensitivity]

## Pass 7 — Persona walkthrough

- Nothing About Us Without Us — design for the margins and the centre benefits; design for the centre and the margins get excluded. [designpowers/inclusive-personas]
- Build 4–6 personas: 2–3 primary users, 1–2 edge-case users, 1 stress-case user. [designpowers/inclusive-personas]
- Accessibility is a spectrum, not binary — map where each core task degrades from "works" to "fails" and for whom, rather than a single pass/fail. [inclusive/ability-spectrum-mapping]
- Weave disability into the full persona — goals, frustrations, context — never as an isolated "accessibility persona" pulled out only when someone remembers it. [inclusive/disability-inclusive-personas]
- Minimum diversity rule for any set of 4+: at least one permanent disability, at least one situational impairment, a range of technical confidence. [inclusive/disability-inclusive-personas]
- Every user is impaired in the right context — bright sunlight, a noisy commute, one hand holding a child — and the fixes that help them also help permanent-disability users. [inclusive/situational-impairment-mapping]
- Name the actual assistive technology and describe the interaction step by step, not just the disability and the goal. [inclusive/assistive-technology-scenarios]
- "That's an edge case" is the most common way accessibility gets deprioritised — if it affects disabled users, it's a design requirement, not an exception. [inclusive/edge-case-identification]
- Invert every happy-path assumption: desktop to mobile/screen reader, fast internet to offline, sees colour to colour-blind, one sitting to interrupted and resumed days later. [inclusive/edge-case-identification]
- Build accessibility into every story's acceptance criteria — keyboard, screen reader, visual, motor, cognitive — never a separate "accessibility ticket". [inclusive/inclusive-user-stories]
- Prioritise scenarios where the highest-risk task meets the most-affected persona, not an even sweep of every combination. [inclusive/scenario-map]
- Cognitive walkthrough per task: will the user try the right action, notice it, associate it with the right effect, and see that progress was made? Any "no" is a finding. [designpowers/heuristic-evaluator]

## Pass 8 — Report and decisions

- Escalation triggers are HIGH the moment confirmed, never averaged down because the surface is minor. [better-interface]
- The bar for reporting is evidence, not taste; a trigger fails regardless of the style guide, and a preference merely disagreed with is not a finding. [better-interface]
- Consolidate one root cause into one row, listing every location it reaches — never pad a report to fill a cap. [better-interface]
- `Approve` claims the coverage actually inspected; never issue it for a domain not checked. [better-interface]
- Accessibility debt compounds: new features build on an inaccessible foundation and inherit its inaccessibility; the longer an issue persists, the more code grows around it. [inclusive/accessibility-debt-tracking]
- Triage by deadline: critical fixes this sprint, major within 30 days, minor within 90 days; anything past its deadline escalates automatically. [inclusive/accessibility-debt-tracking]
- A previously fixed issue that reappears is a regression — treat it as critical by default, not as a fresh minor finding. [inclusive/accessibility-debt-tracking]
- EAA (in force since June 2025) and EN 301 549 align with WCAG 2.1 AA plus extra software, hardware, and documentation requirements; ADA and Section 508 case law both reference WCAG. [compliance-mapping]
- Record context, the decision, alternatives considered, who benefits, and the risks accepted — so a future redesign doesn't undo a deliberate accessibility choice by accident. [inclusive/decision-documentation]
- A user who cannot complete a task (blocked) is more severely affected than one who finds it merely harder (friction) — prioritise removing blockers. [inclusive/tradeoff-analysis]
- Never ship a feature completely inaccessible by keyboard, and never remove existing accessibility to meet a deadline — these are red lines, not tradeoffs to weigh. [inclusive/tradeoff-analysis]
- Match the accessibility argument to who's listening: risk and revenue for leadership, conversion and scope for product, specific criteria for engineers, craft quality for designers. [inclusive/stakeholder-communication]
- Plan a testing strategy across all three pyramid layers — automated, manual expert, real disabled users — not just the automated one. [inclusive/accessibility-testing-strategy]
- Before declaring done: check the debt register, confirm critical and major items are resolved (not just open), and get explicit user acknowledgement for anything accepted as debt. [designpowers/verification-before-shipping]
- On a review of an existing artefact, build a lightweight inferred brief (key task, audience across the ability spectrum, quality bar) rather than skipping straight to findings. [designpowers/design-review]
- Reconciliation order when reviewers disagree: accessibility over aesthetics, usability over style, brief over opinion, personas break ties, escalate to the user only if still unresolved. [designpowers/using-designpowers]
- Classify every finding critical/major/minor, name who is affected, and give a specific fix, not a vague direction. [designpowers/accessibility-reviewer]
- Distinguish issues that block shipping from improvements for a future iteration; acknowledge what works before listing what doesn't. [designpowers/design-critic]

## Source index

Paths are relative to `references/upstream` in the `design` skill.

- `interfaces/skills/better-accessibility/`: SKILL.md, focus-and-keyboard.md, forms.md, hit-areas.md, motion-and-zoom.md, screen-readers.md, semantics-and-aria.md
- `interfaces/skills/better-interface/`: SKILL.md, review-format.md
- `interfaces/skills/better-colors/`: SKILL.md (contrast section)
- `designpowers/agents/`: accessibility-reviewer.md, design-critic.md, heuristic-evaluator.md
- `designpowers/skills/`: accessible-content/SKILL.md, cognitive-accessibility/SKILL.md, adaptive-interfaces/SKILL.md, inclusive-personas/SKILL.md, verification-before-shipping/SKILL.md, design-review/SKILL.md, using-designpowers/SKILL.md (Reconciliation Protocol section only)
- `designer-skills/design-systems/skills/accessibility-audit/SKILL.md`
- `inclusive/accessibility-decisions/skills/`: accessibility-debt-tracking, accessibility-testing-strategy, compliance-mapping, decision-documentation, document, handoff, review, stakeholder-communication, tradeoff-analysis (each `/SKILL.md`)
- `inclusive/accessible-content/skills/`: alt-text-design, form-labelling, heading-structure, link-text-design, multimedia-accessibility, readable-content, review, rewrite, structure, table-accessibility (each `/SKILL.md`)
- `inclusive/adaptive-interfaces/skills/`: colour-independence, flexible-typography, information-density, preference-audit, responsive-accessibility, responsive-review, simplified-views, specify, user-preference-respect (each `/SKILL.md`)
- `inclusive/cognitive-accessibility/skills/`: adaptive-personalisation, assess-load, cognitive-load-assessment, contextual-help-design, error-prevention-recovery, focus-attention-design, memory-load-reduction, plain-language-design, review, simplify, wayfinding-navigation (each `/SKILL.md`)
- `inclusive/inclusive-interaction/skills/`: audit, design-flow, feedback-and-status, gesture-alternatives, keyboard-navigation, keyboard-review, motion-sensitivity, multi-modal-input, touch-target-design, voice-interaction (each `/SKILL.md`)
- `inclusive/inclusive-personas/skills/`: ability-spectrum-mapping, assistive-technology-scenarios, audit-stories, disability-inclusive-personas, edge-case-identification, generate, inclusive-user-stories, scenario-map, situational-impairment-mapping (each `/SKILL.md`)
