#!/usr/bin/env python3
"""Izvlači podatke iz doktorata (Perak 2014) u data/izvori/doktorat-2014/ (CSV + README).

Upotreba: python kod/izvuci_doktorat.py
Napomena: normalizira naslijeđeno kodiranje tekstnog sloja; pomak stranica PDF = tiskana + 24."""
import csv
import os
import re
import pymupdf

PDF = '/home/agent/doktorat/Perak-2014_DOKTORAT_-_Opojmljivanje_leksema_strah.pdf'
BOOK = '/home/agent/knjiga-emergencija'
OUT = os.path.join(BOOK, 'data/izvori/doktorat-2014')
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(PDF)
MAP = {'ĉ': 'č', 'Ĉ': 'Č', 'Ċ': 'ć', 'ţ': 'ž', 'Ţ': 'Ž', 'ŝ': 'š', 'Ŝ': 'Š'}
P = []
for i in range(doc.page_count):
    t = doc[i].get_text()
    for a, b in MAP.items():
        t = t.replace(a, b)
    P.append(t)
PAIR = r'([a-zčćžšđ]{3,20}(?:\s+se)?)\s*\(\s*(\d{1,3})\s*\)'
rows = []
for i, t in enumerate(P):
    flat = re.sub(r'\s+', ' ', t)
    for m in re.finditer(r'(?:' + PAIR + r'\s*[,;]?\s*){3,}', flat):
        pairs = re.findall(PAIR, m.group(0))
        ns = [int(n) for _, n in pairs]
        if max(ns) > 150:
            continue
        if max(ns) >= 100 and sum(1 for a, b in zip(ns, ns[1:]) if abs(a - b) == 1) >= 3:
            continue
        for g, n in pairs:
            rows.append({'leksem': g, 'n': int(n), 'pdf_str': i + 1, 'tiskana_str': i + 1 - 24,
                         'kontekst': flat[max(0, m.start() - 110):m.start()].strip()[-110:]})
rows = sorted(rows, key=lambda r: (-r['n'], r['leksem']))
with open(os.path.join(OUT, 'frekvencije-leksema.csv'), 'w', encoding='utf-8', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=['leksem', 'n', 'pdf_str', 'tiskana_str', 'kontekst'])
    wr.writeheader()
    wr.writerows(rows)
print('frekvencije-leksema.csv:', len(rows))
vrh = rows[:12]
for r in vrh:
    print('  ', r['leksem'], r['n'], '| str.', r['tiskana_str'])

readme = """# Podaci izvuceni iz doktorskog rada (Perak 2014)

**Izvor:** Perak, B. (2014). *Opojmljivanje leksema strah u hrvatskome: sintaktičko-semantička analiza* (doktorski rad).
Filozofski fakultet Sveučilišta u Zagrebu. 474 str. PDF: https://github.com/bperak/doktorat-strah

**Metoda izvlačenja:** automatski, iz tekstualnog sloja PDF-a (PyMuPDF), uz normalizaciju naslijeđenog kodiranja
(č→ĉ, ć→Ċ, ž→ţ, š→ŝ u izvornom sloju). Skripta: `kod/izvuci_doktorat.py`. **Pomak stranica:** PDF stranica = tiskana + 24
(provjereno na trima uzorcima: PDF 269 → 245, PDF 328 → 304, PDF 393 → 369).

## Datoteke

| datoteka | sadržaj | redaka |
|---|---|---|
| `prijedlozne-konstrukcije.csv` | prijedložni izrazi s leksemom *strah* i brojem pojavnica (n) | 41 |
| `frekvencije-leksema.csv` | frekvencijske liste glagola i leksema uz *strah* | %(fb)d |
| `emocije-nabrajanja.csv` | nabrajanja emocionalnih leksema u izvorniku (sirovi retci + izdvojeni leksemi) | 3 |
| `ishodisne-domene.csv` | parovi izraz + aktivirana ishodišna domena (iz tablica) | 50 |

## Ključne provjerene brojke (s izvornim stranicama)

| brojka | vrijednost | mjesto u izvorniku |
|---|---|---|
| korpus | Hrvatski nacionalni korpus, **131,8 Mw** | sažetak, str. 6 (PDF) |
| pojavnice leme *strah* | **14.875** | sažetak, str. 6 (PDF) |
| izraz *od straha* | **825** pojavnica (drugi po čestotnosti) | tiskana str. 304 |
| glagoli uz *od straha* | drhtati (62), umrijeti (61), tresti (39), trnuti (18), plakati (12), kriknuti (11), izbezumiti (10), bježati (9), razboljeti se (8), osloboditi (8), ukočiti (8) | tiskana str. 304 |
| konstrukcija s *miješati* | *miješati* (n=17), *prožeti* (n=6), *prodrijeti* (n=4) | tiskana str. 369 |

## Ograničenja (obavezno navesti u knjizi)

1. **Automatsko izvlačenje** može propustiti retke prelomljene preko stranica i tablice s višestupčanim slogom; svaka brojka koja ulazi u knjigu **provjerava se na navedenoj stranici** izvornika.
2. Kodiranje izvornika ima artefakte (npr. *iznenaćenje* mjesto *iznenađenje*); leksemi se u knjizi navode u normiranom obliku, a izvorni redak ostaje u CSV-u kao dokaz.
3. `ishodisne-domene.csv` je **parcijalan** popis (tablice su višestupčane) — koristi se kao ilustracija, ne kao potpun inventar.
4. Rad nije recenziran kao publikacija (doktorski rad); pri citiranju se navodi kao doktorski rad s mentorom i ustanovom.
""" % {'fb': len(rows)}
open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write(readme)
print('README podataka: napisan')

