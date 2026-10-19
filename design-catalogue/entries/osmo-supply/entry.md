---
title: "Osmo - Dev Toolkit Built to Flex"
url: http://osmo.supply/
source_url: http://osmo.supply/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: creative-dev-toolkit-fan
dna: "Webflow resource platform x a fan of resource cards and purple/lime accents"
register: modern clean
grammar: chaptered editorial
lane: "A creative developer toolkit: 'Dev Toolkit * Built to Flex' over a fan of resource cards on an arc, a play reel, founder cards in purple, 'The platform' with the vault UI, tilted feature cards (community, page transition course), pricing on black, 'Made with Osmo' showcase and a giant repeating 'OSMO' footer."
mode: persuade
traits: ["fan of cards on an arc", "purple and lime accents", "handwritten annotations", "tilted feature cards", "dark pricing section", "giant repeating wordmark footer"]
palette: ["#F5F5F5", "#1E2323", "#603FDB", "#9C9E9D", "#D7E8CA", "#B0FD7B"]
type: ["Haffer VF", "Haffer XH", "Haffer Mono", "Brisa Pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The fanned cards show the breadth of resources in one frame and the handwritten notes give a dev product warmth.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fan resource cards along an arc in the hero
- Handwritten annotations beside product UI

## What to leave

- Very small UI text
- Many sections

## Signature move

A fan of resource cards rotating along an arc under 'Dev Toolkit * Built to Flex'.

## Motion

Intro: the hero with the card fan rotating slowly. Wheel (Lenis ~80 px glide, Barba): the fan spins as you scroll; the reel word splits around a video; founder cards slide in; the vault UI scales up; tilted cards fly in; the pricing panel turns dark; 'Made with Osmo' words spread around a card stack; the footer wordmark runs.

Measured (`motion/probe.json`): GSAP 3.15.0; 5 ScrollTriggers; Lenis; Barba page transitions; 36 video; smoothed scroll (median 92 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a creative developer toolkit: 'Dev Toolkit * Built to Flex' over a fan of resource cards on an arc, a play reel, founder cards in purple, 'The platform' with the vault UI, tilted feature cards (community, page transition course), pricing on black, 'Made with Osmo' showcase and a giant repeating 'OSMO' footer. Type: Haffer VF, Haffer XH, Haffer Mono, Brisa Pro.
Ground and ink from the measured palette (#F5F5F5, #1E2323, #603FDB). Motion carries the page through
a fan of resource cards rotating along an arc under 'Dev Toolkit * Built to Flex'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product UI, resource previews

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product UI, resource previews

## Reference lock

Primary reference/direction: Osmo - Dev Toolkit Built to Flex — A creative developer toolkit: 'Dev Toolkit * Built to Flex' over a fan of resource cards on an arc, a play reel, founder cards in purple, 'The platform' with the vault UI, tilted feature cards (community, page transition course), pricing on black, 'Made with Osmo' showcase and a giant repeating 'OSMO' footer.
Preserve (3-5 traits): fan of cards on an arc; purple and lime accents; handwritten annotations; tilted feature cards; dark pricing section.
Borrow only (1-2): Fan resource cards along an arc in the hero; Handwritten annotations beside product UI
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product UI, resource previews
Reject: Very small UI text; Many sections
Token commitments: palette #F5F5F5, #1E2323, #603FDB, #9C9E9D, #D7E8CA, #B0FD7B; type Haffer VF, Haffer XH, Haffer Mono, Brisa Pro; engine GSAP + Lenis linked (never vendored).
