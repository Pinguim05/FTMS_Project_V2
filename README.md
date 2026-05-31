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
- **Period:** January 2003 – 2025 (monthly)
- **Key features:** strong upward trend (network expansion 2003–2011), stable seasonal pattern, COVID-19 structural break (2020–2021)

## Project Structure

```text
FTMS_Project_V2/
├── data/
│   └── light_rail_passengers.xlsx       # Raw input data
├── src/
│   └── FMTS_v2.ipynb                    # Main analysis notebook (90 cells)
├── outputs/
│   ├── figures/                         # All plots (PNG, 300 DPI)
│   ├── tables/                          # Metrics, decomposition matrices, diagnostics (CSV + Excel)
│   ├── data/                            # Forecast tables and prediction intervals (CSV)
│   ├── diagnostics/                     # SARIMA residual plots and diagnostic tables
│   └── reports/                         # Final report (to be added)
├── tasks.md                             # Project task checklist (priority ordered)
├── report_structure.md                  # Recommended report outline
├── log.md                               # Changelog
└── AI.md                                # AI assistant guidelines
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

## Notebook Structure

| Section | Content |
| --- | --- |
| Setup and Data Loading | Imports, path definitions, helper functions |
| 1. Features of the Time Series | Raw time series plot, data description |
| 2. Exploratory Data Analysis | Resampling, ACF/PACF, structural break discussion |
| 3.1. Decomposition | Additive, multiplicative, and STL (LOESS) decomposition |
| 3.2. Smoothing Methods | Moving averages, SES, Holt, Holt-Winters |
| 3.2B. SARIMA Identification | ACF/PACF on differenced series, model shortlist |
| Walk-Forward Forecast Loop | Expanding-window forecasts 2019-2021, all models |
| Ensemble Forecast | Inverse-MAPE weighted ensemble |
| Downweighting Strategy | COVID-period observation downweighting |
| 4. SARIMA | Stationarity analysis, model selection, AIC/BIC, diagnostics |
| 5. Walk-Forward Validation | Methodology explanation, per-year metrics table |
| Save All Outputs | Comprehensive export of all tables, plots, and CSVs |
| 6. Benefits and Limitations | Per-model analysis and general data constraints |
| Out-of-Sample Forecast | 12-month SARIMA forecast with 95% prediction intervals |
| 7. Conclusions | Best model, summary, limitations, future work |
| Output File Index | Complete index of all generated files |

## Key Outputs

| File | Description |
| --- | --- |
| `outputs/figures/out_of_sample_forecast.png` | 12-month out-of-sample forecast |
| `outputs/data/forecast_out_of_sample.csv` | Point forecast + 95% PI |
| `outputs/data/metrics_walkforward.csv` | Per-year test-set metrics, all models |
| `outputs/tables/metrics_sarima_aic_bic.csv` | SARIMA AIC/BIC shortlist |
| `outputs/diagnostics/sarima_diagnostics.csv` | Ljung-Box and residual diagnostics |
