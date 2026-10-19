---
title: "Blinkpath - UI/UX Design and Creative Studio"
url: https://blinkpath.com/
source_url: https://blinkpath.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "product-focused"
family: pixel-dot-vehicle-studio
dna: "Product design studio x dot-matrix renders of vehicles that form and dissolve"
register: modern clean
grammar: chaptered editorial
lane: "A product design studio: a logo loader on black, a dark panel, then a light page where a dot-matrix truck forms out of scattered pixels inside an orange-framed card, the statement, case cards on charcoal (analytics dashboards, a banner, a boat render), and services as orange-titled cards."
mode: persuade
traits: ["dot-matrix render forming from scattered pixels", "orange frame accent", "charcoal case section", "service cards with orange titles", "Barba transitions", "light to dark flip"]
palette: ["#FFFFFF", "#E9E9E9", "#72706F", "#69392D", "#C8C6C5"]
type: ["Aeonik"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The dot-matrix vehicle that assembles from noise is a neat image for 'clarity from complexity'.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Assemble a product image from scattered dots on scroll

## What to leave

- Generic service cards

## Signature move

A dot-matrix truck forming out of scattered pixels.

## Motion

Intro: black with the logo (~2 s), a dark diagonal panel. Wheel (virtual, Barba): the white panel rises with an orange frame; dots drift together into the truck and later disperse; case cards slide on charcoal; service cards slide sideways.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; Barba page transitions; 5 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a product design studio: a logo loader on black, a dark panel, then a light page where a dot-matrix truck forms out of scattered pixels inside an orange-framed card, the statement, case cards on charcoal (analytics dashboards, a banner, a boat render), and services as orange-titled cards. Type: Aeonik.
Ground and ink from the measured palette (#FFFFFF, #E9E9E9, #72706F). Motion carries the page through
a dot-matrix truck forming out of scattered pixels. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — dot-matrix renders, UI mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: dot-matrix renders, UI mockups

## Reference lock

Primary reference/direction: Blinkpath - UI/UX Design and Creative Studio — A product design studio: a logo loader on black, a dark panel, then a light page where a dot-matrix truck forms out of scattered pixels inside an orange-framed card, the statement, case cards on charcoal (analytics dashboards, a banner, a boat render), and services as orange-titled cards.
Preserve (3-5 traits): dot-matrix render forming from scattered pixels; orange frame accent; charcoal case section; service cards with orange titles; Barba transitions.
Borrow only (1-2): Assemble a product image from scattered dots on scroll
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: dot-matrix renders, UI mockups
Reject: Generic service cards
Token commitments: palette #FFFFFF, #E9E9E9, #72706F, #69392D, #C8C6C5; type Aeonik; engine GSAP + Lenis linked (never vendored).
