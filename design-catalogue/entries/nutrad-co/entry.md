---
title: "NUTRAD - Furniture OEM and brands"
url: https://nutrad.co.jp/
source_url: https://nutrad.co.jp/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "luxury-craft"
family: japanese-furniture-maker-serif
dna: "Japanese furniture manufacturer x serif caps cut by photo panels"
register: editorial print
grammar: chaptered editorial
lane: "A furniture maker from Okawa: a wood-grain photo inside the 'NUTRAD' wordmark, 'The genuine touch' in serif caps over a tree-ring slice, a vertical Japanese statement, 'Our brands' (bond, Dinasta) on grey, 'FACTORY' in serif caps overlapping a silo photo, labo and factory, then services (brand development, OEM manufacturing, contract service) and news."
mode: read
traits: ["serif caps over photos", "wood-grain and tree-ring imagery", "vertical Japanese text", "grey brand panels", "photo panels overlapping words", "navy menu button"]
palette: ["#FFFFFF", "#C4C6CA", "#23282F", "#595045", "#A69986"]
type: ["cardo", "dnp-shuei-gothic-gin-std", "shippori-mincho-b1", "tt-commons-pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Serif caps laid across factory and material photos give an industrial company a crafted, editorial voice.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Lay a big serif word across the photo it names

## What to leave

- Small Japanese body text unreadable for many visitors

## Signature move

'FACTORY' in serif caps across a steel silo photo.

## Motion

Intro: white with a line loader (~2 s), the wordmark with a photo window. Wheel (Lenis ~120 px glide): words split and slide past photos; images scale in panels; brand panels slide; service titles reveal by line.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; Swup page transitions; WebGL canvas x1; smoothed scroll (median 156 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a furniture maker from Okawa: a wood-grain photo inside the 'NUTRAD' wordmark, 'The genuine touch' in serif caps over a tree-ring slice, a vertical Japanese statement, 'Our brands' (bond, Dinasta) on grey, 'FACTORY' in serif caps overlapping a silo photo, labo and factory, then services (brand development, OEM manufacturing, contract service) and news. Type: cardo, dnp-shuei-gothic-gin-std, shippori-mincho-b1, tt-commons-pro.
Ground and ink from the measured palette (#FFFFFF, #C4C6CA, #23282F). Motion carries the page through
'FACTORY' in serif caps across a steel silo photo. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — factory, material and interior photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: factory, material and interior photography

## Reference lock

Primary reference/direction: NUTRAD - Furniture OEM and brands — A furniture maker from Okawa: a wood-grain photo inside the 'NUTRAD' wordmark, 'The genuine touch' in serif caps over a tree-ring slice, a vertical Japanese statement, 'Our brands' (bond, Dinasta) on grey, 'FACTORY' in serif caps overlapping a silo photo, labo and factory, then services (brand development, OEM manufacturing, contract service) and news.
Preserve (3-5 traits): serif caps over photos; wood-grain and tree-ring imagery; vertical Japanese text; grey brand panels; photo panels overlapping words.
Borrow only (1-2): Lay a big serif word across the photo it names
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: factory, material and interior photography
Reject: Small Japanese body text unreadable for many visitors
Token commitments: palette #FFFFFF, #C4C6CA, #23282F, #595045, #A69986; type cardo, dnp-shuei-gothic-gin-std, shippori-mincho-b1, tt-commons-pro; engine GSAP + Lenis linked (never vendored).
