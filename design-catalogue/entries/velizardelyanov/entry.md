---
title: "Velizar Delyanov - Web Developer"
url: https://www.velizardelyanov.com/
source_url: https://www.velizardelyanov.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: pixel-condensed-silk-folio
dna: "Web developer x pixel-condensed display over black and white silk"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer folio: a mono name loader, then a black and white liquid silk field with a giant blurred 'D' behind, the name in a pixelated condensed face, 'About me', 'My work' as a list of project names with a highlight bar, 'Awards*' with a blue asterisk and award cards scattered, and a footer."
mode: read
traits: ["liquid silk field", "pixel-condensed display face", "giant blurred initial", "project name list with highlight bar", "blue asterisk accent", "scattered award cards"]
palette: ["#282828", "#434343", "#686868", "#ABABAB", "#818181", "#E6E6E6"]
type: ["lochley", "geistmonoRegular", "ppneuemontreaBook"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The silk field and the giant blurred initial give the whole page one atmosphere; the pixel face keeps it from feeling generic.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A giant blurred initial behind the whole page

## What to leave

- Cookie bar in frames
- Award cards cluttered

## Signature move

A pixel-condensed name over black and white silk with a giant blurred 'D'.

## Motion

Intro: black with a mono name (~1.5 s). Wheel (Lenis ~110 px glide, 1 pin): the silk ripples; the name glitches out; 'About me' and 'My work' slide in; the highlight bar moves down the list; award cards float in.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; WebGL canvas x2 (three.js); split text; smoothed scroll (median 106 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer folio: a mono name loader, then a black and white liquid silk field with a giant blurred 'D' behind, the name in a pixelated condensed face, 'About me', 'My work' as a list of project names with a highlight bar, 'Awards*' with a blue asterisk and award cards scattered, and a footer. Type: lochley, geistmonoRegular, ppneuemontreaBook.
Ground and ink from the measured palette (#282828, #434343, #686868). Motion carries the page through
a pixel-condensed name over black and white silk with a giant blurred 'D'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL silk, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL silk, portrait

## Reference lock

Primary reference/direction: Velizar Delyanov - Web Developer — A developer folio: a mono name loader, then a black and white liquid silk field with a giant blurred 'D' behind, the name in a pixelated condensed face, 'About me', 'My work' as a list of project names with a highlight bar, 'Awards*' with a blue asterisk and award cards scattered, and a footer.
Preserve (3-5 traits): liquid silk field; pixel-condensed display face; giant blurred initial; project name list with highlight bar; blue asterisk accent.
Borrow only (1-2): A giant blurred initial behind the whole page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL silk, portrait
Reject: Cookie bar in frames; Award cards cluttered
Token commitments: palette #282828, #434343, #686868, #ABABAB, #818181, #E6E6E6; type lochley, geistmonoRegular, ppneuemontreaBook; engine GSAP + Lenis linked (never vendored).
