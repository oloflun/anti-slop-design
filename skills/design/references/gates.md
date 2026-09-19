# Gates

**Load on every build.** Numbered, citable, non-negotiable. A hook that denies a write cites a gate number; so should you when you waive one.

Three sources, one numbering space:

| Range | Source | Where the detail lives |
|---|---|---|
| **1–57** | Hallmark slop-test | [`slop-test.md`](slop-test.md) — ported verbatim, **source of truth** |
| **58–65** | This repo — the gate order, scope, and derivation rules | Below |
| **66–88** | `design-taste-frontend` v2 production-test tells | [`production-tells.md`](production-tells.md) — micro-decoration signatures |
| **89–91** | This repo — reference-lock discipline (Refero-derived) | Below |
| **92–96** | This repo — shape, budget, continuity, provenance, profile | Below |
| **97–98** | `design-taste-frontend` v2, ported 2026-09-09 — two further production tells | [`production-tells.md`](production-tells.md) |
| **99** | This repo — Anton's 2026-09-19 ban on descriptive microtext (F-016) | [`production-tells.md`](production-tells.md) |
| **mechanical** | impeccable v4 detector, 68 deterministic rules | `detect.mjs`, mapped below |

The numbering space is shared and append-only: 66–88, 97 and 98, and now 99 all live in
`production-tells.md`, and a new tell takes the next free number rather than
extending 88, because 89–96 are already spent here.

Do not restate 1–57 here. Read [`slop-test.md`](slop-test.md). Do not restate 66–88, 97, 98, or 99 here. Read [`production-tells.md`](production-tells.md).

**Why 66–88 exist separately.** Gates 1–57 catch structural and visual slop. Gates 66–88 catch *micro-decoration* — version labels, numbered eyebrows, middle-dot chains, status dots, photo-credit captions, scroll cues, locale strips. Each looks like a deliberate designer choice in isolation; together they are the most recognisable AI-page signature in production. Load them on every marketing, landing, or portfolio build.

---

## Both directions — the rule that governs every gate here

> **Every load-bearing check is proved in BOTH directions: a fixture that must fall, and
> a known-good build that must stay silent. A check that can only fire is as worthless
> as one that never does.**

A gate nobody has watched fire is an assumption. A gate that has never been held against
a build you already trust is worse — it will fire on that build too, and the first time
it does, someone waives it, and from then on the gate is decoration.

So each numbered gate, each hook denial and each script threshold needs two proofs on
file:

| Direction | What it proves | Where the fixtures live |
|---|---|---|
| **Must fall** | The detection actually detects | `tests/fixtures/`, `tests/a11y/broken.html`, `tests/perf/heavy.html`, `tests/motion/staircase.html` |
| **Must stay silent** | The threshold is not over-greedy | a catalogue entry, `sites/calyx.html`, `tests/perf/clean.html`, `tests/motion/smooth.html` |

**A check that flags the reference build is too greedy and gets narrowed — never
waived.** `blankBands` in `scroll_verify.py` is exactly such a check: it can fire on the
deliberately quiet act before the peak that `scroll/feel-and-fingerprint.md` requires. The
fix is a narrower band definition, not an exception for that page. Waiving is for a
*brief* that overrides a gate (see § Waiving a gate); it is never the answer to a gate
that misfires.

This is why `verify-design-system.py` runs paired fixtures rather than asserting on
output text, and why a new gate is not finished when its rule is written — it is finished
when both fixtures exist.

---

## Gates 58–65 · the gate-order rules

These exist because Tiers 0–2 are this system's contribution and nothing upstream enforces them.

### 58 · Tier not declared

Did the build state its tier out loud before picking any token? If no tier was named, fail. Silent tier selection is how Tier 1 gets skipped — the model reads brand evidence, does not register it as authority, and invents anyway. The declaration is cheap and makes the omission visible: *"Tier 1 — deriving from the Snajp wordmark and the existing type scale."*

### 59 · Token not traceable to tier evidence

At Tiers 0–2, can every colour, face, radius, and spacing step be traced to a named source — a `DESIGN.md` entry, a file in the codebase, the logo, the studied reference? A token that cannot be traced was invented, and invention is Tier 3 only. Fail per untraceable token. At Tier 3 this gate passes trivially.

### 60 · Demoted-skill palette in a Tier 0–2 build

Does the output contain a hardcoded value from a skill whose palette is fixed?

| Skill | Values that trip this gate |
|---|---|
| `minimalist-ui` | `#F7F6F3` `#FBFBFA` `#F9F9F8` `#EAEAEA` `#111111` `#2F3437` `#787774` `#333333` `#FDEBEC` `#E1F3FE` `#EDF3EC` `#FBF3DB` `#9F2F2D` `#1F6C9F` `#346538` `#956400` |
| `industrial-brutalist-ui` | `#F4F4F0` `#EAE8E3` `#050505` `#0A0A0A` `#121212` `#E61919` `#FF2A2A` `#4AF626` |
| `high-end-visual-design` | `#050505` `#FDFBF7` |

Auto-fail at Tiers 0–2. These skills may contribute craft vocabulary — spacing rhythm, detail patterns, elevation logic — but their palettes are overridden by the locked tokens. At Tier 3 the gate passes if the skill was chosen deliberately and by name.

**This gate is the instrumented trap.** Every firing is logged to the session ledger as a `trap` event with the file and whether it was caught before or after the write. See [`component-routing.md`](component-routing.md) § Telemetry.

### 61 · Undefined link colours

Are default `a` and `a:hover` colours defined from the palette, even when the page currently has no links? If not, fail. Links added later render browser-default blue, which is off-brand on every design ever made.

### 62 · Mobile hit target below 44px

Does every interactive element present at least a 44×44px touch target at mobile widths? Padding counts; visual size does not have to change. Fail per element below the floor.

### 63 · Value snapped to a framework default

Was a source value rounded to a grid step or a framework token? `13px` must not become `14px`; `5px` must not become `4px`; a brand orange must not become the nearest Tailwind orange. The source is ground truth and its odd numbers are the brand. Fail per snapped value.

Mechanically covered by `design-system-radius`, `design-system-font-size`, and `design-system-color` once `DESIGN.md` exists.

### 64 · Change beyond the ask

On a targeted request, did anything change besides what was asked? Layout, spacing, margins, fonts, sizes, positions, colours, and content outside the named target must be byte-identical. Improvements are *suggested in the reply*, never applied. Fail on any unrequested diff hunk.

Does not apply to redesign, new direction, or from-scratch requests — those are substantial by definition. See [`scope-discipline.md`](scope-discipline.md).

### 65 · Second identity inside an established surface

Does a new section, component, feature, or state introduce type, colour, motion, or component language that does not exist elsewhere on the surface? A local addition inherits; it does not start a second identity. Check the eight axes in [`scope-discipline.md`](scope-discipline.md) § inheritance checklist. Fail on any axis that diverges without the user asking for it.

---

## Gates 89–91 · reference-lock and averaging

These exist because [`reference-lock.md`](reference-lock.md) is this repo's
contribution and nothing upstream enforces it. Each fires whether the build
skipped the lock entirely or filled it out and drifted from it anyway.

### 89 · Calm-editorial autopilot

**Rule.** Warm ivory + oversized serif + one italic/serif word swap +
olive/clay/terracotta, applied without a register that earns it, fails. Licensed
only in the **editorial-print register** when the business plausibly publishes an
edition, catalogue, or archive — and even there, never the same word-swap two
generations running.
**Detection.** Palette traces {olive, clay, terracotta} + serif display + one
word carrying italic/serif/colour contrast, on a business with no editorial-print
justification, or the identical word-swap recurring from the prior generation.
**Fix.** Re-run Step 2 honestly — derive the register from the business, not from
taste. See [`reference-lock.md`](reference-lock.md) § Anti-averaging and the
identity / editorial litmus tests.

### 90 · Reference averaging

**Rule.** A build whose palette, type, or structure sits at the safe
intersection of conflicting references — instead of committing to one dominant
direction — fails, per **dark + acid + serif ≠ cream + orange + polite serif**.
**Detection.** Compare the built tokens against each captured reference in the
decision ledger; if no single reference dominates and the result reads as a
softened middle of all of them, it's averaged.
**Fix.** Name one primary reference and rebuild the lock's "Preserve" and
"Borrow only" fields around it. See [`reference-lock.md`](reference-lock.md) §
Anti-averaging.

### 91 · Token-role drift

**Rule.** A token or component pulled from a source reference keeps the role
that source gave it — a CTA-only accent used as a background, a code-only colour
used as UI chrome, or a decorative gradient promoted to a core surface all fail.
**Detection.** Walk the reference-lock's "Role rules" field against the built
page; flag every token or component whose deployed role doesn't match its
declared one.
**Fix.** Restore the token to its licensed role or drop it — never repurpose it
to make a layout "work." See [`reference-lock.md`](reference-lock.md) §
Token-role and media-role preservation.

---

## Gates 92–96 · shape, budget, continuity, provenance, profile

Five checks that existed as prose in five different files and could not be cited by a
hook, a reviewer or a waiver. Each has a mechanical detection and each is proved in both
directions per the rule at the top of this file.

### 92 · Shape Consistency Lock

**Rule.** One radius scale per page — sharp (0), one mid step (12–16), or pill — or a
written rule saying which element class gets which. Mixing 4, 8, 12, 16, 24 and pill
across one surface with no rule behind it fails. The failure has a signature and it is
**8 px on everything**: TASTE.md § 2.5, counted across the 89 sources Anton actually
saved, says rounding is a decision — either 0–3 px or large and deliberate (Raus 20/40,
Bumble 16–24, pill 999) — and *"Ingen ligger på 8 px-default."*
**Detection.** Collect every `border-radius` value in the emitted CSS. More than one
radius family, with no rule for it in `DESIGN.md` or `BRIEF.md`, fails.
`design-system-radius` covers this mechanically **once `DESIGN.md` exists**; this gate is
what holds before it does, which on a single-file HTML page is always. A reference's
radius vocabulary (`design-taste`'s 4 / 8 / 16) is a set to pick *from*, not a licence to
use all of it.
**Fix.** Name the scale in the token block (`--radius-sm` / `--radius-lg` /
`--radius-pill`), derive it from the locked reference, and restate every exception as a
rule rather than as a loose value. Gate **63** still binds on top: a source radius of
14 px stays 14 px and does not snap to 16.

### 93 · Performance budget

**Rule.** A page ships only when every line of [`performance.md`](performance.md) § 1 has
been **measured on this page** and met. A number nobody measured is a failed row, not a
pass — the same failure as an invented metric in copy (gate **46**).
**Detection.** `scripts/perf_probe.py` served through `scripts/serve.py`, at `--cpu 4`,
at 1440×900 and 390×844. Fail per row over its limit: LCP ≤ 1.8 s · CLS ≤ 0.05 · zero
long tasks during scroll · frame p95 ≤ 20 ms with none over 33 ms · ≤ 2.5 MB transferred
at 1440 · hero ≤ 250 kB WebP · ≤ 3 font files / 300 kB · ≤ 1500 DOM nodes · zero resting
`will-change` · no `filter`/`backdrop-filter` over half the viewport. A scrubbed clip has
its own line (≤ 32 MiB desktop, ≤ 16 MiB mobile, fetched as a Blob after first paint) and
does not count against the page. Never measure through `python -m http.server`: it is
HTTP/1.0 and drops large WebP responses under Chromium on Windows, so the run measures a
page that failed to load.
**Fix.** [`performance.md`](performance.md) §§ 2–3 in order, loading before rendering.
Two of the rows are structural rather than numeric and are fixed by deletion: a hero on
another company's CDN, and `will-change` set on a class.

### 94 · Motion continuity

**Rule.** Anything the eye sees move is damped, evenly paced, and holds frame. Three
parts, and they fail independently:

1. **Damped.** Bespoke motion reads `--sc-ps`, never raw `--sc-p`, whenever it drives
   `transform`, `object-position`, `clip-path`, `mask-position` or `background-position`.
   Cue opacity may read `--sc-p`.
2. **Continuous.** At 4× CPU throttling, in **both** scroll directions: `staircase` 0,
   `frame_p95_ms` ≤ 20, `frames_over_33ms` 0, and `max_step_pct` ≤ 3 **on the damped
   playhead (`--sc-ps`)**. On a derived track (`transform`, `clip-path`, …) `max_step` is
   reported, not gated: a smoothstepped value peaks at ~4.4 % per frame by its own
   derivative, and `staircase` already catches the step. (r8 R2, 2026-09-09: V3c's flip
   read 4.12 % with staircase 0 and was correct.) Never track raw `--sc-p` — it steps
   per wheel tick by design.
3. **Evenly paced.** On a multi-act or multi-leg sequence, `rate = weight / clip_seconds`
   holds within ~6 % across the whole run. 36 % is the measured failure, not a
   hypothetical one — see [`scroll/pace.md`](scroll/pace.md).

**Detection.** `scripts/motion_probe.py --track "<sel>:<prop>,…" --cpu 4` over every
value the eye sees move; the script enforces those four thresholds itself. Grep the
emitted source for `--sc-p` inside a `transform` / `clip-path` / `object-position` /
`mask-position` / `background-position` declaration. Per-leg rates are arithmetic off the
markup — weight and clip length are both in the source, so there is no excuse for not
having the table.
**Fix.** Diagnose which fault you have *before* changing anything
([`motion-smoothness.md`](motion-smoothness.md) § The two faults): damp the value, or cut
the work (gate **93**). They need opposite fixes, and an afternoon spent smoothing
something that was never stepping is the standard way to lose one.

### 95 · Catalogue selection not logged

**Rule.** The references were chosen mechanically out of the whole catalogue, and the
`catalogue-select` row in `.impeccable/design-session.jsonl` is the proof. References
recalled from memory, or handed down in an orchestrator's prompt, fail — **even when they
are the right ones.** r7 named the right slugs, the builders read them, the reference
floor was satisfied, and `Skill(design-catalog)` was never invoked; nothing afterwards
could tell the difference. This gate is that difference.
**Detection.** The ledger carries a `catalogue-select` row naming **≥ 2 slugs**; every
named slug has its `entry.md` and a fold read in the same session, plus its
`extract/*-DESIGN.md` where an extract exists; on a scroll brief
`design-fingerprints.md` was read as well. `hooks/design-gate.py`'s reference floor denies
the first UI write until those marks are present.
**Fix.** `python scripts/catalogue/select.py --brief BRIEF.md --k 4 --wildcard --explain`,
then read what comes back as pixels *and* as text and rewrite the lock from it. An empty
result means widen the register, drop the grammar, or try an adjacent category — it is
not permission to work from memory. See [`catalogue-first.md`](catalogue-first.md) § 5.

### 96 · TASTE § 5 hit

**Rule.** TASTE.md § 5 is the rejected list, derived by counting occurrences across the 89
sources Anton actually saved rather than from taste: *"Ett bygge som innehåller något ur
listan ovan ligger utanför profilen oavsett hur välgjort det är."* A nonzero count is not
a licence — it names the single licensed form (Palais' blobs are hand-drawn;
dope.security's indigo is a glow, not an accent). The gate fires on the generic form.
**Detection.** Ten items, mapped to what actually checks them:

| TASTE § 5 item | In 89 saved sources | Mechanical rule |
|---|---|---|
| Icon grid | 0 | `icon-tile-stack` |
| Gradient mesh | 1 (Brand Federation, saved for the hero shape) | none exact; nearest `radial-halo`, `radial-spotlight-glow`, `repeating-stripes-gradient`. **By eye** |
| Glassmorphism | 0 | none. **By eye** |
| Centred hero with a badge row | 0 (outside AI templates) | `hero-eyebrow-chip` catches the badge; the centring is a critique measurement (taste-skill § 4.3, anti-centre above variance 4), not a detector rule |
| Purple / indigo accent | 1 (dope.security, as a glow) | `ai-color-palette`, plus the flat-accent hexes `#6366f1` `#8b5cf6` `#7c3aed` in [`color.md`](color.md) § Bans |
| Shadowed 8 px cards | 3 (all template defaults) | `gpt-thin-border-wide-shadow`, `border-accent-on-rounded` — and gate **92** |
| Stock photo of a smiling team | 0 | none. **By eye** |
| "h1 48 / h2 32" scale | 0 | `flat-type-hierarchy` (`oversized-h1` is the opposite failure) |
| Decorative blobs | 1 (Palais, hand-drawn) | `shape-assembled-illustration` |
| Three identical feature cards | 4 (all in AI templates) | `repeated-container-text` |

**Fix.** Replace the move; never soften it into a version that scores under the
threshold. Four of the ten have no mechanical rule and are read by eye at Step 5 pass 10
([`verbs/critique.md`](verbs/critique.md)) — that is a known coverage gap, written down
here rather than papered over.

---

## Reinterpreting gate 57

`slop-test.md` gate 57 fires when a `study` diagnosis is discarded in favour of a catalog theme. Its principle generalises to our gate order and is read as: **any derived or studied system discarded for a catalog theme, at any tier above 3, is an auto-fail.** The specific catalog-theme name list in the ported text is the Tier-3 vocabulary; the failure it describes — reverting to the attractor after doing the derivation work — is exactly what gates 59 and 60 catch at Tiers 1 and 2.

The ported file is not edited. This paragraph is the reinterpretation.

---

## Mechanical coverage

`detect.mjs` carries 68 deterministic rules. Run it once over changed files at Step 5; parse the JSON, because **exit code stays 0 when findings exist**.

```bash
node "$HOME/.agents/skills/impeccable/scripts/detect.mjs" --json <files>
```

Contract rules — these read `DESIGN.md` directly and are what `design-gate.py` denies on:

| Rule id | Enforces |
|---|---|
| `design-system-color` | Colour outside the `DESIGN.md` palette |
| `design-system-font` | Face not declared in `DESIGN.md` typography |
| `design-system-font-size` | Size outside the declared scale |
| `design-system-radius` | Radius outside the declared scale |

Slop rules overlapping our numbered gates: `side-tab` (gate 3 family), `gradient-text`, `dark-glow`, `radial-halo`, `radial-spotlight-glow`, `overused-font`, `italic-serif-display` (38a), `nested-cards`, `icon-tile-stack`, `hero-eyebrow-chip`, `numbered-section-labels` (54 family), `repeated-section-kickers`, `oversized-h1`, `flat-type-hierarchy`, `cream-palette`, `ai-color-palette`, `border-accent-on-rounded`, `gpt-thin-border-wide-shadow`, `edge-flush-cards`, `repeating-stripes-gradient`, `shape-assembled-illustration`, `codex-grid-background`.

Layout and responsive: `clipped-overflow-container`, `text-overflow`, `text-occlusion`, `first-viewport-column-overflow`, `body-text-viewport-edge`, `broken-image`, `image-hover-transform`, `layout-transition`.

Type and legibility: `low-contrast`, `gray-on-color`, `tiny-text`, `undersized-ui-text`, `line-length`, `tight-leading`, `wide-tracking`, `extreme-negative-tracking`, `all-caps-body`, `justified-text`, `single-font`, `heading-rhythm`, `skipped-heading`.

Copy — these run before the copy gate and catch its cheapest cases mechanically: `em-dash-overuse`, `marketing-buzzword`, `theater-slop-phrase`, `aphoristic-cadence`, `repeated-container-text`.

Motion and state: `bounce-easing`, `blinking-cursor`, `pulsing-dot`, `marquee`, `content-hidden-at-rest`, `monotonous-spacing`, `cramped-padding`, `script-error`.

**Not mechanically covered** — gates 58, 59, 60, 64, 65 and the whole gate order are model-enforced. `design-gate.py` and `design-route.py` cover 60 and 63 by pattern; the rest are judgment and are why the pre-emit self-critique exists.

Of the new block: **93** and **94** are fully mechanical (`perf_probe.py`, `motion_probe.py` — both already enforce their own thresholds), **95** is enforced by `design-gate.py`'s reference floor, **92** is mechanical only once `DESIGN.md` exists (`design-system-radius`) and model-enforced before that, and **96** is mechanical for six of its ten items — the four marked *by eye* in its table are the coverage gap.

---

## Waiving a gate

A gate may be waived only when the user's own brief calls for it. Say which gate, and why the brief overrides it, in one line. Never waive silently, and never waive by softening the element — rewrite it or keep it.

impeccable v4's rule governs: **the brief wins; your own habit does not.**

Persistent, project-wide exceptions go through the detector's config rather than being re-argued each session:

```bash
node "$HOME/.agents/skills/impeccable/scripts/hook-admin.mjs" ignore-value overused-font <Font> --shared --reason "..."
```
