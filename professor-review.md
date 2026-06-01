This is a substantial evaluation. Let me work through it systematically against the full rubric.

---

# Professor Evaluation — Light Rail Passenger Forecasting (Porto Metro)

---

## 1. Assignment Compliance — 15/20

**Requirements fully satisfied:**
- Real time series from a named source (Statistics Portugal / Metro do Porto) ✅
- Monthly frequency, explicitly stated ✅
- Target variable defined (thousands of passengers) ✅
- Period covered: 2004–2025 ✅
- Forecast horizon stated: 12 months, 2026 ✅
- Report appears within 12-page limit ✅
- Smoothing methods present ✅
- Decomposition present ✅
- ARIMA/SARIMA present ✅
- Test-set comparison in Table 5 ✅
- Out-of-sample forecasts in Table 6 and Figure 7 ✅
- Seasonal Naive benchmark included ✅

**Requirements only partially satisfied:**
- 95% prediction intervals: shown for SARIMA in Figure 6 and for HW\_Add in Table 6/Figure 7, but HW prediction intervals are **absent from the test-set comparison figure**. A reader cannot assess whether HW intervals had reasonable empirical coverage over 2025.
- Benefits and limitations: Section 9 exists but is four short paragraphs — barely one sentence per method.
- Technical details in appendices: STL tables correctly moved, but residual diagnostic plots (which do not appear anywhere) should be in an annex.
- Data source: described as "workbook metadata indicates extraction from Statistics Portugal" — this is a provenance chain, not a direct citation. The exact table or series code from INE is not given.

**Missing entirely:**
- No AICc reported anywhere (only AIC and BIC). For sample sizes common in model identification, AICc is the standard.
- No damped-trend Holt-Winters considered or discussed.


---

## 2. Dataset Suitability and Data Preparation — 16/20

**Strengths:** n = 264 is very comfortable for monthly seasonal modelling (22 full cycles of s = 12). The chronological split is clean, the test year 2025 corresponds to one full seasonal cycle, and no data leakage is described. Duplicate timestamps checked and zero.

**Issues:**

- **Missing values repaired but not quantified.** The report says "repair zero/missing values using time interpolation and boundary fills" yet Table 1 reports zero missing after preprocessing. How many observations were repaired? Interpolated values are not the same as observed values, and their number and location matter — particularly because some COVID months had near-zero ridership that may have been flagged as erroneous. This needs explicit disclosure.

- **Minimum value = 548.** This is an extreme outlier (more than 2.5 standard deviations below the mean). Its location is not stated in the data preparation section — it presumably falls inside the COVID window. Whether this reflects a genuine observation or a partially repaired value is not confirmed.

- **COVID disruption (22 months) affects ~9% of the training data.** This is not a data preparation flaw per se, but the report should state explicitly that models are fitted on data containing a structural regime break, and that standard stationarity assumptions are at best approximate over the full training window.

- **Transformation applies only before SARIMA.** The log transformation is used for SARIMA estimation but not for Holt-Winters. The report does not explain why the same variance argument does not apply to the smoothing models, or whether HW forecast intervals account for back-transformation.

**Score reduction:** Minor, mostly disclosure.

---

## 3. Time Series Description — 13/20

**Strengths:** Figure 1 (time plot with COVID highlight) is appropriate and informative. Figure 2 (seasonal profile with mean/median) is a good addition. ACF/PACF in Figure 3 are shown and briefly interpreted. The structural break is identified and quantified with actual numbers (3179 vs 5570).

**Weak or missing observations:**

- **Changing variance not discussed in EDA.** The report justifies a log transformation in Section 6.1 because "the raw series shows larger absolute variation at higher levels" — but this observation is never made in Section 3. The EDA section should have noted this and flagged it as a modelling implication.

- **Seasonal component not interpreted in real-world terms.** Figure 2 shows a clear dip in August and a peak in October–November. These patterns have obvious explanations (summer holiday travel reductions, return to regular commuting patterns) that are never mentioned. A good report connects data features to domain knowledge.

- **Post-COVID recovery trajectory not discussed.** The trend after December 2021 shows a steep recovery. The report doesn't ask whether recovery has plateaued or is still rising — a question directly relevant to whether a flat β=0 forecast for 2026 is defensible.

- **No discussion of cycles.** Beyond the trend, the ACF plot in Figure 3 shows very slow decay consistent with a near-unit-root process. This is noted as "autocorrelation persists across multiple lags" but not connected to what it implies for differencing order.

- **No discussion of whether seasonality changed after COVID.** If the seasonal structure shifted post-2021, additive fixed-seasonal models may produce biased forecasts. This should at minimum be noted.

**Suggested observation to add:** After the COVID disruption, the seasonal amplitude appears broadly preserved but the level of the trend has shifted upward relative to pre-COVID. The August trough (Figure 2 median ~3500) likely reflects reduced commuter demand during summer, consistent with public transport patterns. The post-2021 recovery has been steep but the rate has moderated in 2023–2024, which may limit how much trend extrapolation is appropriate for 2026.

---

## 4. Train/Test Split and Evaluation Design — 16/20

**Strengths:** The split is correctly chronological (no random splitting), clearly documented in Table 2, and the reasoning is explicitly stated. All four methods are evaluated on the same 2025 holdout. ME is included (useful for detecting systematic bias). Seasonal Naive is a correct and appropriate benchmark.

**Issues:**

- **No MASE reported.** MASE is scale-free and directly interpretable relative to the naive benchmark. MAPE is sensitive to small actual values. Both should be included. This is a minor but standard omission.

- **No empirical coverage reported.** With 12 actual observations in 2025, it is straightforward to check how many fell inside the 95% SARIMA intervals. This number appears nowhere in the report. Empirical coverage reporting is standard practice.

- **No time-series cross-validation.** A single 12-month test set is acceptable at this level, but the report never acknowledges that performance estimates from one holdout year are noisy. A brief note acknowledging this limitation would strengthen the evaluation design section.

---

## 5. Smoothing Methods — 12/20

**Methods used:** Holt-Winters additive and multiplicative. Seasonal Naive used as benchmark.

**Missing methods:** Damped-trend Holt-Winters was not considered or mentioned. Given that the post-COVID recovery trend in the data has visibly flattened, a damped trend would be a natural candidate. Its omission is a real methodological gap.

**Critical problems with the estimated parameters:**

Table 3 reports:

| Method | α | β | γ |
|---|---|---|---|
| HW\_Add | 0.9141 | 0.0000 | 0.0000 |
| HW\_Mul | 1.0000 | 0.0000 | 0.0000 |

1. **β = 0 for both models.** This means the trend component is set at initialisation and **never updated** throughout the training period. For a 21-year series with a regime break and a steep post-COVID recovery, a frozen trend is not a defensible modelling choice. The report says "near-zero β... consistent with the visible persistence of the monthly seasonal profile" — this is circular reasoning. β governs trend adaptation, not seasonal persistence. The correct interpretation is that the optimiser hit the lower bound, which may signal over-specification or that a simpler model fits better.

2. **γ = 0 for both models.** This means the seasonal component is **never updated** from its initialised state. For a 22-year series, this implies the seasonal factors estimated from 2004 are applied unchanged in 2024. This is a very strong assumption that the report does not examine or justify.

3. **α = 1.0 for HW\_Mul.** An alpha of exactly 1.0 is a boundary solution. It means the level estimate is always the most recent observation, with zero memory. This is essentially a random-walk level model. Combined with β = 0 and γ = 0, HW\_Mul is operating as a very simple model despite its apparent complexity. The report does not discuss this at all.

**Why this matters statistically:** Boundary parameter solutions often indicate that the model is misspecified or that the series has features the model cannot accommodate. If the optimiser repeatedly hits bounds, the model's prediction intervals — which depend on the parameter estimates — will not be reliable. The report treats these numbers as if they are informative parameter estimates and interprets them without noting the boundary problem.

**What is missing:**
- Residual plots for HW methods — not shown anywhere
- Fitted-value overlay on training data — not shown
- HW prediction intervals in the test-set comparison (Figure 6 shows only SARIMA intervals)
- Discussion of why boundary solutions occurred
- Consideration of damped trend

---

## 6. Decomposition Methods — 11/20

**Appropriate choice:** STL with additive framework is a defensible choice and the justification — that seasonal effects do not scale strictly proportionally across the full sample including the COVID disruption — is reasonable.

**What is done well:** Figure 4 shows all four STL components. Tables 7 and 8 provide component values. The remainder contains the largest spikes in the COVID window, which is correct.

**Critical weakness: no decomposition-based forecasts are produced.** The assignment explicitly requires that decomposition be used as a forecasting approach. The report uses STL purely for exploratory analysis and then states "decomposition alone is not always a full forecasting model." This is true, but it does not discharge the requirement. A standard approach is STL decomposition followed by ETS or ARIMA on the seasonally adjusted series, or Holt-Winters applied within an STL framework. The absence of any decomposition forecast means this section is diagnostic analysis only, not a forecasting method.

**Additional weaknesses:**

- STL window parameters (s.window, t.window, robust flag) are not reported. If robust=True was used to down-weight the COVID observations, that is important to state — it would mean the seasonal and trend estimates are not representative of the full training sample.

- The seasonal component in Table 7 ranges from −1208 to +983. These magnitudes are substantial and the report does not interpret a single one. Which month drives the negative peak? Which the positive? What does that mean for ridership?

- The remainder standard deviation (473.59) is almost as large as the seasonal standard deviation (440.54). This deserves comment. It suggests the irregular component is as variable as the seasonal one, which raises questions about the predictability of the series.

- No decomposition forecast means there is no comparison of decomposition-based accuracy against the other methods.

---

## 7. Transformation and Differencing — 13/20

**Correct decisions:** Log transformation is justified on the right grounds (scale-dependent variance). The choice d = 1, D = 1, s = 12 is standard and the rationale is briefly stated. Figure 5 shows ACF/PACF of the transformed differenced series, and the patterns are broadly consistent with a SARIMA structure.

**Missing or unresolved:**

- **Back-transformation not explicitly confirmed.** The report says SARIMA is fitted on log-transformed data but never states that forecasts are exponentiated back to the original scale before computing test-set errors. If errors in Table 5 were computed on the log scale, the MAPE comparisons across methods are not on the same basis. This is a potential validity issue that requires a one-sentence clarification.

- **Over-differencing not checked.** With d = 1 and D = 1, the combined differencing order is high. The report does not show the sample mean and variance of the differenced series, nor ACF at low lags, to confirm that the series is not over-differenced (which would appear as a unit root in the MA component of the ACF).

- **No formal unit root discussion.** This is actually acceptable given the known problems with ADF/KPSS on seasonal data, but the report should briefly state *why* formal tests were not used (or not relied upon), namely that ADF and KPSS are not designed for seasonal series unless seasonal structure is removed first.

---

## 8. ARIMA/SARIMA Model Identification — 11/20

**The shortlist is methodologically narrow.**

All three candidates share the same seasonal structure (0, 1, 1, 12). Not a single candidate with seasonal autoregressive components (P > 0) was tested. Looking at Figure 5, the ACF of the differenced log series shows a significant spike at lag 12. This is consistent with seasonal MA(1), yes — but it is also consistent with SARIMA(0,1,0)(1,1,0,12) or mixed seasonal structures. The identification of the seasonal component is not discussed in the text: why P = 0 for all candidates? The report provides no argument.

**Problems with identification:**

- The rationale for the non-seasonal orders (p = 3, 1, 0) is not stated. The text says identification uses "ACF/PACF of transformed differenced series" but does not show which ACF/PACF features led to p = 3 specifically. A cut-off in the PACF at lag 3 would justify AR(3), but no such discussion is present.

- The shortlist of three models with the same seasonal part is very limited for a series with 252 training observations and clear seasonal structure. At minimum, a SARIMA with P = 1 and Q = 1 should have been tested.

- No automatic model selection procedure (auto.arima equivalent) is referenced — which could have been used to cross-check the manual shortlist, even if not accepted blindly.

- Model coefficients are never shown. For SARIMA(3,1,0)(0,1,1,12), that is four parameters. The reader cannot evaluate whether the AR(3) terms are all significant, whether any should be dropped for parsimony, or whether the seasonal MA coefficient is consistent with invertibility.

---

## 9. ARIMA/SARIMA Estimation and Model Comparison — 8/20

**This is the most structurally weak section in the report.**

Table 4 shows AIC, BIC, and Ljung-Box p-values at lags 12 and 24. The results are:

| Model | LB p(12) | LB p(24) |
|---|---|---|
| SARIMA\_310\_011 | 2.37e-10 | 2.10e-06 |
| SARIMA\_111\_011 | 1.14e-14 | 2.18e-12 |
| SARIMA\_011\_011 | 1.29e-08 | 3.86e-05 |

All three models **fail the Ljung-Box test catastrophically.** These are not borderline results: p-values in the range of 10⁻¹⁰ to 10⁻¹⁴ indicate the residuals are far from white noise. **Every single candidate model in the shortlist has significant residual autocorrelation.**

What this means statistically: the fitted SARIMA models have not captured the full dependence structure of the series. Forecasts from such models are potentially biased, and prediction intervals are invalid because they are derived under the assumption of white noise residuals.

What the report does with this information: it says "all shortlisted models have very small Ljung-Box p-values at reported lags, suggesting residual autocorrelation concerns." This is an understatement. The appropriate response is:

1. Investigate whether the COVID structural break is causing the autocorrelation (regime shift in residuals)
2. Test additional candidate models (higher orders, seasonal AR components)
3. Consider an intervention variable for the COVID period
4. If no adequate model is found, explicitly state that SARIMA modelling failed to produce a satisfactory fit on this data and explain why

None of these steps are taken. The report simply moves on and includes Best\_SARIMA in the test-set comparison, giving the impression that a valid SARIMA model was found when in fact all candidates failed diagnostics.

**Missing entirely:**
- Model coefficients for any SARIMA candidate
- Standard errors
- AICc
- Discussion of why all models fail
- Any attempt to find a model that passes diagnostics

---

## 10. Diagnostic Checking — 5/20

Section 6.3, the diagnostic checking section, consists of exactly one sentence:

> *"When SARIMA residual tests are reported, Ljung-Box degrees of freedom are adjusted using p + q + P + Q."*

This is not a diagnostic checking section. It is a single methodological note. There are no residual plots, no residual ACF plots, no normality checks, no heteroskedasticity discussion, and no graphical evidence of any kind.

**What is absent:**
- Residual time plot for each SARIMA candidate
- Residual ACF and PACF (which would show where the remaining autocorrelation is concentrated — presumably around lags 12, 24)
- Histogram or Q-Q plot of residuals (normality matters for prediction interval validity)
- Standardised residual plot (to check for variance changes)
- Any residual diagnostics for Holt-Winters methods

**Why this matters:** The prediction intervals reported in Table 6 and Figure 7 for HW\_Add are only valid if the residuals are approximately normally distributed and homoskedastic. Given the COVID period in the training data, this is a non-trivial assumption. No evidence is provided that it holds.

The Ljung-Box degrees-of-freedom adjustment is correctly stated, but adjusting the test correctly while ignoring the catastrophic test outcomes is not diagnostics — it is box-checking. The report acknowledges that all models fail but provides zero follow-up investigation.

---

## 11. Forecast Comparison — 15/20

**Strengths:** Table 5 is clear, well-structured, and covers ME, MAE, MSE, RMSE, and MAPE. All methods are on the same holdout. The metric divergence between HW\_Add (best MAPE) and HW\_Mul (best RMSE) is correctly identified and briefly explained. The observation that SARIMA had better AIC but weaker holdout performance is a valid and correctly interpreted result.

**Issues:**

- **Figure 6 shows only SARIMA prediction intervals.** The reader cannot assess whether HW intervals would have captured the 2025 actuals. Given that HW was selected as the final method, its interval performance on the holdout is the more policy-relevant result.

- **HW\_Add was selected based on MAPE but HW\_Mul has better RMSE and nearly identical MAE.** The report does not explain why MAPE is the preferred criterion for this problem. For public transport demand (where large absolute errors matter operationally), RMSE penalising large errors is arguably more relevant than MAPE. The selection criterion should be justified.

- **No MASE.** Given that seasonal naive is the baseline, reporting MASE (mean absolute scaled error relative to seasonal naive) is natural and would show how much each method improves over the naive.

- **Empirical coverage of SARIMA intervals not stated.** With 12 holdout points and 95% PIs visible in Figure 6, it is trivial to count how many actuals fell inside. This number is never given.

---

## 12. Prediction Intervals and Uncertainty — 11/20

- Final 95% PIs for HW\_Add in 2026 are provided in Table 6. The half-width is approximately ±820 passengers in thousands around point forecasts.
- SARIMA intervals are shown in Figure 6 but appear very wide relative to the HW point forecasts — no discussion of why.
- **No mention of the distinction between prediction intervals and confidence intervals anywhere in the report.** This is a standard examination question.
- **No empirical coverage check.** How many of the 12 test observations in 2025 fell within the SARIMA 95% intervals? This is directly verifiable from Figure 6 and is never stated.
- **Back-transformation of SARIMA PIs not confirmed.** If SARIMA is fitted on log-scale data, the PIs must be exponentiated back. If this was not done, the reported comparison is invalid.
- **HW interval validity not examined.** With β = 0 and γ = 0, the HW model is essentially a frozen level+seasonal model. The theoretical basis for its prediction intervals assumes correctly specified residuals. Given the structural break and boundary parameters, the intervals in Table 6 may be optimistically narrow.
- **No discussion of how COVID-era residuals inflate interval uncertainty.** The irregular component in Table 7 has a minimum of −3688 — the training data contains extreme shocks. A simple residual-variance-based PI will be wider than a post-COVID-only estimate but narrower than what a regime-break-aware model would produce.

---

## 13. Out-of-Sample Forecasts — 14/20

**Strengths:** Table 6 is complete (date, point forecast, lower/upper PI). Figure 7 shows the forecast visually anchored to recent history. The horizon is clearly stated (2026, 12 months). The seasonal pattern in the forecasts is plausible.

**Issues:**

- **β = 0 implies flat trend extrapolation.** The 2026 forecasts carry no upward drift from the growing 2023–2025 trend visible in Figure 7. Monthly forecasts range from 6648 to 8297 — the same seasonal shape as recent years but with no growth. Whether this is appropriate requires a brief justification that is absent.

- **No SARIMA 2026 forecasts presented.** Even though SARIMA underperformed on the holdout, a table or plot of SARIMA forecasts for 2026 would allow comparison and would acknowledge that forecast uncertainty exists across model choices.

- **No real-world interpretation.** Do the 2026 forecasts represent growth from 2025? What is the implied annual total? At what month is peak demand expected and is it consistent with previous years? None of this is discussed.

---

## 14. Benefits and Limitations — 12/20

The section exists and covers all three method categories. Dataset-specific limitations are noted (COVID structural break, univariate framework). However:

- **The acknowledged diagnostic failure of all SARIMA candidates is not listed as a limitation.** This is the single most significant finding in the report and it is absent from the limitations section.
- **The boundary parameter solutions in Holt-Winters are not mentioned as a limitation.** α = 1 and γ = 0 have direct implications for forecast reliability.
- **Prediction interval validity post-COVID is not discussed** as a specific limitation — yet the training residuals contain COVID-era extreme values that inflate interval variance.
- Limitations are generic rather than dataset-specific. "Sensitivity to structural breaks" applies to every time series that has ever experienced a structural break, and adds nothing to the analysis.

---

## 15. Conclusions — 13/20

The conclusion correctly identifies HW\_Add as the best-performing method, cites the MAPE evidence, acknowledges the metric trade-off, and correctly notes that better AIC did not translate to better out-of-sample performance. The caveat about structural breaks is appropriate. These are genuine strengths.

**Weaknesses:**

- **The complete failure of SARIMA diagnostics is not mentioned in the conclusions.** The reader is left thinking that a valid SARIMA was estimated and simply happened to perform less well on the holdout — when in fact all three candidates produced residuals with p-values below 10⁻⁸ at lag 12. This should be acknowledged honestly.

- **The boundary parameter issues are not mentioned.** A conclusion that selects HW\_Add as the final model should acknowledge what is known about its limitations.

- **No statement about forecast usefulness for operational purposes.** Would a MAPE of 4.76% over a 12-month horizon be acceptable for Metro do Porto planning? This contextual judgement is missing.

---

## 16. Visualisations and Tables — 14/20

**Best figures:** Figure 1 (time plot with COVID highlight), Figure 2 (seasonal profile), Table 5 (test-set comparison), Table 6 (2026 forecasts).

**Problems:**

- **Figure 6 y-axis extends to 18,000.** The data never exceeds approximately 9,300. The axis scale is doubled for no visible reason, compressing all the curves into the bottom half of the plot and making the forecast comparisons nearly impossible to read at a glance. This is a significant presentation failure.

- **No residual diagnostic figures anywhere.** For a project with a full SARIMA section, the absence of residual ACF plots is a major gap — both in the main text and in the annexes.

- **Figure 6 shows SARIMA intervals as a broad red band that visually dominates the comparison.** The very wide intervals may reflect the back-transformed log-scale intervals inflating at higher levels, but this is not discussed. The figure is somewhat misleading without explanation.

- **ACF/PACF plots (Figures 3 and 5) are small and shown side-by-side.** They are readable but borderline. The y-axis range of [−1, 1] is appropriate.

- **Figure 7 axis labels say "Passengers (thousands)" — units are present, correct.** ✅

---

## 17. Writing Quality and Report Structure — 14/20

The report is logically structured, well within the page limit, and generally well written. Technical terminology is used correctly. The section organisation follows the assignment requirements.

**Issues:**

- Section 6.3 (Diagnostic Checking) is one sentence. In a report this length, that proportion is unacceptable for such a critical section.
- The Benefits and Limitations section reads like a compressed bullet-point list rather than a substantive discussion.
- The phrase "decomposition alone is not always a full forecasting model" in Section 5 is used to avoid producing decomposition-based forecasts. This is evasion, not analysis.
- Several paragraphs read as technically careful but analytically thin — they describe what was done without interpreting what it means (e.g., the paragraph on high α values in Section 4 is reasonable, but says nothing about the boundary solutions).

---

## 18. Oral Presentation Readiness — 11/20

The core story is clear and defensible in 8 minutes. The evaluation design, benchmark comparison, and final selection are communicable. However, several dangerous questions are not covered by the current report:

**Dangerous questions:**

1. *"All three of your SARIMA models failed the Ljung-Box test with p-values below 10⁻⁸. What does that mean? Why didn't you try to fix it?"* — The report has no answer to this beyond "residual autocorrelation concerns."

2. *"Your HW\_Mul has α = 1.0 and your HW\_Add has γ = 0. What does that mean? How do you interpret a seasonal model where the seasonal component never updates?"* — No answer prepared.

3. *"You selected HW\_Add based on MAPE. Why MAPE and not RMSE? HW\_Mul has clearly better RMSE. For operational transport planning, which metric should matter more?"* — No answer prepared.

4. *"How many of the 2025 actual values fell inside your SARIMA 95% prediction intervals?"* — Directly readable from Figure 6, not stated.

5. *"Why didn't you produce forecasts from your STL decomposition?"* — The report's answer is one sentence.

6. *"Your β = 0 means your HW forecast has flat trend. The data shows an upward trend in 2022–2024. Why should we trust a flat forecast for 2026?"* — Not addressed.

7. *"What is the difference between a confidence interval and a prediction interval? Which are the intervals in Table 6?"* — Never distinguished in the report.

8. *"Why is ADF inappropriate for your series?"* — Not mentioned.

---

## 19. Professor-Style Grading

---

### Final Grade Estimate

**Estimated grade: 11.5/20**

**Confidence: Medium**

The report has a solid structural skeleton — clean evaluation design, appropriate dataset, reasonable train/test split, and a sensible forecast comparison. These are genuine merits. However, the ARIMA/SARIMA section, which carries 18% of the weight, is severely weakened by the total failure of all diagnostic tests and the absence of any investigative follow-up. The diagnostic checking section, worth 10%, is effectively a one-sentence note. The smoothing section contains unreported boundary parameter solutions that require discussion. These are not polish issues — they are substantive methodological gaps.

---

### Grade Breakdown

| Dimension | Score /20 | Weight | Weighted contribution | Main issue |
|---|---:|---:|---:|---|
| Dataset and preparation | 16 | 8% | 1.28 | Repaired values not quantified |
| Time series description | 13 | 8% | 1.04 | Variance not discussed in EDA; seasonal profile not interpreted |
| Smoothing methods | 12 | 10% | 1.20 | Boundary parameters (α=1, β=0, γ=0) unacknowledged; no residuals |
| Decomposition methods | 11 | 10% | 1.10 | No decomposition-based forecasts produced |
| ARIMA/SARIMA modelling | 9 | 18% | 1.62 | All candidates fail Ljung-Box; no coefficients; narrow shortlist |
| Diagnostics | 5 | 10% | 0.50 | Section is one sentence; no residual plots; test failures unaddressed |
| Forecast comparison and test-set | 15 | 12% | 1.80 | HW PIs absent from comparison; MAPE criterion not justified |
| Prediction intervals and OOS | 12 | 7% | 0.84 | No coverage check; PI validity not examined; SARIMA width unexplained |
| Conclusions and limitations | 12 | 5% | 0.60 | SARIMA failure not in conclusions; boundary solutions not mentioned |
| Visualisations and writing | 13 | 4% | 0.52 | Figure 6 y-axis; no residual plots |
| **Total** | | **100%** | **11.70** | |

---

### Critical Issues Ranked by Severity

| Rank | Issue | Severity |
|---|---|---|
| 1 | All three SARIMA candidates fail Ljung-Box (p < 10⁻⁸); no investigation or remediation | **Fatal** |
| 2 | Diagnostic checking section is one sentence; no residual plots for any model | **Fatal** |
| 4 | HW boundary solutions (α=1.0, β=0, γ=0) not identified, reported, or discussed | **Major** |
| 5 | No decomposition-based forecasts produced despite explicit assignment requirement | **Major** |
| 6 | SARIMA model coefficients and standard errors never shown | **Major** |
| 7 | Back-transformation of SARIMA forecasts/errors not confirmed | **Major** |
| 8 | SARIMA seasonal shortlist entirely (0,1,1) — P=0 never challenged | **Moderate** |
| 9 | HW prediction intervals absent from test-set comparison (Figure 6) | **Moderate** |
| 10 | Selection criterion (MAPE over RMSE) not justified | **Moderate** |
| 11 | AICc not reported | **Moderate** |
| 12 | Seasonal component not interpreted in domain terms | **Minor** |
| 13 | Empirical coverage not reported for any PI | **Minor** |
| 14 | Changing variance not discussed in EDA | **Minor** |

---

### Methods That Are Valid

- **Chronological train/test split with seasonal naive benchmark.** Correctly designed, explicitly justified, consistently applied.
- **STL decomposition (additive).** The additive choice is defensible given the COVID disruption and the argument that seasonal amplitude does not scale proportionally with level across the full sample.
- **log transformation for SARIMA.** Correctly motivated by scale-dependent variance.
- **d = 1, D = 1, s = 12.** Consistent with the observed trend, seasonal structure, and ACF behaviour.
- **Ljung-Box degrees-of-freedom adjustment.** Correctly stated as adjusted by p + q + P + Q.
- **Metric choice (ME, MAE, RMSE, MAPE).** Appropriate combination; ME provides bias information.

---

### Methods That Are Questionable

**HW\_Mul with α = 1.0, β = 0, γ = 0**
- Why questionable: α = 1 is a boundary solution — all weight on the most recent observation, zero memory. Combined with frozen trend and frozen seasonality, this is closer to a season-naïve extrapolation than a Holt-Winters model.
- Assumption violated: The optimisation has converged to a corner solution. The model is likely misspecified for the post-COVID recovery dynamics.
- Missing evidence: Whether the optimiser was constrained to [0,1], whether alternative initialisations were tried, whether the model's in-sample fitted values are reasonable.
- Action: Report the boundary solutions as a limitation, test whether removing the β parameter improves the optimisation, and consider whether a damped-trend formulation would avoid the boundary.

**SARIMA with all three candidates sharing (0,1,1,12) seasonal structure**
- Why questionable: The seasonal ACF/PACF patterns may also be consistent with a seasonal AR component. No models with P > 0 were considered.
- Missing evidence: ACF at seasonal lags after differencing does not uniquely identify SMA(1). A spike at lag 12 in the ACF is consistent with ARMA(0,1) but also with AR(1) at the seasonal level.
- Action: Add at minimum SARIMA(0,1,1)(1,1,0,12) and SARIMA(1,1,1)(1,1,1,12) to the shortlist and compare AICs.

**SARIMA models used in holdout comparison despite failing diagnostics**
- Why questionable: Prediction intervals from models with residual autocorrelation are biased (intervals are too narrow; point forecasts may carry systematic errors). Including these in the comparison without flagging the invalid-interval caveat is misleading.
- Action: Either find a model that passes diagnostics, or explicitly caveat that SARIMA intervals are not valid and should not be taken at face value.

---

### Missing Methods or Checks

| Missing element | Essential / Optional | Impact if absent | Grade effect |
|---|---|---|---|
| Decomposition-based forecasts (e.g. STL + ETS) | **Essential** (assignment requires it) | Decomposition section scores as analysis only, not forecasting | High |
| Residual diagnostic plots | **Essential** | Impossibly to evaluate model adequacy; examiner cannot verify claims | High |
| Damped-trend Holt-Winters | Essential for data with post-COVID recovery | Flat-trend HW may underforecast 2026 | Medium |
| SARIMA with P > 0 | Essential for complete identification | Narrow shortlist; may have missed better-fitting model | Medium |
| Model coefficients table | **Essential** for any ARIMA report | Cannot assess parsimony, significance, or invertibility | High |
| AICc | Strongly recommended | AIC slightly over-selects parameters in moderate samples | Low |
| Normality check for residuals | Essential if PI validity claimed | PIs may be unreliable if residuals are skewed | Medium |
| Empirical coverage on holdout | Standard practice | Cannot verify whether stated 95% intervals were actually 95% | Medium |

---

### Unsupported Conclusions

| Conclusion in report | Problem | Evidence needed | Suggested rewrite |
|---|---|---|---|
| "Holt-Winters additive was selected for final 2026 forecasts" | Selection based on MAPE alone; HW\_Mul has better RMSE; criterion not pre-specified | Stated selection criterion with justification | "HW\_Add is selected on MAPE, which penalises proportional errors. HW\_Mul has lower RMSE; if large-error minimisation is operationally preferred, HW\_Mul is preferable." |
| SARIMA "competitive but not top-performing...despite stronger AIC" | All SARIMA models failed Ljung-Box; this framing implies they are valid alternative models | Explicit acknowledgement that SARIMA residual failures invalidate PIs | "All SARIMA candidates showed significant residual autocorrelation (LB p < 10⁻⁸), indicating inadequate model fit. Their holdout errors and prediction intervals should be treated with caution." |
| HW "robust benchmarks for monthly operational demand data" | α = 1 and β = γ = 0 are boundary solutions that indicate possible misspecification | Residual plots and discussion of boundary issues | Remove this claim or add explicit discussion of what the boundary solutions mean |
| "This recommendation is empirically justified for the current dataset" | The recommendation rests on a single holdout year and parameters that hit optimisation bounds | Sensitivity analysis, or at minimum an explicit scope limitation | Add: "This conclusion is contingent on one holdout year and on the smoothing parameters remaining appropriate under continued post-COVID recovery." |

---

### Method-to-Evidence Alignment

| Claim | Evidence used | Sufficient? | Missing evidence | Better support |
|---|---|---|---|---|
| Log transformation justified | "raw series shows larger absolute variation at higher levels" | Partially — stated but not shown in EDA | Residual variance plot before/after transformation | Show a scatter of absolute residuals vs level, or a Box-Cox profile plot |
| STL additive form appropriate | "seasonal effects do not scale proportionally...especially around disruption years" | Partially | Comparison of additive vs multiplicative seasonal amplitudes pre/post COVID | Show seasonal range by year to confirm non-proportional scaling |
| d=1, D=1 appropriate | ACF persists; annual seasonality present | Sufficient for D=1; d=1 justified by trend | Over-differencing not checked | Show mean and variance of differenced series; confirm seasonal ACF cuts off after D=1 |
| HW\_Add best method | Lowest MAPE (4.76%) on 2025 holdout | Weak — single holdout year, criterion not pre-specified | Multiple holdout years or rolling origin; stated primary metric | Pre-specify primary metric; mention result would differ with RMSE as criterion |
| SARIMA has "residual autocorrelation concerns" | LB p-values in table | Severely understated | Residual ACF plots; attempted remediation | Show residual ACF; attempt additional SARIMA orders; explain why autocorrelation persists |

---

### Assumption Checklist

| Method | Key assumptions | Checked? | Problem if not checked | Action |
|---|---|---|---|---|
| Holt-Winters Add/Mul | Additive/multiplicative error structure; parameters in (0,1); no boundary solutions | **No** — boundary solutions (α=1, β=0, γ=0) not checked or reported | Forecasts and PIs unreliable if model misspecified | Report boundary solutions explicitly; test damped trend; verify fitted values |
| STL decomposition | Additive form; stable seasonal pattern; remainder approximately random | Partially — additive justified; stability not tested | If seasonal pattern changed post-COVID, seasonal factors from training are biased | Compare seasonal factors from 2004–2019 vs 2022–2025 sub-periods |
| SARIMA | Stationarity after differencing; white noise residuals; correctly specified seasonal period | **No** — stationarity assumed, residuals fail LB, no normality check | All inference (coefficients, PIs, model selection) unreliable | Add residual plots; attempt models that pass LB; check residual normality |
| ACF/PACF identification | Differenced series approximately stationary; adequate sample size | Partially — Figure 5 shown; over-differencing not checked | Spurious AR/MA suggestions | Show sample mean/variance of differenced series |
| Ljung-Box test | df adjusted correctly for ARMA parameters | **Stated** as p+q+P+Q — but no evidence that this was actually implemented | Inflated Type I error if df not adjusted | Show the actual lag and df used for each model |
| AIC/BIC comparison | All models fitted to same training data; same transformation | Yes — all fitted to same training data | Invalid comparison if transformations differ | Confirm all AIC values are on the same log-likelihood scale |
| Test-set evaluation | No leakage; models not trained on test data | Yes — explicitly stated and Table 2 confirms | Invalid accuracy estimates | Already satisfied; ✅ |
| Prediction intervals | White noise residuals; normality; correct back-transformation | **No** — residuals not white noise; normality not checked; back-transformation not confirmed | Intervals potentially misleading | Add residual normality check; confirm back-transformation |

---

### Priority Fixes Before Submission

---

#### Fix 2 — Add a proper residual diagnostic section with plots
**Severity:** Fatal
**Impact on grade:** High
**What to change:** For each serious SARIMA candidate, add: (a) residual time plot, (b) residual ACF and PACF, (c) histogram or Q-Q plot, (d) standardised residual plot. Move to Annex if needed to save space.
**Why it matters:** Section 6.3 is one sentence. The entire ARIMA section rests on the claim that models were properly evaluated. Without plots, there is no evidence. The examiner cannot grade what they cannot see.
**How to do it:** `plot_diagnostics()` in statsmodels produces all four panels. Add a brief paragraph in Section 6.3 interpreting the plots rather than just the LB table.

---

#### Fix 3 — Acknowledge and investigate the total Ljung-Box failure
**Severity:** Fatal
**Impact on grade:** High
**What to change:** The current treatment ("residual autocorrelation concerns") is insufficient. Add a substantive paragraph explaining: (a) what significant LB means for forecast validity, (b) why all candidates failed (likely COVID structural break creating non-stationary residuals around 2020–2021), (c) what was attempted to address it (or explicitly state no passing model was found).
**Why it matters:** Reporting a failed model without discussion is methodologically dishonest and will attract immediate examiner scrutiny.
**How to rewrite:** "All shortlisted SARIMA models showed statistically significant residual autocorrelation at both lag 12 and lag 24 (Table 4). This is consistent with the COVID structural break generating a non-stationary residual regime in 2020–2021 that standard SARIMA differencing cannot absorb. Attempts to extend the shortlist to models with P = 1 [include if tried] did not resolve the issue. Accordingly, SARIMA prediction intervals in this analysis are not fully valid and should be treated as approximate. Forecast accuracy comparisons remain valid since they are based on point errors."

---

#### Fix 4 — Disclose and discuss the HW boundary parameter solutions
**Severity:** Major
**Impact on grade:** High
**What to change:** Add a paragraph after Table 3 explicitly noting that β = 0, γ = 0 (HW\_Add and Mul) and α = 1 (HW\_Mul) are boundary solutions. Explain what they imply for the model's behaviour.
**Why it matters:** A marker who knows HW well will immediately see these values and question why they are not discussed. Presenting them without comment implies the students do not recognise them as boundary solutions.
**How to rewrite:** "Both methods returned boundary parameter solutions: β = 0 indicates the trend component is frozen at its initialised value throughout training, and γ = 0 indicates the seasonal factors are never updated after initialisation. For HW\_Mul, α = 1.0 means the level is set entirely by the previous observation, eliminating exponential smoothing. These solutions may reflect the model's inability to simultaneously adapt to the COVID disruption and the post-recovery growth. Despite the boundary parameters, the methods produced competitive test-set accuracy. However, their prediction intervals may be unreliable due to model misspecification."

---

#### Fix 5 — Produce at least one decomposition-based forecast
**Severity:** Major
**Impact on grade:** High
**What to change:** Fit a simple forecasting model to the STL-seasonally-adjusted series, or use STL with ETS on the components, and include it in the test-set comparison. Even a naive forecast applied to the seasonally adjusted series plus the seasonal component from STL would count.
**Why it matters:** The assignment explicitly requires decomposition as a forecasting method, not just as an exploratory tool. "Decomposition alone is not always a full forecasting model" is evasion.

---

#### Fix 6 — Add model coefficients for SARIMA candidates
**Severity:** Major
**Impact on grade:** Medium
**What to change:** Add a table showing estimated coefficients, standard errors, and t-statistics for at least the best-AIC SARIMA model (3,1,0)(0,1,1,12).
**Why it matters:** Model coefficients are required to assess parsimony, verify invertibility, and evaluate whether any terms should be dropped. Without them, the model selection section is incomplete.

---

#### Fix 7 — Confirm and document log back-transformation
**Severity:** Major
**Impact on grade:** Medium
**What to change:** Add one sentence in Section 6.2 or 7 confirming that SARIMA forecasts and errors are reported on the original (passenger) scale after exponentiation.
**Why it matters:** If test-set errors in Table 5 were computed on log scale, the MAPE comparison across methods is invalid. This must be explicitly confirmed.

---

#### Fix 8 — Expand the SARIMA shortlist to include P > 0 candidates
**Severity:** Major
**Impact on grade:** Medium
**What to change:** Add at minimum SARIMA(0,1,1)(1,1,0,12) and SARIMA(1,1,1)(1,1,1,12) to Table 4.
**Why it matters:** The current shortlist tests only the SMA(1) seasonal specification. This is a narrow identification that may miss a better-fitting model. A seasonal AR component at lag 12 is plausible given the persistent ACF at lag 12.

---

#### Fix 9 — Justify the MAPE selection criterion
**Severity:** Moderate
**Impact on grade:** Medium
**What to change:** Add a sentence in Section 7 or the conclusion explaining why MAPE was chosen as the primary selection metric.
**Why it matters:** HW\_Mul has better RMSE. Selecting HW\_Add based on MAPE without justifying MAPE as the preferred criterion is a methodological choice that needs reasoning, not assumption.

---

#### Fix 10 — Report empirical coverage of prediction intervals on the 2025 holdout
**Severity:** Moderate
**Impact on grade:** Medium
**What to change:** State how many of the 12 actual 2025 observations fell within the SARIMA 95% PIs visible in Figure 6.
**How to do it:** Count from the plot, or compute programmatically. Add one sentence: "Of the 12 holdout observations, X fell within the SARIMA 95% prediction intervals, against a theoretical expectation of approximately 11.4."

---

#### Fix 11 — Correct Figure 6 y-axis scale
**Severity:** Moderate
**Impact on grade:** Low
**What to change:** The y-axis extends to 18,000 when data maxes at ~9,300. Set ylim to approximately 4,000–10,000 to make the comparison readable.
**Why it matters:** The current scale compresses all forecast lines into the bottom half of the plot, making differences between HW methods visually indistinguishable.

---

#### Fix 12 — Add a paragraph interpreting the seasonal component in real-world terms
**Severity:** Minor
**Impact on grade:** Low
**What to change:** In Section 3 or 5, add one paragraph stating which months have the highest and lowest seasonal factors and why (e.g., August trough likely reflects summer holiday reduction in commuter traffic; October–November peak may reflect return to regular schedules and event attendance).
**Why it matters:** Academic markers at this level expect data features to be connected to real-world context. This is a quick win.

---

## Final Verdict

**Is this project currently passable?** Marginally, at approximately 11–12/20. It would pass at a Portuguese university requiring a minimum of 10/20, but not comfortably, and it depends heavily on whether the examiner weights the SARIMA diagnostic failure as fatal.

**Is it good?** No. The evaluation design is clean and the report is well-structured, but the two sections with the highest combined weight (ARIMA/SARIMA modelling at 18% and diagnostics at 10%) are the weakest. A one-sentence diagnostic section for a project where all candidate models catastrophically fail a white-noise test is not passable at the Master's level.

**What is stopping it from getting a high grade (15+)?** Three things almost entirely: (1) the SARIMA residual diagnostic failure left uninvestigated, (2) the complete absence of residual plots, and (3) the boundary parameter solutions in HW left undiscussed. Fix those three, and produce one decomposition-based forecast, and this project could reach 14–15/20. The underlying analysis is not wrong — it is incomplete and under-examined.

**What would most improve it in the shortest time?** Add residual plots for SARIMA (one figure, 20 minutes of code), write a substantive paragraph explaining why all models fail Ljung-Box, report the HW boundary solutions, and add the Declaration. These four changes alone would recover approximately 2–3 grade points.