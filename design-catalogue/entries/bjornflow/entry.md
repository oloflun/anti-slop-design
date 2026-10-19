---
title: "Bjornflow - Brand Designer and Web Developer"
url: https://www.bjornflow.com/
source_url: https://www.bjornflow.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: freelancer-mockup-strip
dna: "Webflow freelancer x italic serif accents and a strip of site screenshots"
register: cinematic dark
grammar: chaptered editorial
lane: "A freelancer sales page: '_Websites for businesses, practices, and nonprofits that have outgrown theirs' with an italic accent, a strip of site screenshots that grows into one large case (Lendhub, Callisto), a logo strip, about with portrait, 'What makes this approach different' with alternating cases, process cards, testimonials, FAQ and a video call CTA."
mode: persuade
traits: ["italic serif accent words", "screenshot strip that grows", "logo strip", "alternating case rows", "FAQ list", "webcam-style CTA video"]
palette: ["#D4D4D4", "#1E1E1E", "#F0F0F0", "#868D88"]
type: ["Brockmann", "Roboto Mono", "Libre Baskerville"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The webcam-style video at the end makes booking a call feel personal; the rest is a solid conventional sales page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A small webcam-style video for the booking CTA

## What to leave

- Generic layout
- Small text

## Signature move

A strip of site screenshots growing into one large case.

## Motion

Intro: the headline types in (~1 s). Wheel (native): the screenshot strip scales into one case that swaps; logos scroll; cases slide in rows; cards stagger; the FAQ expands; the video panel rises.

Measured (`motion/probe.json`): GSAP 3.15.0; 7 video; split text. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a freelancer sales page: '_Websites for businesses, practices, and nonprofits that have outgrown theirs' with an italic accent, a strip of site screenshots that grows into one large case (Lendhub, Callisto), a logo strip, about with portrait, 'What makes this approach different' with alternating cases, process cards, testimonials, FAQ and a video call CTA. Type: Brockmann, Roboto Mono, Libre Baskerville.
Ground and ink from the measured palette (#D4D4D4, #1E1E1E, #F0F0F0). Motion carries the page through
a strip of site screenshots growing into one large case. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — site screenshots, portrait video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: site screenshots, portrait video

## Reference lock

Primary reference/direction: Bjornflow - Brand Designer and Web Developer — A freelancer sales page: '_Websites for businesses, practices, and nonprofits that have outgrown theirs' with an italic accent, a strip of site screenshots that grows into one large case (Lendhub, Callisto), a logo strip, about with portrait, 'What makes this approach different' with alternating cases, process cards, testimonials, FAQ and a video call CTA.
Preserve (3-5 traits): italic serif accent words; screenshot strip that grows; logo strip; alternating case rows; FAQ list.
Borrow only (1-2): A small webcam-style video for the booking CTA
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: site screenshots, portrait video
Reject: Generic layout; Small text
Token commitments: palette #D4D4D4, #1E1E1E, #F0F0F0, #868D88; type Brockmann, Roboto Mono, Libre Baskerville; engine GSAP + Lenis linked (never vendored).
