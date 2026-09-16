"""fig_scale.py — growth of model size: parameters (left) and training compute (right).
Sources: Epoch AI parameter/compute database (2026); GPT-4 total = 2023 SemiAnalysis leak estimate.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

INK = '#1C2B4A'; INK2 = '#334463'; ACC = '#C0502E'; ACC2 = '#0F766E'
MUTED = '#5A6B80'; LINEC = '#D5DDE8'; PAPER = '#FCFBF8'; DEEP = '#8E3A20'

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.edgecolor': LINEC,
                     'axes.labelcolor': INK, 'xtick.color': MUTED, 'ytick.color': MUTED,
                     'axes.linewidth': 0.9, 'figure.facecolor': PAPER, 'axes.facecolor': PAPER})

fig = plt.figure(figsize=(13.4, 3.72), dpi=220)
gs = fig.add_gridspec(1, 2, width_ratios=[1.46, 1.0], wspace=0.20,
                      left=0.05, right=0.985, top=0.855, bottom=0.135)

# ============================ panel A: parameters ============================
ax = fig.add_subplot(gs[0, 0])
ax.set_yscale('log')
ax.set_ylim(5e7, 9e12)
ax.set_xlim(2017.85, 2026.75)

for x, y in [(2018.45, 1.17e8), (2018.85, 3.4e8), (2019.15, 1.5e9), (2019.80, 1.1e10),
             (2020.45, 1.75e11), (2021.85, 5.3e11), (2021.95, 2.8e11), (2022.25, 5.4e11),
             (2022.20, 7.0e10), (2023.15, 6.5e10), (2024.55, 4.05e11)]:
    ax.plot([x], [y], 'o', ms=5.4, mfc=ACC, mec='white', mew=0.7, zorder=4)

for x, y, a in [(2023.25, 1.76e12, 2.8e11), (2024.95, 6.71e11, 3.7e10),
                (2025.55, 1.00e12, 3.2e10), (2025.32, 2.0e12, 2.88e11),
                (2025.28, 4.0e11, 1.7e10), (2025.30, 2.35e11, 2.2e10)]:
    ax.plot([x, x], [a, y], '-', color=LINEC, lw=1.1, zorder=2)
    ax.plot([x], [y], 's', ms=5.6, mfc='none', mec=INK, mew=1.3, zorder=5)
    ax.plot([x], [a], 'o', ms=3.3, mfc=INK2, mec='none', zorder=5)

ax.add_patch(Rectangle((2023.55, 5e7), 2026.75 - 2023.55, 8.95e12, facecolor=LINEC,
                       alpha=0.42, zorder=0, edgecolor='none'))

labels = [
    ('GPT-1 117M', 2018.45, 1.17e8, 2018.60, 7.0e7, 'left'),
    ('GPT-2 1.5B', 2019.15, 1.5e9, 2019.32, 2.4e9, 'left'),
    ('GPT-3 175B', 2020.45, 1.75e11, 2020.22, 3.1e10, 'right'),
    ('MT-NLG 530B', 2021.85, 5.3e11, 2021.62, 1.05e12, 'right'),
    ('Chinchilla 70B', 2022.20, 7.0e10, 2022.02, 2.5e10, 'right'),
    ('PaLM 540B', 2022.25, 5.4e11, 2022.52, 9.0e11, 'left'),
    ('Llama-3.1-405B', 2024.55, 4.05e11, 2024.30, 9.5e10, 'center'),
    ('GPT-4 total (2023 leak estimate)', 2023.25, 1.76e12, 2023.34, 3.3e12, 'left'),
    ('Llama 4 Behemoth ~2T (preview)', 2025.32, 2.0e12, 2025.42, 4.6e12, 'center'),
    ('Kimi K2 1T / 32B', 2025.55, 1.00e12, 2025.62, 6.4e11, 'left'),
    ('DeepSeek-V3 671B / 37B', 2024.95, 6.71e11, 2024.82, 3.4e10, 'left'),
]
for name, x, y, lx, ly, ha in labels:
    ax.annotate(name, (x, y), xytext=(lx, ly), fontsize=8.0, color=INK, ha=ha, va='center', zorder=7)

ax.annotate('Llama 4 Maverick 400B / 17B\nQwen3-235B-A22B 235B / 22B',
            xy=(2025.29, 3.1e11), xytext=(2026.35, 1.35e10), fontsize=8.0, color=INK,
            ha='center', va='center', linespacing=1.3, zorder=7,
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.7))
ax.text(2026.68, 6.6e7, 'from here the frontier\nstops reporting totals',
        ha='right', va='bottom', fontsize=7.5, color=MUTED, style='italic',
        linespacing=1.3, zorder=6)

ax.set_yticks([1e8, 1e9, 1e10, 1e11, 1e12])
ax.set_yticklabels(['100 M', '1 B', '10 B', '100 B', '1 T'], fontsize=8)
ax.set_xticks([2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
ax.set_xticklabels(['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'], fontsize=8)
ax.set_title('Parameters per model: four orders of magnitude, then a change of axis',
             fontsize=10.4, color=INK, pad=6, loc='left')
ax.grid(axis='y', color=LINEC, lw=0.6, alpha=0.7)
ax.set_axisbelow(True)
for s in ('top', 'right'):
    ax.spines[s].set_visible(False)
ax.plot([], [], 'o', ms=5.4, mfc=ACC, mec='white', label='dense')
ax.plot([], [], 's', ms=5.6, mfc='none', mec=INK, mew=1.3, label='MoE — total parameters')
ax.plot([], [], 'o', ms=3.3, mfc=INK2, label='active per token')
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=7.1, frameon=False,
          labelspacing=0.3, handletextpad=0.5)

# ============================ panel B: compute ============================
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_yscale('log')
ax2.set_ylim(1.2e17, 4e27)
ax2.set_xlim(2011.8, 2027.9)

pts = [('AlexNet', 2012.7, 4.7e17, 2012.85, 5.6e17, 'left'),
       ('GPT-3', 2020.45, 3.14e23, 2020.18, 1.0e23, 'right'),
       ('PaLM', 2022.25, 2.5e24, 2022.00, 7.0e23, 'right'),
       ('GPT-4', 2023.25, 2.0e25, 2023.00, 3.6e24, 'right'),
       ('Gemini 1.5 Ultra', 2024.35, 1.0e26, 2024.12, 2.4e26, 'right'),
       ('Claude 3.5 Sonnet', 2024.50, 3.0e25, 2024.28, 8.0e24, 'right'),
       ('GPT-4.5', 2025.20, 2.0e26, 2024.95, 5.0e26, 'right')]
xs = [p[1] for p in pts]; ys = [p[2] for p in pts]
ax2.plot(xs, ys, '-', color=LINEC, lw=1.2, zorder=2)
for name, x, y, lx, ly, ha in pts:
    ax2.plot([x], [y], 'o', ms=5.0, mfc=ACC2, mec='white', mew=0.7, zorder=4)
    ax2.annotate(name, (x, y), xytext=(lx, ly), fontsize=7.9, color=INK2, ha=ha, va='center', zorder=6)

ax2.add_patch(Rectangle((2026.05, 1.4e26), 1.75, 1.3e27, facecolor=ACC, alpha=0.12,
                        edgecolor=ACC, lw=0.8, linestyle='--', zorder=1))
ax2.text(2026.95, 4.1e26, '2026 runs:\n$200–500 M', fontsize=6.9, color=DEEP,
         ha='center', va='center', linespacing=1.3, zorder=6)
ax2.annotate('~8 orders of magnitude\nin 11 years', xy=(2012.75, 6.8e17), xytext=(2015.9, 3.5e20),
             fontsize=7.4, color=MUTED, ha='center', va='center', linespacing=1.3,
             arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.7))
ax2.set_yticks([1e18, 1e20, 1e22, 1e24, 1e26])
ax2.set_yticklabels(['$10^{18}$', '$10^{20}$', '$10^{22}$', '$10^{24}$', '$10^{26}$'], fontsize=8)
ax2.set_xticks([2013, 2016, 2019, 2022, 2025])
ax2.set_xticklabels(['2013', '2016', '2019', '2022', '2025'], fontsize=8)
ax2.set_title('Training compute per run: ~4–5×/year,\n~10×/year for leading labs (2020–24)',
              fontsize=10.4, color=INK, pad=6, loc='left', linespacing=1.35)
ax2.grid(axis='y', color=LINEC, lw=0.6, alpha=0.7)
ax2.set_axisbelow(True)
for s in ('top', 'right'):
    ax2.spines[s].set_visible(False)

fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_scale.png', dpi=220, facecolor=PAPER)
print('fig_scale.png written')
