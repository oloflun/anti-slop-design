#!/usr/bin/env python3
"""preflight_taste.py - the taste rules the chain states as prose and never ran.

The gap this closes
-------------------
`design-taste-frontend` section 4.7 and its 62-item pre-flight contain a dozen
rules that are exactly countable - eyebrows per section, how many section
layouts repeat, how many zigzags in a row, how many elements in the hero, how
many words in a CTA. The chain carried them as prose, so every build was graded
on them by eye, which means they were graded inconsistently or not at all. The
em-dash rule (gate 75) is the clearest case: zero tolerance, trivially
checkable, and still shipped wrong more than once.

Counted, never judged. Anything needing taste stays with the critic.

    python preflight_taste.py FILE [--url URL] [--register editorial]
                              [--copy] [--json]

--url renders the file so computed styles are real (layout families, eyebrow
detection, radius scale). Without it the DOM-only checks still run.
--copy runs only the copy rules (em dash, filler verbs) - the copy gate's
mechanical sweep.

Exit 0 when clean, 1 with findings, 2 on tool failure.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Gate 75: zero visible em dashes, anywhere. En dash only in ranges.
EM_DASH = "—"
EN_DASH = "–"

FILLER_EN = ["elevate", "seamless", "unleash", "next-gen", "next generation",
             "revolutionize", "revolutionise", "delve", "tapestry", "unlock",
             "empower", "harness", "leverage", "robust", "cutting-edge"]
FILLER_SV = ["lyfta din", "lyfter din", "sömlös", "sömlöst", "nästa generation",
             "revolutionera", "kurerar", "i hjärtat av", "unik upplevelse",
             "älskad mötesplats", "skräddarsydd lösning", "helhetslösning"]

# The premium-consumer palette taste-skill 4.2 bans by name, as gate-89
# detection: cream + brass + espresso is a look every generator lands on.
TRAP_HEX = {
    "#f5f1ea": "premium-consumer cream", "#f7f3ec": "premium-consumer cream",
    "#b08947": "premium-consumer brass", "#c9a227": "premium-consumer brass",
    "#1a1714": "premium-consumer espresso", "#221f1b": "premium-consumer espresso",
    "#6366f1": "indigo (Tailwind default accent)", "#8b5cf6": "violet (AI default)",
    "#7c3aed": "violet (AI default)",
}

DOM_JS = r"""
(() => {
  const vw = innerWidth;
  const sel = (el) => {
    if (el.id) return '#' + el.id;
    const c = String(el.className || '').trim().split(/\s+/).filter(Boolean).slice(0,2).join('.');
    return el.tagName.toLowerCase() + (c ? '.' + c : '');
  };
  const sections = [...document.querySelectorAll('section, main > div, body > div')]
    .filter(el => el.getBoundingClientRect().height > 200);

  // Layout family, from computed layout rather than class names.
  const family = (el) => {
    const cs = getComputedStyle(el);
    const kids = [...el.children].filter(k => k.getBoundingClientRect().height > 20);
    if (el.querySelector('iframe')) return 'iframe';
    if (el.querySelector('table, dl') || kids.length >= 4 &&
        kids.every(k => getComputedStyle(k).borderBottomStyle !== 'none')) return 'ledger';
    if (cs.display === 'grid') {
      const track = (cs.gridTemplateColumns || '').split(' ').filter(Boolean);
      // A 12-column editorial grid is not a "3-up card grid": what matters is
      // how the CHILDREN span it. Measuring the track count alone classified
      // every label-rail section on the reference build as grid-3 and made the
      // section-family check fire on sites/calyx.html (2026-09-08).
      const wide = kids.filter(k => k.getBoundingClientRect().width > vw * 0.5).length;
      const narrow = kids.filter(k => {
        const w = k.getBoundingClientRect().width;
        return w > 0 && w < vw * 0.3;
      }).length;
      if (kids.length === 2 && narrow === 1 && wide === 1) return 'label-rail';
      if (track.length >= 3 && kids.length >= 3 && wide === 0) return 'grid-3';
      if (kids.length === 2) return 'split';
      if (track.length >= 3) return 'grid-3';
    }
    if (cs.display === 'flex' && kids.length === 2) return 'split';
    const img = el.querySelector('img, video, picture');
    if (img) {
      const r = img.getBoundingClientRect();
      if (r.width > vw * 0.92) return 'full-bleed-media';
    }
    if (cs.textAlign === 'center') return 'centered';
    return 'text-only';
  };

  // An eyebrow: small, uppercase, letterspaced, immediately before a heading.
  const eyebrows = [];
  for (const el of document.querySelectorAll('p, span, div, small')) {
    const cs = getComputedStyle(el);
    const size = parseFloat(cs.fontSize) || 0;
    const ls = parseFloat(cs.letterSpacing) || 0;
    if (size > 13 || cs.textTransform !== 'uppercase' || ls / (size || 1) < 0.1) continue;
    const nx = el.nextElementSibling;
    if (nx && /^H[1-3]$/.test(nx.tagName)) eyebrows.push(sel(el));
  }

  const radii = new Set();
  for (const el of document.querySelectorAll('*')) {
    const r = parseFloat(getComputedStyle(el).borderTopLeftRadius) || 0;
    if (r > 0) radii.add(Math.round(r));
  }

  const h1 = document.querySelector('h1');
  let heroLines = 0, heroKids = 0, heroPadTop = 0;
  if (h1) {
    const cs = getComputedStyle(h1);
    const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.2;
    heroLines = Math.round(h1.getBoundingClientRect().height / (lh || 1));
    const host = h1.closest('section, header, div') || h1.parentElement;
    heroKids = host ? [...host.children].filter(k => k.getBoundingClientRect().height > 12).length : 0;
    heroPadTop = host ? parseFloat(getComputedStyle(host).paddingTop) || 0 : 0;
  }

  const ctas = [...document.querySelectorAll('a, button')].filter(a => {
    const r = a.getBoundingClientRect();
    return r.height > 24 && r.width > 60 && (a.textContent || '').trim().length > 2;
  }).map(a => {
    const cs = getComputedStyle(a);
    const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.2;
    return {
      sel: sel(a), text: (a.textContent || '').trim().slice(0, 40),
      words: (a.textContent || '').trim().split(/\s+/).length,
      lines: Math.round(a.getBoundingClientRect().height / (lh || 1)),
    };
  });

  const navEl = document.querySelector('nav, header');
  const navH = navEl ? Math.round(navEl.getBoundingClientRect().height) : 0;

  return {
    sections: sections.map(s => ({ sel: sel(s), family: family(s) })),
    eyebrows, radii: [...radii].sort((a,b)=>a-b),
    heroLines, heroKids, heroPadTop, ctas, navH,
  };
})()
"""


def visible_text(html: str) -> str:
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"(?s)<!--.*?-->", " ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


def copy_checks(html: str):
    out = []
    text = visible_text(html)
    n_em = text.count(EM_DASH)
    if n_em:
        i = text.index(EM_DASH)
        out.append(("em-dash", "gate 75, nolltolerans: " + str(n_em) + " i synlig text, forsta: ..."
                    + text[max(0, i - 40):i + 40].strip() + "..."))
    for ph in FILLER_EN + FILLER_SV:
        if re.search(r"\b" + re.escape(ph) + r"\b", text, re.I):
            out.append(("filler", "'" + ph + "'"))
    low = html.lower()
    for hx, why in TRAP_HEX.items():
        if hx in low:
            out.append(("trap-hex", hx + " (" + why + ")"))
    if re.search(r"height:\s*100vh", low) and "dvh" not in low:
        out.append(("100vh", "height:100vh utan dvh - iOS adressfaltet flyttar den"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--url", default="")
    ap.add_argument("--register", default="", help="editorial/cinematic allow the apparatus budget")
    ap.add_argument("--copy", action="store_true", help="only the copy rules")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    path = Path(args.file)
    if not path.exists():
        print("preflight_taste: " + str(path) + " finns inte", file=sys.stderr)
        return 2
    html = path.read_text(encoding="utf-8", errors="replace")

    findings = [{"rule": r, "detail": d} for r, d in copy_checks(html)]
    notes = []

    if not args.copy and args.url:
        try:
            from playwright.sync_api import sync_playwright
        except Exception as e:
            print("preflight_taste: playwright saknas (" + str(e) + ")", file=sys.stderr)
            return 2
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": 1440, "height": 900})
            try:
                pg.goto(args.url, wait_until="networkidle", timeout=45000)
            except Exception:
                pg.goto(args.url, wait_until="load", timeout=45000)
            pg.wait_for_timeout(600)
            dom = pg.evaluate(DOM_JS)
            b.close()

        fams = [s["family"] for s in dom["sections"]]
        n_sec = len(fams)
        # ADVISORY, not a failure. "At least three distinct section anatomies"
        # is a real rule, but deciding what anatomy a section HAS is a
        # judgement, and this script's contract is "counted, never judged".
        # Measured on sites/calyx.html (2026-09-08) the classifier saw two
        # families where a reader sees five, so a FAIL here would train people
        # to ignore the whole report. It goes to the critic with the counts
        # attached instead.
        if n_sec >= 3 and len(set(fams)) < 3:
            notes.append("sektionsanatomi: klassificeraren ser bara "
                         + str(len(set(fams))) + " familj(er) over " + str(n_sec)
                         + " sektioner (" + ", ".join(sorted(set(fams)))
                         + ") - las sidan sjalv innan du tror pa siffran")
        for i in range(len(fams) - 1):
            if fams[i] == fams[i + 1] and fams[i] not in ("text-only",):
                findings.append({"rule": "upprepad-sektionslayout",
                                 "detail": "sektion " + str(i + 1) + " och " + str(i + 2)
                                           + " delar anatomi (" + fams[i] + ")"})
        runs, cur = 0, 0
        for f in fams:
            cur = cur + 1 if f == "split" else 0
            runs = max(runs, cur)
        if runs > 2:
            findings.append({"rule": "zigzag", "detail": str(runs) + " split-sektioner i rad (tak 2)"})

        cap = max(1, -(-n_sec // 3))
        if len(dom["eyebrows"]) > cap:
            findings.append({"rule": "eyebrows",
                             "detail": str(len(dom["eyebrows"])) + " > ceil(" + str(n_sec)
                                       + "/3) = " + str(cap)})

        # taste-skill's "hero <= 2 lines" is a SaaS-grotesk rule. A display
        # serif at clamp(3rem, 9vw, 9.5rem) is MEANT to wrap - that is the
        # poster. The reference build sites/calyx.html wraps to 4 and is
        # correct, so the print and cinematic registers get the wider cap.
        editorial = args.register.lower() in ("editorial", "editorial print", "print",
                                              "cinematic", "cinematic dark",
                                              "illustrated", "illustrated dark")
        hero_cap = 4 if editorial else 2
        if dom["heroLines"] > hero_cap:
            findings.append({"rule": "hero-h1-rader",
                             "detail": str(dom["heroLines"]) + " rader (tak " + str(hero_cap) + ")"})
        if dom["heroKids"] > 4:
            findings.append({"rule": "hero-stack", "detail": str(dom["heroKids"]) + " element (tak 4)"})
        if dom["heroPadTop"] > 96:
            findings.append({"rule": "hero-padding", "detail": str(round(dom["heroPadTop"])) + " px (tak 96)"})
        # An edition strip above the nav is licensed apparatus in the print
        # registers (house-physics: Hyperborea ships one), so the one-line cap
        # is not the right measure there.
        nav_cap = 104 if editorial else 80
        if dom["navH"] > nav_cap:
            findings.append({"rule": "nav-hojd",
                             "detail": str(dom["navH"]) + " px (tak " + str(nav_cap) + ")"})

        seen_intent = {}
        for c in dom["ctas"]:
            if c["lines"] > 1:
                findings.append({"rule": "cta-radbrytning", "detail": c["sel"] + " '" + c["text"] + "'"})
            if c["words"] > 3:
                findings.append({"rule": "cta-langd", "detail": "'" + c["text"] + "' (" + str(c["words"]) + " ord, tak 3)"})
            intent = re.sub(r"[^a-zaao ]", "", c["text"].lower()).split()
            key = next((w for w in intent if w in
                        ("boka", "kontakt", "kontakta", "hor", "book", "contact", "get", "start")), "")
            if key:
                if key in seen_intent or any(k in seen_intent for k in ("boka", "kontakt")):
                    findings.append({"rule": "cta-dubblerad-intent",
                                     "detail": "'" + c["text"] + "' upprepar en tidigare CTA-avsikt"})
                seen_intent[key] = c["text"]

        scales = {"sharp": range(0, 4), "soft": range(12, 17), "pill": range(999, 10000)}
        stray = [r for r in dom["radii"]
                 if not any(r in v for v in scales.values())]
        if stray and "radius:" not in html:
            findings.append({"rule": "shape-consistency-lock",
                             "detail": "radier utanfor {0-3, 12-16, 999}: "
                                       + ", ".join(str(r) for r in stray[:8])
                                       + " (dokumentera en avvikande skala med "
                                         "<!-- radius: ... --> om den ar avsiktlig)"})

    out = {"file": str(path), "findings": findings, "notes": notes,
           "pass": not findings}
    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print("preflight_taste " + ("PASS" if out["pass"] else
                                    "FAIL (" + str(len(findings)) + ")") + "  " + str(path))
        for f in findings:
            print("  %-26s %s" % (f["rule"], f["detail"]))
        for n in notes:
            print("  not: " + n)
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
