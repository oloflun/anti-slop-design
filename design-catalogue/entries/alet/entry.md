---
title: "ALET Agency"
url: https://aletagency.com/
source_url: https://aletagency.com/
captured: 2026-09-04
origin: refero
extract: ok
category: portfolio
category2: editorial
family: taupe-contact-sheet
dna: "Whisper-small caption typography x a scattered contact-sheet image field"
register: editorial print
grammar: gallery/catalog
lane: "A single warm taupe surface holds the entire site with no section ever changing colour, while an asymmetric, irregularly-offset field of editorial photography scatters across it like a contact sheet, ringed by floating uppercase category captions and a widely-tracked serif masthead"
mode: persuade
traits: ["11-13px UI text, never scaled up for 'primary'", "one monolithic taupe surface, no section changes", "0px image radius, 9999px pill exclusively for the toggle", "wordmark at 0.5-0.8em tracking, letters detached", "scattered irregular-offset image field, no grid", "zero accent colour, photography is the only chroma"]
palette: ["#ada59b", "#000000", "#252525", "#101010", "#454545"]
type: ["SilkSerif", "WorkSans"]
measured: designlang
kind: reference-style
source: anton
status: ready
refero: processed/alet.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the
live capture. Taupe paper `#ada59b` is not a "canvas colour" in the usual
sense — it is the entire site: the source states no section ever changes
background, so there is no light/dark alternation, no card surface, nothing
but one monolithic warm gray that every element floats on directly. Because
white, off-white and near-black are all explicitly forbidden as backgrounds,
photography becomes the only source of colour or contrast variation on the
whole page.

Typography stays deliberately tiny across every functional role — 11-13px
WorkSans for navigation, labels, and body, with an explicit rule against ever
scaling up "for a primary label." That restraint is what makes the one
exception, the SilkSerif wordmark at 23px with letter-spacing opened to
0.5-0.8em, read as a masthead rather than a logo: the letters are so widely
tracked they nearly detach from each other, and because nothing else on the
page is set in serif, that single word instantly reads as the title plate of
a magazine.

The image field is the structural centrepiece: photographs are placed with
irregular margin offsets (101-209px) rather than on a grid, so the layout
reads as a scattered contact sheet, not a portfolio grid. A working
LINEAR/RANDOM toggle — the only rounded (9999px) element in the entire
system — lets a viewer switch between an ordered and a scattered arrangement
of the same images, making the "contact sheet" metaphor an actual, operable
feature rather than just a visual style. Note: the designlang extract flags a
red `#dc3545` (31 uses, Bootstrap's default "danger" hue) not present in the
captured screenshot or documented anywhere in the source — most plausibly an
incidental form-validation or "sold out"-style state colour triggered during
the crawl rather than a deliberate brand accent, so it is not added to the
palette above; the exact taupe hex also reads slightly differently live
(`#e5ddc4`, `#a2a093`) than in the captured tokens, consistent with warm-gray
sampling variance rather than a different brand colour.

## What to borrow (principle)

- **Make the canvas a single, unchanging surface across the entire site.**
  Refusing section-to-section colour changes forces every other design
  decision (spacing, scatter, photography) to carry the visual rhythm
  instead.
- **Cap UI text size with an explicit rule, not just a habit.** "Never scale
  up for a primary label" keeps a whisper-small system from eroding under
  the pressure to make one thing "important."
- **Reserve the one rounded shape for exactly one interactive feature.**
  A 9999px pill appearing only on a working layout toggle — nowhere else —
  makes that single curve meaningful rather than decorative.
- **Offer a genuinely operable metaphor, not just a visual one.** A real
  LINEAR/RANDOM toggle that rearranges the same photographs turns "contact
  sheet" from a style reference into an interactive feature.
- **Open tracking on a masthead word until letters nearly detach.** Extreme
  positive letter-spacing (0.5-0.8em) on a short serif word is what makes a
  wordmark read as a printed title rather than a typed logo.

## What to leave

- A monolithic single-colour canvas with zero section variation is a
  demanding constraint — any content type that needs visual separation (a
  pricing table, a form) has no built-in surface-shift tool to reach for.
- Irregular image offsets (101-209px, scattered) require genuine art
  direction per breakpoint; a naive responsive collapse would either overlap
  badly or lose the contact-sheet read entirely.
- Zero accent colour anywhere means the system offers no built-in way to
  signal state (hover beyond a colour swap to pure ink, active, error)
  without inventing a convention from scratch.

## Signature move

The LINEAR/RANDOM layout toggle: a stroke-only pill switch that rearranges
the same scattered photographs between an ordered and a randomized
composition — the only rounded, only interactive-feeling component on the
entire site, and the one place the "contact sheet" concept becomes literally
operable.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked.
Four durations are confirmed — 200ms, 300ms, 1s and a notably slow 2s — though
no easing curve is confidently identified (no dominant named family
registers). That wide spread, especially the 2s outlier, fits a genuinely
deliberate grid-rearrange animation: images repositioning across the scattered
field when the LINEAR/RANDOM toggle fires would plausibly need a slower,
choreographed duration rather than a snap cut. No keyframes are confirmed
firing. (observed in capture) the live capture confirms the scattered,
irregularly-offset image field and the LINEAR/RANDOM toggle are present and
match the described layout.

| Token | Value | Easing |
|---|---|---|
| sm | 200ms | — |
| md | 300ms | — |
| xl | 1s | — |
| xxl (toggle rearrange) | 2s | — |

## Brief

Build a Copenhagen-style creative-studio portfolio with a single unchanging
canvas. Set the entire page on warm taupe `#ada59b` — no section, card, or
component ever uses a different background; white, off-white and near-black
are all forbidden as surfaces. Cap all UI text (nav, labels, body, metadata)
at 11-13px WorkSans Regular — never scale up for emphasis. Set the studio
name in a light serif at 23px with letter-spacing opened to 0.5-0.8em, tight
0.94 leading, centred in the top bar as the only serif moment on the site.
Arrange 6-8 photographs in an asymmetric scattered field with irregular
margin offsets (roughly 100-210px), each at 0px radius with no border or
shadow, ringed by floating uppercase category labels positioned at irregular
coordinates (top-left, top-centre, top-right, bottom-left, bottom-centre,
bottom-right). Add a working LINEAR/RANDOM toggle — a stroke-only 9999px
pill with a small circular thumb, the only rounded element anywhere — that
rearranges the image field between ordered and scattered layouts. Centre a
single studio-statement paragraph below at 13px with generous (180px) top
padding. No accent colour, no shadows, no elevation anywhere.

## Image recipe

Editorial documentary photograph of [SUBJECT] — packaging, interior, product-
on-table or portrait-detail shots at high resolution, warm and slightly
desaturated, lit naturally rather than in a studio, cropped tight at varying
aspect ratios (1:1, 4:5, 3:2) so the collection reads as a contact sheet
rather than a uniform grid.

## Photo search

Unsplash first, Pexels second.
- "editorial product photography warm natural light"
- "interior photography natural light desaturated"
- "packaging design close up studio"
- "portrait detail natural light editorial"

## Reference lock

Primary reference/direction: ALET Agency — single-surface taupe portfolio,
scattered contact-sheet image field, whisper-small caption typography.
Preserve (3-5 traits): warm taupe `#ada59b` as the entire site's only
background, never white/off-white/near-black; all UI text capped at 11-13px
WorkSans, no scaling up for emphasis; the SilkSerif masthead at 23px with
0.5-0.8em tracking as the only serif moment; photographs at irregular
scattered offsets (not gridded), 0px radius, no border or shadow; 9999px
radius reserved exclusively for the LINEAR/RANDOM toggle.
Borrow only (1-2): the working LINEAR/RANDOM layout toggle that rearranges
the same image set; the floating category-label positioning around the
image field.
Role rules: no chromatic accent is ever introduced; the wordmark's letter-
spacing formula (0.5-0.8em) never applies to body or nav text; body text
never centres except the single studio-statement block.
Media strategy: photo:unsplash — warm, naturally-lit editorial documentary
photography at varying tight crops; no illustration, no icons beyond fine
line-art strokes.
Reject: any second background colour; box-shadow or gradient; radius above
0px outside the toggle and rare small inset frames; a display weight above
Light/Regular; a centred multi-column body layout.
Token commitments: bg `#ada59b`, ink `#000000`, nav-text `#252525`,
secondary `#101010`, inset `#454545`; wordmark SilkSerif 300 at 23px/leading
0.94/0.5-0.8em tracking; body WorkSans 400 at 11-13px/leading 1.0-1.5;
radius 0px images, 9999px toggle only, 10.8px rare small frames; section gap
101-180px, base spacing unit 6px.
