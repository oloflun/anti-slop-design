---
title: "NEIRU - street fashion brand"
url: https://neiru.webflow.io/
source_url: https://neiru.webflow.io/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: ""
family: spiked-metal-fashion-jp
dna: "Japanese street fashion x a blackletter-metal logo and a spiked bracelet in macro 3D"
register: other
grammar: chaptered editorial
lane: "A fashion brand on hot pink and teal: a spiky metal-style 'NEIRU' logo with a model photo inside it, a model in a purple hoodie with Japanese statements, a 3D spiked metal bracelet that the camera orbits extremely close (spikes, leather, clasp) with small product cards, photos of the bracelet worn, a shop section in pink and teal and product cards of hoodies."
mode: persuade
traits: ["spiked metal logo", "3D product macro orbit", "hot pink and teal", "Japanese statements", "product cards", "photo inside the logo"]
palette: ["#E0E0E0", "#DC2459", "#4C1223", "#887883", "#A22448"]
type: ["Geist", "Zenantiquesoft"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Orbiting the bracelet in extreme close-up makes one accessory feel monumental and matches the spiky logo.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Orbit one product in extreme 3D close-up

## What to leave

- Grey empty frames

## Signature move

A spiked metal bracelet filling the screen in a 3D macro orbit.

## Motion

Intro: pink with the logo, a model photo grows inside it (~2 s). Wheel: the hero model slides; statements type; the bracelet rotates and the camera dives along the spikes and strap; cards pop; photos slide; product grid fills.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; smoothed scroll (median 194 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a fashion brand on hot pink and teal: a spiky metal-style 'NEIRU' logo with a model photo inside it, a model in a purple hoodie with Japanese statements, a 3D spiked metal bracelet that the camera orbits extremely close (spikes, leather, clasp) with small product cards, photos of the bracelet worn, a shop section in pink and teal and product cards of hoodies. Type: Geist, Zenantiquesoft.
Ground and ink from the measured palette (#E0E0E0, #DC2459, #4C1223). Motion carries the page through
a spiked metal bracelet filling the screen in a 3D macro orbit. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fashion photography, 3D product

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fashion photography, 3D product

## Reference lock

Primary reference/direction: NEIRU - street fashion brand — A fashion brand on hot pink and teal: a spiky metal-style 'NEIRU' logo with a model photo inside it, a model in a purple hoodie with Japanese statements, a 3D spiked metal bracelet that the camera orbits extremely close (spikes, leather, clasp) with small product cards, photos of the bracelet worn, a shop section in pink and teal and product cards of hoodies.
Preserve (3-5 traits): spiked metal logo; 3D product macro orbit; hot pink and teal; Japanese statements; product cards.
Borrow only (1-2): Orbit one product in extreme 3D close-up
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fashion photography, 3D product
Reject: Grey empty frames
Token commitments: palette #E0E0E0, #DC2459, #4C1223, #887883, #A22448; type Geist, Zenantiquesoft; engine GSAP + Lenis linked (never vendored).
