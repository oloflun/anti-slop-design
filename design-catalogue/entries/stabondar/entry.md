---
title: "Stas Bondar - Front-End Developer"
url: https://www.stabondar.com/
source_url: https://www.stabondar.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: text-cube-room-dev
dna: "Front-end developer x a room of text-covered cube walls"
register: cinematic dark
grammar: continuous world
lane: "A developer folio: a dense red paragraph of the bio, letters scattering into space, a project card, then a room made of cube faces covered in text ('Nominee Independent of the Year', 'Won several international awards') in black, red and cream that the camera moves through, scattered photos, and a contact."
mode: experience
traits: ["text-covered 3D cube room", "red accent", "letters scattering", "scrambled text on walls", "scattered photo collage", "small contact list"]
palette: ["#111111"]
type: ["NeueMachina"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Putting awards on the walls of a room you move through makes achievements spatial; the scrambled text is a strong texture.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Write the achievements on the walls of a 3D room

## What to leave

- Very dark first frames
- Scrambled text unreadable

## Signature move

A room of cube faces covered in 'Won several international awards'.

## Motion

Intro: black (~2 s), the red paragraph types. Wheel: letters scatter; the project card appears; the camera enters a room of text cubes that changes colour (black, red, cream); photos scatter; the contact list settles.

Measured (`motion/probe.json`): GSAP 3.11.4; Lenis; WebGL canvas x1 (three.js); 1 video; split text; smoothed scroll (median 216 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a developer folio: a dense red paragraph of the bio, letters scattering into space, a project card, then a room made of cube faces covered in text ('Nominee Independent of the Year', 'Won several international awards') in black, red and cream that the camera moves through, scattered photos, and a contact. Type: NeueMachina.
Ground and ink from the measured palette (#111111). Motion carries the page through
a room of cube faces covered in 'Won several international awards'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL text, photos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL text, photos

## Reference lock

Primary reference/direction: Stas Bondar - Front-End Developer — A developer folio: a dense red paragraph of the bio, letters scattering into space, a project card, then a room made of cube faces covered in text ('Nominee Independent of the Year', 'Won several international awards') in black, red and cream that the camera moves through, scattered photos, and a contact.
Preserve (3-5 traits): text-covered 3D cube room; red accent; letters scattering; scrambled text on walls; scattered photo collage.
Borrow only (1-2): Write the achievements on the walls of a 3D room
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL text, photos
Reject: Very dark first frames; Scrambled text unreadable
Token commitments: palette #111111; type NeueMachina; engine GSAP + Lenis linked (never vendored).
