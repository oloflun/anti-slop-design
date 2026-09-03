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

After shipping, append the row and say what it shares with prior rows — the
shared columns are exactly what the *next* build has to avoid.
