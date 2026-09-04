---
title: "Studio Ag"
url: https://studioagriculture.co
source_url: https://studioagriculture.co
captured: 2026-09-04
origin: raw-url
raw: raw/4f5a01d1f4de3cfc-studioagriculture-co.webp
extract: ok
category: portfolio
category2: playful
family: red-rounded-agri-wordmark
dna: "Agri-tech product photography x gutsy rounded-sans wordmark poster"
register: modern clean
grammar: typographic poster
lane: "A giant rounded red wordmark straddles a photograph of a hand sketching on a tablet mockup, then the page opens into plain white space carrying a short mission paragraph and a bold black manifesto line"
mode: persuade
traits: ["oversized rounded bold red wordmark", "photo bleeding through wordmark baseline", "small red italic sub-tagline", "generous white negative space", "bold black condensed manifesto line", "copyright mark as a design element", "minimal top nav", "warm wood-and-hand product photo"]
palette: ["#FFFFFF", "#E7371E", "#000000", "#EEEEEE", "#671235"]
type: ["PP Neue Montreal", "Times New Roman"]
measured: designlang
kind: reference-style
source: claude
status: ready
---

## Why it works

The hero repeats a device this catalogue has already logged from Indoek and EXAMPLE — a
giant wordmark that a photograph bleeds through — but tunes it for a different tone. Here
the wordmark ("Studio Ag") is set in a rounded, friendly, saturated red rather than an
outline or a neutral colour, and the photo peeking above its baseline (a hand annotating a
tablet mockup on a wooden desk) is genuine work-in-progress documentation, not styled
lifestyle imagery — appropriate for an agency selling "gutsy design," not polish. A small
italic red sub-tagline ("Turning dated into daring") sits quietly beneath, doing the same
job the italic accent word does elsewhere in this set, but as a full short phrase rather
than one word.

After the loud red hero, the page opens into a large amount of plain white negative
space before a short, centred mission paragraph appears — the pacing itself communicates
confidence; the agency doesn't need to fill the screen to keep the visitor's attention.
That confidence continues into the next statement, "GUTSY DESIGN FOR THE BRANDS THAT
FEED US," set in bold black condensed capitals with no photography or colour at all —
a second, harder claim delivered in a completely different register from the playful red
hero.

The tiny circled "©" beside the wordmark, sized and weighted to match the wordmark
itself, functions as a design flourish rather than legal boilerplate — it's been folded
into the logotype's shape instead of relegated to a footer.

## What to borrow (principle)

- **Choose a wordmark colour and photo pairing that matches your positioning.** A
  friendly rounded red plus an unstyled work-in-progress photo signals approachable and
  hands-on, differently from an outline wordmark with a curated lifestyle shot.
- **Let a large amount of plain negative space follow a loud hero.** The contrast itself
  reads as confidence, not emptiness.
- **State your positioning twice, in two different registers** — once playful (wordmark +
  sub-tagline), once flatly declarative (a bold black manifesto line) — so both a scanning
  and a reading visitor get the message.
- **Fold a legal or copyright mark into the logotype's own visual weight** rather than
  demoting it to fine print — it becomes a design detail instead of an afterthought.

## What to leave

- This entry's images are derived from the archived raw capture, not a fresh render — the
  live site returned HTTP 200 but did not complete the capture pipeline within budget, so
  treat exact copy and layout as approximate.
- A large gap of unstructured white space between the hero and the mission paragraph
  (roughly a full viewport height in the raw capture) risks reading as a loading or layout
  error on a first visit rather than a deliberate pacing choice, especially without a
  scroll cue.
- The rounded wordmark's baseline sits close enough to the photo above it that a taller
  or busier hero photo would risk collision — the device depends on the specific crop
  used here.

## Signature move

The photo bleeding through the wordmark's ascenders while the mark itself stays in a
warm, friendly red rather than a neutral or outline treatment — combining the "logo as
window" device with a colour choice that signals warmth and craft rather than restraint.

## Motion

Motion feel reads as mechanical, and the page is scroll-linked. The duration scale runs
unusually long for a landing page — five steps from 200ms up to a 1.25s top end — and
easing is limited to a single curve, plain `linear` (6 uses), with no ease-in or ease-out
curve anywhere in the extract; the total absence of deceleration is consistent with the
"mechanical" feel rating, since linear motion reads as machine-driven rather than organic.
Keyframe use is small: `fadeIn` (a plain opacity fade) and `scroll-left` (a horizontal
translate to -100%, most likely powering a continuously-scrolling marquee such as a
client-logo or work strip) are the only two logged as in-use; `fadeOut` and a
`swiper-preloader-spin` keyframe also sit in the raw stylesheet — the latter naming a
Swiper.js carousel dependency, so a slider/gallery component is present on the page even
though it isn't counted as in-use here. No stagger pattern is recorded (from designlang
extract).

| kind | name | value |
|---|---|---|
| duration | `sm` | 200ms |
| duration | `md` | 300ms |
| duration | `lg` | 500ms |
| duration | `xl` | 750ms |
| duration | `xxl` | 1.25s |
| easing | linear | `linear` |
| keyframe | `scroll-left` | slide-x marquee, translateX(0 → -100%) |

## Brief

Build a branding-agency landing page for a specific-niche client base (here, agriculture
and food brands) opening on a giant rounded, warm-coloured wordmark with a photograph
bleeding through its ascenders — the photo should be genuine work-in-progress
documentation (hands, tools, a mockup), not styled lifestyle imagery. Add one small
italic sub-tagline beneath in the same accent colour. Follow with generous plain white
negative space before a short, centred mission paragraph in plain sans. State the
agency's core claim a second time as a bold black condensed manifesto line, in a
completely different register from the hero — no colour, no photography. Fold any legal
mark into the wordmark's own visual weight rather than relegating it to a footer.

## Image recipe

Documentary work-in-progress photograph of [SUBJECT] — a hand annotating a tablet or
sketch, a desk with real tools and materials, a design process moment — shot in natural
warm daylight on a wooden or textured surface, true-to-life colour, unstaged framing,
composed so the top portion (where a wordmark's ascenders would sit) has open, uncluttered
space.

## Photo search

Unsplash first, Pexels second.
- "hand sketching tablet design process desk"
- "designer working wooden desk natural light"
- "apple pencil ipad mockup hand"
- "creative process desk overhead warm light"

## Reference lock

Primary reference/direction: Studio Ag — rounded red wordmark bleeding through a work-in-
progress photo, generous white space before a bold black manifesto line.
Preserve (3-5 traits): a giant rounded, warm-coloured wordmark with a genuine work-in-
progress (not styled lifestyle) photograph bleeding through its ascenders; a small italic
sub-tagline in the same accent colour beneath the wordmark; generous plain white negative
space between the hero and the next content block; the core claim restated a second time
in a completely different, colourless, bold condensed register; a legal/copyright mark
folded into the wordmark's own visual weight.
Borrow only (1-2): the centred, understated mission paragraph in plain sans; the minimal
two-item nav split left and right.
Role rules: the wordmark's accent colour never appears more than twice on the page (mark
and sub-tagline); the manifesto line stays black and colourless, never mixed with the
hero's red; negative space between sections is generous, never filled just to avoid gaps.
Media strategy: photo:unsplash — natural-light, unstaged work-in-progress/process
photography; never a polished, professionally lit lifestyle shot.
Reject: a neutral or outline wordmark treatment where the brief calls for warmth; styled
stock lifestyle photography in place of documentary process shots; cramming the hero and
mission statement together without a negative-space pause; relegating the copyright mark
to a small footer line.
Token commitments: bg `#FFFFFF`, accent-red `#E8381E`, green (photography/UI accent)
`#04674C`, warm-tan `#C3A781`, ink-warm `#312819`, ink-deep `#100904`; rounded bold
grotesque for the wordmark, plain sans for body copy, bold condensed sans for the
manifesto line; wordmark and sub-tagline share the one accent red, manifesto line stays
pure black.
