---
title: "Max Milkin - Creative Frontend Developer"
url: https://maxmilkin.com/
source_url: https://maxmilkin.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: scattered-letter-sage-folio
dna: "Creative frontend developer x letters swirling into a circle and a floating 3D rock"
register: modern clean
grammar: chaptered editorial
lane: "A developer folio on sage grey: letters of 'creative developer' swirl in a spiral and scatter into a ring, then a stone and mountain backdrop, a small signed manifesto, a dark section where letters rain into columns around a portrait as 'Fundamentals of web development' fills in, an awards list over a mountain silhouette and a dark project index around a floating 3D rock."
mode: read
traits: ["letters orbiting into a ring", "sage grey and near black", "letters raining into columns", "signature under a manifesto", "mountain silhouettes", "floating 3D rock in the project index"]
palette: ["#C3CABA", "#AAB1A2", "#949B8D"]
type: ["RF Dewi", "Bebas Neue"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Letters are the material of every transition: they spiral for the loader, rain around the portrait and spread for the headline, which makes typography the motion system.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Olha Lazarieva).

## What to borrow (principle)

- Use individual letters as the particle system for transitions
- A floating object in the middle of a radial project index

## What to leave

- Very small text
- Muted contrast throughout

## Signature move

Letters swirling into a ring and later raining down around a portrait.

## Motion

Intro: sage, letters spiral inward then fly out into a ring and fade (~4 s). Wheel (Lenis, ~110 px glide): a stone image wipes up; the manifesto writes and signs; dark section rises; letters fall into vertical columns around the portrait as the big headline assembles; the awards list rises over mountains; project names arrange around the rotating rock.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x4 (three.js); split text; smoothed scroll (median 120 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a developer folio on sage grey: letters of 'creative developer' swirl in a spiral and scatter into a ring, then a stone and mountain backdrop, a small signed manifesto, a dark section where letters rain into columns around a portrait as 'Fundamentals of web development' fills in, an awards list over a mountain silhouette and a dark project index around a floating 3D rock. Type: RF Dewi, Bebas Neue.
Ground and ink from the measured palette (#C3CABA, #AAB1A2, #949B8D). Motion carries the page through
letters swirling into a ring and later raining down around a portrait. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — stone and mountain photography, portrait, 3D rock

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: stone and mountain photography, portrait, 3D rock

## Reference lock

Primary reference/direction: Max Milkin - Creative Frontend Developer — A developer folio on sage grey: letters of 'creative developer' swirl in a spiral and scatter into a ring, then a stone and mountain backdrop, a small signed manifesto, a dark section where letters rain into columns around a portrait as 'Fundamentals of web development' fills in, an awards list over a mountain silhouette and a dark project index around a floating 3D rock.
Preserve (3-5 traits): letters orbiting into a ring; sage grey and near black; letters raining into columns; signature under a manifesto; mountain silhouettes.
Borrow only (1-2): Use individual letters as the particle system for transitions; A floating object in the middle of a radial project index
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: stone and mountain photography, portrait, 3D rock
Reject: Very small text; Muted contrast throughout
Token commitments: palette #C3CABA, #AAB1A2, #949B8D; type RF Dewi, Bebas Neue; engine GSAP + Lenis linked (never vendored).
