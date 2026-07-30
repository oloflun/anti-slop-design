# House physics — the executed quality bar, with exact values

Extracted 2026-07-31 from the full source of the three reference-grade sites
(`~/anti-slop-design/sites/calyx.html`, `horai.html`, `hyperborea.html`) — the
pages every build is measured against. The compressed version lives in
SKILL.md § The craft floor; this file carries the per-site inventory. When in
doubt, read the site source itself: it is the spec, executed.

## Cross-site invariants

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
- **Stagger:** paired photo/text columns offset `md:mt-24` / `md:mt-44`;
  programme columns `md:mt-12` / `md:mt-24`. Never top-aligned.
- **Grain film:** fixed full-page feTurbulence data-URI
  (`baseFrequency 0.85, numOctaves 2`) with feColorMatrix tinted to the
  palette; `mix-blend-mode: multiply` opacity .42–.5 on light ground,
  `screen` opacity .35 on dark.
- **Shared reveal:** `.reveal { opacity:0; transform:translateY(28px);
  transition: 1.2–1.4s cubic-bezier(.16,1,.3,1) }`, one IntersectionObserver
  at threshold 0.1–0.12; `prefers-reduced-motion` neutralizes everything.
  Reveals fail toward visible (threshold 0 for tall elements, mount reveal,
  failsafe, noscript — see the reveal guards).
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

## How to use this file

Pick the register the lane calls for, then **match the invariants, not the
pixels** — a new build shares the physics (kicker, one display-scale accent,
ledgers, rails, stagger, grain, one set-piece) while its palette, faces, and
world are its own. If a section is about to become a card grid, a rounded
button row, or three same-rhythm text blocks, this file is the list of what to
do instead.
