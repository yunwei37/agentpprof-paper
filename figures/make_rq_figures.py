#!/usr/bin/env python3
"""Generate the result figures for the AgentProf paper."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'figure.figsize': (3.33, 2.1),
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'font.family': 'serif',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'lines.linewidth': 1.2,
    'pdf.fonttype': 42,
})

BLUE = '#2196F3'
RED = '#E57373'
GRAY = '#9E9E9E'


def make_rq2_deltas():
    """Paired MAP deltas with bootstrap intervals over the complete RQ2 populations."""
    workloads = ['AgentProcess-\nBench', 'HINTBench', 'TraceElephant']

    # Direct+AgentProf minus the benchmark's own judge/localizer.
    over_direct = [0.031, 0.107, 0.117]
    over_direct_lo = [0.024, 0.093, 0.088]
    over_direct_hi = [0.039, 0.120, 0.148]

    # Direct+AgentProf minus the information-matched raw-action control.
    over_matched = [0.0013, -0.0007, 0.0017]
    over_matched_lo = [-0.0003, -0.0116, -0.0247]
    over_matched_hi = [0.0029, 0.0103, 0.0280]

    def err(point, lo, hi):
        return np.array([[p - l for p, l in zip(point, lo)],
                         [h - p for p, h in zip(point, hi)]])

    x = np.arange(len(workloads))
    width = 0.36
    fig, ax = plt.subplots(figsize=(3.33, 2.25))

    ax.bar(x - width / 2, over_direct, width, color=BLUE, alpha=0.9,
           edgecolor='white', label='vs.\ benchmark judge')
    ax.errorbar(x - width / 2, over_direct, yerr=err(over_direct, over_direct_lo, over_direct_hi),
                fmt='none', ecolor='#37474F', elinewidth=0.9, capsize=2.5)

    ax.bar(x + width / 2, over_matched, width, color=GRAY, alpha=0.9,
           edgecolor='white', hatch='//', label='vs.\ raw-action control')
    ax.errorbar(x + width / 2, over_matched, yerr=err(over_matched, over_matched_lo, over_matched_hi),
                fmt='none', ecolor='#37474F', elinewidth=0.9, capsize=2.5)

    ax.axhline(0, color='#37474F', linewidth=0.8)
    ax.set_ylabel('MAP difference')
    ax.set_xticks(x)
    ax.set_xticklabels(workloads, fontsize=7)
    ax.set_ylim(-0.05, 0.175)
    ax.legend(fontsize=7, loc='upper left', framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('fig-rq2-deltas.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig-rq2-deltas.png', bbox_inches='tight', dpi=300)
    print('Wrote fig-rq2-deltas.pdf/png')


if __name__ == '__main__':
    make_rq2_deltas()
