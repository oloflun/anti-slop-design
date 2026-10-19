---
title: "Silvia Malavasi"
url: https://silviamalavasi.com/
source_url: https://silviamalavasi.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: specimen-dissection-dev-folio
dna: "Creative developer CV x punk lab specimen file"
register: illustrated dark
grammar: live surface
lane: "A developer folio staged as a lab dissection: a wireframe punk skull with a pink mohawk, hazard-tape strips, a 'FRONTEND DEVELOPER' stamp, then a rotating wireframe brain with 'click the brain to start dissection' beside a subject card."
mode: experience
traits: ["wireframe 3D skull and brain (pink/blue)", "hazard-tape stripes", "lime + yellow labels on black", "marquee of skills along a bar", "subject ID card with portrait", "giant outlined 'INTAKE 2015' marquee"]
palette: ["#0B0907", "#4B1C2C", "#76763A"]
type: ["Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The CV is a specimen file: subject card, intake year, a brain to dissect. Wireframe 3D keeps the organs graphic, and the yellow hazard tape and lime labels give it a punk-lab register that matches the mohawk. The interaction (click the brain) replaces scroll as the way in.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stage a CV as a file or specimen so the metadata becomes the design
- Wireframe 3D for organic objects keeps them graphic, not gory
- A giant outlined marquee as moving background texture

## What to leave

- The page pins on the brain and needs a click to continue
- Small neon text on black

## Signature move

A rotating wireframe brain with 'click the brain to start dissection'.

## Motion

Intro: 'loading specimen…' on black, then the skull wireframe rises with hazard tape sliding in and 'FRONTEND DEVELOPER' stamping on (~2 s). Scroll (ScrollSmoother, Observer, SplitText): skills marquee runs along a bar; the camera moves from the skull to the brain; 'INTAKE 2015' outline marquee runs behind; the brain rotates and pulses waiting for a click.

Measured (`motion/probe.json`): GSAP 3.15.0; ScrollSmoother; WebGL canvas x1 (three.js); split text. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: a developer folio staged as a lab dissection: a wireframe punk skull with a pink mohawk, hazard-tape strips, a 'FRONTEND DEVELOPER' stamp, then a rotating wireframe brain with 'click the brain to start dissection' beside a subject card. Type: Inter.
Ground and ink from the measured palette (#0B0907, #4B1C2C, #76763A). Motion carries the page through
a rotating wireframe brain with 'click the brain to start dissection'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — wireframe 3D anatomy in pink and blue on black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: wireframe 3D anatomy in pink and blue on black

## Reference lock

Primary reference/direction: Silvia Malavasi — A developer folio staged as a lab dissection: a wireframe punk skull with a pink mohawk, hazard-tape strips, a 'FRONTEND DEVELOPER' stamp, then a rotating wireframe brain with 'click the brain to start dissection' beside a subject card.
Preserve (3-5 traits): wireframe 3D skull and brain (pink/blue); hazard-tape stripes; lime + yellow labels on black; marquee of skills along a bar; subject ID card with portrait.
Borrow only (1-2): Stage a CV as a file or specimen so the metadata becomes the design; Wireframe 3D for organic objects keeps them graphic, not gory
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: wireframe 3D anatomy in pink and blue on black
Reject: The page pins on the brain and needs a click to continue; Small neon text on black
Token commitments: palette #0B0907, #4B1C2C, #76763A; type Inter; engine GSAP + Lenis linked (never vendored).
