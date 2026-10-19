---
title: "Federico Rosa - Neobrutalist Visual Designer"
url: https://federicorosa.design/
source_url: https://federicorosa.design/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blue-pink-rosa-folio
dna: "Visual designer x a giant pink 'Rosa' on electric blue"
register: other
grammar: chaptered editorial
lane: "A designer folio on electric blue: a giant pink 'Rosa' rising, a bio in white, a services marquee, project mockups (laptop, paper, phone) sliding in a row with small pink tags, 'Scopri tutti i progetti' and a pink footer."
mode: read
traits: ["electric blue ground", "giant pink name", "services marquee", "project mockups row", "pink tags"]
palette: ["#1000FF", "#020202", "#FF6AB3", "#A8B5D2", "#D9D9DC", "#4738C7"]
type: ["Satoshi", "Graphyne"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Two colours and one giant word make a strong identity; the rest is a simple project row.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Two-colour identity with one giant name

## What to leave

- Project row repetitive

## Signature move

A giant pink 'Rosa' on electric blue.

## Motion

Intro: blue, the name rises and turns pink (~1.5 s). Wheel: the bio fades; the marquee runs; mockups slide sideways.

Measured (`motion/probe.json`): GSAP 3.12.2; 122 ScrollTriggers; 1 pinned sections; Lenis; 1 video; smoothed scroll (median 135 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a designer folio on electric blue: a giant pink 'Rosa' rising, a bio in white, a services marquee, project mockups (laptop, paper, phone) sliding in a row with small pink tags, 'Scopri tutti i progetti' and a pink footer. Type: Satoshi, Graphyne.
Ground and ink from the measured palette (#1000FF, #020202, #FF6AB3). Motion carries the page through
a giant pink 'Rosa' on electric blue. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: mockups

## Reference lock

Primary reference/direction: Federico Rosa - Neobrutalist Visual Designer — A designer folio on electric blue: a giant pink 'Rosa' rising, a bio in white, a services marquee, project mockups (laptop, paper, phone) sliding in a row with small pink tags, 'Scopri tutti i progetti' and a pink footer.
Preserve (3-5 traits): electric blue ground; giant pink name; services marquee; project mockups row; pink tags.
Borrow only (1-2): Two-colour identity with one giant name
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: mockups
Reject: Project row repetitive
Token commitments: palette #1000FF, #020202, #FF6AB3, #A8B5D2, #D9D9DC, #4738C7; type Satoshi, Graphyne; engine GSAP + Lenis linked (never vendored).
