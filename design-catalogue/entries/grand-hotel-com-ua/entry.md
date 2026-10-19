---
title: "Grand Hotel Lviv"
url: https://grand-hotel.com.ua/en
source_url: https://grand-hotel.com.ua/en
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "luxury-craft"
family: burgundy-grand-hotel
dna: "Historic Lviv hotel x serif caps and burgundy panels"
register: warm photographic
grammar: chaptered editorial
lane: "A historic hotel that opens on an oval 'EST 1894' seal, then a facade video under 'WELCOME TO GRAND HOTEL LVIV', followed by room carousels on beige, a spa section, events on burgundy panels, restaurant photos and a casino close."
mode: persuade
traits: ["oval seal loader", "light serif caps headlines", "burgundy and khaki panels", "horizontal room carousel", "large serif marquee lines", "GSAP 3.4"]
palette: ["#CCC6C1", "#3A3838", "#0F0F13", "#797270", "#B9ABA5"]
type: ["HelveticaNeueCyr-Light", "HelveticaNeueCyr-Roman", "HelveticaNeueCyr-Medium", "GTSectraBook"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A classic hotel structure done with discipline: one serif in caps, a strict palette (khaki, burgundy, charcoal), and sections that slide as panels over one another so the long page has clear chapters (rooms, spa, events, dining, casino).

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The First The Last Agency).

## What to borrow (principle)

- An oval seal with the founding year as the loader for a heritage brand
- Panels in a strict two-colour palette to chapter a long hospitality page

## What to leave

- Cookie line along every frame
- Very long; older GSAP

## Signature move

An oval 'EST 1894' seal that opens onto the facade film.

## Motion

Intro: oval seal with 'GRAND HOTEL LVIV EST 1894' (~1.5 s). Scroll (window, 2 pins, SplitText): facade video; pool film; colour-glitch transition; history block; 'STAY WITH US' room carousel; spa; 'SPEND AN ATMOSPHERE' marquee; burgundy events and groups panels; spaces gallery; restaurant & bar; values line; offers; casino.

Measured (`motion/probe.json`): GSAP 3.4.1; 2 pinned sections; 1 video; split text; entry gate: PLAY VIDEO. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a historic hotel that opens on an oval 'EST 1894' seal, then a facade video under 'WELCOME TO GRAND HOTEL LVIV', followed by room carousels on beige, a spa section, events on burgundy panels, restaurant photos and a casino close. Type: HelveticaNeueCyr-Light, HelveticaNeueCyr-Roman, HelveticaNeueCyr-Medium, GTSectraBook.
Ground and ink from the measured palette (#CCC6C1, #3A3838, #0F0F13). Motion carries the page through
an oval 'EST 1894' seal that opens onto the facade film. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — heritage architecture, interiors, spa, food photography with warm grading

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: heritage architecture, interiors, spa, food photography with warm grading

## Reference lock

Primary reference/direction: Grand Hotel Lviv — A historic hotel that opens on an oval 'EST 1894' seal, then a facade video under 'WELCOME TO GRAND HOTEL LVIV', followed by room carousels on beige, a spa section, events on burgundy panels, restaurant photos and a casino close.
Preserve (3-5 traits): oval seal loader; light serif caps headlines; burgundy and khaki panels; horizontal room carousel; large serif marquee lines.
Borrow only (1-2): An oval seal with the founding year as the loader for a heritage brand; Panels in a strict two-colour palette to chapter a long hospitality page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: heritage architecture, interiors, spa, food photography with warm grading
Reject: Cookie line along every frame; Very long; older GSAP
Token commitments: palette #CCC6C1, #3A3838, #0F0F13, #797270, #B9ABA5; type HelveticaNeueCyr-Light, HelveticaNeueCyr-Roman, HelveticaNeueCyr-Medium, GTSectraBook; engine GSAP + Lenis linked (never vendored).
