---
title: "Lucci Lambrusco"
url: https://www.luccilambrusco.com
source_url: https://www.luccilambrusco.com
captured: 2026-09-04
origin: raw-url
extract: ok
category: consumer-brand
category2: playful
family: vineyard-pop-condensed
dna: "Tuscan lifestyle photography x condensed pop sans"
register: warm photographic
grammar: rhythmic cutlist
lane: "A full-bleed vineyard photo op opens the page, then it settles into a beat of cream and brick-red panels that alternate product shot, pull quote and Instagram grid"
mode: persuade
traits: ["age-gated entry", "full-bleed lifestyle hero", "condensed pop-sans headlines", "brick red panel fills", "cream ground", "circular pill CTAs", "script co-founder byline", "instagram social-proof strip"]
palette: ["#B83529", "#211612", "#5A462B", "#EFECCE", "#7E633E", "#898566", "#BCC4BF", "#DCD69D"]
type: ["ABC Ginto Nord Condensed", "ABC Solar"]
measured: designlang (confirmed)
kind: reference-style
source: claude
status: ready
raw: raw/5b510c9546f809f0-www-luccilambrusco-com.webp
---

## Why it works

The page is built on one contrast: a soft, sun-warmed vineyard photograph carrying
the hero, and a hard-edged, all-caps condensed sans (ABC Ginto Nord Condensed)
carrying every headline over it. The condensed weight is heavy enough to sit on
top of a busy landscape photo without a scrim — it reads at a glance from the
letterforms' own density, not from added shadow. Body copy and labels drop to
ABC Solar, an unrelated grotesque, so voice and record are cleanly split the way
Calyx splits serif and mono, just with two sans families instead of serif/mono.

Colour carries the section rhythm rather than the grid. After the photographic
hero, the page alternates full-bleed brick-red panels (headline + pull statement)
with cream panels (product photography + copy), so scrolling reads as a beat —
red, cream, red, cream — before landing on an Instagram strip that borrows the
same red ground. Nothing here is subtle: type is huge, colour blocks are flat and
saturated, and the effect is closer to a poster campaign pinned to a wall than a
considered editorial grid.

The founder photography (a recognisable co-founder, mid-pour glass shots, a
polka-dot-dress candid) does the trust work that copy would otherwise have to
do — the page is short on argument and long on "look who's already drinking
this."

## What to borrow (principle)

- **Let one heavy display face carry text over photography with no scrim.**
  Condensed, all-caps and dense enough to stay legible on a busy background.
- **Alternate two flat colour panels to give scroll rhythm** instead of varying
  layout — brick red and cream, repeated, reads as a designed beat rather than a
  stack of sections.
- **Put a real, recognisable person in the hero** if the brand has one — it
  replaces several paragraphs of trust copy.
- **Age-gate before brand**, but keep the gate typeface and colour identical to
  the site so the wall itself starts building the palette.

## What to leave

- The interstitial age-gate screen breaks first-viewport capture and adds a
  click before any brand content — necessary for a wine brand, but worth noting
  it cost the fold.
- The Instagram carousel repeats photography already shown higher up the page
  without adding new information.
- Body copy is thin — several panels are a headline and a single CTA pill with
  little supporting text, which works here because the celebrity photography is
  doing the persuasion, but it would read as empty on a brand without that asset.

## Signature move

Full-bleed hero photography with the headline set directly onto the image in a
dense condensed caps face — no gradient, no scrim, no dark overlay. The type
survives purely because the letterforms are heavy and tightly set.

## Motion

(from designlang extract) The extract rates overall feel "mixed" rather than
one consistent character, but confirms scroll-linked behaviour throughout.
Four duration steps run from a snappy 100ms up to 500ms, split between a
standard material ease (23 uses) for most state changes and a hard `linear`
curve (13 uses) — no spring or overshoot easing anywhere on the page. The only
keyframe actually driving content is `marqyL`, a horizontal
`translateX(-100%)` slide that runs the Instagram/social-proof strip as a
continuous marquee; a mirrored `marqyR` (`translateX(100%)`) is defined in the
stylesheet but not registered as in-use, so the marquee reads as
one-directional in practice, not a two-lane crawl.

| kind | tokens |
|---|---|
| durations | xs 100ms · sm 200ms · md 300ms · lg 500ms |
| easings | custom `cubic-bezier(0.4, 0, 0.2, 1)` (23×) · linear (13×) |

## Brief

Build a D2C drink landing page anchored on one full-bleed lifestyle photograph
with a heavy condensed all-caps sans set directly onto it — no scrim needed if
the face is dense enough. Split voice from record: condensed caps for every
headline, a plain grotesque for body and labels. Ground in warm cream
`#EFEED0`; use one saturated accent, a brick red `#B73528`, as full-panel fills
that alternate with cream panels going down the page — headline panel, product
panel, headline panel — so scrolling has a colour beat. Close on a social-proof
strip in the same red. Keep CTAs as thin-bordered pill buttons, never filled.

## Image recipe

Documentary lifestyle photograph of [SUBJECT] in a sun-warmed outdoor setting,
golden-hour side light, a real person mid-gesture rather than posed, shallow
depth of field with a soft rural or vineyard background, warm desaturated colour
grading with lifted shadows, no studio lighting, no gradient overlay — shot as a
candid moment, not a product still.

## Photo search

Unsplash first, Pexels second.
- "vineyard golden hour woman wine glass"
- "italian countryside lifestyle candid"
- "wine pour glass close up warm light"
- "friends celebrating wine outdoor candid"

## Reference lock

Primary reference/direction: Lucci Lambrusco — condensed pop-sans over
full-bleed vineyard photography, alternating brick-red/cream panel rhythm.
Preserve (3-5 traits): dense condensed all-caps display face set directly onto
photography with no scrim; brick red `#B73528` and cream `#EFEED0` as the only
two panel grounds, alternating down the page; thin-bordered pill CTAs, never
filled; a real recognisable person carrying the hero and social-proof sections;
short, headline-led copy blocks rather than long paragraphs.
Borrow only (1-2): the age-gate screen (only relevant for alcohol/age-restricted
goods); the Instagram carousel at the close.
Role rules: condensed caps face never used below headline size; body grotesque
never used for a headline; red panels always full-bleed, never boxed or
inset.
Media strategy: photo:unsplash — candid, golden-hour lifestyle photography with
a real subject in motion, never a static product-only shot for the hero.
Reject: gradient or dark scrims behind hero text; more than two panel ground
colours; filled CTA buttons; centred symmetrical layouts.
Token commitments: bg `#EFEED0`, accent `#B73528`, ink `#211612`; display "ABC
Ginto Nord Condensed" all-caps, body "ABC Solar"; panels full-bleed edge to
edge with no max-width container on the colour fill itself.
