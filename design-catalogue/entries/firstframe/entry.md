---
title: "First Frame - Creative Production"
url: https://firstframe.fr/
source_url: https://firstframe.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: production-reel-title-list
dna: "Paris production company x a dark reel with large project titles"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A production company home on black: 'Every story starts with a first frame', a small centred play control, and project titles ('The Walk', 'Lena's Dressing Room', 'Wizarding World', 'Buy the ticket, take the ride', 'Flow', 'They make YouTube') large at the bottom left changing as a mostly dark reel plays."
mode: experience
traits: ["large white project titles bottom left", "dark reel", "small play control", "category tag per project", "dot timeline", "mono intro line"]
palette: ["#000000", "#02162B", "#D3D7D9", "#224C5F"]
type: ["IBMPlexMono", "HKRequisite"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Minimal: the titles do the navigation and the reel stays dark until a project shot appears.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Large project title bottom left as the only navigation

## What to leave

- Cookie panel over frames
- Long dark frames

## Signature move

Large white project titles changing over a dark reel.

## Motion

Intro: black with a counter (~2 s). Scroll (virtual): each step changes the title and the clip; the timeline dot advances.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); 6 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a production company home on black: 'Every story starts with a first frame', a small centred play control, and project titles ('The Walk', 'Lena's Dressing Room', 'Wizarding World', 'Buy the ticket, take the ride', 'Flow', 'They make YouTube') large at the bottom left changing as a mostly dark reel plays. Type: IBMPlexMono, HKRequisite.
Ground and ink from the measured palette (#000000, #02162B, #D3D7D9). Motion carries the page through
large white project titles changing over a dark reel. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial and documentary film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial and documentary film

## Reference lock

Primary reference/direction: First Frame - Creative Production — A production company home on black: 'Every story starts with a first frame', a small centred play control, and project titles ('The Walk', 'Lena's Dressing Room', 'Wizarding World', 'Buy the ticket, take the ride', 'Flow', 'They make YouTube') large at the bottom left changing as a mostly dark reel plays.
Preserve (3-5 traits): large white project titles bottom left; dark reel; small play control; category tag per project; dot timeline.
Borrow only (1-2): Large project title bottom left as the only navigation
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial and documentary film
Reject: Cookie panel over frames; Long dark frames
Token commitments: palette #000000, #02162B, #D3D7D9, #224C5F; type IBMPlexMono, HKRequisite; engine GSAP + Lenis linked (never vendored).
