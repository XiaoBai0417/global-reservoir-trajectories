# Global reservoir case bundle

This lightweight bundle contains 100 high-quality reservoir cases from six inhabited continents, their point locations, monthly area data and five short Python examples corresponding to Figs. 1–5.

The examples demonstrate the analysis steps on a small sample. They do not reproduce the manuscript's global statistics or replace the full figure-generation pipeline.

## Files

- data/cases_metadata.csv: locations, continent, inventory size class, trajectory label and annual mean areas.
- data/cases_monthly_area_km2.csv: monthly reservoir surface-water area from January 2017 to May 2026, in km².
- data/case_reservoir_points.geojson: WGS 84 point layer for the 100 cases.
- code/common.py: shared data loading and event definitions.
- code/fig1_global_cases.py through code/fig5_global_trajectories.py: one concise case example per main figure.
- code/source_methods/: four additional supplied methods/example files.

## Sample selection

The candidate pool required complete annual means for 2017–2025, at least 60 valid monthly observations, valid coordinates and a positive 2017–2019 baseline. For the trajectory examples, cases also required a classified trajectory with high confidence (≥0.80). This yielded 207,361 eligible cases across Africa, Asia, Europe, North America, Oceania and South America.

The 100 cases were selected deterministically (seed 20261101) and stratified across the six continents (16–17 cases each), size classes and available trajectory classes. Size-class counts are 30 Tiny, 30 Small, 25 Medium and 15 Large. This is an illustrative, purposive sample, not a probability sample.

Size classes follow the inventory polygon-area field used by the analysis code: Tiny (<0.1 km²), Small (0.1 to <10 km²), Medium (10 to <100 km²) and Large (≥100 km²). This is inventory polygon area, not Sentinel-1 mean surface-water area.

## Data columns

In cases_metadata.csv, case_id is the sample label and source_id is the inventory record identifier. Coordinates are WGS 84 degrees. inventory_polygon_area_km2 is the inventory polygon area; long_term_mean_area_km2 is the 2017–2025 monthly-area baseline; annual_mean_area_2017 through annual_mean_area_2025 are annual mean surface-water areas. trajectory_class and trajectory_confidence are the supplied classification outputs.

In cases_monthly_area_km2.csv, case_id links to the metadata file and each YYYY_MM column is monthly surface-water area in km². Empty cells indicate missing values; zero values are retained. The GeoJSON contains one Point feature per case and includes case ID, source ID, country, continent, size class and trajectory fields.

## Example scripts

- Fig. 1: latest qualifying expansion and contraction years at the global case locations.
- Fig. 2: annual expansion and contraction totals and endpoint net change for the sample.
- Fig. 3: recurrent-event proportions by size class and anomaly threshold.
- Fig. 4: monthly coefficient of variation and median absolute month-to-month change by size class.
- Fig. 5: deseasonalized monthly trajectories summarized by the supplied trajectory classes.

## Run

Install the dependencies:

    python -m pip install -r requirements.txt

Run a script from this directory, for example:

    python code/fig1_global_cases.py

Each script saves one PNG in outputs/. Fig. 1–3 use complete years through 2025; Fig. 4 uses monthly data through May 2026; Fig. 5 uses complete years through 2025.

The files in code/source_methods/ are supplementary examples and are not imported by the five case scripts. Their optional Python dependencies are listed in code/source_methods/requirements-source-methods.txt. The Earth Engine scripts require access to the referenced reservoir asset; the POI script requires an AMap API key.
