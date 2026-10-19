---
title: "Khanh Nguyen"
url: https://khanhnguyen.design/
source_url: https://khanhnguyen.design/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: horizontal-chapter-folio
dna: "Independent designer folio x horizontal book chapters"
register: editorial print
grammar: chaptered editorial
lane: "A designer folio that pans sideways through chapters like spreads of a book, dark and paper panels alternating, from a year-counter intro through a portrait, a 'THE WORK' title that parts around an image mosaic, to service columns that open on hover."
mode: persuade
traits: ["vertical wheel drives horizontal panning", "year counter intro (2013→2018)", "light-condensed serif display (PP Editorial Old)", "chapter labels I–IV", "title that splits apart around an image mosaic", "service columns 01–04"]
palette: ["#26221F", "#FBF9F5", "#A19E9B"]
type: ["PP Editorial Old", "PP Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The horizontal track makes a career into a book: each chapter is a panel, dark or paper, entered by the wheel moving sideways. The best beat is 'THE WORK': the two words sit far apart and the gap fills with a mosaic of project images that grows until it is the whole spread.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Khanh Nguyen).

## What to borrow (principle)

- Pin one long horizontal track and map the wheel to x when the content is sequential (chapters, years)
- Split a title so its words travel apart and the gap becomes the gallery
- Alternate dark and paper panels so the sideways motion has a visible beat

## What to leave

- Sideways reading on a laptop wheel hides how long the track is
- Small sans body against large serif is close to the default folio look

## Signature move

'THE WORK' parting sideways while an image mosaic grows in the gap.

## Motion

Intro: years count up large in serif on dark (2013 → 2018) over 'A journey through years of design', then the name lands. Scroll (ScrollSmoother, one pinned horizontal track): panels slide left; the dark hero gives way to a paper chapter with a portrait; 'THE WORK' letters travel apart while a mosaic of project images scales up between them; a project name list greys inactive rows; chapter III is four tall columns 01–04 whose image appears on hover; chapter IV client list closes.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 pinned sections; Lenis; 2 video; smoothed scroll (median 188 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a designer folio that pans sideways through chapters like spreads of a book, dark and paper panels alternating, from a year-counter intro through a portrait, a 'THE WORK' title that parts around an image mosaic, to service columns that open on hover. Type: PP Editorial Old, PP Neue Montreal.
Ground and ink from the measured palette (#26221F, #FBF9F5, #A19E9B). Motion carries the page through
'THE WORK' parting sideways while an image mosaic grows in the gap. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screens and product renders arranged as a mosaic, neutral daylight

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screens and product renders arranged as a mosaic, neutral daylight

## Reference lock

Primary reference/direction: Khanh Nguyen — A designer folio that pans sideways through chapters like spreads of a book, dark and paper panels alternating, from a year-counter intro through a portrait, a 'THE WORK' title that parts around an image mosaic, to service columns that open on hover.
Preserve (3-5 traits): vertical wheel drives horizontal panning; year counter intro (2013→2018); light-condensed serif display (PP Editorial Old); chapter labels I–IV; title that splits apart around an image mosaic.
Borrow only (1-2): Pin one long horizontal track and map the wheel to x when the content is sequential (chapters, years); Split a title so its words travel apart and the gap becomes the gallery
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screens and product renders arranged as a mosaic, neutral daylight
Reject: Sideways reading on a laptop wheel hides how long the track is; Small sans body against large serif is close to the default folio look
Token commitments: palette #26221F, #FBF9F5, #A19E9B; type PP Editorial Old, PP Neue Montreal; engine GSAP + Lenis linked (never vendored).
