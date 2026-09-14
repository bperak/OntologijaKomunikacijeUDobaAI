#!/usr/bin/env python3
"""Generira rječnik pojmova i CSV pregled iz registra pojmova (pojmovnik/koncepti.yaml).

Upotreba:
    python kod/pojmovnik_build.py            # piše pojmovnik/RJECNIK.md i pojmovnik/koncepti.csv
    python kod/pojmovnik_build.py --check    # samo provjeri (ne piše), izlaz 1 ako registar nije ispravan

Generirane datoteke se NE uređuju ručno — izvor istine je koncepti.yaml.
"""
import csv
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("Nedostaje PyYAML: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "pojmovnik", "koncepti.yaml")
OUT_MD = os.path.join(ROOT, "pojmovnik", "RJECNIK.md")
OUT_CSV = os.path.join(ROOT, "pojmovnik", "koncepti.csv")
BOOKS = {"kom2025": "Komunikacija u doba umjetne inteligencije (2025)",
         "dsk": "Data Science u kulturi (u izradi)",
         "razine": "Razine i entiteti (ova knjiga)"}


def load():
    with open(REG, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


def validate(data):
    errs, ids = [], []
    for k in data.get("koncepti", []):
        cid = k.get("id")
        ids.append(cid)
        for req in ("hr", "en", "definicija", "kanonski"):
            if not k.get(req):
                errs.append(f"{cid}: nedostaje polje '{req}'")
        kan = (k.get("kanonski") or "").split("/")
        if len(kan) != 2 or kan[0] not in BOOKS:
            errs.append(f"{cid}: kanonski='{k.get('kanonski')}' nije oblika <knjiga>/<poglavlje>")
        for rel in k.get("srodni", []) + [x.split("/")[0] for x in k.get("pojavljuje", [])]:
            if rel not in BOOKS and rel not in (data.get("koncepti") and [c["id"] for c in data["koncepti"]]):
                errs.append(f"{cid}: nepoznata referenca '{rel}'")
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errs.append("dvostruki id: " + ", ".join(sorted(dup)))
    return errs


def build(data):
    ks = data["koncepti"]
    lines = [
        "<!-- GENERIRANO skriptom kod/pojmovnik_build.py iz pojmovnik/koncepti.yaml — ne uređivati ručno. -->",
        "",
        "# Rječnik pojmova (zajednički za tri knjige)",
        "",
        f"Verzija registra: **{data['meta'].get('verzija')}** · datum: {data['meta'].get('datum')} · "
        f"pojmova: **{len(ks)}**",
        "",
        "Pojmovi su poredani abecedno. *Kanonski izvor* označava mjesto na kojem je pojam izložen najpotpunije; "
        "ostale knjige upućuju na njega umjesto da ga objašnjavaju iznova.",
        "",
        "| pojam (HR) | pojam (EN) | definicija | kanonski izvor | pojavljuje se još u |",
        "|---|---|---|---|---|",
    ]
    for k in sorted(ks, key=lambda x: x["hr"].lower()):
        kan = k["kanonski"]
        kb, ch = kan.split("/")
        kan_txt = f"{BOOKS[kb]}, pogl. {ch}"
        ostalo = ", ".join(f"{BOOKS.get(b, b)}, pogl. {c}" for b, c in (x.split("/") for x in k.get("pojavljuje", []))) or "—"
        lines.append(f"| **{k['hr']}** | {k['en']} | {k['definicija']} | {kan_txt} | {ostalo} |")
    lines += ["", "## Pojmovi koji se u ovoj knjizi ne smiju upotrebljavati izvan dogovorenog značenja", ""]
    for k in ks:
        if k.get("napomena"):
            lines.append(f"- **{k['hr']}** — {k['napomena']}")
    lines.append("")
    return "\n".join(lines)


def build_csv(data):
    rows = []
    for k in data["koncepti"]:
        for knjiga in ("kanonski", "pojavljuje"):
            val = k.get(knjiga) or []
            for v in ([val] if isinstance(val, str) else val):
                b, ch = v.split("/")
                rows.append({"id": k["id"], "pojam": k["hr"], "knjiga": b, "poglavlje": ch,
                             "uloga": "kanonski" if knjiga == "kanonski" else "pojavljuje se"})
    return rows


def main():
    check_only = "--check" in sys.argv
    data = load()
    errs = validate(data)
    if errs:
        print("❌ registar nije ispravan:")
        for e in errs:
            print("   -", e)
        return 1
    if check_only:
        print(f"✔ registar ispravan ({len(data['koncepti'])} pojmova)")
        return 0
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(build(data))
    rows = build_csv(data)
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "pojam", "knjiga", "poglavlje", "uloga"])
        w.writeheader()
        w.writerows(rows)
    print(f"✔ {OUT_MD} ({len(data['koncepti'])} pojmova)")
    print(f"✔ {OUT_CSV} ({len(rows)} zapisa)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
