---
title: "Lazy Sister - Chinese restaurant"
url: https://www.lazysisterchinese.com/
source_url: https://www.lazysisterchinese.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "playful"
family: restaurant-doodle-pink-red
dna: "Chinese restaurant x pink and red doodles and a chopstick pattern finale"
register: other
grammar: chaptered editorial
lane: "A restaurant site: 'Effortlessly delicious' in italic caps over an interior photo, a pink panel 'Lift a chopstick, not a finger' with black doodle icons floating, cards for 'Congrats on leaving the house' (book a table) and 'Want to stay in?' (takeout), a 'Get lazy' marquee on black, hours and address cards, gift cards, a pattern of red chilli/chopstick shapes and a giant 'LAZY SISTER' footer."
mode: persuade
traits: ["pink and red with black doodles", "italic condensed caps", "witty copy on cards", "curved marquee", "repeating red pattern", "giant footer wordmark"]
palette: ["#F9D5DD", "#151515", "#954247", "#473130", "#A08A90"]
type: ["Labilgroteskvariable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The copy carries the brand (lazy as a virtue) and the doodles and pattern keep it playful and consistent.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Write the two CTAs as jokes for two moods (go out / stay in)

## What to leave

- Short page

## Signature move

'Lift a chopstick, not a finger' with doodles floating on pink.

## Motion

Intro: the interior with the headline. Wheel: the pink panel rises with doodles drifting; cards slide up; the curved marquee runs; the red pattern drops in rows; the footer wordmark rises.

Measured (`motion/probe.json`): GSAP 3.15.0/3.12.2; 5 ScrollTriggers; Lenis; smoothed scroll (median 134 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a restaurant site: 'Effortlessly delicious' in italic caps over an interior photo, a pink panel 'Lift a chopstick, not a finger' with black doodle icons floating, cards for 'Congrats on leaving the house' (book a table) and 'Want to stay in?' (takeout), a 'Get lazy' marquee on black, hours and address cards, gift cards, a pattern of red chilli/chopstick shapes and a giant 'LAZY SISTER' footer. Type: Labilgroteskvariable.
Ground and ink from the measured palette (#F9D5DD, #151515, #954247). Motion carries the page through
'Lift a chopstick, not a finger' with doodles floating on pink. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — interior photography, doodle icons

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: interior photography, doodle icons

## Reference lock

Primary reference/direction: Lazy Sister - Chinese restaurant — A restaurant site: 'Effortlessly delicious' in italic caps over an interior photo, a pink panel 'Lift a chopstick, not a finger' with black doodle icons floating, cards for 'Congrats on leaving the house' (book a table) and 'Want to stay in?' (takeout), a 'Get lazy' marquee on black, hours and address cards, gift cards, a pattern of red chilli/chopstick shapes and a giant 'LAZY SISTER' footer.
Preserve (3-5 traits): pink and red with black doodles; italic condensed caps; witty copy on cards; curved marquee; repeating red pattern.
Borrow only (1-2): Write the two CTAs as jokes for two moods (go out / stay in)
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: interior photography, doodle icons
Reject: Short page
Token commitments: palette #F9D5DD, #151515, #954247, #473130, #A08A90; type Labilgroteskvariable; engine GSAP + Lenis linked (never vendored).
