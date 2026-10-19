---
title: "House of Yellow"
url: https://houseofyellow.nl/
source_url: https://houseofyellow.nl/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: stacked-letter-logo-agency
dna: "Content agency x shape-shifting stacked-letter logo"
register: other
grammar: chaptered editorial
lane: "A content agency whose stacked H-O-Y letters rearrange into new logo shapes over a sequence of full-bleed campaign videos, then the page turns pale yellow for a statement and dark for a phone-mockup of social stats and a three-part service accordion."
mode: persuade
traits: ["stacked-letter logo that recomposes", "full-bleed video sequence behind the logo", "pale yellow ground for statements", "phone mockup with counting social stats", "service accordion (Video / Photography / Animation)", "DrawSVG plus-marks"]
palette: ["#EEECA2", "#0F0F0E", "#612F47", "#351A22", "#937F6E", "#3D7677"]
type: ["icomoon", "Poppins-font"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The logo is the hero animation: three letters stacked in a block keep swapping positions (HOY, YOH, H O Y) while the campaign footage behind them cuts, so the identity is a living mark rather than a static wordmark. The yellow of the name becomes the statement ground, and the service list opens one discipline at a time with thumbnails.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Mees Verberne, Ronald de Groot).

## What to borrow (principle)

- Animate the logo itself as the hero: letters that recompose while footage cuts behind
- Take the brand colour from the name and use it as the reading ground
- A phone mockup whose stats count up as the scroll passes it

## What to leave

- 98 ScrollTriggers for a short page
- Small grey body text on yellow

## Signature move

The H-O-Y letters reshuffling into new stacked shapes over cutting campaign footage.

## Motion

Intro: grey ground, the stacked HOY mark rearranges (~1 s); consent dialog. Hero: full-bleed videos cut (blue concert, street crew, magenta portrait) while the letters recompose over them. Scroll (Lenis, ~80 px glide, SplitText, DrawSVG): pale yellow statement reveals per line; case cards; logo strip; dark section with a phone whose follower/impression counts tick up; 'Video / Photography / Animation' accordion opening each with thumbnails.

Measured (`motion/probe.json`): GSAP 3.12.5; 98 ScrollTriggers; Lenis; 13 video; smoothed scroll (median 100 px still travelling after input stops); entry gate: DENY. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a content agency whose stacked H-O-Y letters rearrange into new logo shapes over a sequence of full-bleed campaign videos, then the page turns pale yellow for a statement and dark for a phone-mockup of social stats and a three-part service accordion. Type: icomoon, Poppins-font.
Ground and ink from the measured palette (#EEECA2, #0F0F0E, #612F47). Motion carries the page through
the H-O-Y letters reshuffling into new stacked shapes over cutting campaign footage. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign and social content stills, saturated night colour, people

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign and social content stills, saturated night colour, people

## Reference lock

Primary reference/direction: House of Yellow — A content agency whose stacked H-O-Y letters rearrange into new logo shapes over a sequence of full-bleed campaign videos, then the page turns pale yellow for a statement and dark for a phone-mockup of social stats and a three-part service accordion.
Preserve (3-5 traits): stacked-letter logo that recomposes; full-bleed video sequence behind the logo; pale yellow ground for statements; phone mockup with counting social stats; service accordion (Video / Photography / Animation).
Borrow only (1-2): Animate the logo itself as the hero: letters that recompose while footage cuts behind; Take the brand colour from the name and use it as the reading ground
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign and social content stills, saturated night colour, people
Reject: 98 ScrollTriggers for a short page; Small grey body text on yellow
Token commitments: palette #EEECA2, #0F0F0E, #612F47, #351A22, #937F6E, #3D7677; type icomoon, Poppins-font; engine GSAP + Lenis linked (never vendored).
