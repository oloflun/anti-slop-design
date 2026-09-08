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
    }
  } catch (e) { /* already registered, or unsupported — the lerp still works */ }

  var acts = [];
  var raf = null;

  function collect() {
    acts = Array.prototype.map.call(
      document.querySelectorAll('[data-sc-act]'),
      function (el) { return { el: el, cur: NaN, last: '' }; }
    );
  }

  function tick() {
    raf = null;
    var live = false;
    var frozen = !!window.__scFreezeMotion;

    for (var i = 0; i < acts.length; i++) {
      var a = acts[i];
      var t = parseFloat(getComputedStyle(a.el).getPropertyValue('--sc-p'));
      if (isNaN(t)) continue;
      if (isNaN(a.cur)) a.cur = t;          // first frame: adopt, never animate in

      if (frozen) {                          // ?preview= forces the formed state
        a.cur = t;
      } else {
        var d = t - a.cur;
        if (Math.abs(d) > DEAD) {
          a.cur += d * LERP;
          live = true;
        } else if (a.cur !== t) {
          a.cur = t;                         // snap the last sliver, no crawl
        }
      }

      // Write ONLY when the value actually changed. A custom property written
      // on a parent recalculates style for every descendant, and an act is the
      // ancestor of its whole stage — so an unconditional per-frame write costs
      // a full subtree recalc for acts that are standing still, on every frame
      // any OTHER act happens to be moving.
      var next = a.cur.toFixed(4);
      if (next !== a.last) {
        a.el.style.setProperty('--sc-ps', next);
        a.last = next;
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
  window.__scSmooth = {
    acts: acts, lerp: LERP, dead: DEAD,
    settle: function () {
      for (var i = 0; i < acts.length; i++) {
        var t = parseFloat(getComputedStyle(acts[i].el).getPropertyValue('--sc-p'));
        if (!isNaN(t)) {
          acts[i].cur = t;
          acts[i].last = t.toFixed(4);
          acts[i].el.style.setProperty('--sc-ps', acts[i].last);
        }
      }
    }
  };
})();
