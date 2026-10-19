---
title: "Dmitrii Dark"
url: https://ddark.dev/
source_url: https://ddark.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: halftone-bust-dev-folio
dna: "Creative developer CV x halftone print poster"
register: editorial print
grammar: typographic poster
lane: "A warm-grey poster folio that counts up to 100 with an orange sun on a horizon line, opens on a halftone bust under the sun, then slides a rounded 'Selected work' sheet up over the hero."
mode: persuade
traits: ["count-up preloader with sun-on-horizon mark", "halftone/ASCII dither portrait", "extended heavy grotesque (Dela Gothic) with mono body", "sheet that slides up over the hero", "word swap band 'DESIGN · CODE · MOTION'", "marquee strip"]
palette: ["#DFDED6", "#C8C5BD", "#7F6E65"]
type: ["Dela Gothic One-064d632ca0195ef3", "Space Mono-a47c08273a98fff3"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A restricted print kit (warm grey, ink, one orange, halftone) makes a developer folio look like a gig poster. Each section arrives as a physical sheet: the work list slides up over the hero with a rounded top edge and a shadow, and the dark band arrives the same way, so the page reads as stacked paper.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Dmitrii Dark).

## What to borrow (principle)

- Let the next section slide up over the previous as a sheet with a radius and shadow: a section change you can feel
- Use a halftone/dither treatment to give a portrait the same texture as the type
- Preloader that ends in the hero's own mark (the sun) so loading and landing are one shot

## What to leave

- Very small mono body text
- Project list hover previews are the only way to see work

## Signature move

A 'Selected work' sheet that slides up over the halftone hero like a page laid on a page.

## Motion

Intro: counter runs to ~100 beside an orange circle on a hairline; circle moves into place over the bust as the hero type lands (~2.5 s). Scroll (ScrollSmoother + Lenis on the list): the work sheet rises over the hero; project names reveal per line, a hover card follows the pointer; experience grid fades in; dark band pins while 'DESIGN · CODE · MOTION' switches which word is orange; a 'DDARK.DEV' marquee runs into the contact block.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; smoothed scroll (median 34 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the typographic poster grammar: a warm-grey poster folio that counts up to 100 with an orange sun on a horizon line, opens on a halftone bust under the sun, then slides a rounded 'Selected work' sheet up over the hero. Type: Dela Gothic One-064d632ca0195ef3, Space Mono-a47c08273a98fff3.
Ground and ink from the measured palette (#DFDED6, #C8C5BD, #7F6E65). Motion carries the page through
a 'Selected work' sheet that slides up over the halftone hero like a page laid on a page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — halftone or dither-processed portrait, one hot accent colour, paper ground

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: halftone or dither-processed portrait, one hot accent colour, paper ground

## Reference lock

Primary reference/direction: Dmitrii Dark — A warm-grey poster folio that counts up to 100 with an orange sun on a horizon line, opens on a halftone bust under the sun, then slides a rounded 'Selected work' sheet up over the hero.
Preserve (3-5 traits): count-up preloader with sun-on-horizon mark; halftone/ASCII dither portrait; extended heavy grotesque (Dela Gothic) with mono body; sheet that slides up over the hero; word swap band 'DESIGN · CODE · MOTION'.
Borrow only (1-2): Let the next section slide up over the previous as a sheet with a radius and shadow: a section change you can feel; Use a halftone/dither treatment to give a portrait the same texture as the type
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: halftone or dither-processed portrait, one hot accent colour, paper ground
Reject: Very small mono body text; Project list hover previews are the only way to see work
Token commitments: palette #DFDED6, #C8C5BD, #7F6E65; type Dela Gothic One-064d632ca0195ef3, Space Mono-a47c08273a98fff3; engine GSAP + Lenis linked (never vendored).
