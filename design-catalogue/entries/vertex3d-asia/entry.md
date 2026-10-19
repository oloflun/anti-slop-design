---
title: "Vertex3D"
url: https://www.vertex3d.asia/
source_url: https://www.vertex3d.asia/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "portfolio"
family: canyon-to-gallery-3d-studio
dna: "Immersive 3D studio x desert canyon to cave gallery"
register: cinematic dark
grammar: continuous world
lane: "A 3D studio site that is one camera journey: from a modernist house on a red canyon under aurora skies, past a particle globe, into a pale blue cave gallery where each case (digital twin, real estate, SaaS) is an object in a lit room."
mode: experience
traits: ["continuous 3D camera journey", "modernist house on a canyon", "aurora sky and pink particle field", "pale blue cave gallery", "cases as furniture in rooms", "italic-bold mixed headline"]
palette: ["#000000", "#2B252A", "#4A575D", "#989795"]
type: ["Inter", "Lato", "Montserrat", "Oswald"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The studio sells 3D experiences and the site is one: the wheel flies the camera from landscape to house to cave, and every case is placed as an object in the cave (a chair with a portal, a desk with a model), so the portfolio is a museum walk.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Place cases as objects in a 3D room the camera walks through
- Change environment (outdoor canyon → indoor cave) as the chapter break

## What to leave

- Long load with only a logo ring
- Small text over busy scenes

## Signature move

A camera journey from a canyon house into a cave gallery of case objects.

## Motion

Intro: 'V' ring logo loading (~3 s). Scroll (Lenis, 4 ScrollTriggers): 'THE IMMERSIVE EXPERIENCE STUDIO' over the canyon house; camera orbits; particle globe 'TRUSTED BY INDUSTRY LEADERS'; aurora and pink particle field; 'THE WEB IS FLAT, WE FIX THAT'; white void; cave gallery with lit rooms: 'Digital Twin Experience' chair and portal, 'Digital Real Estate' desk model, 'Complex SaaS UX/UI' fireplace.

Measured (`motion/probe.json`): GSAP 3.15.0; 4 ScrollTriggers; Lenis; 6 video; smoothed scroll (median 97 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a 3D studio site that is one camera journey: from a modernist house on a red canyon under aurora skies, past a particle globe, into a pale blue cave gallery where each case (digital twin, real estate, SaaS) is an object in a lit room. Type: Inter, Lato, Montserrat, Oswald.
Ground and ink from the measured palette (#000000, #2B252A, #4A575D). Motion carries the page through
a camera journey from a canyon house into a cave gallery of case objects. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D environments: canyon, aurora, minimalist architecture, blue cave interiors

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D environments: canyon, aurora, minimalist architecture, blue cave interiors

## Reference lock

Primary reference/direction: Vertex3D — A 3D studio site that is one camera journey: from a modernist house on a red canyon under aurora skies, past a particle globe, into a pale blue cave gallery where each case (digital twin, real estate, SaaS) is an object in a lit room.
Preserve (3-5 traits): continuous 3D camera journey; modernist house on a canyon; aurora sky and pink particle field; pale blue cave gallery; cases as furniture in rooms.
Borrow only (1-2): Place cases as objects in a 3D room the camera walks through; Change environment (outdoor canyon → indoor cave) as the chapter break
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D environments: canyon, aurora, minimalist architecture, blue cave interiors
Reject: Long load with only a logo ring; Small text over busy scenes
Token commitments: palette #000000, #2B252A, #4A575D, #989795; type Inter, Lato, Montserrat, Oswald; engine GSAP + Lenis linked (never vendored).
