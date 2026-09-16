# figure/ — figure knjige

Figure su **autorske** (Benedikt Perak), izrađene za predavanje *Elements of Cognition in Complex Language* (IUC Dubrovnik, 11. 9. 2026.) i preuzete u knjigu. Svaka figura ima izvornu skriptu, izvor podataka i datum izrade.

## Popis (stvarna imena datoteka)

| datoteka | sadržaj | poglavlja |
|---|---|---|
| `fig_omlcc_s1.png`, `fig_omlcc_s2.png`, `fig_omlcc_s3.png` | ljestvica šesnaest razina kroz tri domene (materijalna 1–8 / psihološka 9–11 / društvena 12–16), svaka razina s relacijskom shemom; podnožje nosi tvrdnju *mreža → emergentni entitet → mreža sljedeće razine* (Emmeche, Køppe & Stjernfelt 1997) i atribuciju domena Searleu (1995; 2010) | **2**, 3 |
| `fig_omlcc16.png` | cjelovita ljestvica šesnaest razina (jedna slika) | 2 |
| `fig_emotion_network.png` | mreža 125 hrvatskih emocionalnih leksema sa *strah* u središtu (objavljeno u: Ban Kirigin & Perak 2020, *Rasprave IHJJ* 46(2): 957–996; ovdje izrezana) | **6** |
| `fig_strah_usporedba.png`, `fig_strah_vektori.png` | usporedba mrežnog i vektorskog prikaza leksema *strah* | 6, 10 |
| `fig_scale.png` | parametri, FLOP, Chinchilla, sparsnost | 9, 10 |
| `fig_trillion_club.png` | „klub 10¹² parametara" (Thompson 2026 — **procjene**) | 10 |
| `fig_scoreboard.png` | rezultati i stropovi testova (GPQA, HLE) | 10 |
| `fig_context.png` | rast kontekstnog prozora (512 → 10 M) | 10 |
| `fig_horizon.png` | vremenski horizont zadataka (METR 2025) | 10 |
| `fig_agent_hijerarhija.png` | pet slojeva koji pretvaraju model u agenta | **12** |
| `fig_searle.png` | Searleova podjela domena (brute / mental / institutional facts) | 2, 8 |
| `fig_razine.png`, `fig_hijerarhija.png`, `fig_emerg_hijerarhija.png` | prikazi hijerarhije i emergencije razina | 1, 3 |
| `fig_loops.png` | petlje procesiranja / unaprjeđenja konteksta | 11 |
| `fig_voda.png` | radni primjer (materijal → informacija → komunikacija) | 3 |

## Dijagrami (Mermaid) — vektorski

Četiri dijagrama izrađena su kao **Mermaid izvori** (`figure/izvori/*.mmd`) i renderirana alatom `kod/mermaid_render.py`: SVG je namijenjen **tisku** (vektor, skalira se bez gubitka), a PNG od 2000 px pregledu na GitHubu.

| dijagram | poglavlje | što prikazuje |
|---|---|---|
| `dijagram-4-2-cjevovod` | 4.2 | cjevovod od korpusa do tvrdnje, u dvama redovima (odluke 1–3, pa ugrađivanje i oznaka razine) |
| `dijagram-12-1-pet-dodataka` | 12.1 | pet dodataka i razine OMLCC-a na koje djeluju (8→13, 12, 6→14, 13, 14) |
| `dijagram-12-4-stablo-entitet` | 12.4 | stablo odluke po trima kriterijima kandidature; svaki negativan odgovor vodi u „poziv funkcije" |
| `dijagram-13-1-tri-konfiguracije` | 13.1 | tri konfiguracije komunikacije i raspored tereta; obveza nije priznata ni u jednoj |

⚠️ **Zamka koju alat rješava.** Mermaid CLI (mmdc) upisuje natpise u SVG kao HTML (`<foreignObject>`). Vektorski rendereri (resvg, InDesign, LaTeX) takve natpise **odbacuju** i okviri ostaju prazni — greška koja se otkrije tek u prijelomu. `kod/mermaid_render.py` zato svaki `foreignObject` prevodi u pravi `<text>` element i ispisuje kontrolu (mora biti 0 preostalih, uz popis vektorskih natpisa).

Izvori dijagrama ne smiju sadržavati ćirilične homoglife (npr. „Rаčuna" s ćiriličnim *а*) — provjerava `kod/check_cisto.py`.

## Koja je slika gdje u tekstu

| slika | datoteka | poglavlje |
|---|---|---|
| 1.1 | `fig_hijerarhija.png` | 1 |
| 1.2 | `fig_razine.png` | 1 |
| 2.1 | `fig_omlcc16.png` | 2 |
| 2.2 | `fig_omlcc_s1.png` | 2 |
| 2.3 | `fig_omlcc_s2.png` | 2 |
| 2.4 | `fig_omlcc_s3.png` | 2 |
| 2.5 | `fig_searle.png` | 2 |
| 3.1 | `fig_emerg_hijerarhija.png` | 3 |
| 3.2 | `fig_voda.png` | 3 |
| 4.1 | `dijagram-4-2-cjevovod.png` | 4 |
| 6.1 | `fig_emotion_network.png` | 6 |
| 9.1 | `fig_scale.png` | 9 |
| 10.1 | `fig_strah_usporedba.png` | 10 |
| 10.2 | `fig_strah_vektori.png` | 10 |
| 10.3 | `fig_context.png` | 10 |
| 10.4 | `fig_scale.png` | 10 |
| 10.5 | `fig_trillion_club.png` | 10 |
| 10.6 | `fig_scoreboard.png` | 10 |
| 10.7 | `fig_horizon.png` | 10 |
| 11.1 | `fig_loops.png` | 11 |
| 12.1 | `dijagram-12-1-pet-dodataka.png` | 12 |
| 12.2 | `fig_agent_hijerarhija.png` | 12 |
| 12.3 | `dijagram-12-4-stablo-entitet.png` | 12 |
| 13.1 | `dijagram-13-1-tri-konfiguracije.png` | 13 |

## Alati i provjera

- vektorski izvori: **SVG → PNG preko `resvg-py`** (`cairosvg` i LibreOffice u ovom okruženju ne rade).
- izvoz iz prezentacije: pptx → PDF → PyMuPDF (render) → **vizualna provjera** (`vision_analyze`): nema rezanog teksta, nema prelijevanja, natpisi odgovaraju tekstu knjige.
- **Pravilo:** ako natpis na slici i tekst knjige ne govore isto, ispravlja se **tekst** (ili se figura ponovno izrađuje) — figura nikad ne smije tvrditi više od onoga što je u tekstu.

## Autorska prava

Tuđe figure se **ne** kopiraju. Ako je figura tuđa, navodi se izvor; inače se izrađuje vlastita figura na temelju podataka, uz citiranje izvora podataka.

## Provjera rezolucije i prelijevanja teksta

```bash
python3 kod/check_figure_overflow.py figure/dijagram-*.png    # mjeri izlazi li tekst iz okvira
python3 kod/mermaid_render.py                                 # ponovno iscrtava sve dijagrame
```

**Rezolucija za tisak:** figura širine ~150 mm pri 300 dpi traži ≈1800 px; dijagrami se
izvoze na ~2200 px (Chromium), a SVG je vektorski pa se skalira bez gubitka. Tri starije
PNG figure (`fig_emerg_hijerarhija` 873×437, `fig_razine` 891×832, `fig_voda` 952×672)
ispod su te granice i treba ih ponovno izraditi ili zamijeniti dijagramom.

**Kako se dijagrami izrađuju (naučeno na vlastitim greškama):**
1. Izvor u `figure/izvori/*.mmd`; opcionalno prva linija `%% wrap: N` određuje širinu lomljenja natpisa.
2. `python3 kod/mermaid_render.py` → SVG (vektor, natpisi prevedeni iz `foreignObject`) + PNG
   (crta ga Chromium, pa se mjere fonta poklapaju s okvirima; ~2200 px širine).
3. `python3 kod/check_figure_overflow.py figure/dijagram-*.png` → mjeri izlazi li tekst iz okvira.
4. **Pregledati sliku očima** (uz `model.supports_vision: true` slika se prilaže izravno):
   mjerilo ne vidi preklapanja, nestale znakove ni prekratke lomove.
5. **Provjera veličine za tisak:** tekst ne smije ispod ~8 pt kad je figura široka 150 mm.
   Mjeri se omjerom visine fonta i širine slike (`veličina_fonta / širina_px × 150 mm`).
