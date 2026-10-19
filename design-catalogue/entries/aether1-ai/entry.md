---
title: "Aether 1 Earbuds"
url: https://aether1.ai/
source_url: https://aether1.ai/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: earbuds-ripple-product-3d
dna: "Earbuds x sound-wave ripples and a 3D case opening"
register: cinematic dark
grammar: filmic one-shot
lane: "A product page in deep blue: a planet-like loader with orbiting points, 'Sound Without Boundaries' with the 3D earbud case on concentric ripples and a glowing ring burst, the case turning and opening, the buds lifting out, 'Unrivalled audio quality' as the buds float on a wire grid with light streaks."
mode: persuade
traits: ["concentric sound ripples", "3D case turning and opening", "buds lifting out", "wire grid", "deep blue palette", "glowing ring burst"]
palette: ["#091019", "#1E3E60", "#597E9C"]
type: ["Azeretmono", "Manrope"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The ripples make the sound visible and the case opening to release the buds is the product's real ritual, done as one continuous shot.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: OFF+BRAND).

## What to borrow (principle)

- Show the product's unboxing ritual as the scroll sequence
- Visualise the invisible benefit (sound) as ripples

## What to leave

- Small body text
- Long dark frames

## Signature move

An earbud case opening on blue sound ripples.

## Motion

Intro: navy, an orb with orbiting points and labels (~3 s), a ring bursts. Wheel (Lenis, 1 pin, Taxi): ripples pulse; the case rotates and the lid lifts; the buds rise and turn; the ground becomes a wire grid; light streaks pass.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 pinned sections; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); 1 video; smoothed scroll (median 36 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a product page in deep blue: a planet-like loader with orbiting points, 'Sound Without Boundaries' with the 3D earbud case on concentric ripples and a glowing ring burst, the case turning and opening, the buds lifting out, 'Unrivalled audio quality' as the buds float on a wire grid with light streaks. Type: Azeretmono, Manrope.
Ground and ink from the measured palette (#091019, #1E3E60, #597E9C). Motion carries the page through
an earbud case opening on blue sound ripples. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product render

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product render

## Reference lock

Primary reference/direction: Aether 1 Earbuds — A product page in deep blue: a planet-like loader with orbiting points, 'Sound Without Boundaries' with the 3D earbud case on concentric ripples and a glowing ring burst, the case turning and opening, the buds lifting out, 'Unrivalled audio quality' as the buds float on a wire grid with light streaks.
Preserve (3-5 traits): concentric sound ripples; 3D case turning and opening; buds lifting out; wire grid; deep blue palette.
Borrow only (1-2): Show the product's unboxing ritual as the scroll sequence; Visualise the invisible benefit (sound) as ripples
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product render
Reject: Small body text; Long dark frames
Token commitments: palette #091019, #1E3E60, #597E9C; type Azeretmono, Manrope; engine GSAP + Lenis linked (never vendored).
