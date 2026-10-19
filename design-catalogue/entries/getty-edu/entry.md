---
title: "Getty - Tracing Art"
url: https://www.getty.edu/tracingart/
source_url: https://www.getty.edu/tracingart/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "institutional"
family: provenance-image-swarm
dna: "Art provenance research x white page where hundreds of artwork thumbnails swarm into a ribbon, a map of owners and a dense sphere"
register: historical art
grammar: continuous world
lane: "A provenance-index story: 'Tracing ... Art' with a ribbon of artwork thumbnails flowing between the words, the ribbon bursting into a cloud of paintings, a statement beside a Greek vase, one still life followed through its owners with a ledger page from a dealer's stock book, the painting full-bleed, painters as dealers (Morisot, Monet), a piebald horse painting followed through its sales, then all the records as a swarm of thumbnails that forms a ring of collectors, a dense sphere of museum acquisitions and a list of the major players."
mode: read
traits: ["thumbnail swarm as data", "ribbon of artworks between title words", "dealer ledger scan", "one painting followed through owners", "sphere of records"]
palette: ["#FFFFFF", "#0F0E0C", "#B0B6AE", "#3B3C35", "#DFE1DC"]
type: ["Bardford"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Turning the database into a swarm of real artwork thumbnails lets the reader see scale and connection without a single chart.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Resn).

## What to borrow (principle)

- Make the data points the actual images and let them swarm into the next figure

## What to leave

- Very small captions

## Signature move

A ribbon of painting thumbnails flowing between 'Tracing' and 'Art'.

## Motion

Intro: title assembles around the ribbon (~2 s). Wheel (Lenis, 15 triggers, WebGL): thumbnails fly into clusters; a single painting scales to full bleed; the swarm reforms into a ring and a sphere as text steps past.

Measured (`motion/probe.json`): GSAP 3.10.4; 15 ScrollTriggers; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 182 px still travelling after input stops); entry gate: close. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A historical art page in the continuous world grammar: a provenance-index story: 'Tracing ... Art' with a ribbon of artwork thumbnails flowing between the words, the ribbon bursting into a cloud of paintings, a statement beside a Greek vase, one still life followed through its owners with a ledger page from a dealer's stock book, the painting full-bleed, painters as dealers (Morisot, Monet), a piebald horse painting followed through its sales, then all the records as a swarm of thumbnails that forms a ring of collectors, a dense sphere of museum acquisitions and a list of the major players. Type: Bardford.
Ground and ink from the measured palette (#FFFFFF, #0F0E0C, #B0B6AE). Motion carries the page through
a ribbon of painting thumbnails flowing between 'Tracing' and 'Art'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — artwork reproductions, archival scans, WebGL particles

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: artwork reproductions, archival scans, WebGL particles

## Reference lock

Primary reference/direction: Getty - Tracing Art — A provenance-index story: 'Tracing ... Art' with a ribbon of artwork thumbnails flowing between the words, the ribbon bursting into a cloud of paintings, a statement beside a Greek vase, one still life followed through its owners with a ledger page from a dealer's stock book, the painting full-bleed, painters as dealers (Morisot, Monet), a piebald horse painting followed through its sales, then all the records as a swarm of thumbnails that forms a ring of collectors, a dense sphere of museum acquisitions and a list of the major players.
Preserve (3-5 traits): thumbnail swarm as data; ribbon of artworks between title words; dealer ledger scan; one painting followed through owners; sphere of records.
Borrow only (1-2): Make the data points the actual images and let them swarm into the next figure
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: artwork reproductions, archival scans, WebGL particles
Reject: Very small captions
Token commitments: palette #FFFFFF, #0F0E0C, #B0B6AE, #3B3C35, #DFE1DC; type Bardford; engine GSAP + Lenis linked (never vendored).
