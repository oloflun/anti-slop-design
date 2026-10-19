# 024 · Kortet vid 90 grader: H-10 mätt, kortets tjocklek synlig

- **Status**: TODO (skriven i loop 1; **utanför R7**, taket åtta planer gick till 026 (kodfel). Byggs i loop 2 om H-10:s kant fortfarande läses som tråd)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46`
- **Severity**: LOW
- **Category**: Physicality (kortets tjocklek), H-10
- **Estimated scope**: 1 fil, 1 rad CSS; resten är mätning som skrivs i NOTES.md

## Problem

HELHET.md § 2 läste `v3c-1440-flip-05-045.png` som "vid 90° står en hårlinje på ~400 px i
ett 896 px brett tomrum", och H-10 satte golvet: kortets projicerade höjd mitt i vändningen
≥ 75 % av vilohöjden. Loop 1 mätte det (`shots/loop-1/diag/diag.json`, `flips`, 1440x900,
shimen frusen):

| `--flip` | framsidans projicerade box (b x h) | kanten `.plate-edge` (b x h) |
|---|---|---|
| 0 | 896 x 504 | 0,3 x 504 |
| 0,2 | 647 x 490 | 1,1 x 490 |
| 0,3 | 453 x 485 | 1,7 x 485 |
| 0,4 | 233 x 482 | 2,2 x 482 |
| 0,45 | 118 x 482 | 2,3 x 482 |
| **0,5** | **0 x 481** | **2,3 x 481** |
| 0,6 | 233 x 482 | 2,2 x 482 |

Projicerad höjd vid 90°: 481 / 504 = **95,5 %** (390x844: 350 / 405 = 86,4 %). H-10:s tal
är alltså uppfyllt i R6-läget; det som HELHET läste som "tunn linje i tomrum" är kortets
egen tjocklek (2 px) sedd rakt från sidan, `preview/preview-1440-mid.png`.

Parabeln `scale(1 - 0.72·f·(1-f))` kan inte lättas: den oskalade projicerade höjden är
~587 px vid 90° (481 / 0,82) och ~553 px vid f = 0,2 (490 / 0,885) mot plåtens 504 px med
`overflow:clip`. Redan 0,57 i stället för 0,72 lägger kortets hörn på klippkanten vid
f = 0,2 till 0,4 (503 px). Parabeln står.

Det som återstår av fyndet är kanten: 2 px vid 1440 läser som en tråd, inte som ett kort
sett på högkant. `.plate-edge` är kortets tjocklek (rad 423-431, "Kortets egen tjocklek");
ett 896 px brett kort med 2 px kant är ett pappersark, inte ett visitkort.

```css
/* index.html:423-424 - current */
  .plate-edge{position:absolute;right:0;top:0;bottom:0;width:2px;
    transform-origin:100% 50%;transform:rotateY(90deg);pointer-events:none;
```

## Target

Kanten 2 px → **4 px** vid 1440 (kortets tjocklek i skala: 4 / 896 = 0,45 %, ett tjockt
visitkort), 3 px vid 390 (kortet är 324 px brett; 4 px vore 1,2 %).

```css
/* target, index.html:423 */
  .plate-edge{position:absolute;right:0;top:0;bottom:0;width:clamp(3px,0.45cqw,4px);
```

`cqw` mäter mot `.hero-plate` (`container-type:inline-size`, rad 356): 896 px → 4,0 px,
324 px → 3 px (golvet). Opacitetskurvan (`64·f³(1-f)³`, topp 1,0 vid f = 0,5) och gradienten
rörs inte. Inget annat ändras: vändningens fönster, span, dwell och parabel står (plan 011).

## Repo conventions to follow

- `.plate-edge` är ett rent CSS-barn på det kompositerade kortet; ingen JS, ingen ny token
  (gradienten är redan rgba-vit på `--frame-line`:s nivå).
- Ledgerrad i `BRIEF.md` § Byggarens rader, R7: "Kortets tjocklek 4 px" med mättabellen ovan
  som källa och H-10-talet 95,5 %.

## Steps

1. Byt rad 423 enligt Target.
2. Mät vid `?preview=mid`, 1440x900 och 390x844: `.plate-edge` `getBoundingClientRect().width`
   ≈ 4,0 respektive 3,0 px (± 0,3 px, perspektivet projicerar); kantens höjd ≥ 75 % av
   kortets vilohöjd (481 / 504 och 350 / 405 i dag).
3. Skriv H-10:s tal (95,5 % / 86,4 %) och kantbredden i NOTES.md § R7.

## Boundaries

- Rör inte `.plate-card`:s transform (rad 375-386), `--flip`-fönstret eller `section.hero`:s
  `data-sc-span`/`data-sc-dwell` (rad 971).
- Ingen ny färg, ingen skugga, ingen bredare gradient.
- Matchar inte rad 423-424: STOPPA.

## Verification

- **Mekaniskt:** rect-mätningen i steg 2; `motion_probe.py --track "section.hero:--sc-ps,.plate-card:transform" --cpu 4 --wheel 100:60 --ticks 40`: staircase 0, `--sc-ps` max_step ≤ 3 %, tal före/efter sida vid sida (ett bredare statiskt barn kostar inget, men det ska stå).
- **Skärmbild:** `?preview=mid` vid 1440 och 390 som bild: kanten läser som en kant, inte en tråd; tolv flip-ramar vid 1440: kanten tonar in sent (f ≈ 0,35) och ut igen (f ≈ 0,65), aldrig synlig i vila.
- **Done when:** H-10 bockad med talen 95,5 % (1440) och 86,4 % (390) och kanten 4 / 3 px.
