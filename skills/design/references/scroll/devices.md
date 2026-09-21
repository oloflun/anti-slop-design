# The device kit, condensed

Nine ways scroll can drive the page. Pick per beat, never per page: ≥4 device
families, never the same one twice running. Every act publishes `--sc-p` (0–1)
on itself, so bespoke CSS can ride the same value the kit devices use. Full
depth, worked examples, and every trap: `upstream/scroll-craft/.../references/devices.md`.

| # | Device | Syntax | Span / rate | One-line rule |
|---|---|---|---|---|
| 1 | `scrub` | `data-sc-act="scrub" data-sc-span="2.6" data-sc-dwell="0.35"` on the section; `data-sc-scrub data-sc-src="…"` on the `<video>` | span 2.2–3.0 for a hero | ≤2 per page. The wheel scrubs a pre-rendered clip; spend it on the open |
| 2 | `pin` | `data-sc-act="pin" data-sc-span="3"` | span ≥1.2 (below that, progress jumps 0→1 in one notch) | The frame holds, copy states cross over inside it |
| 3 | `pan` | `data-sc-act="pan" data-sc-span="3.2"`; rail gets `data-sc-pan="0.08"` | ~1vh per item + 1 | Lateral = breadth, not hierarchy. Overflow must be measured, not assumed |
| 4 | `reveal` | `data-sc-reveal="up|down|left|right|iris" data-sc-reveal-at="0.15 0.55"` | — | `clip-path` wipe = change of state. `iris` once per page at most |
| 5 | `kinetic` | `data-sc-kinetic="lines|words|chars"` on a cued heading | — | Lines almost always right, chars ~never. One kinetic headline per act |
| 6 | `parallax` | `data-sc-parallax="-0.6"` | rate is **hundreds of px total travel**, not a fraction — usable range 0.3–1.5 (framed), 1–2 (full-bleed) | Never on body copy. 3 layers is plenty |
| 7 | `count` | `data-sc-count="0 4,200" data-sc-count-at="0.1 0.5"` | 1.2–1.8s outside an act (`data-sc-count-ms`) | Only real numbers. No verified figure, no counter |
| 8 | `flow` + `in` | `data-sc-in data-sc-stagger="70"` on the wrap | stagger 30–80ms | The rest of the page. Fires once, opacity+14px rise, ~620ms ease-out |
| 9 | pointer: `tilt` / `magnet` / `spotlight` | `data-sc-tilt="7"` (5–9°), `data-sc-magnet="0.28"` (0.2–0.35, CTA only), `data-sc-spotlight` (publishes `--sc-mx`/`--sc-my`) | — | Gated to `(hover:hover) and (pointer:fine)`. Never gated on reduced motion (F-011, superseded 2026-09-07) |

`drift` (`data-sc-drift="#0A0806"` on an act) is not a device, it's a
property: the page ground interpolates toward it while the act is live. 3–5
stops, one theme family. On a page of many *short* acts several can be
part-way through at once — paint grounds per section instead of drifting; see
upstream §10.

## The cue contract — what verification actually catches you on

`data-sc-cue="from [to [rampIn [rampOut]]]"`, all in act progress 0–1.

| Form | Behaviour |
|---|---|
| `"0.2"` | fades in at 0.2, **holds to the end of the act** |
| `"0.1 0.6"` | in, plateau, out (ramps default 30% of window each) |
| `"0 0.78 0"` | **greet**: full opacity at act start, then fades — the hero form |
| `"0 1 0 0"` | **greet and hold**: full at p=0, no ramp either end |

**The plateau is the point.** Without one, a cue is a triangle that touches full
opacity for a single instant, so the reader has to stop on exactly the right
pixel to see the line at full strength and every heading reads slightly faded.
`"0.1 0.9 0.15 0.4"` — fast in, long slow out — is the confident form. Cue
windows on a pinned act **overlap by design**, roughly 15% of the act: the
outgoing line is still fading while the next arrives, and a gap between cues
reads as a loading failure.

Five rules, each one a real bug this fixture has caught:

- **A hero cue needs the greet form.** A plain `"0 0.7"` means the first
  screen every visitor sees has no headline on it.
- **The last act's cue must hold** (one value). A two-value close cue fades
  the CTA out before the page ends.
- **Only the last act may hold.** A one-value cue on a *middle* pinned act
  stays lit through the whole un-pin slide — the line travels a full viewport
  up, crosses fixed chrome, overlaps the next section. Invisible until
  measured; shows up as a contrast failure nobody meant.
- **Ground or greet.** A pinned stage is fully visible ~1vh *before* its own
  progress leaves 0. A plain two-value first cue shows an empty stage for
  that whole travel — give the act a ground (image/colour already doing
  work) or open with a greet cue.
- **Clip time ≠ cue time.** A `scrub` clip is mapped across the stage's
  *entire visible life* (default), not across the pinned travel, because the
  stage is on screen for a viewport before the pin starts and after it ends.
  Cues keep using `p` (they belong to the pin); the clip uses a separately
  computed `vp`. Reaching for `data-sc-clip-map="travel"` reintroduces the
  freeze — there's almost no reason to.

Two more that a harness will not catch by itself:

- **Pan overflow must be measured, not assumed.** The rail travels exactly
  `scrollWidth - viewport`; a rail narrower than the viewport travels **zero**
  and the act reads as a still. `rail.scrollWidth - innerWidth` — check it,
  don't guess.
- **Parallax rate is hundreds of pixels total, not a viewport fraction** — see
  the table above. A rate of 0.35 across three viewport-heights of scroll is
  35px: invisible.

Composing an act: devices stack (a pinned stage can hold a scrub clip, a
parallax layer, a kinetic headline, a spotlight at once), but one thing is the
reason the act exists — say that thing in one sentence or the act has none.

## The playhead is lerped (§1)

The mechanism the whole kit's smoothness rests on, and the one F-012 kept
being blamed on. **Scroll never writes `currentTime`.** It writes a *target*,
and a standalone rAF loop walks the clip toward that target at a fixed
fraction per frame:

> *"Wheel events do not arrive at a constant rate, so a 1:1 write reproduces
> every gap in them and the clip reads as a stutter rather than a glide."*

Three mechanisms, all on by default:

- **Lerp 0.18 per frame.** `data-sc-lerp` overrides it, on the mount root for
  the whole page or on a single `<video>`. **Clamped to 0.02–1 and never read
  as 0** — a 0 lerp is a playhead that never moves. Reach for an override only
  when a page's clips are short enough that 0.18 visibly lags the hand.
  Worldflight wants 0.12 instead; see [`pace.md`](pace.md).
- **Deadband: 8 ms desktop, 20 ms mobile.** A write smaller than that costs a
  seek and shows nothing; on a phone it costs more than it shows.
- **Seek coalescing.** No seek is queued while the decoder is still resolving
  the last one. *"A fast flick otherwise piles seeks up and freezes the clip."*

An offscreen clip that has already reached its target stops being touched at
all. (Upstream states the offscreen skip without a threshold value; the 0.002
figure belongs to `shoot.mjs`'s settle test, below, not to this skip.)

This applies to **every** scrub clip on the page, act or worldflight. It is
also why the shooter waits for the playhead to arrive before each frame:

> *"A frame captured mid-lerp is a frame the page never actually holds."*

`shoot.mjs` settles on `|current − target| < 0.002 && !seeking`. Any harness
the chain runs against a scrubbed page inherits that requirement — a
screenshot taken mid-lerp makes the run unrepeatable, not merely imprecise.

Upstream also drops the damping to 1.0 (no smoothing at all) under reduced
motion. **That branch does not port: F-011.** The lerp is unconditional here,
which is the correct behaviour anyway — it is a smoothing mechanism, not an
effect, and turning it off is what produces the stepping fault.

## Layered scenes: where the premium feel comes from (§6)

Ported from `devices.md` § 6, measured off a reference premium site and proven
on a live build. A flat page moves as one sheet; a layered page is a stack of
cut-out planes sliding past each other, and *"the eye reads that differential
motion as depth before it reads anything else."* It is the single biggest
difference between a page that feels built and one that feels assembled, and
it costs three transparent images and a multiplier each.

- **Plan the planes back to front.** Far ridge, mid ridge, the product, then a
  **foreground plane in front of the product**. The product sits between mid
  and front, so the foreground overtakes it as the reader scrolls. That
  overtaking is the move.
- **Small rate differences, not big ones.** The reference hero lags the far
  plane **31%** behind the page, the mid plane **17%**, the product **20%**,
  and foreground and copy travel at exactly **1×**. Adjacent planes differ by
  **10–30%**. Larger stops reading as distance and starts reading as things
  sliding around. **Copy always rides at 1×.**
- **Shape the foreground for the product.** A straight-edged foreground covers
  the product's CTA within a few hundred pixels of scroll. Cut it so it dips
  where the product is and rises at the edges, and the button stays in view
  two to three times as long.
- **Every plane is solid below its silhouette.** Cut-out art that fades to
  transparent at the bottom lets the plane behind show through as the planes
  separate. Fill each column solid from its first opaque pixel down.
- **Fade the section floor.** Planes travel past the section's bottom edge and
  are clipped there. A gradient to the page ground over the last 200–300 px,
  layered above every plane, hides the clip line at any scroll position.

Three traps, each of which cost a round of fixes:

- A global `img { max-width: 100% }` shrinks an absolutely positioned plane to
  the viewport on phones, so the far layer never shows. **Planes carry
  `max-width: none` and a fixed pixel width.**
- **Never `transition: transform` on a parallaxed element.** A reveal class is
  the usual culprit. The transition eases every per-frame scroll write over
  its own duration, and on a phone that reads as the product lagging a full
  second behind the thumb. Parallaxed elements transition **opacity only**.
- Replacing a plane's art under the same filename ships nothing to a phone
  holding the old bytes. **New art gets a new name.**

`data-sc-parallax` and a raw scroll multiplier are the same tool in different
units. What matters is the **ratio between planes**, not the absolute travel.

## The premium fade-in, exactly (§8)

The `flow` + `in` device is most of the page, so its defaults decide how the
page feels between the acts:

| Ingredient | Value |
|---|---|
| Opacity | 0 → 1 |
| Rise | **~14 px** |
| Duration | **~620 ms**, ease-out |
| Stagger | **30–80 ms**, children in reading order |
| Trigger | IntersectionObserver, `-12%` bottom root margin, **fires once** |

- **A fade with no rise reads as a loading glitch.** A rise **past 24 px reads
  as a slide.** 14 px is the band, not a starting point to tune upward.
- The `-12%` margin fires the reveal when the reader is looking, not when the
  first pixel clears the fold.
- `data-sc-in` is what the engine watches. Without it nothing fires and the
  stagger children stay hidden.
- **Content that re-hides on the way back up is a defect, not an effect.**
- *"Larger, slower, or bouncier is never more premium; the restraint is the
  signal."*

**A flow section directly after a pinned act takes reduced padding.** The
pinned stage needs a full viewport to scroll off, and full `--sc-section`
padding on top of that delays the flow section's first content by another
screen. The harness will not call it dead scroll — correctly, the stage is
moving — and the reader still sees a near-empty screen. Cut the block padding
there and start the first reveal near `p = 0`.

## Rail settle on `pan` (§3)

Lateral travel alone reads as a slideshow on rails. **Give the rail's items a
staggered settle driven from `--sc-p`** and they read as a drawer being
pulled instead.

- **Exempt the first item** — a `pan` act needs its opening content already
  present.
- **Floor the opacity around 0.55**, so a not-yet-settled card reads as
  arriving rather than as failing to load.

Upstream gates the settle to `prefers-reduced-motion` — **utgår, F-011**.
The settle always runs. What *does* survive from
the same passage is the reachability requirement, which is not a motion
preference at all: a `pan` rail's transform **is** the navigation, so nothing
may zero it and park the act on its first screenful. Every item in a rail
stays reachable, and that is checked on the sheet, not assumed.

Two more, from the same section:

- **Card copy is read while cropped.** Items enter and leave through the
  viewport edges, so a heading is half-shown for most of its life, and two
  half-headings side by side can read as a third word (`TRACE` beside
  `EVALUATE` becoming `RE EVALUATE`). Keep card headings to one or two short
  words and expect every line to be read partially cut off.
- If three items do not reach half a viewport of overflow, **the fix is more
  rail, not wider cards**: put the act's heading in as the first item and a
  closing note as the last. Both earn their place, and they add the width the
  travel needs.

## Devices that cannot share an element (§9)

**`magnet`, `parallax` and `cue` all write `transform`.** The magnet writes
every frame in its own rAF loop, so it silently wins and the cue's entrance
rise is discarded — a visible animation lost to a race, with nothing in the
console.

- On a magnetic CTA, set **`data-sc-rise="0"`** so the cue writes a no-op
  instead of losing to the magnet.
- A cued element that wants its own continuous transform drives an **inner
  wrapper** from `--sc-p` in CSS, rather than stacking a second device on the
  same node.

All three pointer devices **interpolate toward** the pointer rather than
tracking it directly: *"direct tracking reads as artificial because it carries
no momentum."* They stay gated to `(hover: hover) and (pointer: fine)` so
touch never fires a false hover — that gate is a pointer-capability query, not
a motion preference, and it stands.
The reduced-motion half of the same sentence does not port (F-011).

## Kinetic type: the mask and the re-split (§5)

Each unit slides up from **behind a mask**, so it enters from a clean edge
rather than simply fading.

- **Line masks must reserve room for descenders.** A mask clipped to the line
  box shears the tails off g, y, p and j, *"and that is the single most common
  way this effect looks broken."*
- **Line splitting measures real line boxes, so it re-runs after
  `document.fonts.ready`.** Do not call it on text still loading its face. The
  same `fonts.ready` handle earns its place twice over: a webfont swapping in
  changes the measured height of every copy block, so anything sized against
  those blocks (a scrim plate, a rail) is wrong until it re-measures.
- Lines are almost always right; words for a short punch line; characters
  approximately never, *"because it turns reading into waiting."*
- **One kinetic headline per act, at most.**

## What makes a `count` land (§7)

- **Ease out, hard.** A cubic ease-out, so most of the distance goes by in the
  first third and the last digits settle slowly. *"A linear count reads as a
  slot machine."*
- **1.2–1.8 s.** Under a second and the reader misses that it moved; past two
  and they are waiting for a number they have already guessed.
- **Fires at half visibility, once**, so the reader is looking at it when it
  starts, and it never re-runs on the way back up.
- **Pair it with the fade.** A counter inside a `data-sc-in` stack rises in
  with its label and starts ticking as it arrives — *"the same numbers static
  on the page read as a spreadsheet."*
- Write the target exactly as it should render, commas included; the engine
  strips them before parsing and applies `tabular-nums` so the layout does not
  jitter.

**A concept, fictional or pre-launch brand has no verified figures, so it has
no counters.** The device suits a SaaS or agency page and will look good in
the score table, *"which is exactly the trap: every number you could put in it
would be invented."* Decide this before designing an act around a number, not
after. Real brand, real stats, or a different device.

## Appendix: pattern vocabulary

Named patterns from taste-skill § 10, carried here so orchestrator, builder
and reviewer name the same thing. It is a **vocabulary, not a menu** — several
entries below are banned as directions elsewhere in the chain (glassmorphism,
holographic foil, carousels, gooey menus) and appear here only so a critique
can say which trope it is refusing.

- **Hero** — Asymmetric Split · Editorial Manifesto · Video/Media Mask ·
  Kinetic-Type · Curtain-Reveal · Scroll-Pinned.
- **Nav** — Dock Magnification · Magnetic Button (`data-sc-magnet`) · Gooey
  Menu · Dynamic Island · Contextual Radial · Floating Speed Dial · Mega Menu
  Reveal.
- **Layout** — Bento Grid · Masonry · Chroma Grid · Split-Screen Scroll ·
  Sticky-Stack Sections.
- **Cards** — Parallax Tilt Card (`data-sc-tilt`) · Spotlight Border Card
  (`data-sc-spotlight`) · Glassmorphism Panel · Holographic Foil ·
  Tinder Swipe Stack · Morphing Modal.
- **Scroll** — Sticky Scroll Stack · Horizontal Scroll Hijack (= `pan`) ·
  Locomotive / Sequence Scroll (= `scrub`) · Zoom Parallax · Scroll Progress
  Path · Liquid Swipe Transition.
- **Galleries** — Dome Gallery · Coverflow Carousel · Drag-to-Pan Grid ·
  Accordion Image Slider · Hover Image Trail · Glitch Effect Image.
- **Type** — Kinetic Marquee · **Text Mask Reveal** (massive type as a
  transparent window onto video — this is K2's letter-window) · Text Scramble
  · Circular Text Path · Gradient Stroke Animation · Kinetic Typography Grid.
- **Micro** — Particle Explosion Button · Liquid Pull-to-Refresh · Skeleton
  Shimmer · Directional Hover-Aware Button · Ripple Click · Animated SVG Line
  Drawing · Mesh Gradient Background · Lens Blur Depth.

Names alone are not permission. A pattern still has to clear the fingerprint
gate, the register, and `../motion.md` before it ships.

## Never restyle the engine's classes (AB06, 2026-09-03)

Theme the engine only through its six colour tokens and two fonts. A project rule on
`.sc-stage`, `.sc-copy`, `.sc-scrim` or any other `.sc-*` class silently wins over the
engine: the console then says `[scrollcraft] act "…" will not pin: its stage computes
position:relative` and every pinned act scrolls away, leaving its spacer as dead scroll.
Read the console for `[scrollcraft]` warnings before anything else in Step 5, and run
`scripts/scroll_verify.py` — a blind one-shot cannot see either. The engine is opt-in per
grammar (scrub, pin, pan); a page that keeps the chain's own single set-piece + shared
reveal does not need it.
