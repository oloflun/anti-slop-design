# Motion

Most AI-generated motion is scattered — hover lifts on every card, fade-in on every scroll, bouncing icons. Quiet it. One orchestrated moment beats ten small ones.

> For per-interaction recipes (button press, focus, modal, toast, optimistic update, command palette, drag handle, etc.), see [`microinteractions.md`](microinteractions.md). This file is the *language* of motion; that file is the *vocabulary*.
>
> For scroll-driven acts — the device kit, pace, the feeling curve — see [`scroll/`](scroll/README.md). The 300 ms UI budget below does not govern them; see § Scroll-linked motion.
>
> For the *stepping* and *dropped-frames* faults behind "hackigt och billigt", see [`motion-smoothness.md`](motion-smoothness.md) and [`scroll/pace.md`](scroll/pace.md).

## The motion thesis

Write it before implementation, in `BRIEF.md`, in four lines. Ported from impeccable `animate.md` § Set the motion thesis:

- **Focal moment** — the one sequence or interaction that deserves authorship, if any.
- **Continuity** — the state, layout, or navigation changes that need explaining.
- **Feedback** — the controls and outcomes that need acknowledgment.
- **Budget** — which effects may be expensive, and how often they run.

> "The focal moment must come from this product and surface concept. A generic fade-and-rise, hover lift, parallax layer, or scroll reveal is not a thesis."

Find the job first: inspect the existing motion language, states, target devices and performance budget, and animate **only** where motion would acknowledge an action, make a state change or spatial relationship legible, preserve continuity through a layout change, direct attention at a meaningful moment, or embody the selected world. "Do not animate a static area merely because it exists."

**One sentence per animation** (taste-skill § 5). Every animation that ships names, in the brief, what it communicates. An animation with no sentence is decoration and gets cut — that is the same test as impeccable's "decoration without purpose is animation debt", made countable.

**Rejected candidates are part of the output.** `find-animation-opportunities` requires the rejected list; so does this file. A motion thesis that lists only what was built cannot be reviewed.

## The build sequence

Seven decisions, in this order, from emil `animate` § The Build Sequence. Steps 1 and 2 gate everything: **do not reach for a curve before you know whether it animates at all.**

1. **Should this animate at all?** — the frequency gate below.
2. **What is the purpose?** — name it in one word: feedback, spatial consistency, state indication, preventing a jarring change, explanation, delight. "Can't name it? Don't build it."
3. **Pick the tool — cheapest that works.** CSS transition → `@starting-style` → CSS animation → WAAPI → a motion library. Walk down, stop at the first that fits. CSS animations run off the main thread and beat JS under load; use CSS for predetermined motion, JS for dynamic and interruptible motion.
4. **Pick the properties** — § Material by meaning.
5. **Easing and duration, or a spring** — § Easings, § Durations.
6. **Interruption and exit** — § Interruption and exit.
7. **Pointer gating** — `@media (hover: hover) and (pointer: fine)` ships with the animation, not as a follow-up. (Upstream's step 7 pairs this with a `prefers-reduced-motion` branch. That half does not port: **F-011**.)

| Frequency | Decision |
|---|---|
| 100+ times/day (keyboard shortcuts, command palette toggle) | **No animation. Ever.** Stop here |
| Tens of times/day (hover effects, list navigation) | Near-imperceptible only — fast and subtle, or nothing |
| Occasional (modals, drawers, toasts) | Standard animation |
| Rare / first-time (onboarding, success, a landing page's one set-piece) | The delight budget lives here |

"Keyboard-initiated actions are a disqualifier, not a judgment call." A Persuade surface is seen once by each visitor, which is why it gets the authored moment an Operate surface must not have.

**No approximated values.** Every curve, duration and spring config comes from the tables in this file. Never invent `cubic-bezier(0.4, 0, 0.2, 1)` because it looks familiar. And **extend the page's existing tokens, don't fork them** — adding a parallel motion scale beside `--ease-*` / `--dur-*` is a defect.

## Principles

- **`transform` and `opacity` are the floor, not the ceiling.** They are GPU-composited and skip layout, so they carry the routine work. The hard rule is the narrower one, in impeccable `motion-design.md`'s own words: *"The hard rule is not 'transform and opacity only.' The hard rule is: avoid animating layout-driving properties casually (`width`, `height`, `top`, `left`, margins), keep expensive effects bounded to small or isolated areas, and verify in-browser that the result is smooth on the target viewports."* See § Material by meaning. **This supersedes the earlier absolute "only `transform` and `opacity`"** — that line banned `clip-path`, `filter` and masks, which are the chain's own reveal and depth vocabulary (scroll-craft `reveal`, kinetic masks, the blur crossfade). The layout-property ban is untouched and absolute.
- **Duration is four buckets.** Micro (100–150ms), minor (150–300ms), major (300–500ms), and one authored focal entrance (500–800ms) per page. Exits are ~75% of the enter.
- **Easing is exponential ease-out.** Elements coming in slow down into place. Elements leaving accelerate away.
- **Motion serves perception.** If you can't explain what a transition communicates, cut it.
- **Never animate text colour.** Photosensitive risk (designpowers `motion-choreography` § What NOT to Animate). Cross-fade the element or swap the node; do not run a colour transition on a run of text.
- ~~**Reduced motion is non-optional.**~~ **F-011 (2026-09-07):** superseded — rörelsen spelar alltid i det här designsystemet; ingen `prefers-reduced-motion`-gren byggs och ingen granskare flaggar att den saknas. Funktionell rörelse (progress, spinners, skeletons) är oförändrad.

## Easings

Use these three. Name them as tokens.

```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);        /* elements entering */
  --ease-in:  cubic-bezier(0.7,  0, 0.84, 0);       /* elements leaving  */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);    /* state toggles     */
}
```

`ease`, `ease-in-out` (default), `cubic-bezier(0.25, 0.1, 0.25, 1)` — these are the browser defaults and they read as uncrafted.

Three named alternates, from emil `emil-design-eng` § 3 and `animate` § 5. Use them when the curve above is not the right shape; do not hand-roll a fourth.

```css
:root {
  --ease-out-strong:    cubic-bezier(0.23, 1, 0.32, 1);    /* strong ease-out for UI      */
  --ease-in-out-strong: cubic-bezier(0.77, 0, 0.175, 1);   /* strong on-screen movement   */
  --ease-drawer:        cubic-bezier(0.32, 0.72, 0, 1);    /* iOS-like drawer (Ionic)     */
}
```

And the exponential ramp, from impeccable `motion-design.md` § Easing, when a micro-interaction wants friction rather than a curve name:

```css
--ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);   /* smooth, refined — recommended default */
--ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);  /* slightly more dramatic                */
--ease-out-expo:  cubic-bezier(0.16, 1, 0.3, 1);   /* snappy, confident                     */
```

**Two conflicts, resolved.**

- **Which `--ease-out`?** Upstream emil names `cubic-bezier(0.23, 1, 0.32, 1)`; this file's `--ease-out` is `cubic-bezier(0.16, 1, 0.3, 1)` (identical to impeccable's `--ease-out-expo`). **This file's value wins**, because the shipped builds, `house-physics.md` and `microinteractions.md` already carry it and a second `--ease-out` is exactly the forked token set step 3 forbids. Emil's rule is *"built-in CSS easings are too weak"*, not *"this cubic-bezier specifically"* — a strong custom curve satisfies it, and `review-animations` standard 3 asks for a custom curve, not for that one. Emil's value stays available as `--ease-out-strong`.
- **`ease` on hover.** Emil's decision tree sends hover/colour changes to built-in `ease`. **The ban in § Bans wins.** A hover that only changes colour reads identically under `--ease-out` at ≤150 ms, and keeping one token set is worth more than the last few percent of that curve. Nothing on this page uses the browser default.

**`ease-in` is for exits only.** Elements leaving the screen accelerate away (impeccable `motion-design.md` § Easing: *ease-in → "Elements leaving"*). Never `ease-in` on anything entering, on anything moving on screen, or on anything the user is waiting for — *"it starts slow, which makes the interface feel sluggish and unresponsive… the exact moment the user is watching most closely."* This is a **known, deliberate divergence** from `review-animations` standard 3 and its escalation trigger "`ease-in` on any UI interaction": that trigger reads a bare `ease-in` as a defect, and here a bare `ease-in` on an exit is correct. State it in the review so the reviewer does not re-flag it; every other use of `ease-in` remains a block.

## Durations

```css
:root {
  --dur-micro: 120ms;   /* button press, toggle tick, color shift  */
  --dur-short: 220ms;   /* hover lift, tooltip, menu open          */
  --dur-long:  420ms;   /* modal, drawer, accordion, page reveal   */
  --dur-focal: 640ms;   /* the one authored focal entrance         */
}
```

Exits use roughly 75% of the enter:

```css
.menu.is-open  { transition: transform var(--dur-short) var(--ease-out); }
.menu.is-close { transition: transform calc(var(--dur-short) * 0.75) var(--ease-in); }
```

**The band each token sits in** — impeccable `motion-design.md` § Duration (the 100/300/500 rule) and `animate.md` § Timing and easing, which agree row for row:

| Duration | Use |
|---|---|
| 100–150 ms | Immediate feedback — button press, toggle, colour change |
| 150–300 ms | Routine state change — menu open, tooltip, hover state |
| 300–500 ms | Layout change — accordion, modal, drawer, view transition |
| 500–800 ms | A **deliberately authored** focal entrance: page load, hero reveal. One per page |

**Per element**, when the band is too coarse (emil `emil-design-eng` § 4):

| Element | Duration |
|---|---|
| Button press feedback | 100–160 ms |
| Tooltips, small popovers | 125–200 ms |
| Dropdowns, selects | 150–250 ms |
| Modals, drawers | 200–500 ms |
| Marketing / explanatory | Can be longer |

**UI animations stay under 300 ms.** *"A 180 ms dropdown feels more responsive than a 400 ms one."* Anything slower on a UI element needs a stated reason or it is a finding. `--dur-focal` is that stated reason, used once.

**Reach for a spring instead** when the motion is a drag with momentum, an element that should feel alive, a gesture the user can interrupt or reverse, or decorative pointer tracking:

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }            // Apple-style, easier to reason about
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }  // traditional physics, more control
```

Keep bounce at 0.1–0.3 and avoid it in most UI. Apple's own defaults, from `apple-design` § 4: **damping 1.0** (critically damped, no overshoot) everywhere by default; **damping ~0.8 only when the gesture itself carried momentum** — a flick, a throw, a drag release. *"Overshoot on a menu that just faded in feels wrong; overshoot on a card you flicked feels right."* Response 0.3–0.4 s; response is not duration — a spring has no fixed duration, its settle time emerges from the parameters.

## Material by meaning

Impeccable `animate.md` § Choose material by meaning. Pick the property for what the transition *communicates*, not for what is cheapest to type:

| Communicates | Material |
|---|---|
| Continuity and relationship | Shared-element motion, FLIP-style transforms, View Transitions, deliberate spatial movement |
| Focus and depth | Bounded `blur`, `filter`, `backdrop-filter`, light and shadow change |
| Reveal and composition | Masks, `clip-path`, cropping, controlled occlusion |
| Material and energy | Colour, gradient position, texture, distortion, shader work where the world and runtime support it |
| State and feedback | The smallest change that makes cause and result unmistakable |
| Expanding layout | `grid-template-rows: 0fr → 1fr` or a FLIP transform — never `height` directly |

> "Do not stack techniques for spectacle. One strong material idea, carried through the focal sequence and quiet supporting states, is usually enough."

Three constraints that come with the wider palette:

- **Bound the expensive ones.** Blur, filter, backdrop, canvas and shader work stay in small or isolated regions. Keep blur under 20 px — heavy blur is expensive, especially in Safari.
- **`clip-path` is the sanctioned fourth property** beside `transform`, `opacity` and `filter`. `height` is tolerated only for accordions, where there is no transform equivalent.
- **Measure, don't assume.** *"Verify in-browser that the result is smooth on the target viewports"* — `transform` does not mean fast, and a bounded blur that measures smooth is allowed even though it is not composited. `scripts/motion_probe.py` is the instrument; see [`motion-smoothness.md`](motion-smoothness.md).

Property picks that are not negotiable (emil `animate` § 4):

- **Never `scale(0)`.** Start from `scale(0.9–0.97)` + `opacity: 0`. Nothing in the real world appears from nothing.
- **Percentages in `translate()`** are relative to the element's own size — `translateY(100%)` moves it by its own height whatever the content. Prefer them to hardcoded pixels.
- **Never drive a child's transform from a CSS custom property on the parent.** It recalculates styles for every child — a style-recalc storm, and one of `review-animations`' flag-on-sight triggers. Set `transform` on the element itself. (The scroll engine's `--sc-p` is the deliberate exception: it is read by `calc()` in the child's *own* rule, not written per frame onto a parent that has children to invalidate.)
- **In a motion library, write the full transform string.** `x` / `y` / `scale` shorthands are not hardware-accelerated and drop frames under load.

## Page-load orchestration

One sequence on page load. Stagger by DOM index using a CSS custom property, not by JS.

```html
<section style="--i: 0">…</section>
<section style="--i: 1">…</section>
<section style="--i: 2">…</section>
```

```css
.reveal {
  opacity: 0;
  transform: translateY(8px);
  animation: reveal var(--dur-long) var(--ease-out) forwards;
  animation-delay: calc(var(--i, 0) * 60ms);
}
@keyframes reveal {
  to { opacity: 1; transform: none; }
}
```

Cap total stagger at ~500ms. Beyond that the page feels slow to settle.

**Stagger has three limits, not one:**

- **30–80 ms between siblings.** Longer feels slow. (designpowers `motion-choreography` names 50–80 ms; that sits inside this range and is a fine default for a group of cards.)
- **Maximum 5 items staggered — the rest appear together.** A ten-item stagger is a queue, not choreography.
- **Follow reading order**, and let the sequence reveal hierarchy: the item that matters arrives first.

Sibling stagger is appropriate *when a list appears as a list*. "Never reinterpret every scrolled section as a staggered list", and never stagger a routine interaction — a row hover, a keystroke, a repeated tab change.

**Blur is the third stagger channel**, beside opacity and translate (interfaces `better-ui/enter-exit.md` § Enter animations). Combine `opacity`, `filter: blur()` and `translateY` for a staged entrance; the blur is what makes the arrival read as focus pulling in rather than as a card sliding:

```css
.stagger-item {
  opacity: 0;
  transform: translateY(12px);
  filter: blur(4px);
  animation: fade-in-up 400ms var(--ease-out) forwards;
  animation-delay: calc(var(--i, 0) * 60ms);
}
@keyframes fade-in-up {
  to { opacity: 1; transform: none; filter: blur(0); }
}
```

Split a large container into semantic groups (title, description, buttons) at ~100 ms between groups; for a display title, splitting into words at ~80 ms is the finer grain. Exits carry the same three channels in reverse and stay softer — a small fixed `translateY(-12px)` plus `blur(4px)` at ~150 ms, because "the user's focus is moving to the next thing, so do not fight for it."

## Interruption and exit

Emil `animate` § 6, interfaces `better-ui/animations.md` § Interruptible animations, `apple-design` § 3. Apple calls interruptibility *"the single most important principle"*, and the chain agrees: an animation the reader cannot grab mid-flight is what reads as the page ignoring them.

| | CSS transition | CSS keyframes |
|---|---|---|
| Behaviour | Interpolates toward the latest state | Runs on a fixed timeline |
| Interruptible | **Yes — retargets mid-animation** | **No — restarts from the beginning** |
| Use for | Interactive state changes: hover, toggle, open/close | Staged sequences that run once: entrances, loaders |

- **Transitions, not keyframes, for anything triggered rapidly** — toasts, toggles, anything a user can fire twice in a second. Keyframes on a rapidly-triggered element is an automatic block. "Clicking again mid-animation smoothly reverses"; the keyframe version "snaps or restarts, feels broken."
- **Always animate from the *presentation* value, never the target value.** On interrupt, read the element's live on-screen transform and start the new animation from there. *"Starting from the logical/target value causes a visible jump."* This is the single most common cause of a flip or drawer that reads as cheap on the second interaction.
- **Springs for gestures**, because they carry velocity through an interruption and animate from the current value by default. Never lock out input during a transition.
- **Blend velocity at a reversal, don't hard-cut it.** Swapping one animation for another at a reversal creates a velocity discontinuity — a "brick wall". Decompose 2D motion into independent X and Y springs; one spring on a 2D distance desyncs when the two axes have different velocities.
- **Exit the way it entered.** A toast that slides in from the bottom leaves through the bottom. Symmetric paths are what make swipe-to-dismiss feel obvious.
- **Asymmetric timing where the user is deciding.** Slow on the deliberate phase (a hold-to-confirm press: 2 s linear), snappy on the system response (release: 200 ms ease-out). Symmetric timing on a press-and-release is a finding.
- **No `animation-fill-mode: forwards` or delays that block interaction** on a panel the user can re-trigger — the transition should simply respond to the new state.

## Origin and anchoring

Refero `motion.md` § Transform Origin and emil `animate` § 4. Getting the origin wrong is read as "hackigt och billigt" long before anyone can name it: the element scales from the wrong place, so it appears to come from nowhere.

**Set `transform-origin` explicitly on every scale or rotate.** The defaults:

| Element | Origin |
|---|---|
| Modal | `center` — **exempt**, it is not anchored to a trigger |
| Dropdown / popover / menu | The trigger: `top left` or `top right` (`var(--transform-origin)` in Base UI) |
| Tooltip | The edge closest to the trigger |
| Button press | `center` |

`transform-origin: center` on a trigger-anchored popover is an automatic block.

**SVG needs `transform-box: fill-box`.** A transform on an SVG child resolves against the viewBox, not the element, so `transform-origin: center` lands somewhere else entirely:

```css
/* wrong: resolves against the viewBox */
svg path { transform: rotate(45deg); }

/* right */
svg g.icon-wrapper {
  transform-box: fill-box;
  transform-origin: center;
  transform: rotate(45deg);
}
```

This is a **build rule, not a review note**, on any page whose art is inline SVG — which is most illustrated and typographic-poster work here. A whole page of inline-SVG marks rotating around the wrong point is one missing declaration, and it is F-012-class: the motion runs and looks wrong.

## Scroll-linked motion

**"UI under 300 ms" does not apply to scroll-driven acts.** The 300 ms budget above governs *UI elements* — a dropdown, a tooltip, a modal, anything the user triggered and is now waiting on. A scroll-driven act is **paced by the hand**: the reader sets its speed, there is no wait to shorten, and its duration is a distance in viewport-heights rather than a number of milliseconds. A 1.4-second reveal or a scrubbed card flip inside a declared act is therefore **correct, not a finding**, and `review-animations` must be told so before it reads the diff. What still applies inside an act: the easing bans, the origin rules, interruptibility, the property list, and the pace bar in [`scroll/pace.md`](scroll/pace.md).

On an ordinary (non-act) page:

- Use IntersectionObserver, **never** an unstructured `scroll` handler. Unobserve after a once-only reveal fires.
- Use it only for *reveal once* effects. Content that re-hides on the way back up is a defect, not an effect.
- **The permitted scroll-listener form**, when a page genuinely drives a value from scroll position: a **passive** listener that only records a number, **one** rAF loop that does the writing, a **deadband** below which nothing is written, and **no layout reads inside the handler**. That is what the vendored engine does; a handler that reads `getBoundingClientRect()` per event is the banned form. Never touch React (or any framework) state from a rAF loop.
- ~~Every scroll-triggered motion must have a reduced-motion fallback.~~ **F-011 (2026-09-07):** utgår; scrollstyrd rörelse har en väg, och den verifieras.

**The scroll-reveal recipe** (emil `animate/RECIPES.md` § Scroll reveal). Marketing surfaces only — "don't do this to functional UI a user visits daily":

```css
.reveal {
  clip-path: inset(0 0 100% 0);
  transition: clip-path 600ms var(--ease-in-out);
}
.reveal[data-visible] { clip-path: inset(0 0 0 0); }
```

Trigger once with IntersectionObserver at a `-100px` root margin. *"Fire it once — re-animating on every scroll-by is an interface fighting its reader."* `clip-path` is relative to the **border box, not the ink**: on type set below `line-height: 1` the wipe shears ascenders and descenders off and every figure renders as a bar. Put `data-*` reveal attributes on a wrapper, or give the element room.

**Masking a crossfade that won't settle** (`RECIPES.md`). When two states overlap visibly and no amount of easing or duration tuning fixes it, blur the seam:

```css
.content { transition: filter 200ms var(--ease-out), opacity 200ms var(--ease-out); }
.content.transitioning { filter: blur(2px); opacity: 0.7; }
```

*"Without blur the eye reads two distinct objects swapping. Blur blends them into one perceived transformation."* (Upstream writes both transitions with the built-in `ease`; retimed to `--ease-out` here so the recipe does not ship a § Bans violation. The blur value and the 200 ms are upstream's.)

**Parallax, reconciled with § Bans.** The ban below stands for *casual* parallax — a background image drifting on an ordinary page because it was easy. Parallax as a **declared device inside a scroll grammar** is sanctioned, and only under the rate discipline and layer rules in [`scroll/devices.md`](scroll/devices.md) § 6: the rate is hundreds of pixels of total travel, adjacent planes differ by 10–30%, copy rides at 1×, never body copy on a moving layer, and never a `transition: transform` on a parallaxed element.

## State transitions

- Button hover / active: micro duration, `--ease-out`, `transform: translateY(-1px)` on hover, `translateY(0)` on active. Never a `box-shadow` transition on hover on a dark background (glow effect).
- Menu / tooltip / dropdown: short duration, `--ease-out` on open, `--ease-in` on close. Use the popover API or `inert` to manage focus.
- Modal: long duration, scale-in (0.96 → 1) + opacity crossfade. Backdrop fades in at the same duration.
- Accordion: animate `grid-template-rows: 0fr` → `grid-template-rows: 1fr` (not `height`). With `--ease-in-out`.

## Felt state to property

From designer-skills `interfaces-that-feel`. Use it when a page is technically correct and lands cold — the translation runs in four steps, and the point is that "premium" is a *behaviour*, not a value you can pick:

1. **Name the felt state** — what the person is actually experiencing at this moment. Not the task. Waiting. Recovering from an error. Arriving somewhere.
2. **Find the physical analogue** — what in the physical world has that quality. "Soft surfaces absorb impact. A held breath before exhaling. The slow release of a door."
3. **Extract the behavioural property** — weight, resistance, speed, recovery arc, rhythm.
4. **Apply it to a layer** — easing curve, delay, duration, spacing, colour temperature, copy tone.

The translation, in this file's terms:

| Felt state | Reads as | Built with |
|---|---|---|
| Heavy, consequential | Weight and momentum | Longer duration, **larger travel distance**, ease-out with a long tail |
| Light, incidental | Quick and unremarkable | Shorter duration, **smaller travel distance**, `--dur-micro` |
| Confident, arriving | Deceleration into place | `--ease-out-quart` / `--ease-out-expo`, a plateau at the end |
| Snappy, responsive | Stiff spring | High stiffness, damping 1.0, no overshoot |
| Playful, forgiving | Loose spring | Lower damping, bounce 0.1–0.3, **only after a gesture with momentum** |

Two timing rules that come with it: **information weight** — heavy news arrives slowly, good news can be instant; and **recovery space** — after an error, give 300–600 ms before the next prompt rather than rushing the recovery. Linear is mechanical; keep it off anything that touches human feeling (progress bars and ticking loaders excepted).

## Perceived performance

Impeccable `motion-design.md` § Perceived Performance. *"Nobody cares how fast your site is, just how fast it feels."*

- **The 80 ms threshold.** The brain buffers sensory input for roughly 80 ms to synchronise perception, so anything under 80 ms reads as instant and simultaneous. That is the target for micro-interactions, and it is why `--dur-micro` sits where it does rather than lower.
- **Preemptive start.** Begin the transition immediately while loading, rather than after. The user perceives work happening.
- **Early completion.** Show content progressively — progressive images, streaming markup — instead of waiting for everything.
- **Optimistic UI.** Update the interface immediately and handle failure gracefully. For low-stakes actions only; never for payments or destructive operations.
- **Easing changes perceived duration.** Ease-out feels satisfying for entrances; ease-in toward the *end* of a task compresses perceived time, because the peak-end effect weights the final moments heavily.
- **A fast spinner makes a load feel faster**, at an identical load time. Instant tooltips after the first one make a whole toolbar feel faster.
- **Caution.** Too-fast responses can decrease perceived value — users distrust an instant result for a complex operation. Sometimes a brief delay signals that real work happened.

## Reduced motion — utgår (F-011)

```css
/* F-011 (2026-09-07): reduced-motion-blocket utgår — rörelsen spelar alltid, aldrig en preferensgrind. */
```

Functional motion (progress bars, loading spinners, skeletons) is unchanged — it runs at its normal speed. ("Just slower" was the reduced-motion branch's wording and went with it; F-011 leaves functional motion alone rather than degrading it.)

**What F-011 dropped, and from where.** Every upstream package this file draws on ships a `prefers-reduced-motion` half; **none of it lands here (F-011)**. Motion plays unconditionally, no build reads a browser or OS preference to switch it off, and no reviewer flags its absence. Listed so nobody re-imports one of them believing it was an oversight:

| Source | Block dropped | Why |
|---|---|---|
| emil `review-animations` § The Ten Non-Negotiable Standards | **Standard 8's first half** — "`prefers-reduced-motion` is honored (gentler, not zero)" | F-011. Standard 8's **second half — hover gating behind `@media (hover: hover) and (pointer: fine)` — is kept** and is in the build sequence, step 7 |
| emil `animate` § 7 + § Never Ship | The `@media (prefers-reduced-motion: reduce)` branch, `useReducedMotion()`, and the "Missing `prefers-reduced-motion`" row | F-011. The pointer-gating half of both is kept |
| emil `review-animations` escalation triggers | "Missing `prefers-reduced-motion` handling on movement" | F-011. "Ungated `:hover` motion" is kept |
| impeccable `motion-design.md` § Reduced Motion | The whole section, including the `animation-duration: 0.01ms !important` reset and the "vestibular disorders affect ~35% of adults over 40" framing, plus the § Avoid line "Ignoring `prefers-reduced-motion`" | F-011, and F-011 records that this is a **deliberate, informed** trade against exactly that population — not an oversight to be quietly corrected |
| designpowers `motion-choreography` § Reduced Motion | The standard/reduced alternatives table and **"Every animation must have a reduced-motion alternative. No exceptions."** | F-011. Its § What NOT to Animate (text colour, layout properties, decorative loops) is kept |
| taste-skill § 5 / § 6.B | `useReducedMotion()` gating in the scroll skeletons; "Reduced Motion (mandatory)" | F-011 |
| interfaces `better-ui/animations.md` § Motion restraint | The clause "Users with reduced motion enabled…" inside the two-channel rule | F-011 for the clause only. **The rule survives**: motion is never the only feedback channel — a state change an animation communicates stays visible when the animation does not run, for anyone who simply blinked |
| scroll-craft `devices.md` §§ 1, 3, 9 · `feel.md` § 4 · `worldflight.md` § 8 | Every "under reduced motion…" branch: lerp rate 1.0, the `pan` scroll-region floor, pointer-device disabling, embodiment gating, the hard-rules exception | F-011. The `pan` **reachability** requirement survives on its own terms — see [`scroll/devices.md`](scroll/devices.md) |

WCAG 2.3.1 (the three-flashes-per-second limit) is untouched. It is a safety limit, not a preference.

## Never Ship

Self-check before finishing. Each row is an automatic block in `review-animations` (emil `animate` § Never Ship, twelve of thirteen rows — the missing `prefers-reduced-motion` row is dropped per F-011, see § Reduced motion).

| Never | Instead |
|---|---|
| `transition: all` | Name the exact properties |
| `transform: scale(0)` entrance | `scale(0.95)` + `opacity: 0` |
| `ease-in` on anything entering or on screen | `ease-out` or a strong custom curve (exits excepted — see § Easings) |
| Built-in `ease-out` on a deliberate animation | `--ease-out`, or `--ease-out-strong` |
| Animation on a keyboard shortcut or a 100+/day action | No animation |
| UI duration over 300 ms with no reason | 150–250 ms (`--dur-focal`, once, is the stated reason; a scroll act is exempt) |
| `transform-origin: center` on a trigger-anchored popover | The trigger's corner (modals exempt) |
| Keyframes on toasts, toggles, rapidly-triggered elements | CSS transitions |
| Animating `width` / `height` / `margin` / `padding` / `top` / `left` | `transform` / `opacity` (accordion: `grid-template-rows`) |
| Motion-library `x` / `y` / `scale` props under load | The full `transform` string |
| Ungated `:hover` motion | `@media (hover: hover) and (pointer: fine)` |
| Everything entering at once | 30–80 ms stagger, max 5 items |

**When feel can't be settled from code, say so and check it** rather than guessing at a value (emil `animate` § Output, `review-animations` § Debugging). Four instruments: play it at **2–5× duration** or in the DevTools animation inspector; step it **frame by frame** to catch timing drift between coordinated properties; test gestures on a **real device**, not headless; and **look again the next day** — imperfections invisible during development surface with fresh eyes. Report findings as a **Before / After / Why** table.

## Bans

- `ease` (browser default, mediocre).
- `linear` on anything except progress bars and ticking loaders.
- Bounce / elastic / overshoot on UI elements. Dated; signals "template".
- Animating `width`, `height`, `top`, `left`, `margin`, `padding`.
- `will-change` set preemptively across a whole class. Only on the element, only while it's animating. (The vendored `scrollcraft.css` sets it preemptively on seven class-level selectors and so breaks this ban. **The engine is never edited** — the deviation is documented in [`motion-smoothness.md`](motion-smoothness.md) and cleared at runtime by the shim, not by touching the engine.)
- Casual parallax — see § Scroll-linked motion for the declared-device exception.
- `transition: transform` on any element that a scroll or pointer loop writes every frame. The transition eases each per-frame write over its own duration, and on a phone the element reads as lagging a full second behind the thumb. Parallaxed and magnetised elements transition **opacity only**.
- Custom cursors.
- Text-colour transitions (photosensitive risk).
- A CSS custom property on a parent used to drive children's transforms (style-recalc storm).
- ~~Scroll-driven animations without a reduced-motion fallback.~~ **F-011 (2026-09-07):** inte längre ett fel.
- Infinite loops (other than functional loaders) — they pull the eye and never let go.
