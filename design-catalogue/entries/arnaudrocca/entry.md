---
title: "Arnaud Rocca"
url: https://arnaudrocca.fr/
source_url: https://arnaudrocca.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blob-mask-project-reel
dna: "Design engineer folio x liquid blob masks between projects"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A folio where each project is a full-bleed image or render with its name in spaced light caps at centre, and the next project grows in through an organic blob mask while the title letters scatter and re-form."
mode: experience
traits: ["full-bleed project imagery", "organic blob mask transition", "spaced light caps title at centre", "letters scattering and re-forming", "Roman numeral index"]
palette: ["#121229", "#C0B593", "#8D6951", "#3A2E30", "#644735", "#525B63"]
type: ["ABCArizonaFlare", "ABCArizonaSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Every cut is the same organic blob opening into the next world (a tiger and pool, a pixel arena, roses, a city model), and the title's letters disperse and regather, so the reel feels liquid and continuous despite very different projects.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One organic blob mask as the transition between every project
- Scatter and regather the title letters on each change

## What to leave

- Thin spaced caps over busy images
- Wheel-only navigation

## Signature move

An organic blob that opens each project into the next.

## Motion

Intro: a hairline on brown, a circle opens to the first project while 'MAI LAN - PUMPER' assembles (~1.5 s). Wheel (virtual, WebGL, SplitText): each step grows a blob mask with the next project (Pixel Arena, Panamæra, Adidas Ozworld, The Avener, Complexland) and the title letters scatter and re-form; the reel loops.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x1; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a folio where each project is a full-bleed image or render with its name in spaced light caps at centre, and the next project grows in through an organic blob mask while the title letters scatter and re-form. Type: ABCArizonaFlare, ABCArizonaSans.
Ground and ink from the measured palette (#121229, #C0B593, #8D6951). Motion carries the page through
an organic blob that opens each project into the next. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — music video stills and 3D renders, saturated

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: music video stills and 3D renders, saturated

## Reference lock

Primary reference/direction: Arnaud Rocca — A folio where each project is a full-bleed image or render with its name in spaced light caps at centre, and the next project grows in through an organic blob mask while the title letters scatter and re-form.
Preserve (3-5 traits): full-bleed project imagery; organic blob mask transition; spaced light caps title at centre; letters scattering and re-forming; Roman numeral index.
Borrow only (1-2): One organic blob mask as the transition between every project; Scatter and regather the title letters on each change
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: music video stills and 3D renders, saturated
Reject: Thin spaced caps over busy images; Wheel-only navigation
Token commitments: palette #121229, #C0B593, #8D6951, #3A2E30, #644735, #525B63; type ABCArizonaFlare, ABCArizonaSans; engine GSAP + Lenis linked (never vendored).
