#!/usr/bin/env python3
"""METR time-horizon growth + other yardsticks (IUC Dubrovnik deck)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

INK='#1C2B4A'; INK2='#334463'; ACC='#C0502E'; ACC2='#0F766E'; SOFT='#EEF2F8'
MUTED='#5A6B80'; LINEC='#D5DDE8'

# (decimal year, seconds, label, colour, dy-offset for label)
PTS = [
    (2020.45, 9,      'GPT-3 agents\n9 s', MUTED, 1.9),
    (2022.9, 36,      'GPT-3.5\n36 s', MUTED, 1.9),
    (2023.2, 240,     'GPT-4\n4 min', INK2, 1.9),
    (2024.7, 2400,    'o1\n40 min', INK2, 1.9),
    (2025.3, 7200,    'o3\n2 h', ACC2, 1.75),
    (2025.6, 12300,   'GPT-5\n3.4 h', ACC2, 0.28),
    (2025.97, 18000,  'Opus 4.5\n5 h', ACC2, 2.0),
    (2026.12, 47700,  'Opus 4.6\n~13 h', ACC, -0.30),
    (2026.35, 57600,  'Mythos Preview\n≥16 h', ACC, 0.28),
]

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.1, 4.0), dpi=200,
                              gridspec_kw={'width_ratios': [1.62, 1.0], 'wspace': 0.22})

# ---------- panel A: METR 50% time horizon, log scale ----------
xs, ys = [p[0] for p in PTS], [p[1] for p in PTS]
ax.plot(xs, ys, '-', color=LINEC, lw=2.0, zorder=2)
for x, y, lab, col, side in PTS:
    ax.scatter([x], [y], s=46, color=col, zorder=4)
    if side < 0:          # label to the left of the point
        ax.annotate(lab, (x, y), textcoords='offset points', xytext=(-8, 4), ha='right',
                    fontsize=7.2, color=col, fontweight='bold', linespacing=1.15, zorder=5)
    elif side > 1:        # label to the right of the point
        ax.annotate(lab, (x, y), textcoords='offset points', xytext=(9, -4), ha='left',
                    fontsize=7.2, color=col, fontweight='bold', linespacing=1.15, zorder=5)
    else:                 # label above the point
        ax.annotate(lab, (x, y), textcoords='offset points', xytext=(3, 7), ha='left',
                    fontsize=7.2, color=col, fontweight='bold', linespacing=1.15, zorder=5)
ax.set_yscale('log')
ax.set_ylim(4, 400000)
ax.set_xlim(2020.0, 2027.1)
ax.set_ylabel('50% time horizon\n(human-expert task length)', fontsize=8.6, color=INK2)
ax.set_title('Autonomy grows exponentially', fontsize=10.6, color=ACC, fontweight='bold', pad=6)
ax.tick_params(labelsize=8, right=False)
yticks = [10, 60, 3600, 86400]
ax.set_yticks(yticks)
ax.set_yticklabels(['10 s', '1 min', '1 h', '24 h'])
for s in ('top', 'right'): ax.spines[s].set_visible(False)
ax.spines['left'].set_color(LINEC); ax.spines['bottom'].set_color(LINEC)
ax.grid(axis='y', color=LINEC, lw=0.6, alpha=0.7)
ax.axhline(57600, color=ACC, lw=0.9, ls=':')
ax.text(2020.05, 92000, 'task suite ceiling — above this, measurements are unreliable',
        fontsize=6.8, color=ACC, style='italic')
ax.text(2020.05, 7000, 'doubling ≈ 7 months all-time\n≈ 3–4 months since 2024',
        fontsize=7.4, color=INK2, linespacing=1.3)

# ---------- panel B: other yardsticks ----------
labels = ['share of production code\nwritten by the model', 'agent research work per\nhuman day of work', 'speedup on well-defined\nresearch experiments']
vals = [80, 3, 52]
disp = [80, 30, 60]                    # normalised widths (diff. units, shown as labels)
cols = [ACC2, ACC, ACC]
ypos = [2.15, 1.05, -0.05]
for y, d, v, lab, col in zip(ypos, disp, vals, labels, cols):
    ax2.barh(y, d, height=0.46, color=col, zorder=3)
    ax2.text(0, y + 0.40, ' '.join(lab.split()), fontsize=7.3, color=INK2, va='bottom')
    ax2.text(d + 1.6, y, f'{v}%' if v == 80 else f'{v}×', va='center', fontsize=9.4,
             color=INK, fontweight='bold')
ax2.set_yticks([])
ax2.set_ylim(-0.55, 2.95)
ax2.set_xlim(0, 100)
ax2.set_xticks([])
ax2.set_title('Other yardsticks — different units, same direction',
              fontsize=9.4, color=ACC, fontweight='bold', pad=6)
for s in ('top', 'right', 'bottom'): ax2.spines[s].set_visible(False)
ax2.spines['left'].set_color(LINEC)
ax2.grid(axis='x', color=LINEC, lw=0.6, alpha=0.6, zorder=0)
ax2.text(0, -0.92, 'Anthropic 2026 (When AI builds itself); OpenAI 2026 (Research acceleration)',
         fontsize=6.8, color=MUTED, style='italic')

fig.subplots_adjust(left=0.085, right=0.985, top=0.90, bottom=0.10, wspace=0.20)
fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_horizon.png', facecolor='white',
            bbox_inches='tight', pad_inches=0.08)
print('saved fig_horizon.png')
