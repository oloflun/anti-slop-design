---
title: "Studio DADO"
url: https://www.studiodado.com/
source_url: https://www.studiodado.com/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/ce99bea7b20b3cd9-screenshot-desktop.webp
category: portfolio
category2: ""
family: form-follows-feeling
dna: "Cruise-ship interior photography x empathy-led design thesis"
register: warm photographic
grammar: chaptered editorial
lane: "A warm cabin-interior photograph carries a stacked all-caps thesis line crossing the photo/white boundary, then a bold empathy statement in oversized caps sits above a plain two-column studio description"
mode: persuade
traits: ["warm interior photography (cruise cabin)", "stacked oversized headline crossing the photo/white boundary", "small quadrant logomark", "plain nav labels", "giant all-caps empathy statement", "small inset project thumbnail", "two-column plain-prose body", "minimal added colour, photography carries it"]
palette: ["#7A5A3A", "#F7F5F0", "#1A1714", "#C9A15C", "#3A2C22"]
type: ["plain sans (visual match, unverified)"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The headline — "FORM FOLLOWS FEELING" — is set so large it spans the boundary
between the photograph and the white section beneath it, with the last word
("FEELING") landing entirely on white ground while the first two sit on the
photo. That single typographic decision does the studio's whole argument for
it: the words literally move from image to plain page, echoing "form" (the
photographed space) giving way to "feeling" (the white, textual, conceptual
part of the page).

The photography itself is warm and specific — a real, warmly lit cabin
interior with a canopy bed frame, brass details and patterned wallcovering —
rather than a generic "luxury interior" stock shot, which matters for a studio
whose actual client base is cruise lines and hospitality: the reference photo
needs to look like a real commission, not an aspiration board.

Below the headline break, the page states its thesis in plain block caps
("EMPATHY SHAPES EVERYTHING WE CREATE...") directly above a small inset project
thumbnail and a two-column plain-prose description — no bullet list, no
feature grid, just two paragraphs of continuous prose. For a studio selling
emotional/experiential design thinking, writing in continuous sentences rather
than fragmented marketing copy matches the message to the medium.

## What to preserve

- **Let a headline span the boundary between photograph and white ground**,
  with the meaning of the words tracking the visual transition (image → page,
  or feeling → thought).
- **Use a real, specific commissioned-work photograph for the hero**, not a
  generic aspirational interior, when the client base needs to recognise their
  own category in the reference.
- **State your thesis in plain block caps, then support it with continuous
  prose**, not a bulleted feature list, when the pitch is conceptual rather than
  transactional.
- **Keep the palette almost entirely photographic** — let the warm tones of the
  interior itself carry the brand colour, adding little to no separate accent.

## What to leave

- A headline spanning the image/white boundary is a striking one-time device;
  it needs careful responsive handling since the split point depends on exact
  photo crop and viewport width.
- Two full paragraphs of continuous prose this early risks losing visitors who
  want to see project variety before reading a philosophy — a "see our work"
  link near the thesis would help.

## Signature move

The boundary-spanning headline: "FORM FOLLOWS FEELING" set at a scale where the
first words sit on the hero photograph and the final word lands on the white
section below, so the type itself performs the transition from image to
argument.

## Motion

(from designlang extract) Feel is "responsive" with scroll-linked motion
confirmed. The captured transitions sit on a slow `500ms`–`1s` pair, almost
entirely on one strong decelerating ease-out (`cubic-bezier(0.23,1,0.32,1)`,
29 uses) with a smaller `ease` group for opacity crossfades — a slower,
heavier settle than most of this catalogue's Framer/Tailwind pages, which
fits a photography-led studio site more invested in a considered image
transition than snappy UI feedback. No keyframes were captured beyond these
transitions, consistent with the "simple crossfade" read already in this
entry.

| token | value | role |
|---|---|---|
| `lg` | 500ms | transform/opacity transitions |
| `xl` | 1s | slower transform settle |
| ease-out | `cubic-bezier(0.23,1,0.32,1)` | dominant (29 uses) |
| ease-in-out | `ease` | opacity crossfades (8 uses) |

## Brief

Build a warm, photography-led interior-design studio page around a single
conceptual thesis. Open on one real, specific commissioned-space photograph
(not generic luxury stock) with a short nav and a small quadrant logomark.
Set a 2-3 word thesis headline at a scale large enough to span the boundary
between the photograph and the white section beneath it, so the type visually
performs the argument. Below, restate the thesis in plain oversized block caps,
paired with a small inset project thumbnail and two columns of continuous
prose — no bullet lists. Keep the palette almost entirely photographic, adding
minimal separate accent colour.

## Image recipe

A warm, specific interior of [SUBJECT] — real commissioned space, brass or
gold fixture details, patterned or textured wallcovering, warm lamp light
against cooler ambient light, shot at a considered angle that shows both
texture and layout, no visible people.

## Photo search

Unsplash first, Pexels second.
- "luxury cabin interior warm brass lamp"
- "hotel suite interior warm lighting detail"
- "boutique interior canopy bed textured wall"

## Reference lock

Primary reference/direction: Studio DADO — a headline spanning the photograph/white boundary, thesis restated in block caps above continuous two-column prose.
Preserve (3-5 traits): a real, specific commissioned-space photograph (not generic luxury stock) for the hero; a short thesis headline set large enough to span the image/white boundary, its meaning tracking the visual transition; thesis restated in plain block caps directly above continuous prose, no bullet lists; palette carried almost entirely by the photography itself.
Borrow only (1-2): the small inset project thumbnail beside the prose; the small quadrant logomark.
Role rules: boundary-spanning headline used once per page (the primary thesis only); prose sections stay in continuous sentences, never bulleted; added accent colour capped at what the photography itself contains.
Media strategy: photo:unsplash — real, warm, specific interior photography only; no CGI renders, no generic "luxury lifestyle" stock.
Reject: a bulleted feature list in place of continuous prose; a generic aspirational interior photo standing in for real commissioned work; adding a separate brand accent colour beyond what the photography carries.
Token commitments: warm-brown `#7A5A3A`, paper `#F7F5F0`, ink `#1A1714`, brass-gold `#C9A15C`, umber `#3A2C22`; plain sans for all type, headline set in oversized block caps.
