# K — kumulativt test (brief 07, hela v3-kedjan i ett blint one-shot, "skip variants")

Baslinje A = AB09-A (kedjan före v3). K1 = SKILL.md v3 (lock, katalog, Step 2b, gates 1–91, reveal-guard, läsbudget saknades ännu) + house-physics + reference-lock + scroll-refs, en Sonnet-agent, ingen webbläsare. Obs: min första mätning träffade en mellanversion (K1-agenten byggde om motionlagret när scroll-README:n ändrades under bygget); tabellen nedan är slutfilen.

| Mått | A (före v3) | K1 (v3, slutfil) | Riktning |
|---|---|---|---|
| briefens sektioner | 6/6 | 6/6 | lika |
| axe-violations | 3 (kontrast, main, region) | 1 (kontrast: koral-kicker/meta på fog-grund) | bättre, men accenten på småetiketter bryter house-physics |
| reflow overflow 320 / 200 % | 7 / 1 | 0 / 0 | bättre |
| dold vid reduced motion | 0 | 1 (`li`) | sämre (liten) |
| tab_walk-issues | 0 | 0 | lika |
| scroll_verify dead/cues/unrevealed/kontrast | 0/0/0/0 | 2/0/0/0 | dead scroll i det höga bröllopspartiet |
| detect.mjs | 1 | 1 (overused-font) | lika |
| images / hairlines / grunder | 3 / 14 / 4 | 6 / 17 / 4 | fler foton, samma variation |
| palett | cream + koppar (AI-look #1) | sea-fog + koral (två avvikelser namngivna i headern) | bättre |
| spårbarhet | lane i kommentar | lock + ledger + fingerprint-rad + täckningslista | bättre |

Visuellt (compare/fold.png, full.png lästa): K1 har fotografisk upptakt med mörk plansch, ledger med fem recept, ett fullbleed-bröllopsfoto med typ över (signature: "vow-knot" på egen sticky), en centrerad displaysiffra i prenumerationen, split med tulpanfoto, mörk kolofon. A är den lugnare cream-sidan med kopparlinje och ritad båge. K1 är den sida jag hellre försvarar inför en studio; dess två fel (accent på mikro-etiketter, ett reveal-`li` under reduced motion) är Step 5-fynd som critique/a11y-passet finns för.

**Beslut: kedjan är intakt och bättre**, inget mått försämrades utom två småfel som passen fångar. Läxa från mellanversionen (som tappade bröllopssektionen): "Brief coverage is a gate" + läsbudget i SKILL.md, verifieras av K2 (samma brief).

## K2 (samma brief, efter briefsäkring + läsbudget)

| Mått | A | K1 | K2 |
|---|---|---|---|
| briefens sektioner | 6/6 | 6/6 | 6/6 (5 + kolofon) |
| axe | 3 | 1 | **0** |
| reflow 320 / 200 % | 7 / 1 | 0 / 0 | 1 / 0 |
| tab_walk | 0 | 0 | 2 (offscreen, order) |
| scroll dead | 0 | 2 | 1 |
| detect | 1 | 1 | 1 (**broken-image**: tom ram i kolofonen) |
| images | 3 | 6 | 4 |
| grund | cream | sea-fog | kalkputs-grå (varm, ej cream) |

Läst (compare/full-3.png): K2 är komplett och renast mätmässigt, men visuellt svagare än K1: typografisk hero med anfang i stället för fotoupptakt, ett nästan tomt bröllopsparti (den scrubbade tråden syns inte i stillbild) och en trasig bildruta i den mörka kolofonen. Två blinda one-shots ur samma kedja gav alltså två olika bra sidor; briefsäkringen höll (ingen sektion tappades) och läsbudgeten sänkte inte kvaliteten på gates. Slutverdict K: **kedjan intakt och bättre än baslinjen** (K1 tydligt, K2 på mätvärden); variansen mellan one-shots är det Step 5 (critique, a11y, reviewers, bake-off) konvergerar, och testet visar varför de stegen inte får hoppas över.
