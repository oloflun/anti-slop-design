# House physics — the executed quality bar, with exact values

Extracted 2026-07-31 from the full source of the worked examples in
`~/example-design-system/sites/`. The compressed version lives in SKILL.md § The craft
floor; this file carries the per-example inventory. When in doubt, read the source
itself: it is the spec, executed.

**Read the structural section, then only your register's inventory.** The first
three examples (Calyx, Hōrai, Hyperborea) are all *editorial print* in different
grounds. Treating their shared traits as universal is what made every build come
back serif, cream and numbered, including for businesses where that is actively
wrong. Tidvatten and Klova are here as the counterweight.

## Structural — true in every register

- **Palette:** 8–10 named tokens, oklch where the stack allows. Exactly ONE
  saturated accent, deployed at display scale (drop caps, giant prices, glyphs, a
  drawn form) and never as fill on a small control.
- **Hierarchy through scale, not decoration.** Display clamp() with leading
  0.9–0.95; body measure capped in ch. No shadow stacks, no gradient borders.
- **Hairlines separate; planes do not.**
- **Stagger:** paired columns never top-align.
- **Every open column carries weight** — a display numeral, a stat, an image, or a
  full-height rule. Otherwise close it.
- **At least three distinct section anatomies** per page.
- **One tonal inversion** somewhere on the page.
- **Motion:** one shared reveal (translateY 28px, 1.2–1.4s,
  cubic-bezier(.16,1,.3,1)), failing toward visible; plus one signature set-piece
  with at least two coordinated layers and a `?preview=` hook. **Motion always
  plays** (Anton, 2026-09-07 — FEEDBACK.md F-011, overrides the reduced-motion
  rule this replaced): never gate the reveal or the set-piece behind
  `prefers-reduced-motion` (F-011) or any other browser/OS accessibility
  setting, and never build a parallel static-fallback document. One motion path, verified
  once. This is a deliberate, permanent design-system override of the usual
  accessibility guidance — `a11y-audit` does not flag it. The set-piece's
  target (a window, a word, an object) is quiet at rest and lights on the
  first scroll: at rest the end state is never previewed. On a scroll brief,
  motion is the authority *inside* the set-piece act and type/photo step down
  there (TASTE.md § 4.8).
- **Two documented reveal profiles, not one.** The values above are the
  *editorial-print* reveal (28px, 1.2–1.4s) — a slow, deliberate arrival that
  suits a page whose sections are chapters. Scroll-craft's premium fade-in is
  the second profile and belongs to ordinary flow sections on a scroll page:
  **opacity from 0, a rise of about 14px over 620ms on an ease-out curve, 30–80ms
  stagger through the children in reading order, triggered slightly inside the
  viewport (`-12%` bottom root margin)** so it fires when the reader is looking
  rather than when the first pixel clears the fold. Its two failure bounds are
  exact and worth memorising: **a fade with no rise reads as a loading glitch; a
  rise past 24px reads as a slide.** *"Larger, slower, or bouncier is never more
  premium; the restraint is the signal."* **Conflict, resolved:** these are not
  competing values for the same thing — 28px/1.3s is the shared *page* reveal in
  the editorial registers, 14px/620ms is the *section* reveal on a scroll build,
  and a page picks one profile and holds it. What is never allowed is a third
  set of numbers invented per section, or a reveal that re-hides when the reader
  scrolls back up (that is a defect, not an effect).
- **A signature act may cost frames; the rest of the page may not.** Any
  continuous, CPU-heavy animation is isolated in a leaf element of its own so
  its work cannot invalidate the layout above it, and 60fps is the target, not
  the ambition (stitch § Motion: *"Isolated Client Components for CPU-heavy
  animations"*). Measurement, budget and the smoothness criteria live in
  `performance.md` and `motion-smoothness.md`.
- **Copy in a specific voice about a specific place**, with honest numbers.
- **Density above 7 puts every number in mono.** At dense settings the figures
  are the content, and proportional digits at that density read as noise —
  tabular mono is what makes a column of them scannable (stitch
  § High-density override). At the airy end of the scale this rule is off; a
  mono numeral in a 3-density editorial page is apparatus, and the apparatus
  budget in SKILL.md governs it instead.

### Craft vocabulary — the values that read as "made", not "generated"

Small, specific, and the difference between a page that looks designed and one
that looks defaulted (designpowers `design-taste` § detail vocabulary):

- **Borders are 1px at ~8 % opacity, not solid lines.** A solid rule at full
  strength is a divider from a template; a hairline at 8 % is a structure the
  eye reads without being interrupted by. Matches this file's *hairlines
  separate; planes do not*.
- **A shadow that must exist is two layers: one tight and sharp, one soft and
  ambient.** One layer reads as a sticker. **Conflict, noted:** the structural
  rule above still stands — depth is weight and scale first, `border` **or**
  `shadow` and never both (impeccable `craft-floor.md`), and
  `layout-and-space.md` § Depth bans stacked shadows *as a default*. The
  two-layer form is what a deliberate elevation looks like when the register has
  decided it needs one; it is not a licence to shadow every card.
- **Hover moves geometry, not colour** — `scale(1.02)`, a 1px lift, a rule
  drawing itself — rather than swapping a fill. A colour-swap hover is the
  cheapest and most generated-looking state on the page.
- **One radius vocabulary per page, spoken in roles**: e.g. 4px inputs, 8px
  cards, 16px modals. Three values with jobs, not seven values that happened.
  This is the Shape Consistency Lock (gate 92); the concentric-radius math in
  `layout-and-space.md` § Optical adjustments derives values *from* this
  vocabulary rather than adding to it.
- **The worked example of a coordinated two-layer set-piece** is
  `animated-navigation`: an arrow element flies from the logo to the hovered nav
  link while the link's underline expands from left to right — and the underline
  is held on `delay-300` so it starts *after* the arrow arrives. That delayed
  dependency is the whole lesson: two layers on one trigger, the second waiting
  on the first, so the motion reads as one gesture with a cause instead of two
  animations that happen to fire together. Its project values (the logo's
  arrow crop, the tuned coordinates, `/arrow.png`) are specific to that site and
  port nothing.

## Surviving the system's own overrides

This house builds structure out of **hairlines, tone-on-tone planes and
low-opacity rules** (TASTE.md § 2.3). That is exactly the structure the
operating system throws away when a reader turns on a colour override — so the
page has to be built to survive it, not patched afterwards.

- **`forced-colors: active` strips your colours and keeps your borders.**
  Windows High Contrast replaces every author colour with the system's own
  palette. A section boundary made of a 6 %-opacity rule, a `background`
  difference, or a tinted plane simply ceases to exist; the page collapses into
  one undifferentiated run. Don't fight the override — make sure **borders and
  outlines define every interactive element and every structural boundary**, and
  never let a background colour alone carry a state.
- **The transparent-border trick.** A `border: 1px solid transparent` is
  invisible in normal rendering and *becomes visible* under forced colours,
  because the system paints it. It is how a plane-and-hairline layout keeps its
  structure for free:

  ```css
  .card, .section--ink, .ledger__row { border: 1px solid transparent; }
  ```

  Then verify at `@media (forced-colors: active)` that every interactive element
  is still distinguishable (`inclusive/user-preference-respect` § forced-colors).
- **`prefers-reduced-transparency: reduce`** — outside F-011 entirely (it is a
  transparency preference, not a motion one), so honour it. It replaces
  semi-transparent surfaces with solid ones and removes frosted-glass and
  backdrop-blur effects; overlays
  become fully opaque. This costs this house almost nothing — glass is already
  refused (TASTE § 5, gate 60) and backdrop-blur is restricted to fixed/sticky
  chrome — but a scrim over a photograph does need a solid fallback, or the text
  above it loses its ground.
- **Motion is not in this list.** F-011: `prefers-reduced-motion` is not
  consulted, here or anywhere — motion always plays (see § Structural). Every
  *other* system preference in this section is honoured in full. The two are
  separate decisions and the override applies to exactly one of them.

## Editorial-print invariants — Calyx · Hōrai · Hyperborea only

- **Kicker microformat** (identical across all three):
  `font-size: 10.5px; letter-spacing: 0.22em; text-transform: uppercase;`
  mono on Calyx/Hyperborea. The page's structural voice — labels, captions, meta.
- **Palette:** 8–10 named oklch tokens. Exactly ONE saturated accent, deployed
  at display scale (88px drop caps, clamp(3.8rem,7vw,6rem) prices, JP glyphs,
  the sun) and essentially never on small controls. A rare second accent
  (Hyperborea's crimson) is sparser still.
- **Buttons barely exist.** CTAs are typeset mailtos/links at italic text-4xl
  (Calyx line 274) or display-size headline links. Hyperborea's one button is a
  sharp amber rectangle.
- **Display type:** clamp() up to 15rem (Horai wordmark
  `clamp(4.5rem,15vw,15rem)`), leading 0.9–0.95, tracking ~-0.02em. Two-tone
  inside the headline: Calyx roman + italic Cardo in one line; Hyperborea
  cream + amber in one line. 2–3 families, hard roles. Body measure in ch
  (max-w-[36ch] … [58ch]).
- **Label-rail section anatomy:** 12-col grid, max-w 1480–1880px. col-span-3
  rail = kicker (accent or stone) + 1px rule at ~20% opacity + optional meta;
  col-span-9 content. Horai upgrades the rail with a JP glyph and
  `md:sticky md:top-32`.
- **Ledger, never card grid** — for pricing, indices, programmes, testimonials.
  Grid rows with hairline border-b at ~20% opacity, italic display numeral
  (`.01`, `I II III` at text-8xl), name + description capped at 44–54ch, meta
  in kicker, price right-aligned in display serif 3xl–8xl, currency in tiny
  kicker with Swedish thin-space formatting (`2 480 kr`).
- **Display size in a price column is for the digits only** (Anton, 2026-09-19,
  FEEDBACK.md F-017). The figures are compact numerals that build the row's
  rhythm; any *text* sharing that column — `"Pris vid förfrågan"`, a unit, a
  condition — sets one typographic step smaller than the digits and
  baseline-aligns to them, never the same size. A contact row (phone, email, a
  booking link) is sized as an action — button- or link-scale — never as a
  heading. Checked by `scripts/microtext_scan.py --price-ledger`, which flags a
  text cell sharing a digit cell's font-size.
- **Stagger:** paired photo/text columns offset `md:mt-24` / `md:mt-44`;
  programme columns `md:mt-12` / `md:mt-24`. Never top-aligned.
- **Grain film:** fixed full-page feTurbulence data-URI
  (`baseFrequency 0.85, numOctaves 2`) with feColorMatrix tinted to the
  palette; `mix-blend-mode: multiply` opacity .42–.5 on light ground,
  `screen` opacity .35 on dark. Those are the *editorial-print* values, where
  grain is a material choice carrying the printed-paper fiction. **On any other
  register grain has one job and one value: a flat dark ground bands on real
  displays, and grain at 4–5 % opacity is what makes it stop.** Scroll-craft
  states the effect exactly — it is *"the difference between 'a dark page' and
  'a lit room'"* (`taste.md` § Depth). Read 4–5 % as the functional floor for a
  dark build and .35–.5 as this register's deliberate excess; a cinematic or
  modern-clean page reaching for .42 has misread which of the two it is doing.
  Either way grain is a fixed, full-page, `pointer-events: none` layer.
- **Shared reveal:** `.reveal { opacity:0; transform:translateY(28px);
  transition: 1.2–1.4s cubic-bezier(.16,1,.3,1) }`, one IntersectionObserver
  at threshold 0.1–0.12; plays unconditionally, never neutralized by
  `prefers-reduced-motion` (F-011 motion-always override, 2026-09-07 —
  FEEDBACK.md). Reveals fail toward visible (threshold 0 for tall elements, mount
  reveal, failsafe, noscript — see the reveal guards).
- **One signature motion set-piece per page**, mathematically scrubbed, both
  directions, plus a `?preview=` debug hook forcing its formed state so it can
  be screenshot-verified.
- **Copy as worldbuilding:** commission numbers (`Cmsn. 0211 — Hotel Pigalle,
  Drottninggatan`), plate indices (`02 / 14`), edition markers (`Vol. IX ·
  spring`, `Edition MMXXVI · Vol. 03`), roman-numeral dates (`cut 14.iv`,
  `12.ix · friday`), real street addresses, cross-referenced fictional
  entities (Atelier Lichtspur is both the identity credit and a speaker's
  studio), self-aware colophons (`Set in Cardo & PT Mono`). Values encoded in
  copy: "120 seats. Three tiers. No platinum." / "Write us a letter, not a
  form."
- **In-situ negation:** section comments name the slop default replaced —
  "INDEX: a typeset price list / commission ledger — NOT a card row",
  "PROGRAMME: three-day numbered list (not 4 icon cards)".
- **Art direction by render:** photos judged under their actual scrims and
  swapped when they fought the type — "darker, moodier photo for the quote
  section (was bright meat plate which conflicted with overlay text)".

## Calyx — light editorial (cream botanical atelier)

- Fonts: Cardo (display AND body, italic as display voice) + PT Mono (kicker only).
- Tokens: cream `oklch(0.965 0.012 88)`, ink `oklch(0.18 0.014 110)`, stone
  `oklch(0.46 0.012 110)`, rust `oklch(0.46 0.108 38)` — rust appears ONLY at
  display scale: one ledger title + four 88px italic drop caps.
- Hero: `text-[clamp(3rem,9vw,9.5rem)] leading-[0.92]`, roman + italic mixed.
- No buttons anywhere; CTA is a mailto at italic text-4xl.
- Duo photos 7-col + 5-col with `md:mt-24` stagger; figcaptions carry the fiction.
- Final section inverts to bg-ink. Grain tinted to ink hue, multiply, .5.

## Hōrai — dark-warm cinematic (three-sister restaurant)

- Fonts: Cinzel (all-caps display, POSITIVE tracking 0.06em; micro-labels 12px
  at 0.28–0.36em) + Vollkorn (body 19px/1.55 set on html) + Noto Serif JP.
- Tokens: paper `oklch(0.93 0.025 80)`, walnut `oklch(0.22 0.022 38)`, lacquer
  `oklch(0.45 0.20 25)` (the hot accent: giant menu prices, JP glyphs, "OPEN
  MONDAYS"), jade `oklch(0.42 0.06 165)` only for pairing prices.
- Sections alternate light/dark like chapters; a 130vh chapter-break with
  sticky inner h-screen.
- Stacked scrims: linear walnut gradient + radial vignette rgba(0,0,0,.45→.85).
- Signature set-piece: scroll-scrubbed quote — bell-curve proximity of section
  center to viewport center through smoothstep, staged tEarly/tMid/tLate,
  lerping opacity, translateY 80→0, scale 0.66→1.02, blur 12→0px, and
  letter-spacing 0.36em→0.12em, with two gold rules expanding 0→48px; plus a
  word-by-word lit scrub of the lede (opacity 0.18→1 per word). rAF parallax
  at 0.32/0.12. `?preview=quote` forces the formed state.

## Hyperborea — dark-navy illustrated (humanist tech conference)

- Fonts: Italiana (hairline display) + Archivo (body) + Noto Serif JP
  (bilingual thread: 温度のある機械 in amber under the English headline).
- Tokens: ink navy `oklch(0.14 0.032 254)`, amber `oklch(0.79 0.158 64)`,
  crimson `oklch(0.50 0.180 25)` (sparse second accent), bone
  `oklch(0.94 0.020 80)`.
- ZERO photographs — a bespoke inline-SVG identity system: radial-gradient
  rising sun (18s idle float), skyline silhouette containing a 3px lone amber
  figure, EIGHT unique geometric sun-disc speaker portraits varying one motif
  (eclipse, twin suns, mountain horizon, orbit ring, wave), and a sundial
  installation diagram. All palette-locked oklch fills, aria-hidden.
- Edition strip ABOVE the nav: `Edition MMXXVI · Vol. 03` / JP motto /
  `Lund · 12—14 september`.
- Tickets are a Calyx-style ledger (display 5xl `4 800 kr`, `0 kr · funded`).
- Grain tinted amber (feColorMatrix 0.96/0.74/0.36), mix-blend screen, .35.

## Tidvatten — modern clean (cold-bath club, Malmö)

Built blind by a subagent as a system test; the owner's read was that it felt the
least AI-generated of the set. Its lesson is that a grotesk can be a *decision*.

- **Fonts:** Familjen Grotesk (display, uppercase, tight), Literata (body serif),
  Fragment Mono (kicker). The grotesk is right because the subject is temperature,
  timetable and protocol — precision, not connoisseurship.
- **Palette:** slate blue-greys and deep sea dark, terracotta as the only warmth,
  used exclusively at display scale.
- **Set-piece:** the two temperatures (`2°` / `85°`) driving together out of blur
  as the section centres — scrubbed both directions, with the mono line beneath
  resolving on a staged offset.
- **Anatomy:** full-bleed sea photograph with the wordmark set into it; a
  statutes ledger (`§4 · Tystnad på lavarna före klockan sju`); a numbered season
  programme; a staggered photo duo; a membership ledger.
- **Where it still slipped:** its values line was a translated clone of
  Hyperborea's. Hence the "borrow the move, never the sentence" rule.

## Klova — warm photographic (harbour restaurant, Bohuslän)

The counter-example that proves the register split. It breaks nearly every
editorial invariant and is correct. Full notes in `sites/klova/README.md`.

- **Centred logo lockup over a full-bleed photograph.** No rail, no kicker, no
  edition marker.
- **A real outlined button** (`SE VÅR MENY`), sized to be pressed. A typeset
  mailto at text-4xl would be affectation here.
- **Rounded corners, generous air** around images; a dotted carousel for the food
  gallery. Both patterns the editorial registers reject, both right here.
- **No grain, no apparatus, no colophon, no ledger.** The menu is a menu.
- **Warm serif display at conversational size** over a plain sans body. The
  headline welcomes rather than announces.
- **Dark navy footer** as the tonal inversion — the one structural invariant it
  keeps unchanged.

## How to use this file

**Pick the register from the business first**, then match that register's
inventory plus the structural section — never the pixels, and never another
register's apparatus. A new build shares the structure (one display-scale accent,
hierarchy through scale, hairlines, stagger, weighted columns, one set-piece)
while its palette, faces, apparatus policy and world are its own.

If a section is about to become a card grid, a rounded gradient pill, or three
same-rhythm text blocks, this file is the list of what to do instead. If a page is
about to receive its eighth 10px mono caption, the answer is in the apparatus
budget in SKILL.md, not here.
