---
title: "Jaimru Technology - Web Development Company in India"
url: http://jaimru.com/
source_url: http://jaimru.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: gradient-card-stack-services
dna: "Indian web development company x gradient service cards that stack and tilt"
register: modern clean
grammar: chaptered editorial
lane: "A dev company site: a cyan-to-magenta gradient loader with the logo, a black blob shape revealing 'Creative web design', a pill nav marquee, then a long pinned stack of rounded gradient service cards (web design, development, marketing, apps, e-commerce, travel, payments, compliance, security, manpower, e-governance) that tilt and stack, a tech logo grid, industries, testimonials on a blue curve and a client logo wall."
mode: persuade
traits: ["rainbow gradient service cards", "pinned card stack with tilt", "blob shape reveal", "pill marquee", "tech logo grid", "client logo wall"]
palette: ["#020818", "#FFD7EC", "#2B2A33", "#A097A2"]
type: ["DM Sans", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The card stack gives a long list of services one repeated motion; it is the whole page's device.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stack many service cards in one pinned sequence

## What to leave

- Generic gradient styling
- Twelve near-identical cards

## Signature move

Rounded gradient service cards tilting and stacking one over another.

## Motion

Intro: gradient with the logo fading in (~2 s). Wheel (ScrollSmoother, 12 pins): a black blob grows and morphs to reveal the headline; the pill marquee slides; each service card slides up, tilts slightly and stacks on the previous; logos fade in; testimonials curve in on blue.

Measured (`motion/probe.json`): GSAP 3.13.0; 17 ScrollTriggers; 12 pinned sections; ScrollSmoother; WebGL canvas x1 (three.js); 1 video; split text. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a dev company site: a cyan-to-magenta gradient loader with the logo, a black blob shape revealing 'Creative web design', a pill nav marquee, then a long pinned stack of rounded gradient service cards (web design, development, marketing, apps, e-commerce, travel, payments, compliance, security, manpower, e-governance) that tilt and stack, a tech logo grid, industries, testimonials on a blue curve and a client logo wall. Type: DM Sans, Inter.
Ground and ink from the measured palette (#020818, #FFD7EC, #2B2A33). Motion carries the page through
rounded gradient service cards tilting and stacking one over another. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — stock photography and device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: stock photography and device mockups

## Reference lock

Primary reference/direction: Jaimru Technology - Web Development Company in India — A dev company site: a cyan-to-magenta gradient loader with the logo, a black blob shape revealing 'Creative web design', a pill nav marquee, then a long pinned stack of rounded gradient service cards (web design, development, marketing, apps, e-commerce, travel, payments, compliance, security, manpower, e-governance) that tilt and stack, a tech logo grid, industries, testimonials on a blue curve and a client logo wall.
Preserve (3-5 traits): rainbow gradient service cards; pinned card stack with tilt; blob shape reveal; pill marquee; tech logo grid.
Borrow only (1-2): Stack many service cards in one pinned sequence
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: stock photography and device mockups
Reject: Generic gradient styling; Twelve near-identical cards
Token commitments: palette #020818, #FFD7EC, #2B2A33, #A097A2; type DM Sans, Inter; engine GSAP + Lenis linked (never vendored).
