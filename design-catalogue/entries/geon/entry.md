---
title: "GEON"
url: https://geon.au/
source_url: https://geon.au/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/3aafa160d22b934a-screenshot-upload.webp
category: luxury-craft
category2: "institutional"
family: concrete-serif-civic
dna: "Property monograph x civic development catalogue"
register: warm photographic
grammar: gallery/catalog
lane: "A warm mocha hero built from close-up architectural sculpture photography carries a mixed sans/serif-italic headline, drops into a tan info panel paired with an aerial photo, then opens into a full-bleed catalogue of developments"
mode: persuade
traits: ["warm mocha/tan grounds", "mixed bold-sans + serif-italic headline", "close-up architectural sculpture photography", "lowercase serif wordmark", "aerial dusk cityscape photo", "tan info panel beside photo pairing", "full-bleed development catalogue cards", "20-year tenure claim"]
palette: ["#8A7A6B", "#2E2B27", "#F3F0EA", "#FFFFFF", "#6C645C"]
type: ["Monument Grotesk", "GT Super Text"]
measured: designlang
kind: reference-style
source: anton
status: ready
---

## Why it works

The hero photograph isn't a building — it's a close, almost abstract crop of
curved concrete forms, cropped so tight it reads as sculpture before it reads as
architecture. That choice lets a property developer open on texture and warmth
rather than a rendering, which is the more common (and more generic) move for
this category.

The headline mixes two registers in one line: "SHAPING" set bold and sans,
"EXTRAORDINARY" set in a serif italic, both in caps. The pairing signals two
claims at once — the sans half says capability, the serif-italic half says
craft — without needing two separate taglines. "FOR 20 YEARS" underneath, small
and tracked out, adds tenure as a quiet third claim.

Below the hero, the page shifts from atmosphere to substance in one move: a warm
tan info panel sits directly beside an aerial dusk photograph of a real completed
tower, so the reader gets mood first, then evidence, in adjacent blocks rather
than a long scroll between them. The developments section that follows treats
each project as a catalogue entry — name, one-line pitch, "explore" link, full-
bleed photo — which is the right grammar for a developer with a multi-project
pipeline.

## What to borrow (principle)

- **Crop architectural photography tight enough to read as texture or sculpture**
  for the hero, saving the wide establishing shot for later in the page.
- **Pair a bold sans word with a serif-italic word in the same headline** to carry
  two different claims (capability + craft) without two separate lines of copy.
- **Put the credibility panel next to a real project photo**, not above or below
  it — adjacency reads as "here's proof" faster than sequence does.
- **Treat multiple developments as a catalogue**, not a portfolio grid: name, one
  line, one action, one full-bleed image per entry.

## What to leave

- The lowercase serif wordmark is quiet to the point of being easy to miss against
  a busy photographic hero — it needs more contrast or a fixed position to anchor
  brand recognition on first load.
- Warm mocha and near-black panels back to back risk muddiness if not given a
  consistent light-source direction across images; the developments section reads
  slightly darker/cooler than the hero without a clear reason.

## Signature move

The mixed-register headline: one bold sans word, one serif-italic word, same
size, same line, both in caps — "SHAPING" then "EXTRAORDINARY." It compresses two
brand claims (competence, craft) into a single visual unit instead of a tagline
plus a sub-tagline.

## Motion

(from designlang extract) Feel is tagged "mechanical" with scroll-linked
motion confirmed — an apt label: the two keyframes present are a plain
`fadeIn`/`fadeOut` pair (opacity plus a 20px vertical shift, nothing more
expressive), and the dominant easing across the page is flat `linear` (38
uses) rather than any eased curve, with a smaller `ease` group for colour
transitions. Duration climbs in a wide, evenly-spaced ladder from `200ms` up
to `1.25s`, suggesting slower, deliberate reveals for the larger photographic
blocks (hero, catalogue cards) and quicker ones for text/colour states —
consistent with a photography-led page that lets images settle in plainly
rather than performing.

| token | value | role |
|---|---|---|
| `sm`–`lg` | 200–500ms | UI/colour state changes |
| `xl`/`xxl` | 850ms/1.25s | large photographic block reveals |
| linear | `linear` | dominant (38 uses) — flat, mechanical settle |
| ease-in-out | `ease` | secondary (3 uses) — colour transitions |

## Brief

Build a warm, photography-led page for a multi-project property developer. Open
on a tightly cropped, almost abstract architectural or sculptural photograph in
warm mocha tones; set a two-word headline with one word bold sans and one word
serif italic, both caps, plus a small tenure line beneath. Drop to a tan info
panel paired directly beside a real project photo (aerial or exterior), with a
short paragraph and a "learn more" link. Continue into a full-bleed development
catalogue: each entry gets a name, one-line pitch, an "explore" action and a
full-width photo. Keep the wordmark small and lowercase-serif throughout.

## Image recipe

A tight, almost-abstract crop of [SUBJECT] — curved or textured architectural
concrete, stone, or sculptural form — shot in warm late-afternoon or dusk light,
shallow depth of field, no visible horizon or context, colour graded toward warm
mocha and taupe.

## Photo search

Unsplash first, Pexels second.
- "concrete sculpture close up warm light"
- "architectural detail curved form shadow"
- "aerial city dusk tower lights"
- "modern glass building golden hour"

## Reference lock

Primary reference/direction: GEON — warm mocha property-developer page opening on abstract architectural photography, closing on a full-bleed development catalogue.
Preserve (3-5 traits): tightly cropped, near-abstract architectural photography for the hero rather than a wide establishing shot; mixed bold-sans + serif-italic headline pairing for the primary claim; tan/mocha info panel placed directly beside a real project photo; each development treated as a catalogue entry (name, one line, action, full-bleed photo).
Borrow only (1-2): the small tenure line ("FOR 20 YEARS") under the headline; the lowercase serif wordmark.
Role rules: serif-italic reserved for exactly one word per headline, never full sentences; mocha/tan panels always paired with a photo, never standing alone; catalogue entries never carry more than one line of copy before the action link.
Media strategy: photo:unsplash — warm, tightly cropped architectural or sculptural detail for hero use; wider establishing/aerial shots reserved for the catalogue section only.
Reject: architectural render or CGI imagery in place of photography; a portfolio grid instead of a named catalogue; more than one accent typeface pairing per page.
Token commitments: mocha `#8A7A6B`, charcoal `#2E2B27`, paper `#F3F0EA`, white `#FFFFFF`, sage `#5C6E63`; display sans for one headline word, serif italic for the other; wordmark lowercase serif, small and fixed.
