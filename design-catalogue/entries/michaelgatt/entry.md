---
title: "Michael Gatt"
url: https://michaelgatt.com/
source_url: https://michaelgatt.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: film-still-tunnel-composer
dna: "Film composer x 3D tunnel of film stills"
register: cinematic dark
grammar: continuous world
lane: "A composer's site behind 'click anywhere to turn on your sound': stills from every film and game he scored float in a 3D tunnel around a small spaced serif menu."
mode: experience
traits: ["sound-on gate", "3D cloud/tunnel of film stills (WebGL)", "tiny spaced caps serif (Zapf Humanist)", "stepped diagonal gate text", "black ground"]
palette: ["#000000", "#262626"]
type: ["Zapf-Humanist-Demi"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The credits list is turned into a space: dozens of stills hang around the viewer at different depths, so the size of the body of work is felt before any title is read. Type is kept tiny and spaced so the stills do the talking.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Synchronized Studio).

## What to borrow (principle)

- Turn a long credits list into a spatial cloud of stills so quantity reads at a glance
- Keep the menu tiny and centred inside the image field

## What to leave

- Gate text is barely legible
- No scroll path; the cloud only drifts

## Signature move

Film stills floating at depth around the viewer in a 3D tunnel.

## Motion

Gate: 'click anywhere to turn on your sound' in stepped small serif (~2 s), 'enter without sound'. Then the stills fade in from black and drift towards the camera in a tunnel (WebGL, MotionPath); the centred menu (Work, About, Contact, Index view) settles; the cloud drifts with the pointer. The wheel does not scroll a document.

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER WITHOUT SOUND, ENTER WITHOUT SOUND. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a composer's site behind 'click anywhere to turn on your sound': stills from every film and game he scored float in a 3D tunnel around a small spaced serif menu. Type: Zapf-Humanist-Demi.
Ground and ink from the measured palette (#000000, #262626). Motion carries the page through
film stills floating at depth around the viewer in a 3D tunnel. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film and game stills, varied colour, scattered at depth

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film and game stills, varied colour, scattered at depth

## Reference lock

Primary reference/direction: Michael Gatt — A composer's site behind 'click anywhere to turn on your sound': stills from every film and game he scored float in a 3D tunnel around a small spaced serif menu.
Preserve (3-5 traits): sound-on gate; 3D cloud/tunnel of film stills (WebGL); tiny spaced caps serif (Zapf Humanist); stepped diagonal gate text; black ground.
Borrow only (1-2): Turn a long credits list into a spatial cloud of stills so quantity reads at a glance; Keep the menu tiny and centred inside the image field
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film and game stills, varied colour, scattered at depth
Reject: Gate text is barely legible; No scroll path; the cloud only drifts
Token commitments: palette #000000, #262626; type Zapf-Humanist-Demi; engine GSAP + Lenis linked (never vendored).
