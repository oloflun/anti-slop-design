---
title: "Mare - the archive that evolves with you"
url: https://mare.run/
source_url: https://mare.run/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: media-cloud-archive-app
dna: "Personal media archive x a cloud of saved items that gathers into a message"
register: cinematic dark
grammar: live surface
lane: "An app home on black: 'Mare. The archive that evolves with you.' in serif surrounded by a 3D cloud of saved items (album covers, articles, photos, posters, notes) floating in depth, then the cloud swirls together as 'Your favourite media is scattered across the internet' becomes 'Mare gathers your media across platforms and formats' with platform icons pulled into the cluster."
mode: persuade
traits: ["3D cloud of saved items", "serif centred title", "cloud gathering into a cluster", "platform icons pulled in", "black ground"]
palette: ["#000000", "#EFEFEC", "#8C796D", "#B7B2A8", "#373334", "#545650"]
type: ["IBM Plex Serif", "IBM Plex Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The product (gathering scattered media) is acted out by the cloud gathering itself; the motion is the pitch.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Act the product out: scatter, then gather the items

## What to leave

- Short capture

## Signature move

A 3D cloud of saved media items gathering into a cluster around a serif line.

## Motion

Intro: black (~1 s), the cloud fades in around the title. Wheel: the cloud drifts; items swirl and pull towards the centre; the line rewrites itself; platform icons fly into the cluster.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; entry gate: Launch Mare. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: an app home on black: 'Mare. The archive that evolves with you.' in serif surrounded by a 3D cloud of saved items (album covers, articles, photos, posters, notes) floating in depth, then the cloud swirls together as 'Your favourite media is scattered across the internet' becomes 'Mare gathers your media across platforms and formats' with platform icons pulled into the cluster. Type: IBM Plex Serif, IBM Plex Sans.
Ground and ink from the measured palette (#000000, #EFEFEC, #8C796D). Motion carries the page through
a 3D cloud of saved media items gathering into a cluster around a serif line. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — media thumbnails

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: media thumbnails

## Reference lock

Primary reference/direction: Mare - the archive that evolves with you — An app home on black: 'Mare. The archive that evolves with you.' in serif surrounded by a 3D cloud of saved items (album covers, articles, photos, posters, notes) floating in depth, then the cloud swirls together as 'Your favourite media is scattered across the internet' becomes 'Mare gathers your media across platforms and formats' with platform icons pulled into the cluster.
Preserve (3-5 traits): 3D cloud of saved items; serif centred title; cloud gathering into a cluster; platform icons pulled in; black ground.
Borrow only (1-2): Act the product out: scatter, then gather the items
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: media thumbnails
Reject: Short capture
Token commitments: palette #000000, #EFEFEC, #8C796D, #B7B2A8, #373334, #545650; type IBM Plex Serif, IBM Plex Sans; engine GSAP + Lenis linked (never vendored).
