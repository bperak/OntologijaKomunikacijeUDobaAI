#!/usr/bin/env python3
"""check_refs.py — provjera unutarnjih uputa u rukopisu.

Zašto postoji
-------------
Knjiga je puna uputa oblika „→ pogl. 7.5", „(→ 14.6)", „slika 3.2", „tablica 10.3".
Takva uputa je obećanje: ako cilj ne postoji, čitatelj ostaje bez teksta, a urednik bez
objašnjenja. Do sada se to provjeravalo ručno (i tri su upute tako otkrivene 17. 9. 2026.),
pa je provjera pretvorena u alat:

  (A) svaka uputa na odjeljak („pogl. X.Y" / „→ X.Y" / „odjeljak X.Y") mora imati cilj;
  (B) svaka uputa na sliku („slika X.Y") mora imati potpis te slike;
  (C) svaka uputa na tablicu („tablica X.Y") mora imati naslov te tablice.

Pokretanje: python3 kod/check_refs.py   (0 = čisto, 1 = ima nalaza)
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUK = os.path.join(ROOT, "rukopis")


def datoteke():
    return sorted(glob.glob(os.path.join(RUK, "**", "*.md"), recursive=True))


def skup(tekst, uzorak):
    return set(re.findall(uzorak, tekst, re.M))


def main() -> int:
    dijelovi = {p: open(p, encoding="utf-8").read() for p in datoteke()}
    sve = "\n".join(dijelovi.values())

    # što postoji
    odjeljci = skup(sve, r"^#{2,4} (\d+\.\d+(?:\.\d+)?)")
    slike = skup(sve, r"^\*\*Slika (\d+\.\d+)\.\*\*")
    tablice = skup(sve, r"^\*\*Tablica (\d+\.\d+)[\.\s—–]")

    print(f"odjeljaka: {len(odjeljci)} | slika s potpisom: {len(slike)} | tablica s naslovom: {len(tablice)}")

    nalazi = []
    for put, tekst in sorted(dijelovi.items()):
        ime = os.path.relpath(put, RUK)
        # (A) upute na odjeljke
        for m in re.finditer(r"(?:pogl\.|odjeljak|odjeljku|→)\s*(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)(?![\d.])", tekst):
            if m.group(1) not in odjeljci:
                nalazi.append((ime, "odjeljak", m.group(1), tekst[max(0, m.start() - 60):m.start() + 40]))
        # (B) slike — preskaču se potpisi (oni su definicija, ne uputa)
        for m in re.finditer(r"(?<!^\*\*)(?<!\!\[)[Ss]lik[ae]\s+(\d{1,2}\.\d{1,2})(?![\d.])", tekst, re.M):
            if m.group(1) not in slike:
                nalazi.append((ime, "slika", m.group(1), tekst[max(0, m.start() - 60):m.start() + 40]))
        # (C) tablice
        for m in re.finditer(r"[Tt]ablic[aeu]\s+(\d+\.\d+)", tekst):
            if m.group(1) not in tablice and m.group(1) not in odjeljci:
                nalazi.append((ime, "tablica", m.group(1), tekst[max(0, m.start() - 60):m.start() + 40]))

    if nalazi:
        print(f"\n⚠ nalaza: {len(nalazi)}")
        for ime, vrsta, cilj, kontekst in nalazi:
            dodatak = "" if vrsta != "tablica" else " (ni kao odjeljak)"
            print(f"   - {ime}: {vrsta} {cilj} ne postoji{dodatak} → …{kontekst.strip()[:90]}…")
        return 1
    print("\n✔ sve unutarnje upute imaju cilj (odjeljci, slike, tablice)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
