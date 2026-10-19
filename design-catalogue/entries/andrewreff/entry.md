---
title: "Andy Reff"
url: https://andrewreff.com/
source_url: https://andrewreff.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: particle-portrait-product-lead
dna: "Lead product designer folio x violet particle portrait"
register: cinematic dark
grammar: chaptered editorial
lane: "A dark folio with 'Beyond the click.' in large sans, a violet cursor-arrow that grows into a field of particles which form the designer's face, then 'From chaos to how did we ever do it the old way?' with paper cards scattering around, and three case studies as image-and-text pairs."
mode: persuade
traits: ["large sans headline with full stop accent", "cursor arrow becoming a particle portrait", "violet single accent", "paper cards scattering around a statement", "case pairs with 'Ask first. Shop second.' style titles"]
palette: ["#141414", "#5B4E79", "#B1AEB3", "#28272A", "#3E2F66"]
type: ["Söhne"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The cursor (the click) literally becomes the person: the arrow icon turns into a particle cloud that resolves into a portrait, which ties 'beyond the click' to the human behind it. The rest is plain and well paced, case titles as two short sentences.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Andy Reff).

## What to borrow (principle)

- Morph a UI icon (cursor) into the person's portrait with particles
- Scatter blank paper cards around a statement to suggest the mess before order
- Two short sentences as each case title

## What to leave

- Cookie card over early frames
- Generic dark folio grid after the hero

## Signature move

A cursor arrow that dissolves into particles and resolves into the designer's face.

## Motion

Intro: headline on dark grey (~1 s). Scroll (window, WebGL, video): a violet cursor arrow appears, explodes into particles that drift and resolve into a portrait; 'Hello.' with the photo; statement with violet second line while paper cards fly in around it; 'Three decisions. Three scales of design.'; case pairs slide in; design-system case with a colour palette card.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x1 (three.js); 3 video; entry gate: Reject optional, Close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a dark folio with 'Beyond the click.' in large sans, a violet cursor-arrow that grows into a field of particles which form the designer's face, then 'From chaos to how did we ever do it the old way?' with paper cards scattering around, and three case studies as image-and-text pairs. Type: Söhne.
Ground and ink from the measured palette (#141414, #5B4E79, #B1AEB3). Motion carries the page through
a cursor arrow that dissolves into particles and resolves into the designer's face. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black-and-white portrait, product UI in device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black-and-white portrait, product UI in device mockups

## Reference lock

Primary reference/direction: Andy Reff — A dark folio with 'Beyond the click.' in large sans, a violet cursor-arrow that grows into a field of particles which form the designer's face, then 'From chaos to how did we ever do it the old way?' with paper cards scattering around, and three case studies as image-and-text pairs.
Preserve (3-5 traits): large sans headline with full stop accent; cursor arrow becoming a particle portrait; violet single accent; paper cards scattering around a statement; case pairs with 'Ask first. Shop second.' style titles.
Borrow only (1-2): Morph a UI icon (cursor) into the person's portrait with particles; Scatter blank paper cards around a statement to suggest the mess before order
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black-and-white portrait, product UI in device mockups
Reject: Cookie card over early frames; Generic dark folio grid after the hero
Token commitments: palette #141414, #5B4E79, #B1AEB3, #28272A, #3E2F66; type Söhne; engine GSAP + Lenis linked (never vendored).
