import numpy as np
import matplotlib.pyplot as plt

from common import (
    MIN_ABSOLUTE_ANOMALY_KM2,
    SIZE_ORDER,
    annual_anomalies,
    load_case_tables,
    save_figure,
    set_plot_style,
)


def recurrence_percent(relative, absolute, threshold, direction):
    detectable = np.abs(absolute) >= MIN_ABSOLUTE_ANOMALY_KM2
    if direction == "Expansion":
        events = (relative >= threshold) & detectable
    else:
        events = (relative <= -threshold) & detectable
    has_event = events.any(axis=1)
    recurrent = events.sum(axis=1) >= 2
    denominator = int(has_event.sum())
    return 100 * recurrent.sum() / denominator if denominator else np.nan


def main():
    set_plot_style()
    metadata, _, _ = load_case_tables()
    _, _, absolute, relative = annual_anomalies(metadata)
    thresholds = [0.10, 0.15, 0.20]
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0), sharey=True)

    for ax, direction in zip(axes, ["Expansion", "Contraction"]):
        for size in SIZE_ORDER:
            part = metadata["size_class"].eq(size).to_numpy()
            values = [
                recurrence_percent(relative[part], absolute[part], threshold, direction)
                for threshold in thresholds
            ]
            ax.plot(np.array(thresholds) * 100, values, marker="o", linewidth=1.5, label=size)
        ax.set_title(direction)
        ax.set_xlabel("Relative anomaly threshold (%)")
        ax.set_xticks([10, 15, 20])
        ax.grid(axis="y", color="#D9DEDF", linewidth=0.5)
    axes[0].set_ylabel("Recurrent cases among cases with ≥1 event (%)")
    axes[1].legend(title="Inventory size class", loc="best")
    fig.suptitle("Recurrence in the global case sample (2017–2025)")
    fig.tight_layout()
    save_figure(fig, "Fig3_global_recurrence.png")


if __name__ == "__main__":
    main()
