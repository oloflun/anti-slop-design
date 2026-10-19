---
title: "Locomotive Scroll v5"
url: https://scroll.locomotive.ca/
source_url: https://scroll.locomotive.ca/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: cobalt-library-docs-poster
dna: "Scroll library x cobalt blue, white grotesk and thin serif, flat geometric shapes that demonstrate each feature"
register: other
grammar: typographic poster
lane: "A library homepage: cobalt ground, 'Locomotive Scroll' wordmark, a marquee of 'Version (5.0)', a white panel 'Version 5 is a complete rewrite', the wordmark repeated in a cascade of outline copies, 'Built-in Tools' in a thin serif, then each feature (in-view detection, progress tracking, parallax) demonstrated by flat black, white and coral shapes (rings, sunbursts, pills) behaving as the feature describes, a black features grid, 'Showcase' in a giant serif running off both edges, and 'We hope you enjoy our library'."
mode: persuade
traits: ["cobalt ground", "flat geometric demo shapes", "outline wordmark cascade", "thin serif display against grotesk", "giant word running off the edges", "black features grid"]
palette: ["#1F2DEC", "#FFFFFF", "#B7BAEC", "#4549DE", "#121B98"]
type: ["Helvetica Now Display", "PP Locomotive New"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The shapes perform the very feature they describe, so the library demonstrates itself instead of listing what it can do.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Locomotive).

## What to borrow (principle)

- Let the demo shapes perform the feature being described

## What to leave

- Tiny grid copy on black

## Signature move

Flat coral and black rings and sunbursts demonstrating parallax on cobalt.

## Motion

Intro: wordmark draws (~1 s). Wheel (Locomotive/Lenis): marquee runs; outline copies cascade with offset; shapes rotate, scale and track progress; the giant word scrolls horizontally.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; smoothed scroll (median 154 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the typographic poster grammar: a library homepage: cobalt ground, 'Locomotive Scroll' wordmark, a marquee of 'Version (5.0)', a white panel 'Version 5 is a complete rewrite', the wordmark repeated in a cascade of outline copies, 'Built-in Tools' in a thin serif, then each feature (in-view detection, progress tracking, parallax) demonstrated by flat black, white and coral shapes (rings, sunbursts, pills) behaving as the feature describes, a black features grid, 'Showcase' in a giant serif running off both edges, and 'We hope you enjoy our library'. Type: Helvetica Now Display, PP Locomotive New.
Ground and ink from the measured palette (#1F2DEC, #FFFFFF, #B7BAEC). Motion carries the page through
flat coral and black rings and sunbursts demonstrating parallax on cobalt. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat vector shapes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat vector shapes

## Reference lock

Primary reference/direction: Locomotive Scroll v5 — A library homepage: cobalt ground, 'Locomotive Scroll' wordmark, a marquee of 'Version (5.0)', a white panel 'Version 5 is a complete rewrite', the wordmark repeated in a cascade of outline copies, 'Built-in Tools' in a thin serif, then each feature (in-view detection, progress tracking, parallax) demonstrated by flat black, white and coral shapes (rings, sunbursts, pills) behaving as the feature describes, a black features grid, 'Showcase' in a giant serif running off both edges, and 'We hope you enjoy our library'.
Preserve (3-5 traits): cobalt ground; flat geometric demo shapes; outline wordmark cascade; thin serif display against grotesk; giant word running off the edges.
Borrow only (1-2): Let the demo shapes perform the feature being described
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat vector shapes
Reject: Tiny grid copy on black
Token commitments: palette #1F2DEC, #FFFFFF, #B7BAEC, #4549DE, #121B98; type Helvetica Now Display, PP Locomotive New; engine GSAP + Lenis linked (never vendored).
