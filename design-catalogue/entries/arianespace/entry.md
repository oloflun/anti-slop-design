---
title: "Arianespace"
url: https://www.arianespace.com/
source_url: https://www.arianespace.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "product-focused"
family: navy-launch-corporate
dna: "Launch provider x navy ground, condensed caps, a mission patch over the Earth, white cards sliding over photos"
register: cinematic dark
grammar: chaptered editorial
lane: "A launch company: 'VA270 MTG-I2' beside a mission patch over the Earth's limb, 'Launch solutions for every mission, to every orbit' with a launch photo, white cards sliding over photos ('We are the experts in launch services', 'Ariane 6 862T' with a rocket in a circle), ground services over a lab photo, a news carousel and a contact footer on the Earth's limb."
mode: persuade
traits: ["mission patch hero", "condensed caps", "white cards sliding over photos", "Earth limb footer"]
palette: ["#00162A", "#FFFEFE", "#728C98", "#394653", "#D9DEDF"]
type: ["Akrobat", "Open Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Opening on the latest mission patch makes a corporate site feel like mission control on launch day.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Lead with the latest real event's emblem

## What to leave

- Generic news carousel

## Signature move

A mission patch over the Earth's limb beside 'VA270 MTG-I2'.

## Motion

Wheel (Lenis): cards slide over photos; images parallax; the carousel drags.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); 1 video; smoothed scroll (median 127 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a launch company: 'VA270 MTG-I2' beside a mission patch over the Earth's limb, 'Launch solutions for every mission, to every orbit' with a launch photo, white cards sliding over photos ('We are the experts in launch services', 'Ariane 6 862T' with a rocket in a circle), ground services over a lab photo, a news carousel and a contact footer on the Earth's limb. Type: Akrobat, Open Sans.
Ground and ink from the measured palette (#00162A, #FFFEFE, #728C98). Motion carries the page through
a mission patch over the Earth's limb beside 'VA270 MTG-I2'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — launch and lab photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: launch and lab photography

## Reference lock

Primary reference/direction: Arianespace — A launch company: 'VA270 MTG-I2' beside a mission patch over the Earth's limb, 'Launch solutions for every mission, to every orbit' with a launch photo, white cards sliding over photos ('We are the experts in launch services', 'Ariane 6 862T' with a rocket in a circle), ground services over a lab photo, a news carousel and a contact footer on the Earth's limb.
Preserve (3-5 traits): mission patch hero; condensed caps; white cards sliding over photos; Earth limb footer.
Borrow only (1-2): Lead with the latest real event's emblem
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: launch and lab photography
Reject: Generic news carousel
Token commitments: palette #00162A, #FFFEFE, #728C98, #394653, #D9DEDF; type Akrobat, Open Sans; engine GSAP + Lenis linked (never vendored).
