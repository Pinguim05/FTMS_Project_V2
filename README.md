# FTMS Project V2 - Porto Metro Passenger Forecasting

## Overview

This repository contains a time series forecasting project for monthly Porto Metro light rail passengers. The project was developed for the Forecasting Methods and Time Series curricular unit and compares smoothing, decomposition, SARIMA, and SARIMAX approaches before producing a final 2026 forecast.

The current version of the project is centered on:

- the analysis notebook: `src/FMTS.ipynb`
- the written report: `report.md`
- the LaTeX submission version: `latex-fep/report.tex`
- the generated figures, tables, diagnostics, and forecast files in `outputs/`

## Current Project Scope

The final workflow uses:

1. A modelling sample from January 2012 to December 2025.
2. A chronological split with:
   - training: 2012-01 to 2024-12
   - validation: 2025-01 to 2025-12
   - out-of-sample forecast: 2026-01 to 2026-12
3. Competing methods:
   - Seasonal Naive
   - Holt-Winters variants
   - STL decomposition plus trend forecasting
   - SARIMA
   - SARIMAX with a COVID intervention specification

The notebook first evaluates models on the observed 2025 holdout and only then produces the 2026 forecast.

## Main Deliverables

- `src/FMTS.ipynb`: main notebook with data preparation, modelling, diagnostics, evaluation, and forecasts
- `report.md`: standalone written report
- `latex-fep/report.tex`: LaTeX report source
- `latex-fep/report.pdf`: compiled PDF report
- `outputs/data/`: forecast and validation CSV files
- `outputs/tables/`: model comparison, decomposition, smoothing, and coefficient tables
- `outputs/figures/`: plots used in the report
- `outputs/diagnostics/`: residual diagnostics and Ljung-Box outputs

## Repository Structure

```text
FTMS_Project_V2/
|-- data/
|   `-- light_rail_passengers.xlsx
|-- docs/
|   `-- notes/
|-- latex-fep/
|   |-- report.tex
|   |-- report.pdf
|   |-- annex_errors_2025.tex
|   `-- annex_stl_full.tex
|-- outputs/
|   |-- data/
|   |-- diagnostics/
|   |-- figures/
|   |-- reports/
|   `-- tables/
|-- src/
|   |-- FMTS.ipynb
|   `-- FMTS copy.ipynb
|-- environment.yml
|-- professor-review.md
|-- report.md
`-- tourism_forecast2_M1_vs_M7.html
```

## Key Outputs

The repository currently includes the generated outputs used in the final report, including:

- `outputs/data/forecast_2025_validation.csv`
- `outputs/data/forecast_2026.csv`
- `outputs/data/forecast_2026_intervention.csv`
- `outputs/data/metrics_2025_validation.csv`
- `outputs/tables/errors_2025_selected_models.csv`
- `outputs/tables/sarima_shortlist_aic_bic.csv`
- `outputs/tables/sarima_best_coefficients.csv`
- `outputs/tables/stl_components_full_2012_2025.csv`
- `outputs/figures/validation_2025_plot.png`
- `outputs/figures/forecast_2026_plot.png`
- `outputs/diagnostics/residual_ljung_box.csv`

## Current Conclusion

In the current project version, the preferred forecasting model is the selected SARIMA specification evaluated on the 2025 holdout. The report and notebook compare that result against Holt-Winters, decomposition-based forecasting, and intervention-based SARIMAX before producing the 2026 forecast.

## How To Run

### Option 1: Open the notebook

```powershell
jupyter notebook src/FMTS.ipynb
```

Then run the notebook top to bottom.

### Option 2: Compile the report

Open `latex-fep/report.tex` in MiKTeX or TeXworks and compile with `pdfLaTeX` twice.

## Notes

- `src/FMTS.ipynb` is the active notebook.
- `src/FMTS copy.ipynb` is a backup copy and not the main deliverable.
- `docs/notes/` contains supporting project notes and process documents.
- The repository includes generated outputs because the report depends on them directly.
