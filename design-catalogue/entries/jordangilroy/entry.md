---
title: "Jordan Gilroy"
url: https://www.jordangilroy.com/
source_url: https://www.jordangilroy.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blackletter-about-webflow-folio
dna: "Webflow designer folio x lilac blackletter and blurred backdrops"
register: cinematic dark
grammar: chaptered editorial
lane: "A designer folio that wipes from lilac blocks to cream, draws a monogram, then sets 'About' in huge lilac blackletter with a portrait card sliding over it, and runs each project as a framed screenshot card over a heavily blurred full-bleed photo of that project."
mode: persuade
traits: ["lilac block wipe intro", "drawn monogram", "huge blackletter 'About'", "portrait card over the word", "project card over its own blurred photo", "231 ScrollTriggers"]
palette: ["#191B1F", "#F3F4EF", "#755D5C"]
type: ["Gt America Mono", "Editorial New", "Respira"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each case gets its own atmosphere for free: the project's photo is blown up and blurred behind a small framed screenshot, so the ground changes colour with every case while the card stays the same size.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Put each project's screenshot card over a heavily blurred enlargement of its own imagery
- A blackletter word as the about-section anchor

## What to leave

- 231 ScrollTriggers and 89 videos is heavy
- Small mono metadata

## Signature move

Each project shown as a framed card over its own blurred, enlarged photo.

## Motion

Intro: lilac blocks step away to cream; a monogram draws (~2 s). Scroll (Lenis, ~60 px glide, SplitText): intro line with thumbnails; 'About' blackletter fades in on dark; portrait card slides up over it; services list; then cases (Claude, Studio X, Truss, MoMoney, LxL Creative, Tesoro, NeoCultural, Real Hotels) each as a card sliding over its blurred backdrop.

Measured (`motion/probe.json`): GSAP 3.12.5; 231 ScrollTriggers; Lenis; WebGL canvas x1; 89 video; split text; smoothed scroll (median 65 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a designer folio that wipes from lilac blocks to cream, draws a monogram, then sets 'About' in huge lilac blackletter with a portrait card sliding over it, and runs each project as a framed screenshot card over a heavily blurred full-bleed photo of that project. Type: Gt America Mono, Editorial New, Respira.
Ground and ink from the measured palette (#191B1F, #F3F4EF, #755D5C). Motion carries the page through
each project shown as a framed card over its own blurred, enlarged photo. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screenshots plus their own campaign photography blurred

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screenshots plus their own campaign photography blurred

## Reference lock

Primary reference/direction: Jordan Gilroy — A designer folio that wipes from lilac blocks to cream, draws a monogram, then sets 'About' in huge lilac blackletter with a portrait card sliding over it, and runs each project as a framed screenshot card over a heavily blurred full-bleed photo of that project.
Preserve (3-5 traits): lilac block wipe intro; drawn monogram; huge blackletter 'About'; portrait card over the word; project card over its own blurred photo.
Borrow only (1-2): Put each project's screenshot card over a heavily blurred enlargement of its own imagery; A blackletter word as the about-section anchor
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screenshots plus their own campaign photography blurred
Reject: 231 ScrollTriggers and 89 videos is heavy; Small mono metadata
Token commitments: palette #191B1F, #F3F4EF, #755D5C; type Gt America Mono, Editorial New, Respira; engine GSAP + Lenis linked (never vendored).
