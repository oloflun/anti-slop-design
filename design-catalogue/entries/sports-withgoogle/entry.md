---
title: "Google Cloud x Team USA"
url: https://sports.withgoogle.com/teamusa
source_url: https://sports.withgoogle.com/teamusa
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "editorial"
family: ai-sport-physics-story
dna: "AI case story x snowboard footage, white and black chapters, motion-tracking overlays that visualise a trick"
register: modern clean
grammar: chaptered editorial
lane: "A case story: 'Google Cloud x Team USA' beside a halfpipe video, a black chapter with a starfield of sensor points, 'Meet the athletes' with a list of names where the active one shows a portrait and quote, 'The physics no one could see' with footage scattered, the analysis tool's UI (3D pose, flight dynamics with a coloured ribbon tracing the jump), 'The build' with three cards, 'Visualizing the invisible', a skeleton tracking figure, and stories."
mode: read
traits: ["athlete list with active portrait", "motion-tracking overlays", "coloured trajectory ribbon", "black and white chapters", "product UI as evidence"]
palette: ["#FFFFFF", "#C5CCD2", "#0D151A", "#B0AFAF", "#53433C", "#798187"]
type: ["Google Sans Flex"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Showing the tracking ribbon over a real trick makes 'AI measures movement' visible in one frame.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Show the data drawn over the real footage it came from

## What to leave

- Long product text

## Signature move

A coloured ribbon tracing a snowboarder's spin over the footage.

## Motion

Wheel (Lenis): names highlight with portrait swaps; footage scales; the ribbon draws over the jump; the skeleton figure animates.

Measured (`motion/probe.json`): Lenis; WebGL canvas x2; 20 video; smoothed scroll (median 155 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a case story: 'Google Cloud x Team USA' beside a halfpipe video, a black chapter with a starfield of sensor points, 'Meet the athletes' with a list of names where the active one shows a portrait and quote, 'The physics no one could see' with footage scattered, the analysis tool's UI (3D pose, flight dynamics with a coloured ribbon tracing the jump), 'The build' with three cards, 'Visualizing the invisible', a skeleton tracking figure, and stories. Type: Google Sans Flex.
Ground and ink from the measured palette (#FFFFFF, #C5CCD2, #0D151A). Motion carries the page through
a coloured ribbon tracing a snowboarder's spin over the footage. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — sports video, UI overlays

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: sports video, UI overlays

## Reference lock

Primary reference/direction: Google Cloud x Team USA — A case story: 'Google Cloud x Team USA' beside a halfpipe video, a black chapter with a starfield of sensor points, 'Meet the athletes' with a list of names where the active one shows a portrait and quote, 'The physics no one could see' with footage scattered, the analysis tool's UI (3D pose, flight dynamics with a coloured ribbon tracing the jump), 'The build' with three cards, 'Visualizing the invisible', a skeleton tracking figure, and stories.
Preserve (3-5 traits): athlete list with active portrait; motion-tracking overlays; coloured trajectory ribbon; black and white chapters; product UI as evidence.
Borrow only (1-2): Show the data drawn over the real footage it came from
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: sports video, UI overlays
Reject: Long product text
Token commitments: palette #FFFFFF, #C5CCD2, #0D151A, #B0AFAF, #53433C, #798187; type Google Sans Flex; engine GSAP + Lenis linked (never vendored).
