#!/usr/bin/env python3
"""Provjera otvaranja poglavlja (metoda 'problem-first openings', ZAPIS-014/015).

Mjeri, za svako poglavlje, PRVA ČETIRI ODLOMKA PROZE nakon teze — neovisno o tome stoji li
otvaranje prije prve numerirane sekcije ili odmah iza njezina naslova (oba su slučaja u knjizi).

Prijavljuje:
  - broj riječi i rečenica u otvaranju;
  - traži li metoda situaciju, presliku i uputu (→);
  - je li otvaranje postalo FORMULA (iste prve četiri riječi u više od dvije datoteke).

Uporaba:  python3 kod/provjeri_otvaranja.py [--strogo]
"""
import os
import re
import sys
from collections import Counter

RUKOPIS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "rukopis")
SIMUL = re.compile(r"\b(?:Uzmimo|Zamisli|Netko|Svaki put|Radije|Pogledajmo|Tko|Vidjeli smo|Postoji|Čovjek|Riječ [a-zšđčćž]+ rabi se|Svaka rasprava)\b[^.]{20,}\.", re.UNICODE)
PRESLIKA = re.compile(r"(tablic|nalaz|uvjet pod kojim|mjerni|instrument|oblik gotovog|prediktivni test|scenarij)", re.I)
UPUTA = re.compile(r"→\s*(?:pogl\.|dodatk|Slika|Tablica)|\bodjeljak\s+\d+")


def otvaranje(tekst, odlomaka=4):
    """Prva `odlomaka` prozna odlomka nakon naslova i teze (bez aparata)."""
    telo = tekst
    telo = re.sub(r"^#\s[^\n]*\n", "", telo, count=1)                  # glavni naslov
    telo = re.sub(r"^>.*$", "", telo, flags=re.M)                      # teza (blok-citat)
    telo = re.sub(r"^!\[.*$", "", telo, flags=re.M)                    # slike
    telo = re.sub(r"^\|.*$", "", telo, flags=re.M)                     # tablice
    telo = re.sub(r"^```.*?^```", "", telo, flags=re.M | re.S)         # blokovi koda
    telo = re.sub(r"^-{3,}\s*$", "", telo, flags=re.M)                 # crte
    telo = re.sub(r"^#{1,6}\s+\d+\.[\d.]*\s.*$", "", telo, flags=re.M)  # numerirani naslovi
    telo = re.sub(r"^#{1,6}\s.*$", "", telo, flags=re.M)               # ostali naslovi
    parovi = [p.strip() for p in re.split(r"\n\s*\n", telo) if len(p.split()) >= 12]
    tok = "\n\n".join(parovi[:odlomaka])
    return tok


def main():
    strogo = "--strogo" in sys.argv
    dat = []
    for ime in sorted(os.listdir(RUKOPIS)):
        if not re.match(r"poglavlje-\d+\.md$", ime):
            continue
        tekst = open(os.path.join(RUKOPIS, ime), encoding="utf-8").read()
        tok = otvaranje(tekst)
        recenice = [r.strip() for r in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", tok)) if r.strip()]
        prva = recenice[0] if recenice else ""
        dat.append({
            "ime": ime, "rijeci": len(tok.split()), "recenica": len(recenice), "prva": prva,
            "kljuc": " ".join(prva.split()[:4]).lower(),
            "situacija": bool(SIMUL.search(tok)),
            "preslika": bool(PRESLIKA.search(tok)),
            "uputa": bool(UPUTA.search(tok)),
        })

    print(f"{'datoteka':<20}{'riječi':>7}{'reč.':>6}  {'situacija':<11}{'preslika':<11}{'uputa':<7}")
    for d in dat:
        print(f"{d['ime']:<20}{d['rijeci']:>7}{d['recenica']:>6}  "
              f"{'da' if d['situacija'] else 'NE':<11}{'da' if d['preslika'] else 'NE':<11}"
              f"{'da' if d['uputa'] else 'NE':<7}")

    nalazi = []
    for k, n in Counter(d["kljuc"] for d in dat if d["kljuc"]).items():
        if n > 2:
            nalazi.append(f"FORMULA: otvaranje počinje istim riječima u {n} datoteke — „{k}…\"")
    for p, n in Counter(d["prva"] for d in dat if d["prva"]).items():
        if n > 1:
            nalazi.append(f"ponovljena prva rečenica ({n}×): {p[:90]}…")
    for d in dat:
        if d["rijeci"] < 150:
            nalazi.append(f"{d['ime']}: otvaranje kratko ({d['rijeci']} riječi; metoda traži 250–450)")
        if not d["situacija"]:
            nalazi.append(f"{d['ime']}: nema konkretne situacije u otvaranju")
        if not d["preslika"]:
            nalazi.append(f"{d['ime']}: nema preslike rješenja (tablica/nalaz/uvjet/test)")
        if not d["uputa"]:
            nalazi.append(f"{d['ime']}: nema upute na ostatak knjige (→)")
    print("\n=== NALAZI ===")
    print("\n".join("  ⚠ " + n for n in nalazi) if nalazi else "  nema nalaza")
    return 1 if (nalazi and strogo) else 0


if __name__ == "__main__":
    sys.exit(main())
