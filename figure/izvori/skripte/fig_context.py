"""fig_context.py — context window growth 2018–2026 (tokens, log). Running maximum + selected model points.
Sources: provider documentation & Sept-2026 comparison trackers; Meta Llama 4 blog (10 M advertised).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

INK = '#1C2B4A'; INK2 = '#334463'; ACC = '#C0502E'; ACC2 = '#0F766E'
MUTED = '#5A6B80'; LINEC = '#D5DDE8'; PAPER = '#FCFBF8'; DEEP = '#8E3A20'

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.edgecolor': LINEC,
                     'axes.labelcolor': INK, 'xtick.color': MUTED, 'ytick.color': MUTED,
                     'axes.linewidth': 0.9, 'figure.facecolor': PAPER, 'axes.facecolor': PAPER})

PTS = [('GPT-1 512', 2018.45, 512, ACC2),
       ('GPT-2 1k', 2019.12, 1024, ACC2),
       ('GPT-3 2k', 2020.42, 2048, ACC2),
       ('GPT-4 8k', 2023.22, 8192, INK),
       ('GPT-4 Turbo 128k', 2023.88, 128000, INK),
       ('Claude 2.1 200k', 2023.90, 200000, DEEP),
       ('Gemini 1.5 Pro 1M', 2024.12, 1000000, INK),
       ('Llama 4 Scout 10M', 2025.26, 10000000, ACC),
       ('Grok 4.20 2M', 2026.18, 2000000, MUTED),
       ('Gemini 3.1 Pro', 2026.10, 1048576, INK),
       ('GPT-5.6', 2026.62, 1050000, INK),
       ('Claude Opus/Sonnet 5', 2026.55, 1000000, DEEP)]

fig, ax = plt.subplots(figsize=(12.6, 2.9), dpi=220)
fig.subplots_adjust(left=0.072, right=0.988, top=0.83, bottom=0.235)
ax.set_yscale('log')
ax.set_ylim(280, 9e7)
ax.set_xlim(2017.9, 2027.7)

xs, ys, mx = [], [], 0
for lab, x, y, c in sorted(PTS, key=lambda p: p[1]):
    if y > mx:
        if xs:
            xs.append(x); ys.append(mx)
        mx = y
        xs.append(x); ys.append(mx)
ax.step(xs, ys, where='post', color=ACC, lw=1.8, zorder=3, alpha=0.9)
ax.text(2021.5, 3.2e6, 'running maximum', fontsize=7.9, color=ACC, style='italic', zorder=6)

for lab, x, y, c in PTS:
    ax.plot([x], [y], 'o', ms=5.6, mfc=c, mec='white', mew=0.8, zorder=5)

# individual labels only where they are unambiguous
LBL = [('GPT-1 512', 2018.45, 512, 2018.58, 512, 'left'),
       ('GPT-2 1k', 2019.12, 1024, 2019.26, 1024, 'left'),
       ('GPT-3 2k', 2020.42, 2048, 2020.58, 2048, 'left'),
       ('GPT-4 8k', 2023.22, 8192, 2023.02, 8192, 'right'),
       ('GPT-4 Turbo 128k', 2023.88, 128000, 2023.60, 330000, 'right'),
       ('Claude 2.1 200k', 2023.90, 200000, 2024.05, 200000, 'left'),
       ('Gemini 1.5 Pro 1M', 2024.12, 1000000, 2024.28, 620000, 'left'),
       ('Llama 4 Scout 10M (advertised record)', 2025.26, 10000000, 2025.05, 2.4e7, 'right'),
       ('Grok 4.20 2M', 2026.18, 2000000, 2025.95, 4.2e6, 'right')]
for lab, x, y, lx, ly, ha in LBL:
    ax.annotate(lab, (x, y), xytext=(lx, ly), fontsize=7.9, color=INK, ha=ha, va='center', zorder=7)

ax.axhspan(1e6, 1.32e6, color=ACC2, alpha=0.12, zorder=1)
ax.text(2018.05, 1.15e6, 'frontier 2026 converged at ~1 M', fontsize=7.7, color=ACC2, va='center', zorder=6)
ax.text(2026.62, 2.1e5, 'GPT-5.6 1.05 M\nClaude Opus/Sonnet 5 1 M\nGemini 3.1 Pro 1 M', fontsize=7.4,
        color=INK2, ha='center', va='center', linespacing=1.35, zorder=7)

ax.annotate('', xy=(2020.42, 2048), xytext=(2025.26, 10000000),
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.8, ls='--'), zorder=2)
ax.text(2022.6, 4.6e4, '×5,000', fontsize=8.4, color=MUTED, style='italic', ha='center', zorder=6)

ax.set_yticks([1e3, 1e4, 1e5, 1e6, 1e7])
ax.set_yticklabels(['1 k', '10 k', '100 k', '1 M', '10 M'], fontsize=8.4)
ax.set_xticks([2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
ax.set_xticklabels(['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'], fontsize=8.4)
ax.grid(axis='y', color=LINEC, lw=0.6, alpha=0.7)
ax.set_axisbelow(True)
for s in ('top', 'right'):
    ax.spines[s].set_visible(False)
ax.set_title('Context window (tokens held at once) — advertised maxima, 512 → 10 M',
             fontsize=10.2, color=INK, pad=7, loc='left')
fig.text(0.072, 0.055, '1 M tokens ≈ 700,000 words ≈ a small reference corpus (10 M ≈ 5 M words). Advertised maxima: effective capacity is lower (context rot), and\n'
         'production harnesses cap below the API maximum — e.g. Codex defaults GPT-5.6 to 272 k. Window size is also a product decision, not a monotone trend (Grok 4.6 ships 500 k).',
         fontsize=7.4, color=MUTED, style='italic', linespacing=1.45)
fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_context.png', dpi=220, facecolor=PAPER)
print('fig_context.png written')
