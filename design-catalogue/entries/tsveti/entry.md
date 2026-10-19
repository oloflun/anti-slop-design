---
title: "Tsvetelina Mladenova - Web Design and Development"
url: https://tsveti.dev/
source_url: https://tsveti.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: desert-stone-flower-folio
dna: "Web designer x sunlit stones, wildflowers and sketched flower diagrams"
register: warm photographic
grammar: chaptered editorial
lane: "A designer folio: a sketched sprout loader, a sunlit image of stones and daisies, a dark manifesto panel with a sketched flower diagram labelling skills (HTML, CSS, GSAP, three.js), a numbered project row where each project card holds a flower photo, an awards list where images flicker between lines, stones with shadows, principles with a heart and a giant email."
mode: persuade
traits: ["sunlit stone and flower imagery", "sketched flower skill diagram", "numbered projects with flower photos", "dark rounded panels", "awards list", "giant email footer"]
palette: ["#1B1B1B", "#654315", "#FFFFFF", "#94714A", "#E8E5E3"]
type: ["Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The flower motif ties skills (sketched flowers) and projects (flower photos) together into one gentle identity.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A sketched diagram of skills as a plant

## What to leave

- Blurred awards transition

## Signature move

A sketched flower diagram labelling web skills.

## Motion

Intro: grey with a sprout drawing (~2 s). Wheel (Lenis ~110 px glide, 2 pins): the photo shrinks into a rounded panel; the manifesto fills; the flower diagram draws; project cards slide in a row; awards blur and sharpen; stones scale; the email rises.

Measured (`motion/probe.json`): GSAP 3.12.5; 11 ScrollTriggers; 2 pinned sections; Lenis; split text; smoothed scroll (median 126 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a designer folio: a sketched sprout loader, a sunlit image of stones and daisies, a dark manifesto panel with a sketched flower diagram labelling skills (HTML, CSS, GSAP, three.js), a numbered project row where each project card holds a flower photo, an awards list where images flicker between lines, stones with shadows, principles with a heart and a giant email. Type: Inter.
Ground and ink from the measured palette (#1B1B1B, #654315, #FFFFFF). Motion carries the page through
a sketched flower diagram labelling web skills. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — stone and flower photography, sketches

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: stone and flower photography, sketches

## Reference lock

Primary reference/direction: Tsvetelina Mladenova - Web Design and Development — A designer folio: a sketched sprout loader, a sunlit image of stones and daisies, a dark manifesto panel with a sketched flower diagram labelling skills (HTML, CSS, GSAP, three.js), a numbered project row where each project card holds a flower photo, an awards list where images flicker between lines, stones with shadows, principles with a heart and a giant email.
Preserve (3-5 traits): sunlit stone and flower imagery; sketched flower skill diagram; numbered projects with flower photos; dark rounded panels; awards list.
Borrow only (1-2): A sketched diagram of skills as a plant
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: stone and flower photography, sketches
Reject: Blurred awards transition
Token commitments: palette #1B1B1B, #654315, #FFFFFF, #94714A, #E8E5E3; type Inter; engine GSAP + Lenis linked (never vendored).
