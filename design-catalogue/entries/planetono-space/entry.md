---
title: "Planetoño"
url: https://www.planetono.space/
source_url: https://www.planetono.space/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: space-burger-meal-builder
dna: "Burger delivery x cartoon outer space"
register: other
grammar: chaptered editorial
lane: "A fast-food site where a burger, fries and a donut float in red space among cartoon planets; 'HOW IT WORKS' steps (choose meal, size fries, pick snack, claim toy) build the order as items fly into a takeaway box that closes, ending on a map of locations."
mode: persuade
traits: ["red and yellow cartoon space", "3D food floating among planets", "step pills that build the order", "takeaway box that packs and closes", "astronaut cat toy", "sparkle stars"]
palette: ["#EB3321", "#FFC638", "#CA6D40", "#E8DB95"]
type: ["Poppins", "Futura Passata"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The order flow is the animation: each step adds an item that flies into the scene, and at the end everything drops into a box that closes, so 'how it works' is shown as one assembly instead of a list.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Tubik Studio).

## What to borrow (principle)

- Show a multi-step process as items assembling into one container
- Step pills that advance with scroll as the progress indicator

## What to leave

- Two flat hues for the whole page get loud
- Sound toggle in the nav

## Signature move

The meal flying piece by piece into a takeaway box that closes.

## Motion

Intro: red, stars twinkle, 'PLANETOÑO' (~2 s), yellow panel with a red oval where the hero tray rises. Scroll (Lenis, ~120 px glide, WebGL): 'Galaxy Bite' hero; red space with the burger assembling layer by layer; fries, planets and a donut join; step pills 1–4 advance; the box rises and items drop in; the lid closes; 'Gift it to a friend…'; 'Where to find us' map.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1; smoothed scroll (median 140 px still travelling after input stops); entry gate: START. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a fast-food site where a burger, fries and a donut float in red space among cartoon planets; 'HOW IT WORKS' steps (choose meal, size fries, pick snack, claim toy) build the order as items fly into a takeaway box that closes, ending on a map of locations. Type: Poppins, Futura Passata.
Ground and ink from the measured palette (#EB3321, #FFC638, #CA6D40). Motion carries the page through
the meal flying piece by piece into a takeaway box that closes. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — cartoon 3D food and space props on flat red and yellow

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: cartoon 3D food and space props on flat red and yellow

## Reference lock

Primary reference/direction: Planetoño — A fast-food site where a burger, fries and a donut float in red space among cartoon planets; 'HOW IT WORKS' steps (choose meal, size fries, pick snack, claim toy) build the order as items fly into a takeaway box that closes, ending on a map of locations.
Preserve (3-5 traits): red and yellow cartoon space; 3D food floating among planets; step pills that build the order; takeaway box that packs and closes; astronaut cat toy.
Borrow only (1-2): Show a multi-step process as items assembling into one container; Step pills that advance with scroll as the progress indicator
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: cartoon 3D food and space props on flat red and yellow
Reject: Two flat hues for the whole page get loud; Sound toggle in the nav
Token commitments: palette #EB3321, #FFC638, #CA6D40, #E8DB95; type Poppins, Futura Passata; engine GSAP + Lenis linked (never vendored).
