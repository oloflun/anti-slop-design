# Feeling curve, peak, signature move, fingerprint gate

Condensed from `upstream/scroll-craft/.../references/feel.md` and
`uniqueness.md` §§3–4. Design the feeling before the acts: a device chosen
before the emotion is a device looking for a reason.

## The feeling curve

One line per act in `BRIEF.md`, written **before a single act exists**: the
emotion, then what on screen causes it. The emotion is the constraint; the
device name only ever appears in the cause column, second.

```
1  Recognition   their own kitchen counter at 7am, shot at eye height
2  Fatigue       the two containers, the mess, held still while copy names it
3  Delight       a wipe, and the whole frame is one cold can, condensation running
4  Trust         macro texture at a scale the eye cannot get in a shop
5  Appetite      the flavours travelling sideways, each one landing whole
6  Resolve       everything stops, one can, one line, one place to buy it
```

Two adjacent acts with the same feeling means one is filler — cut it or
change what it does. The curve outranks the Step 1 journey beats: beats say
what the visitor learns, the curve says what they feel while learning it, and
where they disagree the curve wins.

## The peak

People remember one peak and the ending; the middle compresses into a general
impression. So every build engineers **one** deliberate peak, named in
`BRIEF.md` as the sentence a visitor would say to a friend ("the screen went
black and then the whole ocean lit up under me" — a moment, not "the hero is
impressive"). The peak gets, at the expense of every other act:

| It gets | Because |
|---|---|
| The asset budget | Best generated frames or the only real footage go here |
| The silence before it | A quiet act or empty viewport, so the change has something to be a change from |
| The most scroll room | Largest `data-sc-span` on the page, `dwell` tuned to settle exactly there |

A page with three peaks has none — demote the losers (shorter span, plainer
device). The close must resolve, not trail off: the divider collapses, the
world lands somewhere, the type quiets — never a fade to an empty stage.

## The tell-someone test

Complete, before building: *"it's the site where ___."* "It has a scrub
video" is a device name — no hook. "You drag the letters of the logo apart
and they snap back perfectly" is an experience — that's a hook. The blank has
to be something that happened **to the visitor**. This sentence usually
contains the signature move; if the tell-someone sentence and the signature
move point at different moments, one of them is decoration.

## The signature move

One bespoke interaction that exists on this build alone — coded in the page
off `--sc-p` or a page-authored `data-sc-*`, never a parameter on a kit
device, never in any prior build. The engine stays untouched.

**What counts** (upstream examples, not a menu to pick from): scroll-as-
playhead over a persistent trace rail; a wordmark the pointer pulls apart and
snaps back exactly; a line drawing whose `stroke-dashoffset` is driven from
`--sc-p`; a running receipt that accumulates real figures; one control that
regrades the whole page at once (time-of-day, temperature, load).

**What does not count**: a recoloured/resized spotlight; `data-sc-tilt` turned
up; a different easing on kinetic lines; more cards in a rail; a third
`scrub` act; anything the engine already does under a project class name.
Test: describe the move to someone who has seen the other builds — if they
can't tell it apart from something the kit already does, it isn't one.

## Being in it, not watching it

Upstream `feel.md` § 4. *"A film plays whether you are there or not. The
difference between a viewer and a participant is whether the page acknowledges
that somebody specific is here: how fast they are moving, where their pointer
is, whether they stopped."*

Five techniques, in the kit's own vocabulary:

- **Pointer parallax that moves the world, not a card.** `data-sc-spotlight`
  publishes `--sc-mx` / `--sc-my`. Drive a *background layer's* transform off
  them instead of a highlight, and the environment shifts as the visitor
  moves, slightly, the way a real space does when you lean.
- **Dwell-triggered detail.** Hold still on an act and something further
  arrives — a caption, a second line, a small annotation. Reward for stopping.
  Mechanically: **read `--sc-p` staying constant across a few frames**, in the
  page's own JS, and reveal something that was **never needed for
  comprehension**.
- **Scroll velocity shaping intensity.** Fast scrolling raises grain, blur,
  chromatic offset, ground saturation; slow scrolling settles it. *"The page
  feels like it is being driven rather than played back, and it costs one
  derived custom property."*
- **The page addressing "you" at one moment that lands.** Not throughout,
  which is just copywriting. **One line**, at the emotional turn, in second
  person, when the visitor is already implicated. *"It works because it is the
  only time."*
- **A trace of where they have been.** Anything that accumulates as they
  travel, so arriving at the end means having a record rather than reaching a
  footer.

**Embodiment is seasoning. One or two per page.** *"A page that reacts to
everything feels haunted, not alive: the visitor stops reading and starts
poking, which is the opposite of what any of this is for."* Pick the one that
serves the peak and leave the rest.

These are gated to `(hover: hover) and (pointer: fine)` — a pointer-capability
query, which stands.
Upstream also turns them off under reduced motion — **that half utgår, F-011**.
The rule that does survive is upstream's own:
*"a technique that only exists on desktop cannot be the thing that carries the
page's meaning."*

## Pacing as emotion

Upstream `feel.md` § 5. *"Scroll distance is emotional time. It is the only
clock this medium has, and it is fully under your control, which makes it the
cheapest emotional instrument in the kit and the one most often left at
default."*

| Pacing | Reads as | Built with |
|---|---|---|
| Short acts, hard cuts | Adrenaline, pulse, impatience | Acts under 1.4 vh, no `pin`, `dwell` at 0 |
| A long pin | Held breath, pressure, attention | `data-sc-span` 3+, overlapping cues, one idea |
| An empty viewport before a reveal | Silence before the drop | A ground-only act, no cue until the next one |
| A slow settle mid-act | The shot landing | `data-sc-dwell` 0.35–0.6, cue peak on the settle |
| A fast cue with a long plateau | Confidence, arrival | `data-sc-cue="0.1 0.9 0.08 0.4"` |
| A slow ramp in | Hesitation, dawning | Long `rampIn` — **once per page**, it is close to feeling broken |

Four rules follow:

- **Silence must be authored, not left over.** *"An empty screen you meant
  reads as anticipation. An empty screen you did not mean reads as a page that
  failed to load, and the harness reports both as dead scroll."* If the empty
  viewport before the peak is deliberate, **say so in `BRIEF.md`** so the
  verification pass can tell it from dead scroll. This is the sentence that
  keeps `scroll_verify.py`'s `blankBands` check from being either useless or a
  false alarm.
- **Give the peak room.** The peak act has the largest span on the page by a
  visible margin. *"If every act is 2.2 vh, the page has no shape, whatever
  the curve in BRIEF.md says."*
- **Compress the administrative parts.** Specs, logistics, FAQ, credentials
  are information, not experience — flow sections at short stagger, never
  pinned acts with dwell. Spending scroll on them spends the visitor's
  patience on the part they will not remember.
- **A continuous world is the exception to pacing variety.** All of the above
  is about a page of *acts*. A worldflight is one camera move, and *"a camera
  that changes speed between legs reads as broken rather than as
  expressive."* There, hold one pace and let the peak carry the shape by being
  the single long leg — [`pace.md`](pace.md).

The total-length budget stays **8–14 viewport-heights**. Pacing is how that
budget is spent, not permission to spend more: *"a page that needs 20 vh to
land its curve has too many acts, not too little room."*

## The fingerprint gate

Registry: `VAULT/wiki/projects/_index/design-fingerprints.md`, per-vault,
starting from whatever rows already exist — not repeating **yourself** across
builds, not a universal constraint. **Six dimensions**, recorded per row:

| # | Dimension | What it records |
|---|---|---|
| 1 | Grammar | Which of `grammars.md`, or a named new one |
| 2 | Nav treatment | What the chrome is and what it's for |
| 3 | Hero device | What the first screen does |
| 4 | Act-sequence shape | Device order, act count, total viewport-heights |
| 5 | Close pattern | How the last screen behaves, what the CTA sits in |
| 6 | Signature move | The one bespoke interaction, in a phrase |

**The gate: a new build must differ from EVERY existing row on at least 4 of
the 6** — four against each row individually, not averaged across the table.
Dimension 6 is free (unique by definition), so the gate really asks for 3
more out of the remaining 5 against each row. If the plan fails, **change
the plan, not the log** — rewriting a row to fit is what makes it worthless.

**Row format** — one row per shipped build, all six dimensions plus a world
note and the path: `| Build | Grammar | Nav | Hero device | Act-sequence
shape | Close pattern | Signature move | Register | World / palette | Path |`

**Rows are append-only.** From upstream `templates/FINGERPRINTS.md`:

> *"A build that has been superseded stays in the table, because the space it
> occupies is still occupied."*

A replaced, retired or rejected build keeps its row. The registry does not
record what is live; it records what surface has already been taken, and a
surface stays taken whether or not the build that claimed it is still up.
Deleting a row silently frees a shape for reuse, which is the same failure as
editing one to make room — *"never edit a row to make room for it. If a
planned build fails, change the plan."*

**Fill every column.** A row with blanks cannot be scored 4-of-6 against, so
it weakens the gate for every build after it.

**Keep a "what is taken" list beside the table.** Add a bullet whenever a
build claims something a later build should avoid reusing: a grammar, a nav
treatment, a close pattern, a signature move, an act-count-and-length band.
*"The shared columns are what the next build inherits as a constraint, so
writing them down is the whole point."*

After shipping, append the row and say what it shares with prior rows — the
shared columns are exactly what the *next* build has to avoid.
