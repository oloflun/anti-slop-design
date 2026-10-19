---
title: "Anima"
url: https://www.anima.ai/
source_url: https://www.anima.ai/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: ""
family: bio-render-venture-studio
dna: "Nature-inspired venture studio x surreal bio renders and soft gradients"
register: modern clean
grammar: chaptered editorial
lane: "A venture studio page on soft grey-green gradients with surreal nature renders (a mossy bark fragment, a purple anemone, flowering branches) drifting across thin light sans statements, a 3D-tilted venture card, and a 'Have a seat' marquee close."
mode: persuade
traits: ["surreal nature 3D renders", "soft grey/lime/lilac gradients", "thin light sans statements", "grey-to-ink line fill", "tinted team portraits", "marquee close"]
palette: ["#FFFFFF", "#AAB2B4", "#7D777E", "#D1D6D2"]
type: ["Helvetica Neue", "Martian Mono", "Parabole"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Nature-inspired science is visualised with strange, beautiful specimens (bark, anemone, blossoms) that float through an otherwise minimal, airy layout. The gradients shift colour by section like light in a greenhouse.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Beaucoup).

## What to borrow (principle)

- Float one surreal natural specimen per chapter through a minimal layout
- Shift a soft gradient ground by section

## What to leave

- Very light text on light gradients
- Long blank opening frames

## Signature move

Surreal nature specimens (bark, anemone, blossom) drifting through airy gradients.

## Motion

Intro: pale grey for ~2.5 s, then the bark render drifts in over 'Growing nature-inspired companies'. Scroll (Lenis, ~55–140 px glide, Taxi): bark slides away; statements fill grey to ink; partner text; 'Who we work with' cards; venture card tilts in 3D; anemone rolls in for 'Out of the Lab'; tinted team portraits; blossom branches; testimonial; 'Have a seat' marquee.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; 2 video; smoothed scroll (median 100 px still travelling after input stops); entry gate: REFUSE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a venture studio page on soft grey-green gradients with surreal nature renders (a mossy bark fragment, a purple anemone, flowering branches) drifting across thin light sans statements, a 3D-tilted venture card, and a 'Have a seat' marquee close. Type: Helvetica Neue, Martian Mono, Parabole.
Ground and ink from the measured palette (#FFFFFF, #AAB2B4, #7D777E). Motion carries the page through
surreal nature specimens (bark, anemone, blossom) drifting through airy gradients. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — surreal 3D botanical and mineral specimens on soft gradients

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: surreal 3D botanical and mineral specimens on soft gradients

## Reference lock

Primary reference/direction: Anima — A venture studio page on soft grey-green gradients with surreal nature renders (a mossy bark fragment, a purple anemone, flowering branches) drifting across thin light sans statements, a 3D-tilted venture card, and a 'Have a seat' marquee close.
Preserve (3-5 traits): surreal nature 3D renders; soft grey/lime/lilac gradients; thin light sans statements; grey-to-ink line fill; tinted team portraits.
Borrow only (1-2): Float one surreal natural specimen per chapter through a minimal layout; Shift a soft gradient ground by section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: surreal 3D botanical and mineral specimens on soft gradients
Reject: Very light text on light gradients; Long blank opening frames
Token commitments: palette #FFFFFF, #AAB2B4, #7D777E, #D1D6D2; type Helvetica Neue, Martian Mono, Parabole; engine GSAP + Lenis linked (never vendored).
