# Pace — the third thing people call "not smooth"

Damping fixes the value *between* two writes. Pace is the value's own speed, and no
amount of damping fixes a speed that changes from act to act. Upstream
`worldflight.md` § 7c is the only place in the corpus where someone diagnosed the
complaint to root cause, and its first line is the whole problem:

> *"Two separate faults get described as 'it doesn't feel smooth', and only one of
> them is smoothing."*

Read [`../motion-smoothness.md`](../motion-smoothness.md) first — it separates the
*stepping* fault (a raw value written 1:1) from the *dropped frames* fault (the page
is genuinely slow). This file is the third one, and it is the fault the owner of the
`orrery` build actually had.

## Inconsistent pace is the worse one

```
rate = weight / clip_seconds        // hold this within a few percent everywhere
```

Leg weight divided by clip length is how fast the world moves under the reader's
hand. When that number varies from leg to leg, the world surges and drags for no
reason the reader can see, and it reads as a fault in the page rather than as pacing.

- Every leg with the **same clip length gets the same weight**.
- A **longer clip gets a proportional weight** — proportional, not "bigger by feel".

Measured upstream on `orrery`: the rate varied by **36 % across ten legs** on the
first cut, and the owner's word for it was *"not smooth"*. Evened to a **6 % spread**,
the same footage reads as one continuous move. Same clips, same damping, same engine —
only the weights changed.

That pair is the number to carry: **36 % reads as a defect in the page; 6 % reads as
one movement.**

## Then slow it down

The instinct is to spend as little scroll as possible. A fly-through wants the
opposite: the reader is steering a camera, and a camera that answers too eagerly feels
twitchy.

| | Value |
|---|---|
| Floor for a world you fly through | **0.21–0.22 vh per second of film** |
| What the per-8s line yields | 0.14–0.19 vh/s — *noticeably fast* |
| What the per-8s line actually is | a **dead-scroll guardrail, not a taste ceiling** |

Exceeding the guardrail is fine and often correct; exceeding it *without checking* is
not. The harness defines dead scroll mechanically and will tell you. At 0.216 vh/s a
0.12 vh sample gap still advances the clip by half a second — nowhere near dead.

## Damping and weights fix different halves

> *"The damping is what removes wheel judder; the weights are what remove the
> surging."*

| Knob | Act page | Worldflight | Why the flight differs |
|---|---|---|---|
| `data-sc-lerp` | 0.18 (default) | **0.12** | A flight has more legs mounted and more seams than an act page, and the extra damping is what actually removes wheel-event judder |
| `data-sc-seam` | 0.12 (default) | **~0.16** | A longer crossfade band gives each join more room to disappear in |

`data-sc-lerp` is never 0 and never disabled — a 1:1 playhead reproduces every gap in
the wheel event stream as a stutter. (Upstream's hard-rules table attaches a
reduced-motion exception to that sentence. It does not port: **F-011** — motion always
plays here and no build reads a preference to switch it off.)

Neither knob fixes an uneven `rate`. Raising the lerp on a surging flight only makes
the surge arrive smoothly — the same way damping a value on a page that cannot hold
60 fps makes a smooth curve arrive late.

## Changing a weight changes every window

Weights are the track. Moving one moves every leg boundary after it, so **every
`data-sc-window` has to be recomputed** against the new track and then re-checked on
screen. A copy window is tuned to a frame of film, not to a number; redoing the
arithmetic is not the same as looking at it.

Budget that re-check into any pacing pass. It is the reason pace is settled before the
copy windows are, not after.

## Measuring it

`motion_probe.py` reports `max_step_pct` per tracked value, so an act that surges
relative to its neighbours shows up as a spread across runs rather than as a feeling.

```bash
python ~/.claude/skills/design/scripts/serve.py --port 3000 --root .
python ~/.claude/skills/design/scripts/motion_probe.py --url http://127.0.0.1:3000/page.html \
    --track "#leg1:--sc-ps,#leg2:--sc-ps,#leg3:--sc-ps" --cpu 4 --out shots/motion
```

Write the per-leg `rate` out as a table from the markup — weight and clip length are
both in the source, so this is arithmetic, not a measurement, and there is no excuse
for not having it. The spread between the largest and smallest rate is what gate **94**
reads.

## The bar

- Per-leg `rate` spread **≤ 6 %** across the whole flight. 36 % is the measured
  failure, not a hypothetical one.
- **≥ 0.21 vh per second of film** on anything the reader flies through.
- `data-sc-lerp` **0.12** and `data-sc-seam` **~0.16** on a worldflight; the act-page
  defaults (0.18 / 0.12) elsewhere.
- Every `data-sc-window` re-checked **on screen** after any weight change.
- Plus the continuity bar in [`../motion-smoothness.md`](../motion-smoothness.md) §
  The bar — `staircase` 0, `max_step_pct` ≤ 3 on the `--sc-ps` playhead (reported, not
  gated, on derived tracks), `frame_p95_ms` ≤ 20 at 4× CPU, zero frames over 33 ms,
  both scroll directions.

## What the harness cannot tell you

`shoot.mjs` waits for the lerp to settle before every shot precisely because *"a
screenshot taken mid-lerp is a frame the page never actually holds, and it makes the
run unrepeatable"*. That buys repeatability, not evenness: a contact sheet of settled
frames says nothing about the speed between them. Scroll it cold, one word per leg,
and diff against the intended curve
([`feel-and-fingerprint.md`](feel-and-fingerprint.md) § Peak) before opening
`BRIEF.md`.

## Related

[`../motion-smoothness.md`](../motion-smoothness.md) · [`devices.md`](devices.md) ·
[`README.md`](README.md) · [`../performance.md`](../performance.md) · gate **94** ·
`scripts/motion_probe.py` · upstream `worldflight.md` §§ 7c, 8, 9 · FEEDBACK.md F-011,
F-013.
