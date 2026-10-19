---
title: "Vibrant Wellness - Interactive Digital Health Experience"
url: https://vibrant.noomoagency.com/
source_url: https://vibrant.noomoagency.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: iridescent-3d-head-experience
dna: "Lab-testing wellness brand x iridescent 3D head"
register: modern clean
grammar: filmic one-shot
lane: "A wellness experience: a soft periwinkle orb loader with the logo, then an iridescent 3D head and shoulders on a lilac gradient, 'Personalized Wellness' left, feature list right, female/male toggle and a Start Experience button."
mode: experience
traits: ["iridescent chrome 3D head", "lilac and periwinkle gradient field", "orb loader", "female/male toggle", "Start Experience button", "sound toggle"]
palette: ["#9AB9EF", "#FFFFFF", "#D5D6F2"]
type: ["PlusJakarta Sans Regular", "PlusJakarta Sans Semi Bold", "Ubuntu Mono Bold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The iridescent head makes 'the body' the product in one image and the soft gradient keeps a clinical subject calm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One 3D figure as the whole subject
- Orb loader in the hero palette

## What to leave

- Nothing on scroll before Start Experience
- Low-contrast white text on lilac

## Signature move

An iridescent 3D head on a lilac gradient.

## Motion

Intro: white with a pulsing periwinkle orb and the logo (~2 s), the gradient floods in and the head fades up. No scroll: the head turns slowly and the gradient drifts; content sits behind Start Experience.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: SOUND OFF. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the filmic one-shot grammar: a wellness experience: a soft periwinkle orb loader with the logo, then an iridescent 3D head and shoulders on a lilac gradient, 'Personalized Wellness' left, feature list right, female/male toggle and a Start Experience button. Type: PlusJakarta Sans Regular, PlusJakarta Sans Semi Bold, Ubuntu Mono Bold.
Ground and ink from the measured palette (#9AB9EF, #FFFFFF, #D5D6F2). Motion carries the page through
an iridescent 3D head on a lilac gradient. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL 3D figure

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL 3D figure

## Reference lock

Primary reference/direction: Vibrant Wellness - Interactive Digital Health Experience — A wellness experience: a soft periwinkle orb loader with the logo, then an iridescent 3D head and shoulders on a lilac gradient, 'Personalized Wellness' left, feature list right, female/male toggle and a Start Experience button.
Preserve (3-5 traits): iridescent chrome 3D head; lilac and periwinkle gradient field; orb loader; female/male toggle; Start Experience button.
Borrow only (1-2): One 3D figure as the whole subject; Orb loader in the hero palette
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL 3D figure
Reject: Nothing on scroll before Start Experience; Low-contrast white text on lilac
Token commitments: palette #9AB9EF, #FFFFFF, #D5D6F2; type PlusJakarta Sans Regular, PlusJakarta Sans Semi Bold, Ubuntu Mono Bold; engine GSAP + Lenis linked (never vendored).
