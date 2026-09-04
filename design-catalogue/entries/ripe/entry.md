---
title: "RIPE"
url: https://www.get-ripe.com/
source_url: https://www.get-ripe.com/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/aff6346cfb01ef79-screenshot-upload.webp
category: playful
category2: ""
family: sky-leadership-poster
dna: "Sky/bird photography x bold poster typography leadership brand"
register: modern clean
grammar: none
lane: "A pale blue sky photograph carries a huge condensed poster headline behind two pill CTAs, then a cream section pairs bold statement copy with prose, closing on a horizontal row of product thumbnail cards"
mode: persuade
traits: ["sky/bird photograph hero", "huge condensed bold poster headline", "dual pill CTA (individuals/companies)", "announcement banner above nav", "cream secondary ground", "bold statement + prose pairing", "horizontal thumbnail card row", "playful merch-style product photography"]
palette: ["#7FADD6", "#EDE6C9", "#14140F", "#D9C7EC", "#B7CBAE", "#F5F0B8"]
type: ["SeriouslyNostalgic Condensed", "Inter"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The headline claim — "LEADERSHIP IS A LIFESTYLE." — is set in a huge, heavy
condensed sans directly over a pale blue sky photograph dotted with small
birds. It's an unusual pairing for a leadership/coaching brand: most competitors
in this space reach for boardrooms or handshakes, while this page reaches for
open sky, which reframes "leadership" as expansive and personal rather than
corporate.

Two pill CTAs sit side by side under the headline — "For Individuals" in cream,
"For Companies" in sage — splitting the audience at the very first decision
point rather than making the visitor guess which path applies to them. An
announcement banner above the nav ("GYMR is here...") adds urgency for existing
followers without competing with the primary headline.

Below the fold, the brand's actual product range — merch, memberships, a
physical calendar/journal — is shown as a horizontal row of styled photography
(a man holding a "GET YOUR MIND RIPE" poster, a spiral-bound calendar, workshop
photography), which grounds the aspirational sky-and-birds opening in tangible,
purchasable things by the second screen.

## What to borrow (principle)

- **Split the audience into two named CTAs at the first decision point**
  ("For Individuals" / "For Companies") rather than a single generic button.
- **Use an unexpected photographic register for the category** (sky and birds
  for a leadership brand, not a boardroom) to stand out from category default
  imagery.
- **Run an announcement banner above the main nav** for time-sensitive news
  without disturbing the hero's own message.
- **Ground an aspirational hero in tangible product photography** within the
  first scroll or two, so the brand isn't all mood and no substance.

## What to leave

- A condensed poster headline this heavy, set directly on a busy sky photograph,
  risks legibility issues at smaller sizes or on lower-contrast crops of the
  same photo.
- Mixing merch photography, testimonial-style portraits and product shots in one
  horizontal row (as the page does below the fold) can read as cluttered without
  a consistent photographic treatment across the row.

## Signature move

The sky-and-birds hero: a plain, almost abstract photograph of clouds and small
distant birds, carrying nothing but a huge poster headline and two pill CTAs —
no product, no portrait, no dashboard. For a personal-development brand, empty
sky reads as aspiration rather than emptiness.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed,
though the captured CSS is thin: a single `400ms` duration token drives
opacity and transform transitions, plus a generic `background, box-shadow`
hover rule and a loading-spinner keyframe. No parallax or marquee keyframe was
captured for the sky/bird hero or the announcement banner, so that read stays
inferred from the image rather than confirmed — consistent with a page whose
richer motion, if any, is likely handled outside the static stylesheet.

| token | value | role |
|---|---|---|
| `md` | 400ms | opacity/transform transitions |

## Brief

Build a playful, aspirational leadership-brand page. Open on a plain sky or
open-air photograph — no people, no product — with a huge condensed bold
headline set directly over it and two pill CTAs splitting the audience
(individual / organization) side by side. Run a slim announcement banner above
the nav for current news. Below the fold, shift to a cream ground pairing a
bold short statement against a longer prose paragraph, then show the actual
product range (merch, physical goods, workshop photography) as a horizontal
row of styled photography to ground the opening mood in real substance.

## Image recipe

An open sky of [SUBJECT] — pale blue, soft clouds, a few small birds in flight,
shot wide with no horizon or landmark visible, bright and slightly
overexposed, no colour grading beyond natural daylight.

## Photo search

Unsplash first, Pexels second.
- "open sky clouds birds flying minimal"
- "pale blue sky birds distant"
- "clear sky daylight negative space"

## Reference lock

Primary reference/direction: RIPE — sky-and-birds hero with a huge poster headline, dual audience-split CTAs, product photography grounding the aspiration below the fold.
Preserve (3-5 traits): plain open-sky photography (no people, no product) as the sole hero image; huge condensed bold headline set directly over the photo; two pill CTAs splitting the audience at the first decision point; an announcement banner above the main nav for time-sensitive news.
Borrow only (1-2): the horizontal row of styled product/merch photography below the fold; the bold-statement-plus-prose pairing on cream.
Role rules: hero photography stays empty of people/product — that's reserved for the product row below the fold; only two CTA pills per hero, each naming its audience explicitly; announcement banner never duplicates the hero's own headline claim.
Media strategy: photo:unsplash — plain, minimal sky/nature photography for the hero; styled, warm product/lifestyle photography for the proof row beneath.
Reject: a boardroom or handshake photograph in place of the sky hero; a single generic CTA with no audience split; overcrowding the product row with more than 4-5 mixed-treatment images.
Token commitments: sky `#7FADD6`, cream `#EDE6C9`, ink `#14140F`, lilac-pill `#D9C7EC`, sage-pill `#B7CBAE`, banner-yellow `#F5F0B8`; condensed bold display sans for headlines, plain sans for body and UI.
