---
title: "Dumemearts - Digital Designer"
url: https://dumemearts.webflow.io/
source_url: https://dumemearts.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: yellow-black-condensed-designer
dna: "Digital designer x yellow condensed type and a wireframe globe"
register: cinematic dark
grammar: chaptered editorial
lane: "A designer folio in yellow and black: an eye logo loader on yellow, 'DIGITAL DESIGNER' in yellow condensed type in a bracketed frame over a wireframe globe, an about card with a yellow ring portrait, a checkered band into yellow 'EXPERTISE' letters filling in, three tilted service cards with black-and-yellow graphics, brands, 'PROJECTS' with a striped tape and stacked project cards (Meridian, Logitech, Bamboo, Vogue)."
mode: persuade
traits: ["yellow and black only", "condensed caps", "wireframe globe", "checkered and striped tape bands", "tilted service cards", "stacking project cards"]
palette: ["#FED600", "#191B1C", "#504C39", "#968737", "#D1B62C", "#FADC34"]
type: ["HKGuise", "Humane", "Chaney", "Safiro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A strict two-colour system with racing-tape bands gives a solo designer a recognisable brand, and the cards stack cleanly.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Racing-tape stripe bands as section dividers

## What to leave

- Generic stacked cards

## Signature move

Yellow condensed 'DIGITAL DESIGNER' over a wireframe globe.

## Motion

Intro: yellow with an eye logo (~1.5 s). Wheel (Lenis, 1 pin, 46 triggers): the globe rotates; the about card slides; a checkered band sweeps; letters of 'EXPERTISE' fill; service cards rise tilted; tape crosses the 'PROJECTS' title; project cards stack.

Measured (`motion/probe.json`): GSAP 3.15.0; 46 ScrollTriggers; 1 pinned sections; Lenis; Barba page transitions; 22 video; split text; smoothed scroll (median 97 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a designer folio in yellow and black: an eye logo loader on yellow, 'DIGITAL DESIGNER' in yellow condensed type in a bracketed frame over a wireframe globe, an about card with a yellow ring portrait, a checkered band into yellow 'EXPERTISE' letters filling in, three tilted service cards with black-and-yellow graphics, brands, 'PROJECTS' with a striped tape and stacked project cards (Meridian, Logitech, Bamboo, Vogue). Type: HKGuise, Humane, Chaney, Safiro.
Ground and ink from the measured palette (#FED600, #191B1C, #504C39). Motion carries the page through
yellow condensed 'DIGITAL DESIGNER' over a wireframe globe. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — graphics, project screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: graphics, project screenshots

## Reference lock

Primary reference/direction: Dumemearts - Digital Designer — A designer folio in yellow and black: an eye logo loader on yellow, 'DIGITAL DESIGNER' in yellow condensed type in a bracketed frame over a wireframe globe, an about card with a yellow ring portrait, a checkered band into yellow 'EXPERTISE' letters filling in, three tilted service cards with black-and-yellow graphics, brands, 'PROJECTS' with a striped tape and stacked project cards (Meridian, Logitech, Bamboo, Vogue).
Preserve (3-5 traits): yellow and black only; condensed caps; wireframe globe; checkered and striped tape bands; tilted service cards.
Borrow only (1-2): Racing-tape stripe bands as section dividers
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: graphics, project screenshots
Reject: Generic stacked cards
Token commitments: palette #FED600, #191B1C, #504C39, #968737, #D1B62C, #FADC34; type HKGuise, Humane, Chaney, Safiro; engine GSAP + Lenis linked (never vendored).
