import numpy as np
import matplotlib.pyplot as plt

from common import SIZE_ORDER, load_case_tables, monthly_matrix, save_figure, set_plot_style


def main():
    set_plot_style()
    metadata, monthly, month_columns = load_case_tables()
    values = monthly_matrix(metadata, monthly, month_columns)
    values[values <= 0] = np.nan

    mean = np.nanmean(values, axis=1)
    cv = np.nanstd(values, axis=1, ddof=1) / mean
    adjacent = np.abs(np.diff(values, axis=1))
    valid_pairs = np.isfinite(values[:, 1:]) & np.isfinite(values[:, :-1])
    adjacent[~valid_pairs] = np.nan
    monthly_change = np.nanmedian(adjacent, axis=1)

    med_cv, med_change, counts = [], [], []
    for size in SIZE_ORDER:
        mask = metadata["size_class"].eq(size).to_numpy()
        counts.append(int(mask.sum()))
        med_cv.append(float(np.nanmedian(cv[mask])))
        med_change.append(float(np.nanmedian(monthly_change[mask])))

    x = np.arange(len(SIZE_ORDER))
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.0))
    axes[0].bar(x, med_cv, color="#5789A5")
    axes[0].set_ylabel("Median coefficient of variation")
    axes[1].bar(x, med_change, color="#C47C55")
    axes[1].set_ylabel("Median absolute monthly change (km²)")
    axes[1].set_yscale("log")
    for ax in axes:
        ax.set_xticks(x, [f"{size}\n(n={count})" for size, count in zip(SIZE_ORDER, counts)])
        ax.grid(axis="y", color="#D9DEDF", linewidth=0.5)
    fig.suptitle("Global case sample: relative and absolute variability")
    fig.tight_layout()
    save_figure(fig, "Fig4_global_size.png")


if __name__ == "__main__":
    main()
