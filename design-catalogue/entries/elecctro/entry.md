---
title: "Elecctro"
url: https://elecctro.com/
source_url: https://elecctro.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: isometric-machine-network
dna: "Vending and kiosk tech company x isometric machine network"
register: modern clean
grammar: live surface
lane: "A vending-tech company whose loader cycles counts ('custom software provided', 'machines delivered'), a blob wipe in navy and orange, then an isometric map where kiosks, a car charger and vending machines appear one by one along connecting lines around the logo."
mode: persuade
traits: ["count-up stat loader with labels", "navy and orange blob wipe", "isometric 3D network of machines", "connecting lines and labels", "orange info toast", "57 ScrollTriggers"]
palette: ["#F3F3F3", "#968570", "#DDDAD5"]
type: ["Poppins"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The business (a network of machines) is drawn as a network: an isometric plan where each machine type pops in on its node, connected by lines to the logo at the centre. Stats in the loader prepare the scale before the map appears.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Draw a distributed business as an isometric network that fills in
- Use the loader to show headline stats with labels

## What to leave

- The map stays static after it fills
- Small labels on the map

## Signature move

An isometric network where machines pop in on nodes around the logo.

## Motion

Intro: counters with labels (custom software 21%, machines delivered 44%, our focus 68%) and small isometric machines (~2.5 s), then a navy/orange blob wipe. Then: 'setting up the scenery', lines draw, machines pop onto nodes one by one with labels; an orange hint toast appears. Wheel did not progress further.

Measured (`motion/probe.json`): GSAP 3.15.0; 57 ScrollTriggers; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Decline, Decline. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the live surface grammar: a vending-tech company whose loader cycles counts ('custom software provided', 'machines delivered'), a blob wipe in navy and orange, then an isometric map where kiosks, a car charger and vending machines appear one by one along connecting lines around the logo. Type: Poppins.
Ground and ink from the measured palette (#F3F3F3, #968570, #DDDAD5). Motion carries the page through
an isometric network where machines pop in on nodes around the logo. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — isometric 3D product renders in yellow and grey

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: isometric 3D product renders in yellow and grey

## Reference lock

Primary reference/direction: Elecctro — A vending-tech company whose loader cycles counts ('custom software provided', 'machines delivered'), a blob wipe in navy and orange, then an isometric map where kiosks, a car charger and vending machines appear one by one along connecting lines around the logo.
Preserve (3-5 traits): count-up stat loader with labels; navy and orange blob wipe; isometric 3D network of machines; connecting lines and labels; orange info toast.
Borrow only (1-2): Draw a distributed business as an isometric network that fills in; Use the loader to show headline stats with labels
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: isometric 3D product renders in yellow and grey
Reject: The map stays static after it fills; Small labels on the map
Token commitments: palette #F3F3F3, #968570, #DDDAD5; type Poppins; engine GSAP + Lenis linked (never vendored).
