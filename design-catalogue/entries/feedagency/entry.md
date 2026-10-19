---
title: "FEED Agency"
url: https://www.feedagency.co/
source_url: https://www.feedagency.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: striped-rainbow-production-agency
dna: "NYC production agency x retro rainbow stripes"
register: modern clean
grammar: chaptered editorial
lane: "An agency page with retro rainbow stripes running down the right edge as the nav, a headline 'Playful People first Premium' with small photos set inside the words, a film-strip case carousel, coloured circles, a striped services table, a fan of people photos and big emoji-like numbers."
mode: persuade
traits: ["vertical rainbow stripe nav on the right", "photos set inside headline words", "film-strip carousel with sprocket holes", "colour-striped table", "fanned stack of portraits", "big coloured number circles"]
palette: ["#FAF0E6", "#1A1919", "#DD9675", "#96C0BA", "#7C4C48", "#E4CBB8"]
type: ["Neue Haas Text Pro Roman", "Neue Haas Text Pro Medium", "Neue Haas Text Pro Bold", "Neue Haas Display Pro Black"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The 70s stripe palette (teal, pink, orange) is used as structure: it is the navigation, the table rows and the number circles, so a busy agency page stays coherent. Photos tucked into the headline words introduce the people first.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Use a retro stripe palette as functional structure (nav, table rows)
- Tuck small photos into the headline words
- Film-strip frame for a case carousel

## What to leave

- Barba transitions plus many sections feel long
- Small body text

## Signature move

Rainbow stripes running down the right edge as the navigation.

## Motion

Intro: 'People first Premium' with a photo popping into the gap (~1 s). Scroll (Barba, 20 ScrollTriggers): photos swap inside headline words ('Playful'); '01/09 Feed on our latest work' with a film strip sliding; dark card with coloured circles; striped services table; people photos fan out in 3D as they scroll; testimonials; '1 roof / 42 flow / 57 vision' counters.

Measured (`motion/probe.json`): GSAP 3.15.0; 20 ScrollTriggers; Lenis; Barba page transitions; 12 video; entry gate: Skip to main content. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an agency page with retro rainbow stripes running down the right edge as the nav, a headline 'Playful People first Premium' with small photos set inside the words, a film-strip case carousel, coloured circles, a striped services table, a fan of people photos and big emoji-like numbers. Type: Neue Haas Text Pro Roman, Neue Haas Text Pro Medium, Neue Haas Text Pro Bold, Neue Haas Display Pro Black.
Ground and ink from the measured palette (#FAF0E6, #1A1919, #DD9675). Motion carries the page through
rainbow stripes running down the right edge as the navigation. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — candid production photos and portraits, warm retro grade

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: candid production photos and portraits, warm retro grade

## Reference lock

Primary reference/direction: FEED Agency — An agency page with retro rainbow stripes running down the right edge as the nav, a headline 'Playful People first Premium' with small photos set inside the words, a film-strip case carousel, coloured circles, a striped services table, a fan of people photos and big emoji-like numbers.
Preserve (3-5 traits): vertical rainbow stripe nav on the right; photos set inside headline words; film-strip carousel with sprocket holes; colour-striped table; fanned stack of portraits.
Borrow only (1-2): Use a retro stripe palette as functional structure (nav, table rows); Tuck small photos into the headline words
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: candid production photos and portraits, warm retro grade
Reject: Barba transitions plus many sections feel long; Small body text
Token commitments: palette #FAF0E6, #1A1919, #DD9675, #96C0BA, #7C4C48, #E4CBB8; type Neue Haas Text Pro Roman, Neue Haas Text Pro Medium, Neue Haas Text Pro Bold, Neue Haas Display Pro Black; engine GSAP + Lenis linked (never vendored).
