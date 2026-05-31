# Project Tasks

Tasks are ordered by priority. Complete them top to bottom for a clean final delivery.

---

## 1. Fix folder and file naming

- [x] Rename `00_DATA` to `data` and `01_OUTPUTS` to `outputs`.
- [x] Rename `data/passageiros_transportados_ferroviario_ligeiro.xlsx` to `data/light_rail_passengers.xlsx`.
- [x] Rename any remaining Portuguese folder or file names to English (`outputs/FIGURES` → `outputs/figures`).
- [x] Standardize output subfolders: `outputs/figures`, `outputs/tables`, `outputs/data`, `outputs/reports`, `outputs/diagnostics`.

---

## 2. Centralize notebook paths and export logic

- [x] Add a dedicated cell near the top of the notebook that defines all base paths and output file names.
- [x] Use relative paths consistently throughout (`../data`, `../outputs/figures`, etc.).
- [x] Replace every scattered `savefig` / `to_excel` / `to_csv` call with a named path variable defined in the central cell.
- [x] Define one canonical name per saved file (forecast tables, metrics, diagnostic plots, STL components).

---

## 3. Convert the notebook to English

- [x] Replace all Portuguese markdown narrative cells with English explanations.
- [x] Translate Portuguese code comments to English.
- [x] Rename Portuguese variable names that appear in output or reports (e.g. `serie_limpa`, `treino`, `teste_real` can stay internal, but labels in plots and saved files must be English).
- [x] Ensure all plot titles, axis labels, legend entries, and table column headers are English-only.
- [x] Ensure all saved file names are English-only.

---

## 4. Complete missing analytical content

These are the items required by the assignment rubric that are not yet fully done.

- [x] Data source, description, and series features discussion.
- [x] Exploratory analysis: trend, seasonality, and COVID interruption visualization.
- [x] Data cleaning, resampling, and COVID downweighting implemented.
- [x] Smoothing methods: moving averages, SES, Holt, Holt-Winters.
- [x] STL decomposition, component display, and seasonal adjustment.
- [x] SARIMA shortlist methodology with AIC/BIC comparison.
- [x] SARIMA diagnostics: ACF/PACF graphs, Ljung-Box test, residual checks.
- [x] Forecast comparison with test-set metrics (ME, MAE, MSE, MAPE, RMSE).
- [x] 95% prediction intervals generated for SARIMA.
- [x] **Ensemble model:** add a markdown cell that justifies the ensemble weights (e.g. inverse-MAPE weighting), show the combined forecast vs actuals, and report ensemble metrics on the test set.
- [x] **Walk-forward validation:** add a clear markdown section explaining the expanding-window loop already in the code; include a summary table of per-year forecast errors across all models.
- [x] **Benefits and limitations:** add a dedicated markdown cell discussing what each model does well and where it fails (COVID distortion, data length, parameter stability, forecast horizon).
- [x] **Out-of-sample forecast:** generate and save point forecasts and 95% prediction intervals for at least 12 months beyond the last observed date for the best model.
- [x] **Conclusions:** add a final notebook section that names the best model, summarises test-set performance, and states the main limitations.

---

## 5. Save all required outputs

- [x] Identify every table and figure referenced in the report structure.
- [x] Save all model metrics to `outputs/tables/metrics_summary.csv`.
- [x] Save all forecast tables (smoothing, SARIMA, ensemble, walk-forward) to individual CSVs in `outputs/data/`.
- [x] Save STL component plots and seasonally adjusted series to `outputs/figures/`.
- [x] Save SARIMA diagnostic plots (residuals, ACF/PACF of residuals, Ljung-Box results) to `outputs/diagnostics/`.
- [x] Save the final out-of-sample forecast with prediction intervals to `outputs/data/forecast_out_of_sample.csv`.
- [x] Save the ensemble forecast table to `outputs/data/forecast_ensemble.csv`.

---

## 6. Clean and organize notebook structure

- [x] Align notebook section headings with the report outline (Introduction, EDA, Smoothing & Decomposition, SARIMA, Forecast Evaluation, Conclusions).
- [x] Remove duplicate cells and any leftover exploratory/testing code.
- [x] Remove broken or commented-out export calls.
- [x] Add a final summary cell that lists all saved output files and their locations.

---

## 7. Validate the full project

- [x] Run the notebook from top to bottom without errors.
- [x] Confirm all expected files exist in `outputs/` after a clean run.
- [x] Verify all paths resolve correctly after any renaming.
- [x] Update `README.md` to document the final project layout, how to run the notebook, and what outputs are generated.
- [x] Update `report_structure.md` if the report outline changed.
- [x] Add a log entry to `log.md` summarising all changes made.

---

## 8. Fix compliance gaps (assignment rubric)

- [x] **Ljung-Box degrees of freedom:** add `model_df=p+q+P+Q` to both `acorr_ljungbox` calls (cells 81 and 83) so the test uses the correct degrees of freedom as required by the professor.
- [x] **Residual ACF/PACF plot saved:** save the residual diagnostic figure (cell 83) to `outputs/figures/sarima_residuals_acf_pacf.png`.
- [x] **Out-of-sample intervals for smoothing methods:** added OOS Holt-Winters and Holt (linear) forecasts with 95% simulation intervals (1000 paths, percentile method); saved to `outputs/data/forecast_oos_smoothing.csv` and `outputs/figures/out_of_sample_smoothing.png`.
- [ ] **Data source citation:** add a formal citation cell with the Metro do Porto data source name, URL, and access date. *(user will handle)*
- [ ] **Declaration of Authenticity:** add to the notebook or report. *(user will handle)*

---

## 9. Extended models (Section 8)

- [x] **ARIMAX with COVID dummy:** aggregate MAPE 51.69% (worse than SARIMA due to coefficient distortion in 2021–2022); OOS 2026 PI tighter: [5,624; 8,533] Jan vs SARIMA [1,117; 64,569].
- [x] **Bootstrap prediction intervals for ensemble:** 2,000 paths; avg 95% PI width 2,962 thousand (vs >60,000 SARIMA parametric). Saved to `outputs/data/forecast_ensemble_bootstrap.csv`.
- [x] **Gradient Boosting ML model:** aggregate MAPE 28.90% (marginal improvement vs SARIMA 29.18%); best in 2024–2025 (7.94%, 6.69%). Top features: trend, lag_12, lag_1.
- [x] **Conclusions rewritten from real output data:** per-year MAPE tables, COVID coefficient dynamics, feature importance, honest sub-period comparison vs SARIMA baseline.

---

## 10. Git and version control

- [x] Updated `.gitignore`: ignore all output files, keep folder structure via `.gitkeep`; track `data/` in full; exclude `.venv/`, `packages_r.txt`, `00_DATA/`.
- [x] Created branch `manuel` and pushed to `origin`.
- [x] `tasks.md`, `log.md`, `AI.md`, `report_structure.md`, `time_series_subject_content.md` all tracked and pushed.
