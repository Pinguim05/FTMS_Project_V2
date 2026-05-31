# FTMS Project V2 — Light Rail Passenger Forecasting

## Assignment Brief

Produce forecasts for a time series using smoothing, decomposition, and statistical models. Write a report explaining the analysis, covering:

1. Features of the time series.
2. Smoothing and decomposition methods (estimation results, trend/seasonal/error components, seasonally adjusted data).
3. SARIMA model development (transformations, differencing, shortlist methodology, ACF/PACF, Ljung-Box, AIC/BIC).
4. Forecast comparison across methods with test-set metrics and 95% prediction intervals.
5. Out-of-sample point forecasts and 95% prediction intervals.
6. Benefits and limitations of the models.

> Note: Unit root tests (ADF, PP, KPSS) are not appropriate for seasonal data.
> Apply the Ljung-Box test with the correct degrees of freedom.

## Dataset

- **Source:** Metro do Porto — monthly passenger counts (thousands)
- **File:** `data/light_rail_passengers.xlsx`
- **Period:** January 2004 – December 2025 (264 monthly observations)
- **Key features:** strong upward trend (network expansion 2003–2011), stable annual seasonal cycle (peak: September/April; trough: July), COVID-19 structural break (March 2020 – December 2021)

## Authors

- Manuel Sampaio

## Project Structure

```text
FTMS_Project_V2/
├── data/
│   └── light_rail_passengers.xlsx       # Raw input data (tracked in full)
├── src/
│   └── FMTS_v2.ipynb                    # Main analysis notebook (102 cells)
├── outputs/                             # Generated files (gitignored — run notebook to populate)
│   ├── figures/                         # All plots (PNG, 300 DPI)
│   ├── tables/                          # Metrics, decomposition matrices (CSV + Excel)
│   ├── data/                            # Forecast tables and prediction intervals (CSV)
│   ├── diagnostics/                     # SARIMA residual plots and Ljung-Box results
│   └── reports/                         # Final report (to be added)
├── tasks.md                             # Project task checklist (priority ordered)
├── report_structure.md                  # Recommended report outline
├── log.md                               # Full session changelog
├── AI.md                                # AI assistant guidelines
└── environment.yml                      # Conda environment specification
```

## How to Run

```bash
# 1. Activate the virtual environment
.venv\Scripts\activate          # Windows PowerShell
# source .venv/bin/activate     # macOS/Linux

# 2. Launch Jupyter
jupyter notebook src/FMTS_v2.ipynb

# 3. Run all cells top to bottom (Kernel → Restart & Run All)
```

All outputs are saved automatically to `outputs/` during the notebook run.
Output files are gitignored — only folder structure (`.gitkeep`) is tracked.

## Notebook Structure (102 cells)

| Section | Content |
| --- | --- |
| Setup and Data Loading | Imports, path definitions, helper functions, data load |
| 1. Features of the Time Series | Raw time series plot, structural phases, data description |
| 2. Exploratory Data Analysis | Resampling, ACF/PACF of raw series, COVID break |
| 3.1. Decomposition | Additive, multiplicative, STL-LOESS across 4 phases |
| 3.2. Smoothing Methods | Moving averages (MA, 2×12, 2×4, 3×3), SES, Holt, Holt-Winters |
| 3.2B. SARIMA Identification | Log transform, differencing, ACF/PACF, shortlist |
| Walk-Forward Forecast Loop | Expanding-window forecasts 2019–2021, all models |
| Ensemble Forecast | Inverse-MAPE weighted combination with justification |
| COVID Downweighting | Hyndman (2020) downweighting strategy |
| 4. SARIMA | AIC/BIC shortlist, Ljung-Box (corrected df), residual diagnostics |
| 5. Walk-Forward Validation | Methodology, per-year metrics table (2019–2025) |
| Save All Outputs | Comprehensive export cell |
| 6. Benefits and Limitations | Per-model analysis, data limitations |
| OOS Forecast (SARIMA) | 12-month forecast + 95% PI |
| OOS Forecast (Smoothing) | Holt-Winters + Holt with simulation intervals |
| 7. Extended Models | ARIMAX, Bootstrap ensemble PI, Gradient Boosting ML |
| 8. Conclusions | Best model, real MAPE numbers, limitations, future work |
| Output File Index | Complete reference table of all generated files |

## Key Results

| Model | Aggregate MAPE (2019–2025) | 2022–2025 avg MAPE |
| --- | --- | --- |
| SARIMA(0,1,1)(0,1,1)₁₂ | 29.18% | 8.90% |
| Ensemble (inverse-MAPE) | 29.31% | 10.67% |
| Gradient Boosting (ML) | 28.90% | 13.10% |
| Holt-Winters | 31.16% | 13.41% |
| ARIMAX (COVID dummy) | 51.69% | 28.84% |

All models fail in 2020 (MAPE > 110%) due to the COVID structural break.

## Key Output Files

| File | Description |
| --- | --- |
| `outputs/figures/out_of_sample_forecast.png` | 12-month SARIMA OOS forecast + 95% PI |
| `outputs/figures/extended_models_comparison.png` | ARIMAX, GBM, ensemble OOS comparison |
| `outputs/data/forecast_out_of_sample.csv` | SARIMA point forecast + 95% PI |
| `outputs/data/forecast_oos_arimax.csv` | ARIMAX OOS forecast + 95% PI |
| `outputs/data/forecast_oos_gbm.csv` | Gradient boosting recursive OOS forecast |
| `outputs/data/forecast_ensemble_bootstrap.csv` | Ensemble + bootstrap 95% PI |
| `outputs/data/metrics_walkforward.csv` | Per-year walk-forward metrics, all models |
| `outputs/tables/metrics_sarima_aic_bic.csv` | SARIMA AIC/BIC shortlist |
| `outputs/diagnostics/sarima_diagnostics.csv` | Ljung-Box and residual diagnostics |
| `outputs/diagnostics/gbm_feature_importance.csv` | GBM permutation feature importance |
