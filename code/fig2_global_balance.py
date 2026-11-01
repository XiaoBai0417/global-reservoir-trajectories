import numpy as np
import matplotlib.pyplot as plt

from common import annual_matrix, load_case_tables, save_figure, set_plot_style


def main():
    set_plot_style()
    metadata, _, _ = load_case_tables()
    areas = annual_matrix(metadata)
    changes = np.diff(areas, axis=1)
    expansion = np.maximum(changes, 0).sum(axis=0)
    contraction = -np.minimum(changes, 0).sum(axis=0)
    gross = np.abs(changes).sum()
    net = (areas[:, -1] - areas[:, 0]).sum()
    intervals = [f"{year}–{year + 1}" for year in range(2017, 2025)]
    x = np.arange(len(intervals))

    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.bar(x, expansion, color="#C75B45", label="Expansion")
    ax.bar(x, -contraction, color="#447A9C", label="Contraction")
    ax.axhline(0, color="#30383A", linewidth=0.8)
    ax.set_xticks(x, intervals, rotation=35, ha="right")
    ax.set_ylabel("Area change across the 100 global cases (km²)")
    ax.set_title(f"Gross interannual change = {gross:,.1f} km²; endpoint net change = {net:+,.1f} km²")
    ax.legend(ncols=2)
    fig.tight_layout()
    save_figure(fig, "Fig2_global_balance.png")


if __name__ == "__main__":
    main()
