/* TEST COPY of scroll/sc-smooth.js for plan 028's measurement. Two changes:
 *  (1) --sc-p is read from the act's INLINE style (the engine writes it there),
 *      never through getComputedStyle: a computed-style read after the engine's
 *      writes forces a synchronous style recalc per act per frame.
 *  (2) all --sc-ps writes happen after all reads (one recalc per frame).
 *  (3) --sc-p registered inherits:false (no consumer reads it via var()).
 * Everything else identical to the shipped shim. */
(function () {
  'use strict';
  var LERP = 0.16;
  var DEAD = 0.0005;
  try {
    if (window.CSS && CSS.registerProperty) {
      CSS.registerProperty({ name: '--sc-ps', syntax: '<number>', inherits: true, initialValue: '0' });
    }
  } catch (e) {}
  try {
    if (window.CSS && CSS.registerProperty && window.__scpNoInherit !== false) {
      CSS.registerProperty({ name: '--sc-p', syntax: '<number>', inherits: false, initialValue: '0' });
    }
  } catch (e) {}
  var acts = [];
  var raf = null;
  function collect() {
    acts = Array.prototype.map.call(document.querySelectorAll('[data-sc-act]'),
      function (el) { return { el: el, cur: NaN, last: '', next: '' }; });
  }
  function tick() {
    raf = null;
    var live = false;
    var frozen = !!window.__scFreezeMotion;
    var i, a, t, d;
    for (i = 0; i < acts.length; i++) {
      a = acts[i];
      t = parseFloat(a.el.style.getPropertyValue('--sc-p'));   // inline, no recalc
      if (isNaN(t)) { a.next = ''; continue; }
      if (isNaN(a.cur)) a.cur = t;
      if (frozen) { a.cur = t; }
      else {
        d = t - a.cur;
        if (Math.abs(d) > DEAD) { a.cur += d * LERP; live = true; }
        else if (a.cur !== t) { a.cur = t; }
      }
      a.next = a.cur.toFixed(4);
    }
    for (i = 0; i < acts.length; i++) {
      a = acts[i];
      if (a.next && a.next !== a.last) { a.el.style.setProperty('--sc-ps', a.next); a.last = a.next; }
    }
    if (live) raf = requestAnimationFrame(tick);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(tick); }
  function start() {
    collect(); kick();
    addEventListener('scroll', kick, { passive: true });
    addEventListener('resize', function () { collect(); kick(); }, { passive: true });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(kick).catch(function () {});
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
  window.__scSmooth = {
    acts: acts, lerp: LERP, dead: DEAD,
    settle: function () {
      for (var i = 0; i < acts.length; i++) {
        var t = parseFloat(acts[i].el.style.getPropertyValue('--sc-p'));
        if (!isNaN(t)) { acts[i].cur = t; acts[i].last = t.toFixed(4); acts[i].el.style.setProperty('--sc-ps', acts[i].last); }
      }
    }
  };
})();
