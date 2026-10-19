---
title: "Davide Cattaneo"
url: https://davidecattaneo.it/
source_url: https://davidecattaneo.it/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "portfolio"
family: green-wireframe-data-consultant
dna: "Data-automation consultant x green wireframe terminal"
register: cinematic dark
grammar: chaptered editorial
lane: "A near-black consultant page with one neon-green: a wireframe ribbon twists through the hero, data lines draw and converge to a single point, and sections hand over through a pixel-block dissolve."
mode: persuade
traits: ["single neon green on near-black", "3D wireframe ribbon hero", "drawn data lines converging to one node", "pixel-block dissolve transitions", "mono labels with green highlight chip", "light section for the case list"]
palette: ["#F1F1F1", "#070707", "#738474"]
type: ["neue-haas-grotesk-display", "basicallyAMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The subject (making messy data simple) is drawn: several green lines enter from the left, meet as labelled nodes, and converge to one point labelled 'Il tuo successo inizia Ora'. The palette is one green on black, so the converging line is the most visible thing on the page. Between chapters the screen breaks into white pixel blocks, a data-like transition instead of a fade.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Draw the argument: many lines converging to one point as the value proposition, scrubbed by scroll
- Hand over between sections with a blocky pixel dissolve that suits a technical subject
- One neon accent on black, used only for the thing that moves

## What to leave

- Tiny grey body text
- The light case-list section breaks the dark world briefly

## Signature move

Green data lines that draw in and converge on a single 'start now' node.

## Motion

Intro: logo mark builds from four petals at centre, then the wireframe ribbon twists in beside the headline (~2 s). Scroll (Lenis, ~150 px glide, 6 pins, three.js): white about text reveals per line with a black block cursor; pinned scene where green curves draw from the left with labelled nodes (strategy, analytics, consulenza) and converge; services cards with small animated graphs; a pixel-block dissolve to the light case list; active case row turns green; 'Make your business fly' under a large circle; footer marquee 'Lavora con me'. ScrambleText on labels.

Measured (`motion/probe.json`): GSAP 3.13.0; 6 pinned sections; Lenis; WebGL canvas x2 (three.js); 4 video; split text; smoothed scroll (median 125 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a near-black consultant page with one neon-green: a wireframe ribbon twists through the hero, data lines draw and converge to a single point, and sections hand over through a pixel-block dissolve. Type: neue-haas-grotesk-display, basicallyAMono.
Ground and ink from the measured palette (#F1F1F1, #070707, #738474). Motion carries the page through
green data lines that draw in and converge on a single 'start now' node. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — wireframe 3D forms and line graphics in one neon colour on near-black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: wireframe 3D forms and line graphics in one neon colour on near-black

## Reference lock

Primary reference/direction: Davide Cattaneo — A near-black consultant page with one neon-green: a wireframe ribbon twists through the hero, data lines draw and converge to a single point, and sections hand over through a pixel-block dissolve.
Preserve (3-5 traits): single neon green on near-black; 3D wireframe ribbon hero; drawn data lines converging to one node; pixel-block dissolve transitions; mono labels with green highlight chip.
Borrow only (1-2): Draw the argument: many lines converging to one point as the value proposition, scrubbed by scroll; Hand over between sections with a blocky pixel dissolve that suits a technical subject
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: wireframe 3D forms and line graphics in one neon colour on near-black
Reject: Tiny grey body text; The light case-list section breaks the dark world briefly
Token commitments: palette #F1F1F1, #070707, #738474; type neue-haas-grotesk-display, basicallyAMono; engine GSAP + Lenis linked (never vendored).
