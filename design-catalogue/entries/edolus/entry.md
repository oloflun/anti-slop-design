---
title: "EDOLUS"
url: https://edolus.com/
source_url: https://edolus.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: orbital-satellite-cinematic
dna: "AI infrastructure company x orbital satellite film"
register: cinematic dark
grammar: filmic one-shot
lane: "An AI-infrastructure page that is one continuous camera move: from a black wordmark gate to Earth from orbit, past a satellite unfolding its solar wings, down through the clouds to a glowing 'primary node' emblem."
mode: experience
traits: ["INITIATE SYSTEM gate", "Earth-from-orbit hero", "3D satellite with solar panels", "camera descent through clouds", "heavy grotesque caps labels", "constellation line overlay"]
palette: ["#000000", "#4F5D73", "#1C293E", "#324056", "#818A96"]
type: ["General Sans", "JetBrains Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The claim 'intelligence at planetary scale' is made literal by scale itself: the camera starts in orbit, flies along a satellite's solar array and then plunges through cloud to a single node. Each scroll beat is a change of altitude, so the story reads as zooming in from planet to product.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Tell a scale story as one camera descent (orbit → cloud → object)
- Use clouds as the cut between the space chapter and the product chapter
- Thin constellation lines over the 3D scene to suggest a network

## What to leave

- A gate before any content
- Virtual scroll; the descent has no progress cue

## Signature move

A camera descent from orbit, along a satellite's solar wing and down through the clouds to the product node.

## Motion

Gate: 'EDOLUS' on black, 'INITIATE SYSTEM'. Then: a dark panel of capability cards with a gold ring flashes past, and the camera holds on Earth from orbit (~2 s). Wheel (virtual, WebGL): 'ORBITAL INTELLIGENCE' over a satellite; the camera tracks along the solar array with constellation lines; the satellite banks away; the camera dives into cloud, light rays break through, and a 'PRIMARY NODE' emblem rises.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1; 2 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: INITIATE SYSTEM. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: an AI-infrastructure page that is one continuous camera move: from a black wordmark gate to Earth from orbit, past a satellite unfolding its solar wings, down through the clouds to a glowing 'primary node' emblem. Type: General Sans, JetBrains Mono.
Ground and ink from the measured palette (#000000, #4F5D73, #1C293E). Motion carries the page through
a camera descent from orbit, along a satellite's solar wing and down through the clouds to the product node. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — photoreal space and satellite renders, cloudscapes, one emblem

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: photoreal space and satellite renders, cloudscapes, one emblem

## Reference lock

Primary reference/direction: EDOLUS — An AI-infrastructure page that is one continuous camera move: from a black wordmark gate to Earth from orbit, past a satellite unfolding its solar wings, down through the clouds to a glowing 'primary node' emblem.
Preserve (3-5 traits): INITIATE SYSTEM gate; Earth-from-orbit hero; 3D satellite with solar panels; camera descent through clouds; heavy grotesque caps labels.
Borrow only (1-2): Tell a scale story as one camera descent (orbit → cloud → object); Use clouds as the cut between the space chapter and the product chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: photoreal space and satellite renders, cloudscapes, one emblem
Reject: A gate before any content; Virtual scroll; the descent has no progress cue
Token commitments: palette #000000, #4F5D73, #1C293E, #324056, #818A96; type General Sans, JetBrains Mono; engine GSAP + Lenis linked (never vendored).
