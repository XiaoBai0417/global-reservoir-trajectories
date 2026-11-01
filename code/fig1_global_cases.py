import numpy as np
import matplotlib.pyplot as plt

from common import annual_anomalies, load_case_tables, save_figure, set_plot_style
from common import MIN_ABSOLUTE_ANOMALY_KM2


def latest_year(flags):
    result = np.full(flags.shape[0], np.nan)
    for index, row in enumerate(flags):
        years = np.flatnonzero(row)
        if len(years):
            result[index] = 2017 + years[-1]
    return result


def main():
    set_plot_style()
    metadata, _, _ = load_case_tables()
    _, _, absolute, relative = annual_anomalies(metadata)
    detectable = np.abs(absolute) >= MIN_ABSOLUTE_ANOMALY_KM2
    expansion = (relative >= 0.10) & detectable
    contraction = (relative <= -0.10) & detectable
    last_expansion = latest_year(expansion)
    last_contraction = latest_year(contraction)

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.0), sharex=True, sharey=True)
    panels = [
        (axes[0], last_expansion, "Expansion", "YlGn"),
        (axes[1], last_contraction, "Contraction", "OrRd"),
    ]
    for ax, event_year, title, cmap in panels:
        valid = np.isfinite(event_year)
        points = ax.scatter(
            metadata.loc[valid, "lon"], metadata.loc[valid, "lat"],
            c=event_year[valid], cmap=cmap, vmin=2017, vmax=2025,
            s=23, edgecolor="white", linewidth=0.35,
        )
        ax.set_title(f"Latest {title.lower()} year")
        ax.set_xlim(-180, 180)
        ax.set_ylim(-60, 85)
        ax.set_xlabel("Longitude")
        ax.grid(color="#D9DEDF", linewidth=0.5)
        fig.colorbar(points, ax=ax, label="Year", ticks=np.arange(2017, 2026, 2))
    axes[0].set_ylabel("Latitude")
    fig.suptitle("Global reservoir sample: latest qualifying annual anomalies")
    fig.tight_layout()
    save_figure(fig, "Fig1_global_cases.png")


if __name__ == "__main__":
    main()
