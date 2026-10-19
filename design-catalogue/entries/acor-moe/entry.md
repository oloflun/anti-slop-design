---
title: "ACOR - Haroun Sadek, Maitre d'oeuvre and Architecture"
url: http://acor-moe.fr/
source_url: http://acor-moe.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: architect-horizontal-photo-run
dna: "Grenoble project manager x thin monogram and a long sideways project photo run"
register: warm photographic
grammar: gallery/catalog
lane: "An architect's site: a thin line monogram on black, a giant serif 'acor' cut by a circular window, a short tagline, then a long horizontal run of numbered interior and house photos (01-26) that slides sideways as you scroll down, and a plain contact block."
mode: read
traits: ["line monogram loader", "giant serif wordmark cut by a circle", "horizontal photo run", "numbered small captions", "white ground", "serif contact details"]
palette: ["#FFFFFF", "#0C0C0C", "#5E5854", "#B9B8B7", "#282525"]
type: ["Regola Pro", "Hatton"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The sideways run lets a large portfolio be browsed like contact sheets without leaving the page; the circular window in the wordmark is a neat first frame.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Jeremy Fagis, Thierry Chopain).

## What to borrow (principle)

- Turn vertical scroll into one long sideways photo run

## What to leave

- Grey placeholder tiles while loading
- Very small captions

## Signature move

A long sideways run of numbered interior photographs.

## Motion

Intro: black with the monogram drawn in line (~1.5 s), the giant wordmark appears with a circle cutting into it. Wheel (Lenis ~135 px glide): the black hero lifts; the photo run scrolls sideways with images at different sizes; numbers tick; the contact block rises and a last photo scales up.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; smoothed scroll (median 137 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the gallery/catalog grammar: an architect's site: a thin line monogram on black, a giant serif 'acor' cut by a circular window, a short tagline, then a long horizontal run of numbered interior and house photos (01-26) that slides sideways as you scroll down, and a plain contact block. Type: Regola Pro, Hatton.
Ground and ink from the measured palette (#FFFFFF, #0C0C0C, #5E5854). Motion carries the page through
a long sideways run of numbered interior photographs. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — interior and architectural photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: interior and architectural photography

## Reference lock

Primary reference/direction: ACOR - Haroun Sadek, Maitre d'oeuvre and Architecture — An architect's site: a thin line monogram on black, a giant serif 'acor' cut by a circular window, a short tagline, then a long horizontal run of numbered interior and house photos (01-26) that slides sideways as you scroll down, and a plain contact block.
Preserve (3-5 traits): line monogram loader; giant serif wordmark cut by a circle; horizontal photo run; numbered small captions; white ground.
Borrow only (1-2): Turn vertical scroll into one long sideways photo run
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: interior and architectural photography
Reject: Grey placeholder tiles while loading; Very small captions
Token commitments: palette #FFFFFF, #0C0C0C, #5E5854, #B9B8B7, #282525; type Regola Pro, Hatton; engine GSAP + Lenis linked (never vendored).
