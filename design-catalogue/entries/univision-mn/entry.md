---
title: "FIX-IT - Univision"
url: https://www.univision.mn/game/en/
source_url: https://www.univision.mn/game/en/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "institutional"
family: 3d-town-support-game
dna: "Mongolian telecom support game x low-poly 3D town and avatar picker"
register: illustrated dark
grammar: live surface
lane: "A telecom's support game: a 'FIX-IT' logo with a percent loader, then a bright low-poly 3D town with a waving technician, 'Welcome to FIX-IT' and a Start button that leads to a character picker."
mode: experience
traits: ["low-poly 3D town", "waving mascot", "green and white logo", "percent loader", "character select screen", "sound and language toggles"]
palette: ["#333333", "#298A66", "#6FB76A", "#A4B9AA", "#4B6052", "#CDDEBF"]
type: ["Magicoon", "icomoon", "Montserrat"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Turning troubleshooting into a game in a friendly town lowers the stress of a support task; the mascot carries the brand.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Gamify a chore with a friendly 3D place and a guide character

## What to leave

- No scroll content
- Long loader

## Signature move

A waving technician in a bright low-poly town.

## Motion

Intro: dark grey with the logo and a percent counter (~3 s), the town fades in and the welcome title types. No scroll: the mascot waves and the camera drifts; Start (unlocked) opens a character picker.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: START. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: a telecom's support game: a 'FIX-IT' logo with a percent loader, then a bright low-poly 3D town with a waving technician, 'Welcome to FIX-IT' and a Start button that leads to a character picker. Type: Magicoon, icomoon, Montserrat.
Ground and ink from the measured palette (#333333, #298A66, #6FB76A). Motion carries the page through
a waving technician in a bright low-poly town. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — low-poly 3D scene

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: low-poly 3D scene

## Reference lock

Primary reference/direction: FIX-IT - Univision — A telecom's support game: a 'FIX-IT' logo with a percent loader, then a bright low-poly 3D town with a waving technician, 'Welcome to FIX-IT' and a Start button that leads to a character picker.
Preserve (3-5 traits): low-poly 3D town; waving mascot; green and white logo; percent loader; character select screen.
Borrow only (1-2): Gamify a chore with a friendly 3D place and a guide character
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: low-poly 3D scene
Reject: No scroll content; Long loader
Token commitments: palette #333333, #298A66, #6FB76A, #A4B9AA, #4B6052, #CDDEBF; type Magicoon, icomoon, Montserrat; engine GSAP + Lenis linked (never vendored).
