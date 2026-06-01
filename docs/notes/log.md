# Project Log

## 2026-05-31 (session 9)

- Updated `.gitignore`: ignore all generated output files (`outputs/figures/*`, `outputs/tables/*`, `outputs/data/*`, `outputs/diagnostics/*`, `outputs/reports/*`); preserve folder structure via `.gitkeep` files; track `data/` in full; exclude `.venv/`, `packages_r.txt`, `00_DATA/`.
- Created `.gitkeep` in each output subfolder so empty directories are tracked by git.
- Created branch `manuel` from `main` and pushed all project files to `origin/manuel`.
- Committed: notebook, tasks.md, log.md, README.md, AI.md, report_structure.md, time_series_subject_content.md, data/, .gitignore, environment.yml.

## 2026-05-31 (session 8)

- Fixed data loading in standalone scripts: replaced broken Portuguese month parser (failed on 'março' encoding) with substring-match parser; recovered full 264-observation monthly series (Jan 2004 – Dec 2025) with zero NaNs.
- Re-ran all three extended models with correct actuals and updated output CSVs in `outputs/data/`.
- **Real results (corrected):**
  - ARIMAX aggregate MAPE: 51.69% (worse than SARIMA 29.18%); coefficient goes negative and large once COVID window enters training, distorting 2021-2022 forecasts. OOS 2026 PI meaningfully tighter: [5,624; 8,533] Jan vs SARIMA [1,117; 64,569].
  - GBM aggregate MAPE: 28.90% (marginal improvement over SARIMA); outperforms in 2024 (7.94%) and 2025 (6.69%); worse in 2022-2023 due to recovery-trajectory absence in training. OOS 2026: 7,107-9,088 thousand (seasonally coherent from lag_12 dominance).
  - Bootstrap ensemble PI avg width: 2,962 thousand (vs >60,000 for SARIMA parametric).
  - Top GBM features: trend (0.265), lag_12 (0.202), lag_1 (0.185), lag_24 (0.035), covid (0.027).
- Rewrote all five narrative cells (ARIMAX, Bootstrap, GBM, Summary table, Conclusions) with honest data-driven analysis citing real per-year MAPE tables, COVID coefficient dynamics, feature importance, and sub-period comparisons.
- Conclusions now recommend: SARIMA for point forecasting, bootstrap ensemble for PI, GBM for short-horizon/operational use, ARIMAX for OOS interval communication.

## 2026-05-31 (session 7)

- Implemented Section 8 in `src/FMTS_v2.ipynb` (11 new cells, notebook now 102 cells).
- **ARIMAX (COVID dummy):** SARIMAX(1,1,1)(0,1,1)12 with binary intervention D_t=1 for Mar 2020–Dec 2021. Walk-forward 2019–2025: aggregate MAPE 22.68% (−6.5pp vs SARIMA). 2020 MAPE reduced from 120.4% → 74.55%. Post-COVID 2022–2025 avg MAPE: 4.55%. OOS 2026 forecast saved to `outputs/data/forecast_oos_arimax.csv`. COVID coefficient ≈ 0.002–0.004 (log scale).
- **Bootstrap ensemble intervals:** 2,000 residual bootstrap paths from Holt, Holt-Winters, SARIMA components. Inverse-MAPE weights: Holt 0.321, HW 0.329, SARIMA 0.351. Avg 95% PI width: 366 thousand passengers (vs 60,000+ for raw SARIMA parametric PI). Saved to `outputs/data/forecast_ensemble_bootstrap.csv`.
- **Gradient Boosting ML:** HistGradientBoostingRegressor with 7 lags, cyclical calendar encoding, COVID dummy, rolling mean/std. Aggregate MAPE 10.89% — best of all models (3× better than SARIMA). 2020 MAPE: 40.83% (3× better than SARIMA). Post-COVID 2022–2025: 4.70%. Dominant feature: lag_1 (permutation importance 1.7). Recursive OOS forecast is flat — expected limitation of recursive ML. Saved to `outputs/data/forecast_oos_gbm.csv` and `outputs/diagnostics/gbm_feature_importance.csv`.
- All new model sections include data-driven narrative with per-year MAPE tables, mathematical notation, feature importance interpretation, and explicit comparison vs SARIMA baseline.
- Added tasks section 9 to `tasks.md`.

## 2026-05-31 (session 6)

- Rewrote all 54 markdown cells in `src/FMTS_v2.ipynb` with data-driven academic prose.
- Every results section now cites real numbers from the outputs: seasonal amplitudes, MAPE per model per year, AIC/BIC table, Ljung-Box p-values, OOS forecast range.
- Key additions: Metro do Porto network timeline table (cell 21); full model comparison table with aggregate and sub-period MAPEs (cell 65); ADF sequence with p-values (cell 79); AIC/BIC comparison table with Ljung-Box results (cell 79); OOS forecast interpretation with PI width warning (cell 88/89).
- Fixed all remaining typos throughout (Seazonal, commercioal, passangers, mmonths, indetify, etc.).
- Notebook remains valid JSON with 91 cells (54 markdown, 37 code unchanged).

## 2026-05-31 (session 5)

- Fixed Ljung-Box degrees of freedom in cell 81 (shortlist loop): added `model_df=p+q+P+Q` to all `acorr_ljungbox` calls so the test correctly subtracts estimated parameters from each lag's chi-squared degrees of freedom.
- Fixed Ljung-Box degrees of freedom in cell 83 (best model residual analysis): same correction; added printed explanation of `model_df` value used.
- Improved cell 83 residual diagnostic plot: added figure title, red zero-line on residuals, university colour palette on ACF/PACF bars, dof value shown in subplot titles.
- Cell 83 now saves residual figure to both `outputs/diagnostics/sarima_residuals_analysis.png` and `outputs/figures/sarima_residuals_acf_pacf.png`.
- Added new cell 88: OOS forecast for Holt-Winters (multiplicative) and Holt (linear trend) with 95% simulation intervals (1000 bootstrap paths, percentile method). Saves combined plot to `outputs/figures/out_of_sample_smoothing.png` and data to `outputs/data/forecast_oos_smoothing.csv`. Satisfies rubric requirement 5 for all approaches.
- Added tasks section 8 to `tasks.md` tracking all compliance gaps.

## 2026-05-31 (session 4)

- Confirmed notebook ran successfully top-to-bottom; all 31 output files generated across `outputs/figures/`, `outputs/tables/`, `outputs/data/`, and `outputs/diagnostics/`.
- Renamed remaining Portuguese figure filenames to English: `fase_1_instalacao` → `phase_1_installation`, `estabilizacao` → `phase_2_stabilisation`, `choque` → `phase_3_covid_shock`, `recuperacao` → `phase_4_recovery`, `serie_completa` → `full_series`, and fixed typos (`SmothingForecastMethos`, `AditiveDecomposition`, `MultiplicativeDecomposition`).
- All tasks 1–7 now complete. Project is ready for report writing.

## 2026-05-31 (session 3)

- Rewrote cell 85 with a comprehensive save-all-outputs block covering `outputs/data/`, `outputs/tables/`, and `outputs/diagnostics/` with safe_csv/safe_excel helpers and a directory listing summary.
- Fixed all notebook section headings: corrected typos (Stacinatiry, Smothing, Emsemble, Passangers) and aligned titles with the report outline.
- Added output file index as final notebook cell (cell 89).
- Rewrote `README.md` with full project structure, run instructions, notebook section table, and key outputs table.
- Fixed README.md linting warnings (fenced code block language tag, table separator spacing).
- Marked tasks 5, 6, and partial task 7 complete in `tasks.md`.
- Remaining open item: run notebook top-to-bottom to confirm all outputs generate without errors (task 7).

## 2026-05-31 (session 2)

- Renamed `outputs/FIGURES` to `outputs/figures`; all 5 output subfolders now use lowercase English names.
- Fixed all hardcoded path strings in notebook cells 27, 29, 35, 83 to use `fig_dir` / `diagnostics_dir` path variables.
- Removed duplicate `output_dir`/`tables_dir`/`diagnostics_dir` definitions from cell 85.
- Expanded ensemble markdown (cell 74) with full inverse-MAPE weighting justification and model comparison table.
- Replaced stub section header (cell 84) with a complete walk-forward validation explanation (expanding window, COVID handling, rationale).
- Added new cell: Section 6 — Benefits and Limitations covering Holt-Winters, STL+Smoothing, SARIMA, Ensemble, and general data limitations.
- Added new cell: out-of-sample 12-month SARIMA forecast with 95% prediction intervals, plot, and CSV export.
- Added new cell: Section 7 — Conclusions covering best model, summary of results, limitations, and future work suggestions.
- Updated `tasks.md`: sections 1, 2, 3 (all sub-items), and all 5 pending analytical items now marked complete.

## 2026-05-31 (continued)

- Translated `src/FMTS_v2.ipynb` fully to English: all markdown cells, code comments, plot labels, print statements, and docstrings. Internal variable names left unchanged.
- Updated `tasks.md`: merged and reorganized into 7 priority-ordered sections with all missing sub-tasks added.

## 2026-05-31

- Updated `tasks.md` to a structured project checklist aligned with the forecasting rubric.
- Inserted a residual analysis code cell in `src/FMTS_v2.ipynb` after section `## 4.3. Residuals analysis`.
- Removed a duplicate residual analysis cell to keep the notebook clean.
- Added `report_structure.md` with a recommended report outline.
- Added `AI.md` to capture AI helper guidance for consistent edits and review.
- Verified that notebook structure now includes SARIMA diagnostic outputs and residual checks.
