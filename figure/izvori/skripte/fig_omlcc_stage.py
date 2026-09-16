#!/usr/bin/env python3
"""OMLCC 16 levels, three progressive stages (three click-through slides).
stage 1 = MATERIAL (levels 1-8) · stage 2 = + PSYCHOLOGICAL (9-11) · stage 3 = + SOCIAL (12-16) and the new entity.
Domains follow Searle's ontology of facts: brute/physical · mental/psychological · social-institutional.
"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import textwrap

INK='#1C2B4A'; INK2='#334463'; ACC='#C0502E'; ACC2='#0F766E'; SOFT='#EEF2F8'
MUTED='#5A6B80'; LINEC='#D5DDE8'; DEEP='#8E3A20'

LEVELS = [
    ('01', 'Existence', 'A (Entity) exists', INK2, 1),
    ('02', 'Emergence', 'A (Form) becomes B (Transformation)', INK2, 1),
    ('03', 'MaterialStructure', 'A (Part) isPartOf B (Whole) · {stuff–object, member–collection}', INK2, 1),
    ('04', 'Spatial', 'A (Figure) is_in_spatial_relation_to B (Ground) · {place–area}', INK2, 1),
    ('05', 'Force', 'A (Force structure) influences B (Patient) · {portion–mass}', INK2, 1),
    ('06', 'Motion', 'A (Mover) moves on B (Path) with (Vehicle) · {mover–path}', INK2, 1),
    ('07', 'SequenceActivity', 'A (Activity) has sequence (3–6) · {feature–event}', INK2, 1),
    ('08', 'InformationSystem', 'A (Organism) acts / reacts to B (Environment 1–8)', ACC2, 1),
    ('09', 'Perception', 'A (Perceiver 8–11) perceives B (Object of perception 1–8)', ACC2, 2),
    ('10', 'Affect', 'A (Experiencer 8–14) experiences B (Affect state 10)', ACC2, 2),
    ('11', 'Cognition', 'A (Cogitor 8–14) thinks B (Mental representation 11)', ACC2, 2),
    ('12', 'SocIdentity', 'A (Person 8–14) identifies as B (Social identity 12)', ACC, 3),
    ('13', 'SocBehaviourInteraction', 'A (Person.Agent) performs B (Social interaction 13)', ACC, 3),
    ('14', 'SocCommunication', 'A (Communicator) communicates with B about C on D (code)', ACC, 3),
    ('15', 'SocCulturalInstitution', 'conventionalized norms and institutionalized power', ACC, 3),
    ('16', 'CulturalModel', 'values, beliefs and institutions shared by a community', DEEP, 3),
]
DOMS = {1: ('MATERIAL', 'brute facts · Searle 1995', INK2),
        2: ('PSYCHOLOGICAL', 'mental facts · Searle 1995', ACC2),
        3: ('SOCIAL', 'institutional facts · Searle 1995', ACC)}

STAGE = 3
fig, ax = plt.subplots(figsize=(12.1, 5.5), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

CW, GAPX = 46.0, 5.0
X0, X1 = 2.0, 2.0 + CW + GAPX
ROWH, ROWGAP, HDR = 6.4, 0.7, 3.3

# ---------- header + step chip ----------
ax.text(50, 98.6, 'OMLCC — 16 levels of ontological complexity (Perak 2018; 2019)',
        ha='center', va='center', fontsize=11.4, color=ACC, fontweight='bold')
steps = {1: ('1 / 3', 'material domain (levels 1–8)'),
         2: ('2 / 3', '+ psychological domain (9–11)'),
         3: ('3 / 3', '+ social domain (12–16) — and a new entity')}
lbl, sub = steps[STAGE]
if STAGE < 3:
    ax.add_patch(FancyBboxPatch((33.0, 93.9), 34.0, 3.6, boxstyle='round,pad=0,rounding_size=0.8',
                                fc=SOFT, ec='none', zorder=2))
    ax.text(50, 95.6, f'{lbl}    {sub}', ha='center', va='center', fontsize=8.6, color=INK2, zorder=4)

# ---------- rows, grouped in domain containers ----------
def draw_group(x, y_top, dom, indices):
    name, sub, col = DOMS[dom]
    revealed = dom <= STAGE
    n = len(indices)
    h = HDR + n * (ROWH + ROWGAP)
    y_bot = y_top - h
    ax.add_patch(FancyBboxPatch((x, y_bot), CW, h, boxstyle='round,pad=0,rounding_size=1.2',
                                fc='#FFFFFF' if revealed else '#FBFCFE',
                                ec=col if revealed else LINEC, lw=1.4 if revealed else 0.9,
                                ls='solid' if revealed else (0, (3, 3)), alpha=1.0 if revealed else 0.75, zorder=1))
    ax.add_patch(FancyBboxPatch((x + 1.2, y_top - HDR + 0.4), CW - 2.4, HDR - 0.8,
                                boxstyle='round,pad=0,rounding_size=0.7',
                                fc=col if revealed else '#F4F6FA', ec='none', zorder=2))
    ax.text(x + 2.4, y_top - HDR / 2 - 0.1,
            f'{name}  ·  {sub}',
            ha='left', va='center', fontsize=8.0,
            color='white' if revealed else MUTED, fontweight='bold', zorder=3)
    for k, idx in enumerate(indices):
        num, lname, schema, lcol, ld = LEVELS[idx]
        y = y_top - HDR - (k + 1) * (ROWH + ROWGAP) + ROWGAP
        if revealed:
            ax.add_patch(FancyBboxPatch((x + 1.2, y), 2.4, ROWH, boxstyle='round,pad=0,rounding_size=0.7',
                                        fc=lcol, ec='none', zorder=3))
            ax.text(x + 4.6, y + ROWH * 0.70, f'{num}  {lname}', ha='left', va='center',
                    fontsize=9.2, color=lcol, fontweight='bold', zorder=4)
            ax.text(x + 4.6, y + ROWH * 0.26, textwrap.fill(schema, 74), ha='left', va='center',
                    fontsize=6.9, color=MUTED, style='italic', zorder=4, linespacing=1.1)
        else:
            ax.add_patch(FancyBboxPatch((x + 1.2, y), CW - 2.4, ROWH, boxstyle='round,pad=0,rounding_size=0.7',
                                        fc='#F7F9FC', ec=LINEC, lw=0.7, ls=(0, (3, 3)), zorder=3))
            ax.text(x + 4.6, y + ROWH / 2, num, ha='left', va='center', fontsize=7.6,
                    color='#C7D0DE', zorder=4)
    return y_bot

y_after_material = draw_group(X0, 84.0, 1, list(range(0, 8)))
draw_group(X1, 84.0, 2, list(range(8, 11)))
draw_group(X1, 84.0 - (HDR + 3 * (ROWH + ROWGAP)) - 1.2, 3, list(range(11, 16)))

# ---------- footer ----------
ax.text(50, 12.6, 'Each level: network x  →  emergent entity {property}  →  network x+1   (Emmeche, Køppe & Stjernfelt 1997)',
        ha='center', va='center', fontsize=8.4, color=INK2)
bx = 8.0
for lab, col, dom in (('1–7  material', INK2, 1), ('8  informational', ACC2, 1),
                      ('9–11  psychological', ACC2, 2), ('12–15  social', ACC, 3), ('16  cultural', DEEP, 3)):
    if dom <= STAGE:
        ax.add_patch(FancyBboxPatch((bx, 4.4), 1.4, 3.0, boxstyle='round,pad=0,rounding_size=0.6', fc=col, ec='none'))
        ax.text(bx + 2.2, 5.9, lab, ha='left', va='center', fontsize=7.8, color=INK2)
    bx += 17.6
ax.text(50, 0.9, 'Three domains after Searle (1995; 2010): material (brute facts) · psychological (mental facts) · social (institutional facts).',
        ha='center', va='center', fontsize=8.4, color=ACC, fontweight='bold')

fig.savefig(f'/home/agent/iuc-dubrovnik-2026/fig_omlcc_s{STAGE}.png', facecolor='white',
            bbox_inches='tight', pad_inches=0.06)
print(f'saved fig_omlcc_s{STAGE}.png')
