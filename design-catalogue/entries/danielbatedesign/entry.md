---
title: "Daniel Rodrigues-Bate - Freelance Digital Designer"
url: http://danielbatedesign.com/
source_url: http://danielbatedesign.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: slash-monogram-designer-folio
dna: "Freelance digital designer x 'D//RB' monogram and wobbling words"
register: modern clean
grammar: chaptered editorial
lane: "A designer folio: 'D//RB' on white with a small project card, a full-bleed project image, 'Telling stories through design' in black with words that tilt and wobble, an about with portraits, service cards fanned in 3D over 'SERVICES', a white 'WORK' panel with project pairs, and a black ending where 'Ready to create maaaaagic?' letters scatter and reform."
mode: persuade
traits: ["slash monogram", "words that tilt and wobble on scroll", "3D fanned service cards", "black and white alternation", "projects in pairs", "scattering letters finale"]
palette: ["#000000", "#FFFFFF", "#B1AAA7", "#292929", "#8F8A89", "#5D5A5A"]
type: ["Geist", "Hvsmegs Style 2", "neuzeit-grotesk", "rama-gothic-m"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The wobbling words and the stretched 'maaaagic' give a clean folio a playful voice; the fanned service cards are a good one-frame summary.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fan service cards in 3D over the section title
- Stretch a word letter by letter in the closing CTA

## What to leave

- Long black gaps
- Small project captions

## Signature move

'Ready to create maaaaagic?' with letters scattering across black.

## Motion

Intro: white with the monogram; a project card slides up (~1 s). Wheel (Lenis ~150 px glide, 3 pins, 57 triggers): the image scales to full bleed; the black panel rises and the words tilt as they move; portraits drift; service cards fan out over the title; the white WORK panel rises; letters of the closing line fly in from scattered positions and stretch.

Measured (`motion/probe.json`): GSAP 3.15.0/3.12.5; 57 ScrollTriggers; 3 pinned sections; Lenis; 7 video; split text; smoothed scroll (median 148 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a designer folio: 'D//RB' on white with a small project card, a full-bleed project image, 'Telling stories through design' in black with words that tilt and wobble, an about with portraits, service cards fanned in 3D over 'SERVICES', a white 'WORK' panel with project pairs, and a black ending where 'Ready to create maaaaagic?' letters scatter and reform. Type: Geist, Hvsmegs Style 2, neuzeit-grotesk, rama-gothic-m.
Ground and ink from the measured palette (#000000, #FFFFFF, #B1AAA7). Motion carries the page through
'Ready to create maaaaagic?' with letters scattering across black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand and product photography, portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand and product photography, portraits

## Reference lock

Primary reference/direction: Daniel Rodrigues-Bate - Freelance Digital Designer — A designer folio: 'D//RB' on white with a small project card, a full-bleed project image, 'Telling stories through design' in black with words that tilt and wobble, an about with portraits, service cards fanned in 3D over 'SERVICES', a white 'WORK' panel with project pairs, and a black ending where 'Ready to create maaaaagic?' letters scatter and reform.
Preserve (3-5 traits): slash monogram; words that tilt and wobble on scroll; 3D fanned service cards; black and white alternation; projects in pairs.
Borrow only (1-2): Fan service cards in 3D over the section title; Stretch a word letter by letter in the closing CTA
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand and product photography, portraits
Reject: Long black gaps; Small project captions
Token commitments: palette #000000, #FFFFFF, #B1AAA7, #292929, #8F8A89, #5D5A5A; type Geist, Hvsmegs Style 2, neuzeit-grotesk, rama-gothic-m; engine GSAP + Lenis linked (never vendored).
