---
title: "Jextures - UI/UX and Digital Experience Agency"
url: https://jextures.com.my/
source_url: https://jextures.com.my/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: neon-ring-services-agency
dna: "Malaysian UX agency x a neon ring portal that frames each service"
register: cinematic dark
grammar: chaptered editorial
lane: "An agency: 'Cracking the code of creativity' on a purple glow, a glass label that flips to 'Jext because', a neon ring that glows blue and orange as each service passes through it with floating 3D icons (web, mobile, motion), then white sections with 'No templates / No copy-paste' word swaps, a navy manifesto and 'Here's where we've made our mark'."
mode: persuade
traits: ["neon ring portal", "services passing through the ring", "3D icons floating", "glass label swap", "word swap in a statement", "navy and white alternation"]
palette: ["#020103", "#780F08", "#101F57", "#6697A4", "#21112D", "#3F3B6A"]
type: ["Exo"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The ring is the signature object and each service gets its moment inside it, which makes a list of services feel like stepping through gates.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A ring that frames one service at a time

## What to leave

- Very small labels
- Long empty frames

## Signature move

A neon ring glowing blue and orange as services pass through it.

## Motion

Intro: navy with a small loader dot (~2 s), the glow and headline fade in. Wheel (ScrollSmoother): the glass label flips; the ring grows from the dark and changes colour per service while icons orbit; white panel rises; words swap in place; the navy manifesto types; the closing title assembles.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 ScrollTriggers; ScrollSmoother; 1 video; split text; entry gate: close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an agency: 'Cracking the code of creativity' on a purple glow, a glass label that flips to 'Jext because', a neon ring that glows blue and orange as each service passes through it with floating 3D icons (web, mobile, motion), then white sections with 'No templates / No copy-paste' word swaps, a navy manifesto and 'Here's where we've made our mark'. Type: Exo.
Ground and ink from the measured palette (#020103, #780F08, #101F57). Motion carries the page through
a neon ring glowing blue and orange as services pass through it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D icons, WebGL glow

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D icons, WebGL glow

## Reference lock

Primary reference/direction: Jextures - UI/UX and Digital Experience Agency — An agency: 'Cracking the code of creativity' on a purple glow, a glass label that flips to 'Jext because', a neon ring that glows blue and orange as each service passes through it with floating 3D icons (web, mobile, motion), then white sections with 'No templates / No copy-paste' word swaps, a navy manifesto and 'Here's where we've made our mark'.
Preserve (3-5 traits): neon ring portal; services passing through the ring; 3D icons floating; glass label swap; word swap in a statement.
Borrow only (1-2): A ring that frames one service at a time
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D icons, WebGL glow
Reject: Very small labels; Long empty frames
Token commitments: palette #020103, #780F08, #101F57, #6697A4, #21112D, #3F3B6A; type Exo; engine GSAP + Lenis linked (never vendored).
