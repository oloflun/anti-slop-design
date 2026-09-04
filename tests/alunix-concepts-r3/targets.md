# Måltabell — sektionshöjder ur referensen (2026-09-04, Antons rättning 2)

Mätt i `reference-mosaic.png` (spaltbredd 603 px). Alla värden i **andelar av spaltbredden (w)**.
Vid 1440 px viewport är w = 720 px; multiplicera. Höjder ska sättas i `cqw` (container-enheter), aldrig
i `vh`/`svh`, så att spalten är källsidans 1440-layout i halv skala oavsett fönsterhöjd.

## Vänster spalt (R5)

| sektion | från | till | höjd | vid w=720 |
|---|---|---|---|---|
| hero (konsolkortet, ljus text 0.10–0.35w) | 0 | 0.52w | 0.52w | 374 px |
| blått block (tes + Hyperborea-foto) | 0.52w | 0.99w | 0.47w | 338 px |
| papper: `VI BYGGER ERT VARUMÄRKE.` två rader | 1.09w | 1.25w | | rubriken börjar 72 px under blockets slut |
| ledger 01 / 02 / 03 (rubrikradernas överkant) | 1.41w · 1.53w · 1.65w | | 0.12w per rad | 86 px per rad |
| `Utvalda projekt` + Calyx-ramen börjar | 1.87w | | | 1346 px |
| sidan slutar (= Calyx-ramens nederkant) | | **2.69w** | Calyx 0.82w | 1937 px; Calyx 590 px |

## Höger spalt (R6)

| sektion | från | till | höjd | vid w=720 |
|---|---|---|---|---|
| affischordmärke `ALUNIX` (bokstäverna 0–0.19w) | 0 | 0.24w | 0.24w | 176 px |
| foto med `Er webbplats är nutidens visitkort.` (text 0.72–0.76w) | 0.24w | 0.83w | 0.59w | 421 px |
| tjänster (rubrik 1.08–1.28w, tre kolumner) | 0.83w | 1.28w | 0.45w | 328 px |
| svart ruta = **Hōrai-ramen, ingen rubrik, ingen intro** | 1.28w | 2.10w | 0.82w | 586 px |
| prisrutan (inverterad filosofi) | 2.10w | **2.69w** | 0.59w | 425 px |

Kolofonen (2.46–2.87w i referensen) finns inte längre. Båda spalterna slutar på 2.69w.

## Loggan

Höjd × 1.3 mot förra bygget: `--logo-h: clamp(114px, 11.7vw, 195px)`. Position oförändrad: centrerad på
skarven, vertikalt mitt emellan vänster heros nederkant (0.52w) och höger ordmärkes nederkant (0.24w),
dvs. 0.38w från sidans topp.

## Kontroll

`compare.py` renderar bygget vid 1440 och lägger referensen bredvid; sektionsgränserna ska ligga inom
±0.03w från tabellen.

## Tillägg (Anton, samma dag): Tidvatten i fotorutan

Höger spalts fotoruta (0.24w–0.83w, 0.59w hög) visar `<iframe src="/sites/tidvatten.html" title="Tidvatten">`
i stället för skrivbordsfotot: kantlös, kant till kant, interaktiv, exakt samma ruta och proportion.
Rubriken `Er webbplats är nutidens visitkort.` (+ kickern SVERIGE) ligger kvar som overlay men **nere till
höger, högerställd** (Tidvattens egen fold har sin text nere till vänster, se `tidvatten-720x421.png`; vattnet
nere till höger är mörkt och tomt), `pointer-events:none` så ramen förblir klickbar, ingen scrim om
kontrasten mäts ≥ 4.5:1 mot `tidvatten-720x421.png` (contrast_over_media.py), annars en liten lokal scrim
bara bakom texten. Fotots parallax utgår (en iframe får inte transformeras). Ramen laddas `loading="eager"`
(den är i folden).
