import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from common import (
    TRAJECTORY_COLORS,
    TRAJECTORY_ORDER,
    load_case_tables,
    monthly_matrix,
    save_figure,
    set_plot_style,
)


def main():
    set_plot_style()
    metadata, monthly, month_columns = load_case_tables()
    use_columns = [column for column in month_columns if column[:4] <= "2025"]
    values = monthly_matrix(metadata, monthly, use_columns)
    dates = pd.to_datetime([column.replace("_", "-") for column in use_columns])
    deseasonalized = np.full_like(values, np.nan, dtype=float)

    for row in range(len(metadata)):
        series = values[row]
        baseline = float(metadata.iloc[row]["long_term_mean_area_km2"])
        if not np.isfinite(baseline) or baseline <= 0:
            continue
        for month in range(1, 13):
            month_mask = dates.month == month
            climatology = np.nanmean(series[month_mask])
            deseasonalized[row, month_mask] = (series[month_mask] - climatology) / baseline * 100

    fig, ax = plt.subplots(figsize=(9.0, 4.4))
    classes = metadata["trajectory_class"].astype(str).to_numpy()
    for name in TRAJECTORY_ORDER:
        indices = np.flatnonzero(classes == name)
        if not len(indices):
            continue
        subset = deseasonalized[indices]
        median = np.nanmedian(subset, axis=0)
        lower = np.nanpercentile(subset, 25, axis=0)
        upper = np.nanpercentile(subset, 75, axis=0)
        color = TRAJECTORY_COLORS[name]
        ax.plot(dates, median, color=color, linewidth=1.5, label=f"{name} (n={len(indices)})")
        ax.fill_between(dates, lower, upper, color=color, alpha=0.13, linewidth=0)
    ax.axhline(0, color="#343A3C", linewidth=0.8)
    ax.set_ylabel("Deseasonalized anomaly (% of reservoir mean)")
    ax.set_xlabel("Year")
    ax.set_xlim(dates[0], dates[-1])
    ax.set_title("Global case trajectories, 2017–2025")
    ax.legend(ncols=2, fontsize=8)
    ax.grid(axis="y", color="#D9DEDF", linewidth=0.5)
    fig.tight_layout()
    save_figure(fig, "Fig5_global_trajectories.png")


if __name__ == "__main__":
    main()
