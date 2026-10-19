---
title: "Manish Kumar"
url: https://manishkr.xyz/
source_url: https://manishkr.xyz/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blue-dither-field-notebook
dna: "Design engineer and photographer x blue dot-dither notebook"
register: editorial print
grammar: chaptered editorial
lane: "A cream notebook folio where a blue dot field dissolves the screen between chapters, the bio highlights its keywords in blue chips word by word, photographs scatter as loose prints, and cyanotype cards fan out of a dithered circle."
mode: persuade
traits: ["blue dot-dither field as the transition", "keyword highlight chips in a running bio", "scattered photo prints with captions", "cyanotype card fan", "small serif greeting with a bird mark", "folder props for projects"]
palette: ["#FDFBF7", "#BECAEC", "#97A0C1"]
type: ["Geist", "Gambarino", "Lay Grotesk", "Instrument Serif"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One blue and one cream carry everything, and the transition between chapters is a field of blue dots that fills the screen and then resolves into the next thing (a camera, a bird, a circle). The bio is a sentence where each skill is highlighted in turn, so reading it is the motion.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Use a dither/dot field as the transition that forms the next object out of noise
- Highlight the keywords of a running sentence one by one as the reader passes
- Scatter photographs as loose prints at different depths instead of a grid

## What to leave

- 'enter with sound' gate
- Many small motifs (bird, camera, folders) compete for identity

## Signature move

A blue dot field that floods the screen and resolves into the next chapter's object.

## Motion

Gate: 'welcome to my little corner of the internet' with a bird mark and 'enter with sound'. Then the screen fills with blue dots (~0.5 s) that cluster into a camera shape. Scroll (Lenis, 1 pin, SplitText): the bio sets in and its keywords get blue chips word by word; a bird made of dots drifts across; photographs drop in as scattered prints with captions; cyanotype cards fan out inside a dithered ring; project folders open with labels orbiting; closing ring with 'Design / Engineer'.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 pinned sections; Lenis; 3 video; smoothed scroll (median 136 px still travelling after input stops); entry gate: enter with sound. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a cream notebook folio where a blue dot field dissolves the screen between chapters, the bio highlights its keywords in blue chips word by word, photographs scatter as loose prints, and cyanotype cards fan out of a dithered circle. Type: Geist, Gambarino, Lay Grotesk, Instrument Serif.
Ground and ink from the measured palette (#FDFBF7, #BECAEC, #97A0C1). Motion carries the page through
a blue dot field that floods the screen and resolves into the next chapter's object. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film photography of landscapes and animals, plus cyanotype prints

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film photography of landscapes and animals, plus cyanotype prints

## Reference lock

Primary reference/direction: Manish Kumar — A cream notebook folio where a blue dot field dissolves the screen between chapters, the bio highlights its keywords in blue chips word by word, photographs scatter as loose prints, and cyanotype cards fan out of a dithered circle.
Preserve (3-5 traits): blue dot-dither field as the transition; keyword highlight chips in a running bio; scattered photo prints with captions; cyanotype card fan; small serif greeting with a bird mark.
Borrow only (1-2): Use a dither/dot field as the transition that forms the next object out of noise; Highlight the keywords of a running sentence one by one as the reader passes
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film photography of landscapes and animals, plus cyanotype prints
Reject: 'enter with sound' gate; Many small motifs (bird, camera, folders) compete for identity
Token commitments: palette #FDFBF7, #BECAEC, #97A0C1; type Geist, Gambarino, Lay Grotesk, Instrument Serif; engine GSAP + Lenis linked (never vendored).
