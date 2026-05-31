# Report Structure

This document provides a recommended structure for the FTMS forecasting report.

## 1. Introduction
- Problem statement and objective.
- Description of the data source and time series.
- Forecast horizon and evaluation framework.

## 2. Data and Preprocessing
- Data import steps and cleaning strategy.
- Handling missing values and zero / COVID interruption periods.
- Resampling or aggregation decisions.

## 3. Exploratory Data Analysis
- Time series plots and seasonality discussion.
- Trend analysis and COVID interruption effects.
- Summary statistics and any notable structural changes.

## 4. Smoothing and Decomposition Methods
- Smoothing methods applied: moving average, SES, Holt, Holt-Winters.
- STL decomposition results and trend / seasonal / residual components.
- Seasonally adjusted series and interpretation.

## 5. SARIMA Model Development
- Transformation and differencing strategy.
- SARIMA shortlist: candidate orders, AIC/BIC ranking.
- Diagnostic checks: ACF/PACF, Ljung-Box, residual analysis.
- Final model selection rationale.

## 6. Forecast Evaluation and Comparison
- Test-set results and error metrics.
- Comparison across smoothing, decomposition, and SARIMA forecasts.
- 95% prediction intervals and uncertainty assessment.
- Ensemble or combined forecast approach if available.

## 7. Conclusions and Limitations
- Best-performing forecasting approach.
- Practical interpretation of results.
- Limitations of the model(s) and data.
- Suggestions for future work.

## 8. Appendix
- Additional tables, figures, and saved output references.
- Excel sheets, plots, and detailed diagnostics.
