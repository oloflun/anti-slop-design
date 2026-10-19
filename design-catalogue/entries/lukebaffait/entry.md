---
title: "Luke Baffait"
url: https://www.lukebaffait.fr/
source_url: https://www.lukebaffait.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: red-glow-statue-dev-folio
dna: "Creative developer folio x red glow and marble statue"
register: cinematic dark
grammar: chaptered editorial
lane: "A dark folio whose name types in sans and italic serif, flashes on red, then glows over a red smoke, a marble statue image grows between the name's words, a red ribbon swings behind the project list, and project images float around a centred line."
mode: persuade
traits: ["name in sans + italic serif", "red flash and red smoke glow", "marble statue photo growing between words", "red ribbon curve behind the list", "floating project screens around a statement", "skills accordion"]
palette: ["#0A0A0A", "#A32D25", "#521819", "#C5C6C6", "#965F52"]
type: ["Inter", "Breton", "other", "Zirena"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The name is split into two typefaces and the gap between them is where the first image (a classical statue) grows, so the identity line literally opens onto the work. A red ribbon then sweeps behind the project list as the one gestural element.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Luke Baffait).

## What to borrow (principle)

- Grow an image inside the gap of a split wordmark
- A single red ribbon curve sweeping behind a list
- Float project screens around a centred sentence

## What to leave

- Dark text-light sections are sparse
- Contact panel switch to white is abrupt

## Signature move

A marble statue image growing in the gap between 'Luke' and 'Baffait.'

## Motion

Intro: 'Luke Baffait.' types with the serif part italic (~1 s), flashes on red, then settles over a red smoke glow. Scroll (Lenis, ~150 px glide, 49 ScrollTriggers, 1 pin, SplitText, WebGL): a statue image opens between the words and grows to full; about block with portrait; project list where a red ribbon swings behind and the active name lights; project screens float around 'Each project is a chance…'; skills accordion; awards table; white contact panel; name footer.

Measured (`motion/probe.json`): GSAP 3.12.5; 49 ScrollTriggers; 1 pinned sections; Lenis; WebGL canvas x1; split text; smoothed scroll (median 207 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a dark folio whose name types in sans and italic serif, flashes on red, then glows over a red smoke, a marble statue image grows between the name's words, a red ribbon swings behind the project list, and project images float around a centred line. Type: Inter, Breton, other, Zirena.
Ground and ink from the measured palette (#0A0A0A, #A32D25, #521819). Motion carries the page through
a marble statue image growing in the gap between 'Luke' and 'Baffait.' Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black-and-white classical sculpture, red atmospheric glow, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black-and-white classical sculpture, red atmospheric glow, device mockups

## Reference lock

Primary reference/direction: Luke Baffait — A dark folio whose name types in sans and italic serif, flashes on red, then glows over a red smoke, a marble statue image grows between the name's words, a red ribbon swings behind the project list, and project images float around a centred line.
Preserve (3-5 traits): name in sans + italic serif; red flash and red smoke glow; marble statue photo growing between words; red ribbon curve behind the list; floating project screens around a statement.
Borrow only (1-2): Grow an image inside the gap of a split wordmark; A single red ribbon curve sweeping behind a list
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black-and-white classical sculpture, red atmospheric glow, device mockups
Reject: Dark text-light sections are sparse; Contact panel switch to white is abrupt
Token commitments: palette #0A0A0A, #A32D25, #521819, #C5C6C6, #965F52; type Inter, Breton, other, Zirena; engine GSAP + Lenis linked (never vendored).
