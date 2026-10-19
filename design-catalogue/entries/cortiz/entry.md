---
title: "Christian Ortiz - Full Stack Developer and Designer"
url: https://cortiz.dev/
source_url: https://cortiz.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: holo-card-dev-folio
dna: "Creative developer x holographic trading-card frames for each project"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer folio on black: a wireframe sphere loader with a music notice, a serif 'Take creativity to the next level' over anime eyes in smoke, an about with a portrait, client logo marquee, then 'Selected works' where each project sits in a glowing holographic card frame that glitches from one project to the next, and a labs teaser with a YouTube tutorial card."
mode: persuade
traits: ["wireframe sphere loader", "holographic trading-card frame", "glitch between project cards", "smoke and particles", "high-contrast serif headline", "floating project thumbnails"]
palette: ["#000000", "#1D1D1D", "#3C3C3C", "#616161"]
type: ["__Gloock_e266ae", "__Amiri_Quran_30f8ef", "__Rajdhani_6184ad", "Doto"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The trading-card frame is the signature object: every project is dealt into the same glowing frame, and the glitch between them makes the switch feel like a game.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One frame object that each project is dealt into
- Glitch as the transition between case studies

## What to leave

- Long tutorial teaser at the end
- Small body text

## Signature move

A glowing holographic card frame that glitches from one project to the next.

## Motion

Intro: black, a wireframe sphere spins and fills (~2 s), sound notice dismissed. Wheel (Lenis ~80 px glide, WebGL): the serif headline splits around the eyes; 'Further' and 'About' slide in; the portrait card rises; logos scroll; the card frame pins, each project's art appears inside with sparkles, then glitches and is replaced; thumbnails float around it.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x5 (three.js); 8 video; split text; smoothed scroll (median 77 px still travelling after input stops); entry gate: OK, I UNDERSTAND OK, I UNDERSTAND. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer folio on black: a wireframe sphere loader with a music notice, a serif 'Take creativity to the next level' over anime eyes in smoke, an about with a portrait, client logo marquee, then 'Selected works' where each project sits in a glowing holographic card frame that glitches from one project to the next, and a labs teaser with a YouTube tutorial card. Type: __Gloock_e266ae, __Amiri_Quran_30f8ef, __Rajdhani_6184ad, Doto.
Ground and ink from the measured palette (#000000, #1D1D1D, #3C3C3C). Motion carries the page through
a glowing holographic card frame that glitches from one project to the next. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL card frames, project art, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL card frames, project art, portrait

## Reference lock

Primary reference/direction: Christian Ortiz - Full Stack Developer and Designer — A developer folio on black: a wireframe sphere loader with a music notice, a serif 'Take creativity to the next level' over anime eyes in smoke, an about with a portrait, client logo marquee, then 'Selected works' where each project sits in a glowing holographic card frame that glitches from one project to the next, and a labs teaser with a YouTube tutorial card.
Preserve (3-5 traits): wireframe sphere loader; holographic trading-card frame; glitch between project cards; smoke and particles; high-contrast serif headline.
Borrow only (1-2): One frame object that each project is dealt into; Glitch as the transition between case studies
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL card frames, project art, portrait
Reject: Long tutorial teaser at the end; Small body text
Token commitments: palette #000000, #1D1D1D, #3C3C3C, #616161; type __Gloock_e266ae, __Amiri_Quran_30f8ef, __Rajdhani_6184ad, Doto; engine GSAP + Lenis linked (never vendored).
