---
title: "GrabGains - Fitness Platform"
url: https://grabgains.com/
source_url: https://grabgains.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: dark-teal-fitness-app
dna: "Workout app x tilted phone mockups and outline word marquees"
register: cinematic dark
grammar: chaptered editorial
lane: "A fitness app landing page on dark teal with lime accents: tilted phones with 'Welcome champ' over a gym, an outline 'Strength - Progress - Results' marquee, a community video, phone screens, three feature cards, 3D exercise figures, a wall of member photos, reviews, goals, articles and a closing marquee."
mode: persuade
traits: ["dark teal with lime accent", "tilted phone mockups", "outline word marquee", "3D exercise figure renders", "member photo wall", "app store badges"]
palette: ["#02222E", "#33483F", "#87976E"]
type: ["ClashGrotesk", "ClashDisplay", "Archivo"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The tilted phones and outline marquees bring energy to an otherwise standard app page; the 3D exercise figures show the product's content directly.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Outline word marquee as section divider
- 3D figure demonstrating the exercise

## What to leave

- Long list of generic sections
- Small text throughout

## Signature move

Tilted phones over a dark gym with a lime outline marquee.

## Motion

Intro: logo on teal (~1 s), phones slide in tilted. Wheel (Lenis, Barba): marquees slide sideways; the video card scales up; phones tilt back; cards stagger; the 3D figure lifts the bar; the photo wall shifts; articles slide in.

Measured (`motion/probe.json`): Barba page transitions; WebGL canvas x1 (three.js); 3 video; split text; smoothed scroll (median 120 px still travelling after input stops); entry gate: Skip to main content. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a fitness app landing page on dark teal with lime accents: tilted phones with 'Welcome champ' over a gym, an outline 'Strength - Progress - Results' marquee, a community video, phone screens, three feature cards, 3D exercise figures, a wall of member photos, reviews, goals, articles and a closing marquee. Type: ClashGrotesk, ClashDisplay, Archivo.
Ground and ink from the measured palette (#02222E, #33483F, #87976E). Motion carries the page through
tilted phones over a dark gym with a lime outline marquee. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — gym photography, app UI, 3D figures

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: gym photography, app UI, 3D figures

## Reference lock

Primary reference/direction: GrabGains - Fitness Platform — A fitness app landing page on dark teal with lime accents: tilted phones with 'Welcome champ' over a gym, an outline 'Strength - Progress - Results' marquee, a community video, phone screens, three feature cards, 3D exercise figures, a wall of member photos, reviews, goals, articles and a closing marquee.
Preserve (3-5 traits): dark teal with lime accent; tilted phone mockups; outline word marquee; 3D exercise figure renders; member photo wall.
Borrow only (1-2): Outline word marquee as section divider; 3D figure demonstrating the exercise
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: gym photography, app UI, 3D figures
Reject: Long list of generic sections; Small text throughout
Token commitments: palette #02222E, #33483F, #87976E; type ClashGrotesk, ClashDisplay, Archivo; engine GSAP + Lenis linked (never vendored).
