---
title: "WLKR 76 - Decathlon sneaker launch"
url: https://decathlon-wlkr76.index.studio/
source_url: https://decathlon-wlkr76.index.studio/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: surreal-3d-sneaker-world
dna: "Sneaker launch x a 3D shoe floating through surreal worlds of moss, scaffolding, foam and tubes"
register: cinematic dark
grammar: continuous world
lane: "A sneaker drop as a journey: a 'chargement' loader on clouds, the shoe on a mossy hill above a city haze, the camera diving through chrome scaffolding with pastel tubes, a macro of the outsole ('Inspirée par la ville'), the shoe in a tube-and-foam machine, back to the moss world with mushrooms ('45 années d'expertise', 'Et vous invite'), a concrete floor with the shoe dropped on it, then 'Limitée 1500 pièces' with a photo grid, three colourways and a material breakdown pairing macro textures with wearers."
mode: experience
traits: ["3D shoe through surreal sets", "moss, scaffolding and foam worlds", "outsole macro", "limited-count statement with photo grid", "material swatches paired with wearers"]
palette: ["#E3E6E6", "#141B0B", "#CFD0BD", "#395423", "#829061", "#A7A58B"]
type: ["Roboto Flex"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Each world says something about the shoe (city, comfort, grip) without words, so the copy only has to name the edition.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Index).

## What to borrow (principle)

- Give each product claim its own physical world for the object to pass through

## What to leave

- Tiny buy button

## Signature move

A white sneaker floating over a mossy hill above a hazy city skyline.

## Motion

Intro: loader on clouds (~3 s). Wheel (Lenis, 3 pins, swup): pre-rendered sequence scrubbed per world; type wipes in italic caps; the photo grid assembles around 'Limitée'; material panels slide in pairs.

Measured (`motion/probe.json`): GSAP 3.12.5; 3 pinned sections; Lenis; Swup page transitions; split text; smoothed scroll (median 70 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a sneaker drop as a journey: a 'chargement' loader on clouds, the shoe on a mossy hill above a city haze, the camera diving through chrome scaffolding with pastel tubes, a macro of the outsole ('Inspirée par la ville'), the shoe in a tube-and-foam machine, back to the moss world with mushrooms ('45 années d'expertise', 'Et vous invite'), a concrete floor with the shoe dropped on it, then 'Limitée 1500 pièces' with a photo grid, three colourways and a material breakdown pairing macro textures with wearers. Type: Roboto Flex.
Ground and ink from the measured palette (#E3E6E6, #141B0B, #CFD0BD). Motion carries the page through
a white sneaker floating over a mossy hill above a hazy city skyline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D render sequences, fashion photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D render sequences, fashion photography

## Reference lock

Primary reference/direction: WLKR 76 - Decathlon sneaker launch — A sneaker drop as a journey: a 'chargement' loader on clouds, the shoe on a mossy hill above a city haze, the camera diving through chrome scaffolding with pastel tubes, a macro of the outsole ('Inspirée par la ville'), the shoe in a tube-and-foam machine, back to the moss world with mushrooms ('45 années d'expertise', 'Et vous invite'), a concrete floor with the shoe dropped on it, then 'Limitée 1500 pièces' with a photo grid, three colourways and a material breakdown pairing macro textures with wearers.
Preserve (3-5 traits): 3D shoe through surreal sets; moss, scaffolding and foam worlds; outsole macro; limited-count statement with photo grid; material swatches paired with wearers.
Borrow only (1-2): Give each product claim its own physical world for the object to pass through
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D render sequences, fashion photography
Reject: Tiny buy button
Token commitments: palette #E3E6E6, #141B0B, #CFD0BD, #395423, #829061, #A7A58B; type Roboto Flex; engine GSAP + Lenis linked (never vendored).
