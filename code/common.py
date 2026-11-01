from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"
ANNUAL_YEARS = np.arange(2017, 2026)
ANNUAL_COLUMNS = [f"annual_mean_area_{year}" for year in ANNUAL_YEARS]
MIN_ABSOLUTE_ANOMALY_KM2 = 0.0001  # one nominal 10-m pixel
SIZE_ORDER = ["Tiny", "Small", "Medium", "Large"]
TRAJECTORY_ORDER = [
    "Stable",
    "Recurrent/reversible",
    "Persistent gain",
    "Persistent loss",
    "Loss-recovery",
    "Gain-reversal",
]
TRAJECTORY_COLORS = {
    "Stable": "#7A8588",
    "Recurrent/reversible": "#3E7CB1",
    "Persistent gain": "#B64E3B",
    "Persistent loss": "#375A7F",
    "Loss-recovery": "#D58A35",
    "Gain-reversal": "#7A6AA6",
}


def load_case_tables():
    metadata = pd.read_csv(DATA_DIR / "cases_metadata.csv")
    monthly = pd.read_csv(DATA_DIR / "cases_monthly_area_km2.csv")
    months = [
        column for column in monthly.columns
        if len(column) == 7 and column[:4].isdigit() and column[4] == "_"
    ]
    monthly = monthly.set_index("case_id").loc[metadata["case_id"]].copy().reset_index()
    return metadata, monthly, months


def annual_matrix(metadata):
    return metadata[ANNUAL_COLUMNS].to_numpy(dtype=float)


def annual_anomalies(metadata):
    areas = annual_matrix(metadata)
    baseline = metadata["long_term_mean_area_km2"].to_numpy(dtype=float)
    absolute = areas - baseline[:, None]
    relative = absolute / baseline[:, None]
    return areas, baseline, absolute, relative


def event_flags(metadata, threshold=0.10):
    _, _, absolute, relative = annual_anomalies(metadata)
    detectable = np.abs(absolute) >= MIN_ABSOLUTE_ANOMALY_KM2
    expansion = (relative >= threshold) & detectable
    contraction = (relative <= -threshold) & detectable
    return expansion, contraction


def monthly_matrix(metadata, monthly, month_columns):
    ordered = monthly.set_index("case_id").loc[metadata["case_id"], month_columns]
    return ordered.to_numpy(dtype=float, copy=True)


def set_plot_style():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "legend.frameon": False,
        "savefig.dpi": 300,
    })


def save_figure(fig, filename):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close(fig)
