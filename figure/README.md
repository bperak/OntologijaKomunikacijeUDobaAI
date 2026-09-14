# figure/ — figure knjige

Svaka figura ima: (1) izvornu skriptu u `kod/`, (2) izvor podataka, (3) datum izrade i (4) popis poglavlja u kojima se pojavljuje.

## Figure preuzete iz predavanja (IUC Dubrovnik, 11. 9. 2026.)

| datoteka | sadržaj | poglavlja |
|---|---|---|
| `omlcc_1.png`, `omlcc_2.png`, `omlcc_3.png` | ljestvica šesnaest razina kroz tri domene (materijalna / psihološka / društvena) | 2, 3 |
| `emotion_network.png` | mreža 125 hrvatskih emocionalnih leksema sa *strah* u središtu (izvor: vlastita figura) | 6 |
| `scale.png` | parametri, FLOP, Chinchilla, sparsnost | 9, 10 |
| `scoreboard.png` | rezultati i stropovi testova (GPQA, HLE) | 10 |
| `context.png` | rast kontekstnog prozora (512 → 10 M) | 10 |
| `trillion_club.png` | „klub 10¹² parametara" (Thompson 2026 — **procjene**) | 10 |
| `agent.png` | pet slojeva koji pretvaraju model u agenta | 12 |

## Alati
- vektorski izvori: **SVG** → PNG preko **resvg-py** (`cairosvg` i `soffice` u ovom okruženju ne rade).
- izvoz iz prezentacije: pptx → PDF → PyMuPDF (render) → provjera okvira.
- sve figure moraju proći **vizualnu provjeru** (nema rezanog teksta, nema prelijevanja).

## Napomena o autorskim pravima
Tuđe figure se **ne** kopiraju. Ako je figura tuđa, u knjizi se navodi izvor i, kad je dopušteno, preuzima uz atribuciju; inače se izrađuje vlastita verzija na temelju podataka uz citiranje izvora podataka.
