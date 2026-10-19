---
title: "Felix Nieto"
url: https://felix-nieto.com/
source_url: https://felix-nieto.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: "portfolio"
family: property-film-art-direction
dna: "Real-estate art director x cinematic property films"
register: editorial print
grammar: chaptered editorial
lane: "A real-estate art director's site with a thin serif-and-caps headline and a teal brush stroke, an aerial film that grows from a frame, 'TRANSFORMING PROPERTIES INTO CINEMATIC VISUAL NARRATIVES', property stills that fly in as a collage and converge into one, then projects as full-bleed films with blurred companion stills."
mode: persuade
traits: ["mixed sans caps and thin serif headline", "teal brush stroke", "video frame growing to full bleed", "stills converging into one image", "full-bleed project films with names", "testimonial columns"]
palette: ["#FAF8F4", "#292824", "#9C9B9F", "#535352", "#C3CAC8", "#E8E3DA"]
type: ["Nohemi", "Merchant"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Images arrive as a scattered collage that converges into a single frame, which is literally what the service does (many shots, one narrative). The palette is cream with one teal brush stroke, so the property films carry all the colour.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Converge a scattered collage of stills into a single frame
- One brush-stroke accent as the only graphic

## What to leave

- Blurred companion stills reduce clarity
- Long testimonial columns

## Signature move

Property stills flying in as a collage and converging into one frame.

## Motion

Intro: black 'felixnieto.' (~1 s), cream headline with the teal stroke drawing. Scroll (Lenis, 6 ScrollTriggers, Barba, SplitText): video frame grows to the aerial film; statement in mixed weights; stills fly in from the edges and stack into one; projects (Kensho, Sanctuary, Panoramah) as films with blurred stills sliding; testimonials; logo row; 'LET'S WORK TOGETHER'.

Measured (`motion/probe.json`): GSAP 3.15.0/3.15.0; 6 ScrollTriggers; Lenis; Barba page transitions; 8 video; split text; smoothed scroll (median 146 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a real-estate art director's site with a thin serif-and-caps headline and a teal brush stroke, an aerial film that grows from a frame, 'TRANSFORMING PROPERTIES INTO CINEMATIC VISUAL NARRATIVES', property stills that fly in as a collage and converge into one, then projects as full-bleed films with blurred companion stills. Type: Nohemi, Merchant.
Ground and ink from the measured palette (#FAF8F4, #292824, #9C9B9F). Motion carries the page through
property stills flying in as a collage and converging into one frame. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — luxury architecture photography and drone footage, Mediterranean light

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: luxury architecture photography and drone footage, Mediterranean light

## Reference lock

Primary reference/direction: Felix Nieto — A real-estate art director's site with a thin serif-and-caps headline and a teal brush stroke, an aerial film that grows from a frame, 'TRANSFORMING PROPERTIES INTO CINEMATIC VISUAL NARRATIVES', property stills that fly in as a collage and converge into one, then projects as full-bleed films with blurred companion stills.
Preserve (3-5 traits): mixed sans caps and thin serif headline; teal brush stroke; video frame growing to full bleed; stills converging into one image; full-bleed project films with names.
Borrow only (1-2): Converge a scattered collage of stills into a single frame; One brush-stroke accent as the only graphic
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: luxury architecture photography and drone footage, Mediterranean light
Reject: Blurred companion stills reduce clarity; Long testimonial columns
Token commitments: palette #FAF8F4, #292824, #9C9B9F, #535352, #C3CAC8, #E8E3DA; type Nohemi, Merchant; engine GSAP + Lenis linked (never vendored).
