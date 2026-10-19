---
title: "The Combine Driver by WOW Factories"
url: https://wowfactories.com/
source_url: https://wowfactories.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: product-tool-exploded-story
dna: "Repairable screwdriver x one product render that turns, explodes and reassembles"
register: modern clean
grammar: chaptered editorial
lane: "A Kickstarter product page on light grey: 'We wanted to make the repair tool repairable' beside the driver, the driver rotating between short claims (dual mechanism, bit interface, ergonomics, compatibility), a white italic serif 'The Combine Driver Stack' title, the bit stack, the driver exploding into its parts for 'Because the world needs repair, and not replacement', recycled-material cards, 'What's in the box' and a footer where the parts scatter around a Kickstarter signup."
mode: persuade
traits: ["one product render through the whole page", "exploded view as a section", "orange accent words", "white italic serif titles over renders", "framed spec cards", "parts scattered in the footer"]
palette: ["#E0E0E0", "#CBCBCA", "#837E7C"]
type: ["Poppins", "georgia"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The product is the signature object and it changes state chapter by chapter (whole, turned, stacked, exploded, scattered), which makes the repairability claim visible.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Explode the product into its parts at the moment you say it is repairable
- Keep one product render on screen and change its state per section

## What to leave

- Signup popup at the start
- Small spec text

## Signature move

A screwdriver exploding into its parts under 'Because the world needs repair'.

## Motion

Intro: a signup popup over a blurred hero, closed (~2 s). Wheel (Lenis ~70-160 px glide, 20 triggers): the driver rotates and moves between framed claim cards; the italic title passes over it; the bit stack spins; the driver separates into parts along its axis; part cards slide in; the box contents lay out; the footer scatters all parts.

Measured (`motion/probe.json`): GSAP 3.13.0; 20 ScrollTriggers; Lenis; 41 video; smoothed scroll (median 117 px still travelling after input stops); entry gate: close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a Kickstarter product page on light grey: 'We wanted to make the repair tool repairable' beside the driver, the driver rotating between short claims (dual mechanism, bit interface, ergonomics, compatibility), a white italic serif 'The Combine Driver Stack' title, the bit stack, the driver exploding into its parts for 'Because the world needs repair, and not replacement', recycled-material cards, 'What's in the box' and a footer where the parts scatter around a Kickstarter signup. Type: Poppins, georgia.
Ground and ink from the measured palette (#E0E0E0, #CBCBCA, #837E7C). Motion carries the page through
a screwdriver exploding into its parts under 'Because the world needs repair'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product 3D renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product 3D renders

## Reference lock

Primary reference/direction: The Combine Driver by WOW Factories — A Kickstarter product page on light grey: 'We wanted to make the repair tool repairable' beside the driver, the driver rotating between short claims (dual mechanism, bit interface, ergonomics, compatibility), a white italic serif 'The Combine Driver Stack' title, the bit stack, the driver exploding into its parts for 'Because the world needs repair, and not replacement', recycled-material cards, 'What's in the box' and a footer where the parts scatter around a Kickstarter signup.
Preserve (3-5 traits): one product render through the whole page; exploded view as a section; orange accent words; white italic serif titles over renders; framed spec cards.
Borrow only (1-2): Explode the product into its parts at the moment you say it is repairable; Keep one product render on screen and change its state per section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product 3D renders
Reject: Signup popup at the start; Small spec text
Token commitments: palette #E0E0E0, #CBCBCA, #837E7C; type Poppins, georgia; engine GSAP + Lenis linked (never vendored).
