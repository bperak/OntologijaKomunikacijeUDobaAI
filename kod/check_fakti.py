#!/usr/bin/env python3
"""Provjera zajedničke evidencije brojki (data/fakti.csv) protiv rukopisa.

Provjerava:
  1. strukturu evidencije (broj polja, obavezna polja, dopuštene vrste);
  2. brojke s mjernom jedinicom u rukopisu — postoje li u evidenciji;
  3. dvostruke id-ove i nepotvrđene brojke (oznaka ❓ u napomeni).

Upotreba:
    python kod/check_fakti.py           # izvještaj (upozorenja ne ruše izlaz)
    python kod/check_fakti.py --strict  # izlaz 1 ako ima neevidentiranih brojki
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "data", "fakti.csv")
RUK = os.path.join(ROOT, "rukopis")
POLJA = ["id", "brojka", "jedinica", "izvor", "datum_izvora", "vrsta", "pojavljuje_se_u", "napomena"]
VRSTE = {"mjereno", "procjena", "izvedeno", "mjereno (zaokruženo)"}

# jedinice koje u tekstu označavaju mjerljivu tvrdnju (ne godine, ne brojevi poglavlja)
UNITS = r"(tokena|token|parametara|parametra|neurona|sinapsi|leksema|tipova neurona|dimenzija|%|sekundi|sati|milijuna|razina)"

# generičke vrijednosti: pojavljuju se kao dio argumenta, a ne kao mjerenje
# (npr. „100 % pitanja", „oko 20 % pitanja nema neosporan odgovor") — ne idu u evidenciju
GENERICKE = {0.0, 20.0, 100.0}


def num(t: str):
    """Broj iz zapisa; podržava raspone ('10-20') i oba decimalna zapisa ('51.3' i '51,3').

    Hrvatski rukopis piše decimalni zarez, a evidencija decimalnu točku. Ranija je verzija
    svaku točku brisala kao razdjelnik tisućica, pa se '51.3' čitalo kao 513 i provjera je
    lažno prijavljivala svaku decimalnu brojku (npr. HLE 51,3 %). Zato:
      - '10.000'  -> 10000   (sve skupine iza prve imaju točno 3 znamenke = tisućice)
      - '51.3'    -> 51.3    (decimalna točka)
      - '51,3'    -> 51.3    (decimalni zarez)
      - '10.000,5'-> 10000.5 (hrvatski zapis)
    """
    t = t.strip()
    if "," in t and "." in t:
        t = t.replace(".", "").replace(",", ".")
    elif "," in t:
        t = t.replace(",", ".")
    elif "." in t:
        dijelovi = t.split(".")
        if (len(dijelovi) > 1
                and all(len(x) == 3 and x.isdigit() for x in dijelovi[1:])
                and dijelovi[0].isdigit()):
            t = "".join(dijelovi)          # tisućice: 10.000 -> 10000
    for sep in ("-", "\u2013", "\u2014", " do "):
        if sep in t:
            dijelovi = [x for x in t.split(sep) if x.strip()]
            if len(dijelovi) == 2:
                a, b = (num(x) for x in dijelovi)
                if a is not None and b is not None:
                    return (a + b) / 2
    try:
        return float(t)
    except ValueError:
        return None


def norm(v: float):
    return str(int(v)) if v == int(v) else str(v)


def main():
    strict = "--strict" in sys.argv
    errs, warn = [], []
    rows = {}
    with open(LEDGER, encoding="utf-8") as f:
        lines = [l for l in f if not l.startswith("#")]
    for i, r in enumerate(csv.DictReader(lines), start=2):
        if None in r or len(r) != len(POLJA):
            errs.append(f"redak {i}: krivi broj polja ({len(r)} umjesto {len(POLJA)})")
            continue
        rid = r["id"]
        if rid in rows:
            errs.append(f"redak {i}: dvostruki id '{rid}'")
        rows[rid] = r
        if not r["vrsta"] in VRSTE:
            errs.append(f"redak {i} ({rid}): nedopuštena vrsta '{r['vrsta']}'")
        if r["brojka"] and num(r["brojka"]) is None and r["jedinica"].upper() not in {"ISBN", "DOI", "URN"}:
            errs.append(f"redak {i} ({rid}): brojka '{r['brojka']}' nije broj (jedinica '{r['jedinica']}' traži broj)")
        if "❓" in (r["napomena"] or ""):
            warn.append(f"{rid}: nepotvrđeno (❓) — ne citirati bez provjere")

    # brojke iz rukopisa s jedinicom
    known = {num(r["brojka"]) for r in rows.values() if num(r["brojka"]) is not None}

    def poznato(v: float) -> bool:
        """Je li brojka u evidenciji — uz toleranciju za zaokruživanje (51 % ≈ 51.3 %)."""
        return any(abs(k - v) <= max(0.01 * abs(k), 0.5) for k in known)
    hits = []
    if os.path.isdir(RUK):
        for fn in sorted(os.listdir(RUK)):
            if not fn.endswith(".md"):
                continue
            txt = open(os.path.join(RUK, fn), encoding="utf-8").read()
            for m in re.finditer(r"(\d[\d.,]*)\s*" + UNITS, txt):
                v = num(m.group(1))
                if v is None or v < 10:      # jednocifrene brojke su najčešće redni brojevi razina
                    continue
                if v in GENERICKE:           # opisno, ne mjerljivo
                    continue
                if not poznato(v):
                    hits.append(f"{fn}: '{m.group(0).strip()}' nema u evidenciji")

    print("=== Evidencija brojki ===")
    print(f"zapisa: {len(rows)} | mjereno: {sum(1 for r in rows.values() if r['vrsta'].startswith('mjereno'))}"
          f" | procjena: {sum(1 for r in rows.values() if r['vrsta']=='procjena')}"
          f" | izvedeno: {sum(1 for r in rows.values() if r['vrsta']=='izvedeno')}")
    if warn:
        print("\n⚠ nepotvrđeno u evidenciji:")
        for w in warn:
            print("   -", w)
    if hits:
        print("\n⚠ brojke u rukopisu koje nisu u evidenciji:")
        for h in hits:
            print("   -", h)
    if errs:
        print("\n❌ greške u evidenciji:")
        for e in errs:
            print("   -", e)
        return 1
    if strict and hits:
        return 1
    print("\n✔ evidencija je strukturno ispravna")
    return 0


if __name__ == "__main__":
    sys.exit(main())
