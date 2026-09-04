---
title: "Creative Giants"
url: https://creativegiants.art
source_url: https://creativegiants.art
captured: 2026-09-04
origin: refero
extract: ok
category: portfolio
category2: editorial
family: weight-300-poster-studio
dna: "Art-book poster typography x rationed saturated accent cards"
register: editorial print
grammar: typographic poster
lane: "A warm off-white canvas opens on a single weight-300 headline set at poster scale, drops straight into a full-bleed documentary photograph, then runs a sequence of whitespace-led editorial sections where colour appears only as single accent cards, never as background"
mode: portfolio
traits: ["84px weight-300 display, -0.04em tracking", "1440px pill on interactive only, 0px on editorial", "bone-white canvas, never pure white", "chromatic accents rationed to single-card hits", "full-bleed sharp-cornered photography", "near-invisible chrome — logo + one Menu pill"]
palette: ["#fffef7", "#000000", "#666666", "#8a0467", "#03624c", "#ffd001"]
type: ["Switzer"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Creative Giants.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. A single family, Switzer, carries the entire system on exactly two
weights: 300 for every display and headline size from 12px to 84px, 400 for body
and UI. Using weight 300 at poster scale is the anti-convention choice the source
calls out explicitly — most systems would bold up at 64-84px, but the light weight
keeps the hairline strokes intact, so the type reads as airbrushed onto the cream
canvas rather than shouted. Letter-spacing tightens as size grows (-0.04em at 84px
down to -0.018em at 14px), which is what keeps those large light strokes from
reading as merely thin — they lock together instead of drifting apart.

Colour is treated as a rationed resource in an unusually literal way: eleven named
hues exist in the token set, but the rule governing them is "never flood a
section" — chromatic colour appears only as a single accent card in a grid, a
border on an image edge, or a rare inverted dark field, and "never more than one
[accent card] in a row." That discipline is what keeps eleven possible hues from
reading as a messy palette; at any given moment the page is showing at most one of
them.

Interactive and editorial geometry are kept strictly separate: 1440px pill radius
belongs only to buttons, tags and the Menu control; cards and images stay
perfectly square at 0px. Combined with a shadow system that amounts to a single
1px inner ring (not a drop shadow), the page has no elevation at all — separation
comes purely from whitespace, the rare inverted field, and full-bleed photography
that is always allowed to be the loudest thing on screen.

## What to borrow (principle)

- **Use a light weight at poster scale on purpose.** Weight 300 at 64-84px reads
  as considered restraint precisely because most systems reach for 700+ at that
  size — the whisper is the signal.
- **Tighten tracking as size grows, don't just enlarge.** Progressive negative
  letter-spacing keeps oversized light type from looking merely stretched.
- **Ration a large colour set to one hit at a time.** "Never more than one accent
  card in a row" turns a big palette into a controllable, auditable rule instead
  of a free-for-all.
- **Split radius by function, not by whim.** One radius value for every
  interactive control, zero for every editorial surface (cards, images) — no
  values in between.
- **Let a single 1px ring stand in for all elevation.** A near-invisible highlight
  ring, used once, communicates "this is different" without the weight of a
  drop shadow.

## What to leave

- Weight-300 display type at 84px is a high-fidelity requirement: it needs a
  genuine light cut of the chosen face, rendered crisply, or it will look broken
  rather than airbrushed on lower-quality screens or fallback fonts.
- Reserving eleven distinct accent colours for single-card use only demands real
  editorial discipline in a CMS-driven site; without an enforced limit, "one at a
  time" tends to erode under content-team pressure.
- Zero elevation and near-invisible chrome (one logo mark, one Menu pill) puts
  the entire wayfinding burden on photography and whitespace — this will not
  translate to a content-dense product or dashboard context.

## Signature move

The oversized poster headline sitting directly on the cream canvas with a subtle
vertical charcoal-to-black gradient inside the cream-coloured letterforms — a
sculptural, chiseled treatment rather than flat-printed type, occupying roughly
40% of the viewport before any photograph appears.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked.
Three easing families are in play at three short durations (200/300/550ms): a
plain `ease` for simple state changes, a sharp custom accelerate-decelerate family
(`cubic-bezier(0.65, 0.05, 0, 1)`, `cubic-bezier(0.625, 0.05, 0, 1)`) for snappier
panel/background transitions, and plain `linear` for continuous motion. The one
keyframe confirmed firing is `marquee_timeline`, a slide-x transform driving a
horizontal ticker — likely the "latest news"/timeline strip rather than a
decorative band. A `spin` keyframe exists in the stylesheet but isn't confirmed
in use. (observed in capture) the gradient-lettered headline resolves as a static
graphic on load with no animated reveal, and scroll transitions between the
image-led sections read as simple cuts rather than parallax or scroll-scrub
effects — consistent with the source's insistence that "the system has no
meaningful elevation" and that whitespace, not motion, is the primary structural
tool.

| Token | Value | Easing |
|---|---|---|
| sm | 200ms | `ease` |
| md | 300ms | `ease` |
| lg | 550ms | `cubic-bezier(0.65, 0.05, 0, 1)` |
| marquee_timeline | — | slide-x transform, 1 use |

## Brief

Build a design-studio portfolio homepage. Canvas is bone white `#fffef7`
everywhere — never pure white. Open on a single Switzer weight-300 headline at
64-84px, letter-spacing tightening to -0.04em, occupying about 40% of the
viewport, optionally with a vertical charcoal-to-black gradient inside the
lettering. Drop immediately into a full-bleed, sharp-cornered documentary
photograph with bottom-left meta text and a 34px weight-300 statement headline
overlaid. Below, run monolithic sections — a small all-caps eyebrow, a 34-54px
weight-300 statement, 48-64px of whitespace before and after, no rules or
dividers. Use a 3-column card grid for project/news items: square sharp-cornered
images, 18-20px weight-300 titles, 14px graphite body copy, no card border, no
shadow. Let exactly one card per row swap to a saturated or pastel accent surface
(never more than one at a time). Every button, tag and the single Menu control
gets a 1440px pill radius; every card and image stays at 0px. No drop shadows
anywhere — the one permitted shadow is a 1px white inner ring on dark elements.

## Image recipe

Documentary editorial photograph of [SUBJECT] — full-bleed, sharp-cornered, no
overlay or rounded mask, atmospheric and candid rather than staged, natural
available light, human subjects or public installations in real environments,
no product mockups, no illustration, no studio backdrop.

## Photo search

Unsplash first, Pexels second.
- "public art installation outdoor documentary"
- "creative studio team candid documentary"
- "event production behind the scenes photography"
- "urban architecture wide shot natural light"

## Reference lock

Primary reference/direction: Creative Giants — weight-300 poster-scale editorial
studio site, colour rationed to single accent cards, near-invisible chrome.
Preserve (3-5 traits): bone-white `#fffef7` canvas, never pure white; Switzer
weight 300 for every display/headline size, weight 400 only for body and UI, never
bolder; progressive negative tracking as size grows (-0.04em at 84px); 1440px
pill radius on interactive elements only, 0px on every card and image; chromatic
accents limited to a single card or border hit at a time, never a flooded section.
Borrow only (1-2): the charcoal-to-black gradient treatment inside display
lettering; the single 1px white inner-ring "shadow" on dark elements.
Role rules: headlines never exceed two lines or bold past 300; no chromatic CTA
fill — all interactive surfaces stay black or transparent; body text always
left-aligned except the centred hero headline.
Media strategy: photo:unsplash — full-bleed, sharp-cornered documentary and
atmospheric photography only; no illustration, no 3D, no product mockups.
Reject: bold headlines; pure white canvas; rounded corners on cards or images;
any drop shadow; a chromatic CTA background; two accent-coloured cards in the
same row; browser-default link blue.
Token commitments: bg `#fffef7`, ink `#000000`, graphite `#666666`, ash `#aaaaaa`,
accents `#8a0467`/`#03624c`/`#a5c8eb`/`#ffacea`/`#a5ebd6`/`#101731`/`#ffd001`;
display weight 300 at 64-84px/leading 1.0/-0.04em to -0.027em tracking; radius
1440px interactive, 0px editorial; base spacing unit 8px, section gap 64px.
