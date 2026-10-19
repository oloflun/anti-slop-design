---
title: "FlowFest 2025 - Manchester"
url: https://www.flowfest.co.uk/
source_url: https://www.flowfest.co.uk/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: retro-rainbow-community-festival
dna: "Webflow community festival x 70s rainbow stripes and cut-out speakers"
register: other
grammar: chaptered editorial
lane: "A community event page on cream: 70s rainbow stripe arches in pink, orange and yellow, 'Webflow chat, festival vibes, good times' in a retro display with highlight boxes, a festival photo, sponsor marquee, speaker cards with cut-out portraits on coloured blocks, 'What to expect' in colour bars, tweets stacking, FAQ and a sun with cut-out attendees in the footer."
mode: persuade
traits: ["70s rainbow stripe arches", "retro rounded display", "highlight boxes on words", "cut-out speaker portraits", "colour bar list", "sun and crowd footer"]
palette: ["#F3ECD3", "#111111", "#E1B142", "#D3876C", "#7E4D37"]
type: ["Sugar Peachy", "Quicksand"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The retro rainbow system is fully committed and every section uses the same stripes, which makes a volunteer event feel like a festival.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One retro stripe motif reused as frame, divider and list

## What to leave

- Small speaker bios

## Signature move

70s rainbow stripes arching around 'FlowFest is back'.

## Motion

Intro: cream, stripes draw in from the corners (~2 s). Wheel (Lenis): stripes slide; the black panel rises with a sponsor marquee; speaker cards pop in; colour bars slide in from the right; tweet cards stack; the sun rises behind the crowd.

Measured (`motion/probe.json`): GSAP 3.13.0; 7 ScrollTriggers; Lenis; Locomotive; Barba page transitions; smoothed scroll (median 121 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a community event page on cream: 70s rainbow stripe arches in pink, orange and yellow, 'Webflow chat, festival vibes, good times' in a retro display with highlight boxes, a festival photo, sponsor marquee, speaker cards with cut-out portraits on coloured blocks, 'What to expect' in colour bars, tweets stacking, FAQ and a sun with cut-out attendees in the footer. Type: Sugar Peachy, Quicksand.
Ground and ink from the measured palette (#F3ECD3, #111111, #E1B142). Motion carries the page through
70s rainbow stripes arching around 'FlowFest is back'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — cut-out photography, event photos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: cut-out photography, event photos

## Reference lock

Primary reference/direction: FlowFest 2025 - Manchester — A community event page on cream: 70s rainbow stripe arches in pink, orange and yellow, 'Webflow chat, festival vibes, good times' in a retro display with highlight boxes, a festival photo, sponsor marquee, speaker cards with cut-out portraits on coloured blocks, 'What to expect' in colour bars, tweets stacking, FAQ and a sun with cut-out attendees in the footer.
Preserve (3-5 traits): 70s rainbow stripe arches; retro rounded display; highlight boxes on words; cut-out speaker portraits; colour bar list.
Borrow only (1-2): One retro stripe motif reused as frame, divider and list
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: cut-out photography, event photos
Reject: Small speaker bios
Token commitments: palette #F3ECD3, #111111, #E1B142, #D3876C, #7E4D37; type Sugar Peachy, Quicksand; engine GSAP + Lenis linked (never vendored).
