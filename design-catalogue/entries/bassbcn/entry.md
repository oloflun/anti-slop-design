---
title: "BASS - Barcelona Arts Summer School"
url: https://bassbcn.com/
source_url: https://bassbcn.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: blur-to-sharp-summer-school
dna: "Arts summer school x names that come into focus as they reach the centre"
register: modern clean
grammar: chaptered editorial
lane: "A summer school: dates and a download button over a blurred 'BASS', a black statement, a video 'Welcome to BASS', then a pale gradient section where venues, mentors and guests are listed in large type that is blurred at the edges and sharp only in the middle of the screen, a photo carousel and selection criteria."
mode: persuade
traits: ["names blurred until mid-screen", "pale peach gradient", "huge blurred wordmark", "black statement panel", "video player", "criteria list"]
palette: ["#030303", "#F3F3F3", "#A09C9A", "#D9D4D0", "#2B2928"]
type: ["EaseStandard-Medium"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Focus as scroll position turns a list of 40 names into something you read one at a time.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Digital of Things).

## What to borrow (principle)

- Blur list items until they reach the reading line

## What to leave

- Blur makes skimming hard
- Small criteria text

## Signature move

Names of venues and mentors coming into focus as they cross the middle of the screen.

## Motion

Intro: white with dates, the blurred wordmark fades up (~1.5 s). Wheel (virtual via Barba/Lenis): black panel rises with the statement; the video scales up; the list scrolls with a blur gradient top and bottom so only the centre line is sharp; photos slide in a carousel.

Measured (`motion/probe.json`): GSAP 3.12.4; 29 ScrollTriggers; Lenis; Barba page transitions; 1 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a summer school: dates and a download button over a blurred 'BASS', a black statement, a video 'Welcome to BASS', then a pale gradient section where venues, mentors and guests are listed in large type that is blurred at the edges and sharp only in the middle of the screen, a photo carousel and selection criteria. Type: EaseStandard-Medium.
Ground and ink from the measured palette (#030303, #F3F3F3, #A09C9A). Motion carries the page through
names of venues and mentors coming into focus as they cross the middle of the screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — event photography, video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: event photography, video

## Reference lock

Primary reference/direction: BASS - Barcelona Arts Summer School — A summer school: dates and a download button over a blurred 'BASS', a black statement, a video 'Welcome to BASS', then a pale gradient section where venues, mentors and guests are listed in large type that is blurred at the edges and sharp only in the middle of the screen, a photo carousel and selection criteria.
Preserve (3-5 traits): names blurred until mid-screen; pale peach gradient; huge blurred wordmark; black statement panel; video player.
Borrow only (1-2): Blur list items until they reach the reading line
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: event photography, video
Reject: Blur makes skimming hard; Small criteria text
Token commitments: palette #030303, #F3F3F3, #A09C9A, #D9D4D0, #2B2928; type EaseStandard-Medium; engine GSAP + Lenis linked (never vendored).
