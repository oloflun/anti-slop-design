---
title: "ZINEN - Riverside villa with sauna"
url: https://naturehood-pj.com/zinen/
source_url: https://naturehood-pj.com/zinen/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "luxury-craft"
family: forest-villa-circle-chapters
dna: "Japanese riverside villa x forest film and circle-framed chapter titles"
register: warm photographic
grammar: chaptered editorial
lane: "A private villa near Fukuoka: forest and stream film, a dark green concept section with drifting photos (waterfall, dragonfly, rice terraces) and vertical Japanese text, then full-bleed chapters (Stay, Retreat, Dining, Experience) each with a thin circle around the title and a thumbnail strip, ending in news and access."
mode: read
traits: ["forest and stream film", "dark green ground", "thin circle around chapter titles", "thumbnail strip per chapter", "drifting nature photos", "serif titles"]
palette: ["#3A4340", "#272B27", "#A2A583"]
type: ["minerva-modern", "ten-mincho-text", "tt-commons-pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The same thin circle frames every chapter title over full-bleed photos, giving a calm, consistent rhythm for a retreat.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One thin circle frame repeated around each chapter title

## What to leave

- Small Japanese text

## Signature move

A thin circle framing 'Retreat' over a barrel sauna by a fire.

## Motion

Intro: forest film (~2 s). Wheel: concept photos drift up at different speeds; chapters cross-fade full bleed while the circle and title stay centred; thumbnails switch; the light news panel rises.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 1 video; smoothed scroll (median 205 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a private villa near Fukuoka: forest and stream film, a dark green concept section with drifting photos (waterfall, dragonfly, rice terraces) and vertical Japanese text, then full-bleed chapters (Stay, Retreat, Dining, Experience) each with a thin circle around the title and a thumbnail strip, ending in news and access. Type: minerva-modern, ten-mincho-text, tt-commons-pro.
Ground and ink from the measured palette (#3A4340, #272B27, #A2A583). Motion carries the page through
a thin circle framing 'Retreat' over a barrel sauna by a fire. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — nature and interior photography, film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: nature and interior photography, film

## Reference lock

Primary reference/direction: ZINEN - Riverside villa with sauna — A private villa near Fukuoka: forest and stream film, a dark green concept section with drifting photos (waterfall, dragonfly, rice terraces) and vertical Japanese text, then full-bleed chapters (Stay, Retreat, Dining, Experience) each with a thin circle around the title and a thumbnail strip, ending in news and access.
Preserve (3-5 traits): forest and stream film; dark green ground; thin circle around chapter titles; thumbnail strip per chapter; drifting nature photos.
Borrow only (1-2): One thin circle frame repeated around each chapter title
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: nature and interior photography, film
Reject: Small Japanese text
Token commitments: palette #3A4340, #272B27, #A2A583; type minerva-modern, ten-mincho-text, tt-commons-pro; engine GSAP + Lenis linked (never vendored).
