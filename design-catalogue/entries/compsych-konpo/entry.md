---
title: "ComPsych - design guidelines (Konpo)"
url: https://compsych.konpo.co/
source_url: https://compsych.konpo.co/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "institutional"
family: gradient-brand-guidelines
dna: "Brand guidelines site x soft colour gradients that change per chapter, a serif wordmark and portrait cards"
register: modern clean
grammar: chaptered editorial
lane: "An online brand guideline: a navy loader, 'ComPsych' in a large serif with 'Design Guidelines' in script on pale blue, a face portrait card with 'Brand Model & Story' as the ground warms to yellow, Why/How/What/Who cards revealing in a row, 'Tone of Voice' on a green gradient with a 'Redefining workplace support' photo card, 'Logo' on blue with the mark drawn in outline, and a tote bag photo."
mode: read
traits: ["per-chapter colour gradients", "large serif wordmark with script", "portrait cards", "outlined logo construction", "card row revealing"]
palette: ["#3E303F", "#D9EBFC", "#FCF2DA", "#FFF693", "#9E9694"]
type: ["Beatrice", "Bright Clones", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The ground's colour drifting per chapter tells you where you are in a long guideline without a menu.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Konpo).

## What to borrow (principle)

- Shift the ground gradient per chapter as wayfinding

## What to leave

- Very pale card text

## Signature move

The ground drifting from blue to yellow to green as chapters change.

## Motion

Intro: navy (~2 s). Wheel (Lenis): gradients interpolate; cards scale; the logo outline draws.

Measured (`motion/probe.json`): GSAP 3.12.5; 39 ScrollTriggers; Barba page transitions; WebGL canvas x1 (three.js); 3 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an online brand guideline: a navy loader, 'ComPsych' in a large serif with 'Design Guidelines' in script on pale blue, a face portrait card with 'Brand Model & Story' as the ground warms to yellow, Why/How/What/Who cards revealing in a row, 'Tone of Voice' on a green gradient with a 'Redefining workplace support' photo card, 'Logo' on blue with the mark drawn in outline, and a tote bag photo. Type: Beatrice, Bright Clones, Inter.
Ground and ink from the measured palette (#3E303F, #D9EBFC, #FCF2DA). Motion carries the page through
the ground drifting from blue to yellow to green as chapters change. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait photography

## Reference lock

Primary reference/direction: ComPsych - design guidelines (Konpo) — An online brand guideline: a navy loader, 'ComPsych' in a large serif with 'Design Guidelines' in script on pale blue, a face portrait card with 'Brand Model & Story' as the ground warms to yellow, Why/How/What/Who cards revealing in a row, 'Tone of Voice' on a green gradient with a 'Redefining workplace support' photo card, 'Logo' on blue with the mark drawn in outline, and a tote bag photo.
Preserve (3-5 traits): per-chapter colour gradients; large serif wordmark with script; portrait cards; outlined logo construction; card row revealing.
Borrow only (1-2): Shift the ground gradient per chapter as wayfinding
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait photography
Reject: Very pale card text
Token commitments: palette #3E303F, #D9EBFC, #FCF2DA, #FFF693, #9E9694; type Beatrice, Bright Clones, Inter; engine GSAP + Lenis linked (never vendored).
