/* sc-smooth.js — publishes `--sc-ps` (smoothed) beside the engine's raw `--sc-p`.
 *
 * WHY THIS EXISTS (F-012, measured 2026-09-08)
 * --------------------------------------------
 * scrollcraft's own docstring explains why the video playhead is damped:
 * "wheel events do not arrive at a constant rate and a 1:1 write reproduces
 * every gap in them." That reasoning is correct and the engine applies it to
 * exactly two things — video `currentTime` and pointer tilt/magnet. Everything
 * else `read()` writes is 1:1 with raw scroll position, including `--sc-p`
 * itself (scrollcraft.js line ~857). So any bespoke motion a page drives off
 * `--sc-p` — a card that flips, a light pool that travels, a word scrub —
 * steps at the wheel's notch rate on a Windows mouse. That is the "hackigt och
 * billigt" Anton saw in r7.
 *
 * F-011 did NOT cause it. Setting `var reduce = false` turned the playhead
 * lerp ON (rate 1.0 -> 0.18); it removed no smoothing. The stepping is
 * architectural and has always been there.
 *
 * Two further reasons a raw custom property cannot glide on its own:
 *   1. `--sc-p` is UNREGISTERED, so it is a string to CSS and never
 *      interpolates. `CSS.registerProperty` below fixes that for `--sc-ps`.
 *   2. scrollcraft.css sets `transition: none` on cues and copy once
 *      `.sc-ready` lands, deliberately, so nothing bridges per-event writes.
 *
 * THE RULE THIS FILE ENFORCES
 * ---------------------------
 * Bespoke motion reads `--sc-ps`, never `--sc-p`, whenever it drives something
 * the eye sees MOVE (transform, object-position, clip-path, mask-position).
 * Cue opacity may read `--sc-p`. See references/motion-smoothness.md.
 *
 * The engine is never edited (scroll/NOTE.md: copy, never edit). This file is
 * copied in beside it and loaded after it.
 */
(function () {
  'use strict';

  var LERP = 0.16;      // per frame; 0.18 is the engine's playhead value, and a
                        // travelling element wants marginally more damping than
                        // a video seek because it has no decode latency of its own.
  var DEAD = 0.0005;    // below this the value has arrived; stop the loop.

  // Register --sc-ps as a real number so CSS can interpolate it and so a page
  // may `transition: --sc-ps` if it wants belt and braces. Guarded: Safari
  // before 16.4 has no registerProperty, and re-registering the same name
  // throws, which must not take the page down.
  //
  // inherits MUST be true. The value is published on the act element and read
  // by its descendants — the card, the plate, the scrubbed word. Measured
  // 2026-09-08: with `inherits: false` a child reading var(--sc-ps) gets the
  // initial value 0, not the parent's, so the act would sit frozen at its
  // start state on every page while the console stayed clean. The engine's own
  // --sc-p is unregistered and therefore inherits by default; registering the
  // smoothed twin with different inheritance would have broken the contract it
  // exists to mirror.
  try {
    if (window.CSS && CSS.registerProperty) {
      CSS.registerProperty({
        name: '--sc-ps', syntax: '<number>', inherits: true, initialValue: '0'
      });
      // PLAN 028 B (loop 2 profiling): --sc-p is the engine's raw value, written
      // on every act every frame. Unregistered, it inherits by default (a string
      // to CSS with no interpolation, but still an ordinary inherited custom
      // property) and so a write on the act invalidates its ENTIRE descendant
      // subtree — measured 1.84ms per write on hero alone (synth3.py). Nothing
      // in index.html, scrollcraft.css or scrollcraft.js ever reads var(--sc-p)
      // (grep, loop 2): only this file's own tick() reads it, off the element's
      // inline style, never through inheritance. Registering it inherits:false
      // measured 0.27ms per write on the same act — the descendants stop being
      // invalidated by a variable none of them consume.
      CSS.registerProperty({
        name: '--sc-p', syntax: '<number>', inherits: false, initialValue: '0'
      });
    }
  } catch (e) { /* already registered, or unsupported — the lerp still works */ }

  var acts = [];
  var raf = null;

  function collect() {
    acts = Array.prototype.map.call(
      document.querySelectorAll('[data-sc-act]'),
      function (el) { return { el: el, cur: NaN, last: '', next: '' }; }
    );
  }

  // PLAN 028 A (loop 2 profiling, profile.json/profile4.json): the engine
  // writes --sc-p as an INLINE style on every act, every frame, before this
  // shim ever runs. Reading it back through getComputedStyle forced a
  // synchronous style recalculation per act per frame (RecalcStyleCount 1.7
  // on hero alone, up to 4.6 on the band, against 1.0 in the control) because
  // each read landed between the engine's writes and this shim's OWN writes
  // to --sc-ps on the SAME elements, and every intervening write invalidated
  // the next read. Reading a.el.style.getPropertyValue skips the recalc
  // entirely: the value is already sitting on the element, no cascade needed.
  // Every read now happens in one pass, then every write happens in a SECOND
  // pass — batched — so no write in this function can dirty a read that
  // hasn't happened yet. Measured (synth/profile4, batched, cpu 1): hero p95
  // 35.5 -> 18.8ms, RecalcStyleCount per frame down to ~1.2 everywhere.
  function tick() {
    raf = null;
    var live = false;
    var frozen = !!window.__scFreezeMotion;
    var i, a, t, d;

    for (i = 0; i < acts.length; i++) {
      a = acts[i];
      t = parseFloat(a.el.style.getPropertyValue('--sc-p'));
      if (isNaN(t)) { a.next = ''; continue; }
      if (isNaN(a.cur)) a.cur = t;           // first frame: adopt, never animate in

      if (frozen) {                          // ?preview= forces the formed state
        a.cur = t;
      } else {
        d = t - a.cur;
        if (Math.abs(d) > DEAD) {
          a.cur += d * LERP;
          live = true;
        } else if (a.cur !== t) {
          a.cur = t;                         // snap the last sliver, no crawl
        }
      }
      a.next = a.cur.toFixed(4);
    }

    // Second pass: write only when the value actually changed. A custom
    // property written on a parent recalculates style for every descendant,
    // and an act is the ancestor of its whole stage — so an unconditional
    // per-frame write costs a full subtree recalc for acts that are standing
    // still, on every frame any OTHER act happens to be moving.
    for (i = 0; i < acts.length; i++) {
      a = acts[i];
      if (a.next && a.next !== a.last) {
        a.el.style.setProperty('--sc-ps', a.next);
        a.last = a.next;
      }
    }
    if (live) raf = requestAnimationFrame(tick);
  }

  function kick() { if (!raf) raf = requestAnimationFrame(tick); }

  function start() {
    collect();
    kick();
    addEventListener('scroll', kick, { passive: true });
    addEventListener('resize', function () { collect(); kick(); }, { passive: true });
    // A late-arriving font changes act heights, which changes --sc-p without a
    // scroll event; adopt the new target rather than waiting for the reader.
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(kick).catch(function () {});
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start, { once: true });
  } else {
    start();
  }

  // Handle for motion_probe.py and for a page that needs to force a settle.
  //
  // PLAN 031 (discovered while wiring the wrapper-reveal latch, not a plan
  // 028 change): `acts: acts` below captured the closure variable's value
  // AT OBJECT-LITERAL-CREATION TIME, which runs synchronously here, before
  // collect() has populated it (collect() waits for DOMContentLoaded when
  // the document is still parsing). window.__scSmooth.acts therefore stayed
  // permanently bound to the initial empty array `var acts = [];` declared
  // above, even after collect() reassigned the LOCAL `acts` variable to a
  // freshly populated one — the object's own property never saw the
  // reassignment. `settle()` was unaffected (a function closes over the
  // variable itself, not a snapshot of it, so it always read the live
  // value) — only the plain `acts` property was stale, and nothing before
  // plan 031 ever read it externally. A getter re-evaluates the closure
  // variable on every access instead of freezing it once.
  window.__scSmooth = {
    get acts() { return acts; }, lerp: LERP, dead: DEAD,
    settle: function () {
      for (var i = 0; i < acts.length; i++) {
        var t = parseFloat(acts[i].el.style.getPropertyValue('--sc-p'));
        if (!isNaN(t)) {
          acts[i].cur = t;
          acts[i].last = t.toFixed(4);
          acts[i].el.style.setProperty('--sc-ps', acts[i].last);
        }
      }
    }
  };
})();
