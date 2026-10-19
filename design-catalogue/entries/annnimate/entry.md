---
title: "Annnimate - GSAP motion components"
url: https://www.annnimate.com/
source_url: https://www.annnimate.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: motion-component-library
dna: "GSAP component library x a dark catalogue and a 3D ring of cards"
register: cinematic dark
grammar: chaptered editorial
lane: "A component library: 'The components behind work that gets noticed' on dark with a library UI of animated component previews, 'Good motion takes days. Fast motion looks generic.' in two-tone, 'Find it, copy it, ship it' with three steps, 'One component, told properly' with a code panel beside a demo, 'Just shipped' cards, testimonials with images scattered in 3D, pricing, FAQ and 'Take the component you'd have built yourself' over a 3D ring of tilted image cards."
mode: persuade
traits: ["library UI preview", "two-tone statement", "code panel beside demo", "3D scattered image field", "3D ring of cards", "orange accent"]
palette: ["#000000", "#F1F1F1", "#463E3A", "#D7D5CF"]
type: ["geistMono", "aktivGrotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A library selling motion shows motion in its own sections (scatter, ring) rather than describing it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Good Fella).

## What to borrow (principle)

- Close on a 3D ring of tilted cards

## What to leave

- Black frames between sections

## Signature move

A 3D ring of tilted image cards around the closing CTA.

## Motion

Intro: the dark hero with previews loading. Wheel: preview grid fades in; the statement greys its second line; steps slide; images scatter in 3D around testimonials; the ring rotates around the CTA.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); 4 video; smoothed scroll (median 156 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a component library: 'The components behind work that gets noticed' on dark with a library UI of animated component previews, 'Good motion takes days. Fast motion looks generic.' in two-tone, 'Find it, copy it, ship it' with three steps, 'One component, told properly' with a code panel beside a demo, 'Just shipped' cards, testimonials with images scattered in 3D, pricing, FAQ and 'Take the component you'd have built yourself' over a 3D ring of tilted image cards. Type: geistMono, aktivGrotesk.
Ground and ink from the measured palette (#000000, #F1F1F1, #463E3A). Motion carries the page through
a 3D ring of tilted image cards around the closing CTA. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — component demos, photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: component demos, photography

## Reference lock

Primary reference/direction: Annnimate - GSAP motion components — A component library: 'The components behind work that gets noticed' on dark with a library UI of animated component previews, 'Good motion takes days. Fast motion looks generic.' in two-tone, 'Find it, copy it, ship it' with three steps, 'One component, told properly' with a code panel beside a demo, 'Just shipped' cards, testimonials with images scattered in 3D, pricing, FAQ and 'Take the component you'd have built yourself' over a 3D ring of tilted image cards.
Preserve (3-5 traits): library UI preview; two-tone statement; code panel beside demo; 3D scattered image field; 3D ring of cards.
Borrow only (1-2): Close on a 3D ring of tilted cards
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: component demos, photography
Reject: Black frames between sections
Token commitments: palette #000000, #F1F1F1, #463E3A, #D7D5CF; type geistMono, aktivGrotesk; engine GSAP + Lenis linked (never vendored).
