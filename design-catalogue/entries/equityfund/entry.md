---
title: "The Climate and Clean Energy Equity Fund"
url: https://theequityfund.org
source_url: https://theequityfund.org
captured: 2026-09-04
origin: raw-url
raw: raw/09f832a2cef0ce3a-theequityfund-org.webp
extract: ok
category: institutional
category2: ""
family: lavender-advocacy-poster
dna: "Protest photography x civic condensed poster type"
register: editorial print
grammar: typographic poster
lane: "A giant condensed slogan straddles a documentary protest photo in a lavender field, then drops to a cream state-by-state ledger of where the fund operates"
mode: persuade
traits: ["lavender field ground", "oversized condensed display sans", "serif body copy", "photo bleeding through cut-out headline", "maroon ink", "state-map grid", "cream ledger section", "documentary protest photography"]
palette: ["#C4B4E0", "#FCF6ED", "#521224", "#77686A", "#743B43", "#B99498", "#D5C1B4"]
type: ["Judge", "Feature Text", "Metrify Narrow"]
measured: designlang (confirmed)
kind: reference-style
source: claude
status: ready
---

## Why it works

The page pairs one very loud device with one very quiet one and gives each exactly one
job. "HOW WE WIN" is set in an ultra-condensed display sans (Judge) at a size that breaks
out of any normal headline scale, and a single documentary photograph is windowed through
the middle of it so the type reads as a frame around real people rather than a slogan
floating in space. Everything else on the page — the mission paragraph, the state
descriptions — drops into a serif (Feature Text) at conservative body size, so the poster
gesture never repeats and stays singular.

Colour does the organisational work that hierarchy usually does: a warm lavender field
marks the mission/identity zone at the top, and a cream ledger zone below marks the
operating-record zone (states, partners, resources), with deep maroon ink used
consistently across both as the only accent. Because the palette shift is the section
boundary, the page doesn't need rules or cards to tell the reader they've moved from "who
we are" to "where we work."

The state grid is the credibility payload: a small-caps condensed label, a state name in
serif, and a tinted silhouette map, repeated as a plain ruled list rather than a
map visualisation. Like Calyx's priced index, it turns a claim ("we work in 13 states")
into a scannable, literal inventory — the restraint of the list is what makes it read as
fact rather than marketing copy.

The copy voice reinforces the same institutional stance as the layout: friendly in tone but
we-only in pronoun throughout ("HOW WE WIN," "WHAT WE DO"), so the fund narrates its own
action rather than issuing instructions to the reader (from designlang extract).

## What to borrow (principle)

- **Let one photograph interrupt the headline instead of sitting beside it.** Windowing an
  image through oversized type creates a single unmissable focal point without adding a
  second hero element.
- **Use a hard colour-field change as the only section break you need.** A palette shift
  from mission-lavender to record-cream does the job rules and dividers usually do.
- **Turn a claim into a list.** "13 states" becomes 13 named, mapped rows — the inventory
  is more convincing than the number alone.
- **Reserve the display face for exactly one line per page.** Everything else, however
  important, goes into a body serif — the poster line stays singular because nothing
  competes with it.

## What to leave

- The oversized headline's baseline sits close enough to the photo that at narrower
  viewports the crop and the "WIN" descender risk collision — worth a wider photo mask or
  a fixed minimum gap.
- Deep maroon-on-lavender body text (mission paragraph) sits close to the contrast floor
  for extended reading; fine for two short paragraphs, risky if copy grows.
- The state-grid silhouette maps are decorative rather than informational at this size —
  they read as a texture, not a real map; a plain state list would carry the same
  credibility with less production weight.

## Signature move

The photograph windowed through the cut of the giant headline — "HOW WE" above the image,
"WIN" below it, so the type and the photo occupy the same vertical column and the reader's
eye reads slogan-photo-slogan as one continuous unit instead of stacked elements.

## Motion

Feel reads as mixed and the page is technically scroll-linked, but the extract's motion
layer is thin: no keyframe animations were recorded at all, only instant-feeling property
transitions on hover/focus states (colour, background-colour, border-colour, fill, stroke,
transform, grid-template-rows). Every recorded transition rides the same single easing
curve, a standard decelerate `cubic-bezier(0.4,0,0.2,1)`, with no spring or overshoot
variant anywhere. Durations sit short, 100-150ms, consistent with link and button
micro-states rather than section entrances — nothing in the extract animates the hard
lavender-to-cream colour-field break or the windowed photo-through-headline composition, so
that pairing reads as a single static reveal rather than a scroll-triggered sequence. No
stagger or choreography pattern is present in the data. (from designlang extract)

| token | value | used for |
|---|---|---|
| xs | 100ms | fastest hover/focus states |
| (unnamed) | 150ms | colour/background/border/fill/stroke/transform hovers |
| ease (custom) | `cubic-bezier(0.4,0,0.2,1)` | every recorded transition |

## Brief

Build an advocacy-fund landing page anchored on one oversized condensed display slogan
with a documentary photograph windowed through its middle. Ground the hero/mission zone in
a warm lavender field with deep maroon ink; drop to a cream ledger zone below for the
operating record. Set the slogan in an ultra-condensed display sans at a size that exceeds
normal headline scale — one line only, never repeated elsewhere on the page. Set all body
copy, mission statements and descriptions in a body serif at conservative size. Use the
colour-field change alone as the section break between "who we are" and "where we work."
Below the fold, list the operating footprint as a plain ruled grid: label, name, and a
small tinted marker per row, not a live map. Close with resources/news in the same
cream/maroon system.

## Image recipe

Documentary photograph of [SUBJECT] — a civic rally, a statehouse rotunda, a community
organising moment — shot handheld, available light, warm and slightly warm-toned, real
signage and real crowds in frame, no staged studio lighting, cropped to read cleanly when
windowed through large type (a clear horizontal band of legible subject matter through the
middle third of the frame).

## Photo search

Unsplash first, Pexels second.
- "statehouse rotunda rally crowd"
- "community organizing protest signs documentary"
- "civic rally megaphone daylight"
- "state capitol building exterior"

## Reference lock

Primary reference/direction: The Climate and Clean Energy Equity Fund — lavender advocacy
poster, oversized condensed headline windowing a documentary photo, cream state ledger.
Preserve (3-5 traits): lavender mission field paired with cream record field, maroon ink
consistent across both; one oversized ultra-condensed display line per page, never
repeated; body copy always in a conservative serif, never the display face; a photograph
windowed through the headline rather than placed beside it; operating footprint shown as a
ruled list of named, mapped rows.
Borrow only (1-2): the small tinted state-silhouette markers; the small-caps condensed
section labels ("STATES WHERE WE ARE ADVANCING CLIMATE EQUITY").
Role rules: display face appears once per page at poster scale, never at body or button
size; body serif never exceeds two short paragraphs per screen; maroon is the only accent
across both colour fields; section breaks are colour-field changes, not rules or cards.
Media strategy: photo:unsplash — handheld documentary crowd/rally photography, warm
available light, no staged studio shots.
Reject: multiple accent colours; the display face used for body copy or buttons; a live
interactive map in place of the ruled list; centred hero copy; gradient or drop-shadow
treatments on the headline.
Token commitments: bg-mission `#C4B4E0`, bg-record `#FCF6ED`, ink `#521224`, ink-soft
`#743B43`, stone `#77686A`, tint-1 `#B99498`, tint-2 `#D5C1B4`; display `Judge` (or nearest
ultra-condensed grotesque), body `Feature Text` (or nearest text serif), label `Metrify
Narrow`; display set at poster scale only, body conservative, labels small-caps tracked.
