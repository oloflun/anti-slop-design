---
title: "Anyflow Labs"
url: https://labs.anyflow.agency/
source_url: https://labs.anyflow.agency/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: lime-3d-mark-agency
dna: "Web agency lab x lime 3D logo mark and a vortex finale"
register: other
grammar: chaptered editorial
lane: "An agency lab in acid lime, white and black: a lime loading counter, 'We are good at...' with the 3D logo mark spinning into the sentence, the mark orbiting service labels, a process mind-map of cards, a lime featured-work section where projects arrive in pixel-edged frames, a black 'Built different' word cycle and a lime vortex that swallows the screen and spits out the mark."
mode: persuade
traits: ["giant loading counter on lime", "3D logo mark as the recurring object", "pixel-stepped section edges", "floating mind-map cards", "word cycle on black", "lime vortex finale"]
palette: ["#F5F5F5", "#9BE700", "#A4DB42", "#333C26", "#DCF0B9"]
type: ["Bebas Neue", "Inter Tight"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The mark is in every chapter (in the sentence, orbiting services, inside the vortex) and the stepped pixel edges are the material of every section change, so a busy agency page stays one system.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stepped pixel edges as the section wipe
- End on a vortex that resolves into the logo

## What to leave

- Tiny card text in the mind map
- Many disconnected mini-ideas

## Signature move

A lime vortex that swallows the page and resolves into the 3D mark.

## Motion

Intro: lime screen with a giant counter 04 to 100 and a line loader (~2 s). Wheel (Lenis ~130 px glide): the mark spins into the headline; the camera orbits it past service labels; process cards connect with lines; lime rises from below in pixel steps; project frames open with pixel edges; black takes over and 'Built different' cycles words; a lime swirl grows from a dot to fill the screen and the mark appears in it.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x3 (three.js); split text; smoothed scroll (median 102 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: an agency lab in acid lime, white and black: a lime loading counter, 'We are good at...' with the 3D logo mark spinning into the sentence, the mark orbiting service labels, a process mind-map of cards, a lime featured-work section where projects arrive in pixel-edged frames, a black 'Built different' word cycle and a lime vortex that swallows the screen and spits out the mark. Type: Bebas Neue, Inter Tight.
Ground and ink from the measured palette (#F5F5F5, #9BE700, #A4DB42). Motion carries the page through
a lime vortex that swallows the page and resolves into the 3D mark. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D renders, project screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D renders, project screenshots

## Reference lock

Primary reference/direction: Anyflow Labs — An agency lab in acid lime, white and black: a lime loading counter, 'We are good at...' with the 3D logo mark spinning into the sentence, the mark orbiting service labels, a process mind-map of cards, a lime featured-work section where projects arrive in pixel-edged frames, a black 'Built different' word cycle and a lime vortex that swallows the screen and spits out the mark.
Preserve (3-5 traits): giant loading counter on lime; 3D logo mark as the recurring object; pixel-stepped section edges; floating mind-map cards; word cycle on black.
Borrow only (1-2): Stepped pixel edges as the section wipe; End on a vortex that resolves into the logo
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D renders, project screenshots
Reject: Tiny card text in the mind map; Many disconnected mini-ideas
Token commitments: palette #F5F5F5, #9BE700, #A4DB42, #333C26, #DCF0B9; type Bebas Neue, Inter Tight; engine GSAP + Lenis linked (never vendored).
