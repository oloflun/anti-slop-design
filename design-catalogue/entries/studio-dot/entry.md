---
title: "Studio DOT - Boutique digital studio"
url: https://studio-dot.fr/
source_url: https://studio-dot.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blue-glow-cursor-cases
dna: "Paris studio x a blue glow and a case viewer with a blue cursor dot"
register: cinematic dark
grammar: chaptered editorial
lane: "A studio site: 'We cut through the noise, delivering impactful solutions' under a blue planet-like glow, a central case viewer that swaps projects (Adidas, L'Oreal, a Paris building, Juventus) with a blue dot cursor, 'Precision isn't just what we do' in italic serif, a white work list, 'We are makers, not overthinkers' with values and testimonials."
mode: persuade
traits: ["blue planet glow", "central case viewer", "blue dot cursor", "italic serif accent", "black and white alternation", "values list"]
palette: ["#000000", "#FCFCFC", "#CC99B0", "#7F8C90", "#D4D4D5", "#4D4B52"]
type: ["PP Editorial New", "Avenir"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The single case viewer swapping clients in place keeps the hero focused.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One central case window that swaps projects in place

## What to leave

- Generic lower half

## Signature move

A central case window swapping client work under a blue glow.

## Motion

Intro: black with a blue glow rising (~1.5 s). Wheel (Lenis): the case window rises and swaps projects; the statement fills; the page turns white; work rows slide; values fade in.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); 4 video; smoothed scroll (median 121 px still travelling after input stops); entry gate: Mute. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a studio site: 'We cut through the noise, delivering impactful solutions' under a blue planet-like glow, a central case viewer that swaps projects (Adidas, L'Oreal, a Paris building, Juventus) with a blue dot cursor, 'Precision isn't just what we do' in italic serif, a white work list, 'We are makers, not overthinkers' with values and testimonials. Type: PP Editorial New, Avenir.
Ground and ink from the measured palette (#000000, #FCFCFC, #CC99B0). Motion carries the page through
a central case window swapping client work under a blue glow. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — case imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: case imagery

## Reference lock

Primary reference/direction: Studio DOT - Boutique digital studio — A studio site: 'We cut through the noise, delivering impactful solutions' under a blue planet-like glow, a central case viewer that swaps projects (Adidas, L'Oreal, a Paris building, Juventus) with a blue dot cursor, 'Precision isn't just what we do' in italic serif, a white work list, 'We are makers, not overthinkers' with values and testimonials.
Preserve (3-5 traits): blue planet glow; central case viewer; blue dot cursor; italic serif accent; black and white alternation.
Borrow only (1-2): One central case window that swaps projects in place
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: case imagery
Reject: Generic lower half
Token commitments: palette #000000, #FCFCFC, #CC99B0, #7F8C90, #D4D4D5, #4D4B52; type PP Editorial New, Avenir; engine GSAP + Lenis linked (never vendored).
