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


def num(t: str):
    """Broj iz zapisa; podržava i raspone (npr. '10-20', '10–20')."""
    t = t.strip().replace(".", "").replace(",", ".")
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
    known = {norm(num(r["brojka"])) for r in rows.values() if num(r["brojka"]) is not None}
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
                if norm(v) not in known:
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
