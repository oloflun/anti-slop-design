# Upstream reference index

One line per vendored `SKILL.md` / agent `.md`, grouped by vendor. Path is relative to
`references/upstream/`. Description is the frontmatter `description:` first line, or the
first heading when there is no frontmatter. See `MANIFEST.md` for source repos, commit
SHAs, and licenses.

## anthropic

- `anthropic/frontend-design/SKILL.md` — Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one.

## designer-skills (7 files)

- `designer-skills/design-systems/skills/accessibility-audit/SKILL.md` — Audit an existing interface against WCAG, producing findings with severity ratings and remediation steps.
- `designer-skills/interaction-design/skills/error-handling-ux/SKILL.md` — Design error prevention, detection, and recovery across a product.
- `designer-skills/interaction-design/skills/form-design/SKILL.md` — Design a form end to end — field order, grouping, validation, and completion.
- `designer-skills/interaction-design/skills/loading-states/SKILL.md` — Design waiting experiences — spinners, skeletons, optimistic updates, progressive reveal.
- `designer-skills/interaction-design/skills/onboarding-design/SKILL.md` — Design the first-run experience — activation path, progressive disclosure, time to first value.
- `designer-skills/ui-design/skills/dark-mode-design/SKILL.md` — Adapt an existing palette to dark mode — surface elevation, contrast rebalancing, desaturation.
- `designer-skills/visual-critique/skills/critique-affordance/SKILL.md` — Critique a rendered screen's affordances — clickability, state visibility, CTA clarity.
- `designer-skills/visual-critique/skills/critique-brand-consistency/SKILL.md` — Critique a rendered screen against mood/voice/tokens brand files.
- `designer-skills/visual-critique/skills/critique-color/SKILL.md` — Critique a rendered screen's colour — contrast ratios, palette coherence, semantic meaning.
- `designer-skills/visual-critique/skills/critique-composition/SKILL.md` — Critique a rendered screen's composition — balance, whitespace, rhythm, gestalt grouping.
- `designer-skills/visual-critique/skills/critique-information-density/SKILL.md` — Critique a rendered screen's density — cognitive load, prioritisation, scanning patterns.
- `designer-skills/visual-critique/skills/critique-typography/SKILL.md` — Critique a rendered screen's typography — scale usage, readability, consistency.
- `designer-skills/visual-critique/skills/critique-visual-hierarchy/SKILL.md` — Critique a rendered screen's hierarchy — entry point, eye flow, weight distribution.

## designpowers (14 files)

- `designpowers/agents/accessibility-reviewer.md` — Review any design output for inclusive design compliance (WCAG, COGA).
- `designpowers/agents/design-critic.md` — Review design work against the original plan, brief, and design principles.
- `designpowers/agents/heuristic-evaluator.md` — Evaluate a design against Nielsen's 10 usability heuristics; cognitive walkthroughs.
- `designpowers/skills/accessible-content/SKILL.md` — Writing/structuring user-facing content so it's readable, navigable, meaningful for everyone.
- `designpowers/skills/adaptive-interfaces/SKILL.md` — Designing for user preferences — motion sensitivity, contrast, colour scheme, text sizing.
- `designpowers/skills/cognitive-accessibility/SKILL.md` — Evaluating mental load, wayfinding, focus management, memory demands, decision complexity.
- `designpowers/skills/design-debt-tracker/SKILL.md` — Maintain a living register of deferred findings and design compromises.
- `designpowers/skills/design-review/SKILL.md` — Evaluate something that already exists: runs critic/accessibility/heuristic reviewers in parallel.
- `designpowers/skills/design-taste/SKILL.md` — Calibrate aesthetic direction — references, quality benchmarks, shared sense of "good".
- `designpowers/skills/inclusive-personas/SKILL.md` — Defining who a design serves so the full ability spectrum is represented from the start.
- `designpowers/skills/inspiration-scouting/SKILL.md` — Find aesthetic references, interaction examples, visual inspiration beyond competitive research.
- `designpowers/skills/motion-choreography/SKILL.md` — Designing animation sequences, transitions, micro-interactions that are purposeful and safe.
- `designpowers/skills/using-designpowers/SKILL.md` — Must run before any other Designpowers skill; welcome + routing sequence.
- `designpowers/skills/verification-before-shipping/SKILL.md` — Require running verification and confirming output before success claims.

## inclusive (58 files, 6 plugin dirs)

### accessibility-decisions (9)
- `accessibility-debt-tracking`, `accessibility-testing-strategy`, `compliance-mapping`, `decision-documentation`, `document`, `handoff`, `review`, `stakeholder-communication`, `tradeoff-analysis` — SKILL.md each, under `inclusive/accessibility-decisions/skills/<name>/`. Track, plan, map, document, and communicate accessibility decisions and testing/compliance strategy.

### accessible-content (10)
- `alt-text-design`, `form-labelling`, `heading-structure`, `link-text-design`, `multimedia-accessibility`, `readable-content`, `review`, `rewrite`, `structure`, `table-accessibility` — SKILL.md each, under `inclusive/accessible-content/skills/<name>/`. Writing and structuring accessible content: alt text, labels, headings, links, media, tables.

### adaptive-interfaces (9)
- `colour-independence`, `flexible-typography`, `information-density`, `preference-audit`, `responsive-accessibility`, `responsive-review`, `simplified-views`, `specify`, `user-preference-respect` — SKILL.md each, under `inclusive/adaptive-interfaces/skills/<name>/`. Interfaces that adapt to colour, typography, density, responsive, and system preference needs.

### cognitive-accessibility (11)
- `adaptive-personalisation`, `assess-load`, `cognitive-load-assessment`, `contextual-help-design`, `error-prevention-recovery`, `focus-attention-design`, `memory-load-reduction`, `plain-language-design`, `review`, `simplify`, `wayfinding-navigation` — SKILL.md each, under `inclusive/cognitive-accessibility/skills/<name>/`. Reducing cognitive load, memory demands, and confusion across flows and content.

### inclusive-interaction (10)
- `audit`, `design-flow`, `feedback-and-status`, `gesture-alternatives`, `keyboard-navigation`, `keyboard-review`, `motion-sensitivity`, `multi-modal-input`, `touch-target-design`, `voice-interaction` — SKILL.md each, under `inclusive/inclusive-interaction/skills/<name>/`. Multi-modal, keyboard, touch, gesture, and motion-sensitive interaction design.

### inclusive-personas (9)
- `ability-spectrum-mapping`, `assistive-technology-scenarios`, `audit-stories`, `disability-inclusive-personas`, `edge-case-identification`, `generate`, `inclusive-user-stories`, `scenario-map`, `situational-impairment-mapping` — SKILL.md each, under `inclusive/inclusive-personas/skills/<name>/`. Personas, scenarios, and user stories that include disability as a natural dimension.

## interfaces (10 files)

- `interfaces/skills/better-accessibility/SKILL.md` — Comply with accessibility standards and best practices.
- `interfaces/skills/better-colors/SKILL.md` — Build a color system: palettes, semantic tokens, format conversion, contrast checks.
- `interfaces/skills/better-interface/SKILL.md` — Combines all `better-*` skills into a single review across a11y/layout/writing/typography/color/UI.
- `interfaces/skills/better-layout/SKILL.md` — Grouping, alignment, reading order, progressive disclosure.
- `interfaces/skills/better-typography/SKILL.md` — Type scale, spacing, sizing, variable fonts, OpenType, wrapping, truncation.
- `interfaces/skills/better-ui/SKILL.md` — Concentric border radius, optical alignment, surface depth, contextual icons, hit areas.
- `interfaces/skills/better-writing/SKILL.md` — Improving product copy.
- `interfaces/skills/break/SKILL.md` — Renders a component in every state/scenario on a temporary page and stress tests it.
- `interfaces/skills/interface-review/SKILL.md` — Reviews work across UI, typography, layout, color, writing, accessibility.
- `interfaces/skills/variant/SKILL.md` — Builds multiple variants of a component and helps iterate/pick one.

## refero

- `refero/skills/refero-design/SKILL.md` — Primary/default skill for UI/product/web design; research-first methodology, reference locks, decision ledgers, anti-averaging quality gates, live Refero MCP research (styles/screens/flows).

## scroll-craft

- `scroll-craft/plugins/nateherk-design/skills/scroll-craft/SKILL.md` — Build a premium, scroll-driven interactive landing page; scroll-as-timeline, pinned sections, signature moves, verifies via self-screenshot.

---
Total: 98 SKILL.md/agent files indexed above (1 anthropic + 13 designer-skills + 14 designpowers + 58 inclusive + 10 interfaces + 1 refero + 1 scroll-craft).
