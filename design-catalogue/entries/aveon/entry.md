---
title: "Avéon (interior design template)"
url: https://aveon.framer.website/
source_url: https://aveon.framer.website/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/f8977101fef085af-screenshot.webp
category: portfolio
category2: ""
family: brooklyn-bento-atelier
dna: "Live-clock console header x interior photo bento grid"
register: warm photographic
grammar: gallery/catalog
lane: "A cream header carries a live clock and a small show-reel thumbnail rather than a full hero photo, drops into a giant black headline, then opens into a dense nine-photo interior bento grid on black"
mode: persuade
traits: ["cream header with live date/time readout", "small show-reel video thumbnail in place of a full hero photo", "star-rating trust line", "right-aligned vertical service list", "giant black headline crossing cream ground", "dense nine-photo bento grid on black", "dark closing services panel"]
palette: ["#E4DCCB", "#171410", "#B4784A", "#FFFFFF", "#8C7A62"]
type: ["Geist", "Inter Display"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The header withholds the expected full-bleed hero photo, replacing it with a
small "SHOW REEL" video thumbnail, a live location/date/time readout
(`BROOKLYN - NEW YORK`, a real clock ticking), and a star-rating trust line —
more console than hero. It's an unusual restraint for an interior-design
studio, where a big atmospheric room photo is the category default; here the
metadata itself (place, time, rating) is doing the opening work instead.

A giant black headline ("SPACES THAT TELL A STORY") then takes the full width
on cream, functioning as the page's actual visual anchor in place of a hero
image — type as the hero, not photography.

The real photographic payload arrives afterward as a dense, nine-image bento
grid on black ground: kitchens, bathrooms, hallways and courtyards shown at
once, uneven tile sizes, all outlined in thin borders. Rather than a slow
photographic narrative (one room, then the next), the studio shows its whole
range in a single glance — a catalogue view rather than a story, despite the
headline's claim.

## What to borrow (principle)

- **Replace a full hero photograph with a metadata console** — a small video
  thumbnail, a live clock, a location tag — when you want restraint over
  spectacle in the first screen.
- **Let a giant headline serve as the actual visual anchor** of a section, in
  place of an image, when the copy itself is strong enough to hold the space.
- **Show your full photographic range as one dense bento grid** rather than a
  slow one-image-at-a-time scroll, when breadth is the more persuasive claim
  than any single room.
- **Pair a star-rating with a specific client-count** ("trusted by 200+
  homeowners") rather than either alone, for a fast, legible trust signal.

## What to leave

- A live, ticking clock in the header is a small technical flourish that adds
  engineering overhead for very little persuasive return — it's a template
  signature more than a brand asset.
- A nine-image bento grid this dense, with no captions or project names, asks
  a lot of the reader to infer context; at minimum a hover state naming each
  space would help.
- The headline's claim ("spaces that tell a story") sits oddly against a grid
  structure built for breadth-at-a-glance rather than narrative sequence — the
  copy and the layout are making different arguments.

## Signature move

The metadata console in place of a hero photo: a small show-reel thumbnail, a
live location/date/time readout, and a star-rating line stand in for the
expected full-bleed atmospheric interior shot, deferring the big photography
until after the headline.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed,
though the captured CSS only carries a single `250ms` opacity transition and
a generic `background, box-shadow` hover rule, plus a loading-spinner
keyframe. No staggered bento-tile reveal was captured in the static CSS — the
grid's fade/scale-in, if present, is most likely driven by Framer's inline
whileInView animation rather than a CSS keyframe, so that read stays inferred
from the image.

| token | value | role |
|---|---|---|
| `sm` | 250ms | opacity transitions |

## Brief

Build a restrained interior-design studio page that defers its hero
photography. Open on a cream header with a small show-reel video thumbnail, a
live location/date/time readout, a star-rating trust line, and a right-aligned
vertical service list — no full hero image yet. Let a giant black headline
serve as the visual anchor of the next section. Follow with a dense bento grid
of 8-10 real project photographs on black ground, uneven tile sizes, thin
borders, shown all at once rather than one room at a time. Close on a dark
panel restating the studio's full-spectrum service offering.

## Image recipe

A set of real interior spaces — kitchens, bathrooms, living areas, courtyards —
shot with natural warm light, considered material detail (marble, wood,
brass), varied angles and crops so a dense grid of them reads as textured
rather than repetitive, no visible people.

## Photo search

Unsplash first, Pexels second.
- "warm interior kitchen natural light detail"
- "marble bathroom interior design detail"
- "courtyard interior warm light architectural"

## Reference lock

Primary reference/direction: Avéon — a metadata console replacing the hero photo, a giant black headline as visual anchor, a dense nine-image bento grid on black.
Preserve (3-5 traits): a metadata console (show-reel thumbnail, live clock, location tag, star rating) in place of a full hero photograph; a giant headline serving as the section's visual anchor rather than an image; a dense bento grid showing the full photographic range at once rather than a sequential narrative; a right-aligned vertical service list as understated navigation.
Borrow only (1-2): the star-rating-plus-client-count trust line; the dark closing services panel.
Role rules: bento grid tiles never carry more than a thin border, no heavy captions; headline copy must match the layout's actual argument (breadth vs. narrative) rather than contradict it.
Media strategy: photo:unsplash — warm, real interior photography with varied crops and angles for grid texture; no CGI renders.
Reject: a full-bleed hero photograph replacing the metadata console (defeats the device); a bento grid with uniform tile sizes; headline claims that contradict the layout's actual structure.
Token commitments: cream `#E4DCCB`, black `#171410`, terracotta `#B4784A`, white `#FFFFFF`, warm-stone `#8C7A62`; bold sans for all type, headline set at giant scale as the visual anchor.
