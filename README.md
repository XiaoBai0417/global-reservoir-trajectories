# Global reservoir trajectories

Code and supporting data for reproducing reservoir surface-water-area analyses based on Sentinel-1 observations.

## Contents

- `data/` — reservoir locations and area records used by the included analyses.
- `code/` — analysis scripts for Figs. 1–5 and supplementary methods code.
- `outputs/` — generated figure files.

## Reproduce

From the repository root, install the required packages and run the figure scripts:

```bash
python -m pip install -r requirements.txt
python code/fig1_global_cases.py
python code/fig2_global_balance.py
python code/fig3_global_recurrence.py
python code/fig4_global_size.py
python code/fig5_global_trajectories.py
```

The scripts regenerate the analyses from the data provided in this repository. Reproducing the manuscript’s full global estimates requires the complete input data and processing workflow, which are not included here.

## Data and code

Area records are derived from Sentinel-1 observations; reservoir locations and attributes come from a harmonized inventory. Supplementary source files and their requirements are documented in `code/source_methods/`. Check source terms and permissions before reuse; no license is assigned here to third-party files.
