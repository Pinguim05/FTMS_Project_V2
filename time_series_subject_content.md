# Time Series and Forecasting — Class Content Summary

> Based on the full ZIP material `FEP-2MDA08-2025_2026-2S_20260531_1449.zip`.
>
> Purpose: this file summarises what was taught in the class and what a university project for this subject should demonstrate.

---

## 1. Subject overview

This subject focuses on **time series analysis and forecasting**.

A time series is a sequence of observations collected over time, usually at regular intervals. Unlike ordinary cross-sectional data, time series observations are normally **ordered**, **dependent on the past**, and may contain patterns such as **trend**, **seasonality**, **cycles**, **structural breaks**, and **autocorrelation**.

The course combines two main perspectives:

1. **Classical statistical time series modelling**
   - stationarity;
   - autocorrelation;
   - AR, MA, ARMA, ARIMA and SARIMA models;
   - exponential smoothing;
   - STL decomposition;
   - multivariate time series;
   - dynamic regression and cross-correlation.

2. **Machine learning for time series**
   - datetime handling;
   - lagged features;
   - rolling-window features;
   - cyclical feature engineering;
   - leakage-safe validation;
   - tree-based forecasting models;
   - gradient boosting and quantile regression.

The central objective is not only to generate forecasts, but also to **understand the temporal structure of the data**, choose appropriate methods, validate assumptions, and evaluate forecast quality correctly.

---

## 2. Expected learning outcomes

By the end of the subject, a student should be able to:

1. Understand the main concepts and terminology of time series analysis.
2. Perform exploratory data analysis on time-indexed data.
3. Identify and describe the main components of a time series.
4. Analyse stationarity and temporal dependence.
5. Use ACF and PACF to support model identification.
6. Fit and interpret AR, MA, ARMA, ARIMA and SARIMA models.
7. Use decomposition and smoothing methods.
8. Forecast future values and evaluate forecast accuracy.
9. Analyse multivariate time series and lead-lag relationships.
10. Apply machine learning methods to time series while avoiding data leakage.
11. Use appropriate software tools, mainly R and Python.
12. Communicate results clearly, with justified methodological choices.

---

## 3. Material structure in the ZIP

The ZIP contains the following main blocks:

| Folder / Block | Main purpose |
|---|---|
| `A few elements of Probability and Statistics` | Statistical background needed for modelling and estimation |
| `Exploratory Data Analysis for Time Series` | Initial analysis, plots, trend, seasonality and components |
| `Stationarity and measures of correlation` | Stationarity, autocovariance, autocorrelation, ACF and PACF |
| `Decomposition and Smoothing Methods` | Exponential smoothing and STL decomposition |
| `AutoRegressive -AR- models` | AR models and their behaviour |
| `Moving- Average, MA, models` | MA models and their properties |
| `ARMA, ARIMA and SARIMA Models` | Integrated and seasonal time series models |
| `Forecasting with SARIMA models` | Forecasting workflow, diagnostics and accuracy evaluation |
| `Multivariate time series` | Cross-correlation, dynamic regression and lag relationships |
| `ML for Time Series` | Python-based machine learning workflows for time series |
| `References` | Supporting textbooks and theoretical references |

---

## 4. Probability and statistics background

### 4.1 Random variables

The course starts with basic probability concepts:

- random variables;
- discrete and continuous variables;
- probability mass functions;
- probability density functions;
- cumulative distribution functions;
- joint distributions;
- independence between random variables.

This background is important because time series models are stochastic models. The observed data are treated as one possible realisation of an underlying random process.

### 4.2 Expected value, variance and covariance

Key concepts:

- expected value / mean;
- variance;
- standard deviation;
- covariance;
- correlation;
- linear dependence between variables.

These are later extended to time series through concepts such as autocovariance and autocorrelation.

### 4.3 Random samples and estimators

The material also reviews:

- random samples;
- iid assumptions;
- statistics as functions of samples;
- sample mean;
- sample variance;
- point estimators;
- bias;
- consistency;
- efficiency.

This matters because many classical statistical methods assume independent observations, while time series data often violate that assumption due to autocorrelation.

---

## 5. Introduction to time series

### 5.1 Definition of a time series

A time series is a sequence of observations indexed by time:

```text
Y1, Y2, Y3, ..., Yt
```

Examples include:

- monthly sales;
- daily temperatures;
- stock prices;
- production volumes;
- website traffic;
- electricity demand;
- air quality measurements.

### 5.2 Why time series are different

Time series data are different from ordinary tabular data because:

- observations are ordered;
- the past may influence the present;
- neighbouring observations may be correlated;
- trend and seasonality may dominate the behaviour;
- random train-test splits can create data leakage;
- forecasting requires respecting chronological order.

### 5.3 Main components of a time series

A time series may contain:

| Component | Meaning |
|---|---|
| Trend | Long-term increase or decrease |
| Seasonality | Repeating pattern with fixed frequency |
| Cycles | Long-term fluctuations without fixed frequency |
| Noise / remainder | Random unexplained variation |
| Structural breaks | Sudden changes in level, variance or pattern |
| Outliers | Extreme values not representative of normal behaviour |

---

## 6. Exploratory Data Analysis for Time Series

Exploratory Data Analysis, EDA, is a major part of the subject. Before modelling, the data must be understood visually and statistically.

### 6.1 Initial time plot

The first step is usually to plot the series against time.

This helps identify:

- trend;
- seasonality;
- outliers;
- missing periods;
- changes in variance;
- changes in behaviour over time;
- possible structural breaks.

A project should not start directly with modelling. It should first describe what the data look like.

### 6.2 Seasonal analysis

For seasonal data, the course includes seasonal exploration such as:

- seasonal plots;
- monthly/quarterly comparisons;
- repeated yearly patterns;
- identifying seasonal peaks and troughs.

Example questions:

- Are some months always higher than others?
- Is the seasonal pattern stable over time?
- Does the amplitude of seasonality increase with the level of the series?

### 6.3 Transformations

Transformations may be needed when:

- variance increases with the level of the series;
- the series is strongly skewed;
- multiplicative seasonality is present;
- forecast errors should be stabilised.

Common transformations:

- logarithmic transformation;
- Box-Cox transformation;
- scaling or standardisation in ML contexts.

### 6.4 Lag plots

Lag plots compare a time series with lagged versions of itself.

They are useful to detect:

- autocorrelation;
- non-random structure;
- nonlinear dependence;
- possible autoregressive behaviour.

### 6.5 EDA outputs expected in a project

A good project should include:

- time plot;
- discussion of trend;
- discussion of seasonality;
- discussion of variance stability;
- missing value analysis;
- outlier analysis;
- relevant transformations;
- initial modelling implications.

---

## 7. Stationarity and measures of dependence

Stationarity is one of the central theoretical ideas in the subject.

### 7.1 Stationarity

A time series is stationary when its statistical properties do not change over time.

The course distinguishes between:

- strict stationarity;
- weak stationarity / covariance stationarity.

For most practical modelling, weak stationarity is the key concept.

A weakly stationary series has:

1. constant mean over time;
2. constant variance over time;
3. autocovariance depending only on the lag, not on the specific time point.

### 7.2 Why stationarity matters

Many classical models, such as ARMA models, assume stationarity.

If a series has trend or seasonality, it is often non-stationary. In that case, the project should consider:

- differencing;
- seasonal differencing;
- transformation;
- decomposition;
- fitting ARIMA/SARIMA instead of ARMA.

### 7.3 Autocovariance

Autocovariance measures how a time series is related to itself at different lags.

It answers questions like:

- Is today's value related to yesterday's value?
- Are values 12 months apart related?
- Does dependence disappear quickly or slowly?

### 7.4 Autocorrelation Function — ACF

The ACF measures correlation between a series and its lagged values.

It is used to:

- detect serial dependence;
- identify seasonality;
- identify possible MA components;
- check if residuals behave like white noise;
- assess whether differencing was sufficient.

Typical interpretations:

- ACF near zero for all lags: possible white noise.
- Slowly decaying ACF: possible non-stationarity or AR behaviour.
- Significant spikes at seasonal lags: seasonality.
- Sharp cut-off after lag q: possible MA(q) process.

### 7.5 Partial Autocorrelation Function — PACF

The PACF measures correlation between a series and a lag after removing the effect of intermediate lags.

It is useful for identifying AR models.

Typical interpretations:

- PACF cuts off after lag p: possible AR(p) process.
- ACF cuts off after lag q: possible MA(q) process.
- Both ACF and PACF decay: possible ARMA process.

### 7.6 White noise

White noise is a sequence of uncorrelated random variables with constant mean and variance.

In model diagnostics, residuals should ideally behave like white noise.

If residuals still show autocorrelation, the model has not captured all temporal structure.

---

## 8. Decomposition and smoothing methods

### 8.1 Decomposition

Time series decomposition separates the observed series into components:

```text
Observed = Trend + Seasonal + Remainder
```

or, in multiplicative form:

```text
Observed = Trend × Seasonal × Remainder
```

Decomposition helps explain the structure of the series before forecasting.

### 8.2 STL decomposition

STL means **Seasonal-Trend decomposition using LOESS**.

It decomposes the series into:

- trend component;
- seasonal component;
- remainder component.

Advantages of STL:

- flexible trend estimation;
- useful for complex seasonal patterns;
- can be robust to outliers;
- useful for visual understanding before modelling.

### 8.3 Exponential smoothing

Exponential smoothing methods forecast using weighted averages of past observations, with more recent observations receiving higher weight.

Methods include:

- simple exponential smoothing;
- Holt's linear trend method;
- damped trend methods;
- seasonal exponential smoothing;
- Holt-Winters-type methods.

These methods are especially useful when the goal is forecasting and the series contains trend and/or seasonality.

### 8.4 ARIMA versus exponential smoothing

The subject compares ARIMA and exponential smoothing.

In general:

- ARIMA focuses on autocorrelation and stochastic dependence;
- exponential smoothing focuses on level, trend and seasonal components;
- both can produce forecasts;
- the best method depends on the data and must be validated empirically.

---

## 9. Autoregressive models — AR

### 9.1 AR model idea

An autoregressive model explains the current value using previous values of the same series.

An AR(1) model has the form:

```text
Yt = c + φ1Yt-1 + εt
```

An AR(p) model uses p previous lags:

```text
Yt = c + φ1Yt-1 + φ2Yt-2 + ... + φpYt-p + εt
```

### 9.2 Interpretation

AR models are useful when the past values of the series contain predictive information.

For example:

- sales this month may depend on sales last month;
- temperature today may depend on temperature yesterday;
- electricity demand at one hour may depend on previous hours.

### 9.3 Stationarity in AR models

AR models require stationarity conditions.

For AR(1), the model is stationary when:

```text
|φ1| < 1
```

If this condition is violated, shocks may not disappear over time and the process may be explosive or non-stationary.

### 9.4 ACF and PACF patterns for AR models

For AR processes:

- ACF usually decays gradually;
- PACF often cuts off after the AR order p.

This is important for model identification.

---

## 10. Moving Average models — MA

### 10.1 MA model idea

A moving average model explains the current value using current and past shocks/errors.

An MA(1) model has the form:

```text
Yt = μ + εt + θ1εt-1
```

An MA(q) model uses q previous shocks:

```text
Yt = μ + εt + θ1εt-1 + ... + θqεt-q
```

### 10.2 Interpretation

MA models are useful when shocks have short-term effects.

For example, an unexpected event may affect the current period and a few following periods, but not the long-term trajectory.

### 10.3 Invertibility

MA models require invertibility conditions.

Invertibility ensures that the model can be represented and estimated in a stable and meaningful way.

### 10.4 ACF and PACF patterns for MA models

For MA processes:

- ACF often cuts off after lag q;
- PACF usually decays gradually.

This contrasts with AR models.

---

## 11. ARMA models

### 11.1 ARMA model idea

ARMA models combine autoregressive and moving average components.

An ARMA(p, q) model includes:

- p autoregressive terms;
- q moving average terms.

General structure:

```text
AR component + MA component + random error
```

### 11.2 When ARMA is appropriate

ARMA models are appropriate for stationary time series.

If the original series is not stationary, then ARMA should not be applied directly. The data should first be transformed or differenced, leading to ARIMA or SARIMA models.

### 11.3 ACF and PACF pattern

For ARMA models:

- both ACF and PACF usually decay gradually;
- neither has a clean cut-off pattern.

This makes model identification more complex than pure AR or pure MA models.

---

## 12. ARIMA models

### 12.1 ARIMA model idea

ARIMA stands for:

```text
Autoregressive Integrated Moving Average
```

An ARIMA(p, d, q) model contains:

| Parameter | Meaning |
|---|---|
| p | autoregressive order |
| d | number of non-seasonal differences |
| q | moving average order |

The integration part, `d`, refers to differencing used to make the series stationary.

### 12.2 Differencing

Differencing removes trend or non-stationary behaviour.

First difference:

```text
Yt - Yt-1
```

Second difference:

```text
(Yt - Yt-1) - (Yt-1 - Yt-2)
```

Differencing should be used carefully.

Too little differencing leaves non-stationarity. Too much differencing can introduce unnecessary noise and distort the model.

### 12.3 Box-Jenkins methodology

The ARIMA modelling workflow follows the Box-Jenkins logic:

1. Identify the structure of the data.
2. Transform and difference if needed.
3. Use ACF/PACF to suggest candidate models.
4. Estimate the models.
5. Diagnose residuals.
6. Compare candidate models.
7. Forecast using the selected model.

### 12.4 Residual diagnostics

After fitting ARIMA models, residuals should be checked.

A good model should have residuals that:

- have no visible pattern;
- have approximately constant variance;
- show no significant autocorrelation;
- behave approximately like white noise.

---

## 13. SARIMA models

### 13.1 SARIMA model idea

SARIMA extends ARIMA to seasonal data.

A SARIMA model is written as:

```text
SARIMA(p, d, q)(P, D, Q)s
```

Where:

| Parameter | Meaning |
|---|---|
| p | non-seasonal AR order |
| d | non-seasonal differencing |
| q | non-seasonal MA order |
| P | seasonal AR order |
| D | seasonal differencing |
| Q | seasonal MA order |
| s | seasonal period |

Examples of `s`:

- monthly data with yearly seasonality: `s = 12`;
- quarterly data with yearly seasonality: `s = 4`;
- daily data with weekly seasonality: `s = 7`.

### 13.2 Seasonal differencing

Seasonal differencing removes repeating seasonal patterns.

For monthly data:

```text
Yt - Yt-12
```

This is useful when the value this month is strongly related to the value in the same month of the previous year.

### 13.3 Seasonal ACF/PACF patterns

Seasonal models are identified by checking spikes at seasonal lags:

- lag 12, 24, 36 for monthly yearly seasonality;
- lag 4, 8, 12 for quarterly yearly seasonality;
- lag 7, 14, 21 for daily weekly seasonality.

### 13.4 Model redundancy

The exercises include checking whether AR and MA factors cancel each other.

If the same factor appears in both the AR and MA parts, it may be redundant and should be simplified.

A project should avoid blindly fitting overly complex SARIMA models without checking whether the structure makes sense.

---

## 14. Forecasting workflow

A complete forecasting workflow should include the following stages.

### 14.1 Define the forecasting problem

Before modelling, define:

- target variable;
- time frequency;
- forecast horizon;
- available historical period;
- business or analytical objective;
- whether the task is univariate or multivariate.

### 14.2 Prepare the data

Important steps:

- parse dates correctly;
- sort observations by time;
- set the correct time index;
- check missing dates;
- handle missing values;
- aggregate/resample if needed;
- check for duplicates;
- align external variables if used.

### 14.3 Explore the series

Use EDA to understand:

- trend;
- seasonality;
- variance;
- outliers;
- structural breaks;
- autocorrelation;
- possible need for transformations.

### 14.4 Split data correctly

Time series should be split chronologically.

Wrong approach:

```text
Random train/test split
```

Correct approach:

```text
Train = older observations
Test = later observations
```

This mimics the real forecasting problem, where the future is unknown at training time.

### 14.5 Fit candidate models

Candidate models may include:

- naive forecast;
- seasonal naive forecast;
- exponential smoothing;
- ARIMA;
- SARIMA;
- dynamic regression;
- machine learning models with lagged features.

A project should compare models against simple baselines.

### 14.6 Diagnose residuals

After fitting the model, analyse residuals:

- residual time plot;
- residual ACF;
- distribution of residuals;
- remaining seasonality;
- remaining autocorrelation;
- large errors or outliers.

### 14.7 Evaluate forecast accuracy

Use test data or time-series cross-validation.

Metrics taught include:

| Metric | Meaning |
|---|---|
| ME | Mean Error |
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |
| MAPE | Mean Absolute Percentage Error |
| MASE | Mean Absolute Scaled Error |

### 14.8 Interpret the forecasts

A project should explain:

- forecast direction;
- uncertainty;
- expected trend;
- expected seasonal behaviour;
- limitations;
- whether the forecast is reliable for the chosen horizon.

---

## 15. Forecast accuracy metrics

### 15.1 Mean Error — ME

ME measures average signed error.

It shows bias:

- positive ME: forecasts are too low on average;
- negative ME: forecasts are too high on average.

### 15.2 Mean Absolute Error — MAE

MAE measures average absolute error.

It is easy to interpret because it is in the same unit as the original data.

### 15.3 Mean Squared Error — MSE

MSE penalises large errors more strongly because errors are squared.

It is useful when large forecast errors are especially undesirable.

### 15.4 Root Mean Squared Error — RMSE

RMSE is the square root of MSE.

It is also in the same unit as the original data, but still penalises large errors more than MAE.

### 15.5 Mean Absolute Percentage Error — MAPE

MAPE expresses error as a percentage.

However, MAPE has limitations:

- it fails or becomes unstable when actual values are zero or close to zero;
- it can be misleading with small denominators;
- it is asymmetric in some contexts.

### 15.6 Mean Absolute Scaled Error — MASE

MASE compares forecast errors against a naive benchmark.

It is useful because it is scale-independent and can be compared across series.

---

## 16. Forecasting with interruptions and structural breaks

The subject includes material on forecasting time series with interruptions.

Interruptions can be caused by:

- pandemics;
- strikes;
- policy changes;
- production stops;
- sudden market disruptions;
- extraordinary events.

In a project, if the data contain interruptions, they should not be ignored.

Possible approaches:

- include intervention variables;
- model pre- and post-interruption periods separately;
- treat the interruption as an outlier or structural break;
- avoid training the model as if the interruption was normal behaviour;
- discuss how the interruption affects forecast reliability.

---

## 17. Multivariate time series

### 17.1 Cross-correlation

The course includes cross-correlation between two time series.

The cross-correlation function, CCF, helps identify whether one series leads or lags another.

Example questions:

- Does variable X help predict variable Y?
- Does X lead Y by one period, two periods, or more?
- Are the two series contemporaneously correlated?

### 17.2 Prewhitening

Prewhitening is used before interpreting cross-correlations.

The idea is to remove autocorrelation from one or both series so that cross-correlation results are not misleading.

Without prewhitening, two autocorrelated series can appear related simply because both have internal temporal structure.

### 17.3 Dynamic regression

Dynamic regression models include lagged explanatory variables.

Example structure:

```text
Yt = β0 + β1Xt + β2Xt-1 + β3Xt-2 + εt
```

This is useful when the effect of an explanatory variable is delayed.

### 17.4 Autocorrelated errors

Ordinary regression assumes independent errors.

In time series, errors are often autocorrelated.

If autocorrelated errors are ignored:

- coefficients may appear more significant than they are;
- confidence intervals may be wrong;
- forecasts may be unreliable;
- residual assumptions are violated.

A good project should check residual autocorrelation when using regression with time series data.

---

## 18. Machine Learning for Time Series

The ML section uses Python and focuses on transforming time series forecasting into supervised learning.

### 18.1 Datetime handling in pandas

Key skills:

- parsing datetime columns;
- setting datetime indexes;
- sorting by time;
- extracting date components;
- resampling data;
- filtering by time windows.

### 18.2 Resampling

Resampling changes the frequency of the data.

Examples:

- hourly to daily;
- daily to monthly;
- transaction-level data to weekly totals.

Common aggregations:

- mean;
- sum;
- minimum;
- maximum;
- count.

### 18.3 Rolling windows

Rolling windows compute statistics over recent observations.

Examples:

- rolling mean over the last 7 days;
- rolling standard deviation over the last 30 days;
- rolling sum over the last 24 hours.

These features help ML models understand recent behaviour.

### 18.4 Lagged features

Lagged features are past values of the target or explanatory variables.

Examples:

```text
Yt-1
Yt-2
Yt-7
Yt-12
```

Lagged features are one of the most important tools in ML forecasting.

### 18.5 Cyclical feature engineering

Calendar variables like hour, day of week or month are cyclical.

For example:

- hour 23 is close to hour 0;
- December is close to January;
- Sunday is close to Monday.

Instead of treating these as simple numbers, the course includes sine/cosine transformations:

```text
sin(2πx / period)
cos(2πx / period)
```

This helps ML models understand cyclic patterns.

### 18.6 Time-based cross-validation

Machine learning models must be validated using time-aware splits.

Common approaches:

- expanding window validation;
- rolling window validation;
- walk-forward validation.

The validation process must respect the order of time.

### 18.7 Data leakage

Data leakage happens when information from the future is accidentally used to predict the past.

Examples of leakage:

- random train/test split;
- calculating rolling features using future values;
- scaling using the full dataset before splitting;
- using target-derived features not available at prediction time;
- using future external variables that would not be known in reality.

Avoiding leakage is one of the most important parts of a time series ML project.

### 18.8 Tree-based models and gradient boosting

The ML materials include tree-based models and Histogram-Based Gradient Boosting Regression.

These models can handle:

- nonlinear relationships;
- interactions between features;
- lagged variables;
- calendar effects;
- rolling statistics.

However, they do not automatically understand time. Time structure must be encoded through features.

### 18.9 Quantile regression and uncertainty

The ML section includes quantile regression.

Quantile regression can be used to estimate prediction intervals, such as:

- lower forecast bound;
- median forecast;
- upper forecast bound.

This is useful because forecasting should not only provide a point estimate, but also an idea of uncertainty.

---

## 19. Software used in the subject

### 19.1 R

R is used for classical time series examples and modelling.

The ZIP includes:

- `.Rmd` files;
- generated `.html` reports;
- examples using time series plots;
- ARIMA/SARIMA modelling workflows;
- forecasting examples;
- diagnostic analysis.

Typical R workflow:

1. Load data.
2. Convert to time series object.
3. Plot and explore.
4. Check ACF/PACF.
5. Fit models.
6. Diagnose residuals.
7. Forecast.
8. Compare accuracy.

### 19.2 Python

Python is used mainly in the ML section.

The ZIP includes Jupyter notebooks using:

- pandas;
- datetime functionality;
- resampling;
- rolling features;
- lagged features;
- scikit-learn;
- gradient boosting models.

Typical Python workflow:

1. Load data.
2. Parse datetime variables.
3. Sort and index by time.
4. Create time-based features.
5. Create lagged and rolling features.
6. Split data chronologically.
7. Train ML model.
8. Evaluate forecasts on future data.
9. Analyse errors.

---

## 20. Datasets and examples in the materials

The ZIP includes several datasets and worked examples.

### 20.1 Retail and tourism-type data

Used for EDA, trend and seasonality analysis.

Likely objectives:

- identify components;
- visualise seasonality;
- understand transformations;
- practise time series plots.

### 20.2 Milk production data

Used in ARIMA/SARIMA modelling and forecasting examples.

Likely objectives:

- model monthly seasonality;
- use seasonal differencing;
- inspect ACF/PACF;
- fit SARIMA models;
- forecast future values.

### 20.3 Hare and lynx example

Used in multivariate time series.

Likely objectives:

- analyse cross-correlation;
- identify lead-lag relationships;
- discuss dynamic regression;
- understand biological/time-dependent interaction between variables.

### 20.4 Air quality data

Used in Python ML time series examples.

Likely objectives:

- work with datetime data;
- resample observations;
- analyse pollution measurements over time;
- build time-aware features.

### 20.5 Fremont Bridge bicycle data

Used in ML forecasting examples.

Likely objectives:

- forecast traffic/counts;
- use calendar features;
- use lagged features;
- apply machine learning regression models;
- evaluate forecasts correctly.

---

## 21. What a project for this subject should demonstrate

A strong project should demonstrate that you understand both the statistical and practical sides of time series forecasting.

### 21.1 Data understanding

The project should clearly explain:

- what the dataset represents;
- what the time index is;
- what the target variable is;
- the frequency of the data;
- the forecast horizon;
- whether the problem is univariate or multivariate.

### 21.2 Exploratory analysis

The project should include:

- time plot;
- trend analysis;
- seasonality analysis;
- missing values;
- outliers;
- changes in variance;
- structural breaks;
- ACF/PACF analysis.

### 21.3 Methodological justification

Every method should be justified.

Weak justification:

```text
I used SARIMA because it is a forecasting model.
```

Strong justification:

```text
The series showed trend and yearly seasonality. After applying first differencing and seasonal differencing, the ACF and PACF suggested a seasonal ARIMA structure. Candidate models were compared using out-of-sample MAE and MASE, and residual diagnostics were used to check whether autocorrelation remained.
```

### 21.4 Model comparison

The project should compare at least some of the following:

- naive forecast;
- seasonal naive forecast;
- exponential smoothing;
- ARIMA/SARIMA;
- ML model with lagged features;
- dynamic regression if external variables are used.

A project should not present only one model without a benchmark.

### 21.5 Forecast evaluation

Evaluation must be done on future data, not random observations.

The project should include:

- chronological train/test split;
- possibly rolling-origin validation;
- suitable error metrics;
- comparison table;
- discussion of which model performs best and why.

### 21.6 Residual analysis

For statistical models, residuals should be analysed.

Include:

- residual plot;
- residual ACF;
- comment on whether residuals resemble white noise;
- discussion of remaining patterns.

### 21.7 Forecast interpretation

The project should explain the forecast in plain language:

- expected future behaviour;
- trend direction;
- seasonality;
- uncertainty;
- limitations;
- practical implications.

---

## 22. Common methodological mistakes to avoid

### 22.1 Random train-test split

This is one of the biggest mistakes in time series projects.

Random splitting allows information from the future to influence the training set.

Use chronological splitting instead.

### 22.2 Ignoring stationarity

Do not fit ARMA/ARIMA/SARIMA blindly.

Check:

- trend;
- seasonality;
- ACF/PACF;
- differencing needs;
- residual autocorrelation.

### 22.3 Using ACF/PACF mechanically

ACF and PACF are guides, not automatic answers.

They should be interpreted together with:

- plots;
- transformations;
- differencing;
- seasonality;
- model diagnostics;
- forecast performance.

### 22.4 Overfitting complex models

A complex SARIMA model is not automatically better.

Avoid:

- too many parameters;
- redundant AR/MA terms;
- poor residual diagnostics;
- selecting the model only by in-sample fit.

### 22.5 Ignoring simple baselines

A project should compare against simple forecasts.

For example:

- naive forecast;
- seasonal naive forecast;
- moving average forecast.

If a complex model does not beat the baseline, it may not be useful.

### 22.6 Ignoring forecast horizon

A model can be good for short-term forecasting and weak for long-term forecasting.

The project should define the forecast horizon clearly.

### 22.7 Leakage in ML features

When using ML, ensure features only use information available at prediction time.

Incorrect:

```text
rolling average centred around the target date
```

Correct:

```text
rolling average using only past observations
```

---

## 23. Recommended project structure

A good project report could follow this structure:

```text
1. Introduction
   1.1 Objective
   1.2 Dataset description
   1.3 Forecasting problem
   1.4 Forecast horizon

2. Data Preparation
   2.1 Date parsing and frequency
   2.2 Missing values
   2.3 Duplicates and consistency checks
   2.4 Train/test split

3. Exploratory Data Analysis
   3.1 Time plot
   3.2 Trend
   3.3 Seasonality
   3.4 Outliers and structural breaks
   3.5 ACF/PACF

4. Modelling Approach
   4.1 Baseline models
   4.2 Exponential smoothing / STL if applicable
   4.3 ARIMA/SARIMA if applicable
   4.4 ML models with lagged features if applicable
   4.5 Justification of methods

5. Model Evaluation
   5.1 Error metrics
   5.2 Forecast comparison
   5.3 Residual diagnostics
   5.4 Final model selection

6. Forecast Results
   6.1 Forecast plots
   6.2 Forecast interpretation
   6.3 Uncertainty and limitations

7. Conclusion
   7.1 Main findings
   7.2 Best model
   7.3 Practical implications
   7.4 Limitations and future work
```

---

## 24. Checklist for the project

Use this checklist before submitting the project.

### Data and problem definition

- [ ] The target variable is clearly defined.
- [ ] The time index is correctly parsed.
- [ ] The frequency of the data is stated.
- [ ] The forecast horizon is stated.
- [ ] The project explains why the problem is a time series problem.

### EDA

- [ ] Time plot included.
- [ ] Trend discussed.
- [ ] Seasonality discussed.
- [ ] Outliers discussed.
- [ ] Missing values checked.
- [ ] ACF/PACF analysed.
- [ ] Transformations justified, if used.

### Modelling

- [ ] Baseline forecast included.
- [ ] Model choices are justified.
- [ ] Stationarity is considered.
- [ ] Differencing is justified, if used.
- [ ] Seasonal structure is considered.
- [ ] ML features use only past information.
- [ ] No random train-test split is used.

### Evaluation

- [ ] Test set respects chronological order.
- [ ] Suitable metrics are used.
- [ ] Forecasts are compared fairly.
- [ ] Residuals are analysed.
- [ ] Final model selection is justified.

### Conclusions

- [ ] Conclusions follow from the results.
- [ ] The project does not overclaim.
- [ ] Limitations are stated.
- [ ] Practical implications are explained.

---

## 25. How to connect class content to a project

The project should show the connection between data characteristics and method choice.

| Data characteristic | Possible method / response |
|---|---|
| Clear trend | differencing, Holt trend, trend features |
| Clear seasonality | seasonal plots, STL, SARIMA, seasonal naive, seasonal features |
| Non-stationary mean | differencing or transformation |
| Changing variance | log or Box-Cox transformation |
| Strong autocorrelation | AR/ARIMA/SARIMA models, lagged ML features |
| External predictors | dynamic regression or ML with exogenous variables |
| Structural break | intervention variable, separate modelling, limitation discussion |
| Nonlinear patterns | tree-based ML models |
| Need uncertainty intervals | statistical forecast intervals or quantile regression |

---

## 26. Summary of all major methods taught

### Classical time series methods

- time series plots;
- decomposition;
- STL;
- exponential smoothing;
- AR models;
- MA models;
- ARMA models;
- ARIMA models;
- SARIMA models;
- Box-Jenkins methodology;
- residual diagnostics;
- forecast accuracy evaluation.

### Dependence and stationarity methods

- mean function;
- autocovariance;
- autocorrelation;
- ACF;
- PACF;
- white noise;
- stationarity conditions;
- invertibility conditions;
- differencing;
- seasonal differencing.

### Multivariate methods

- cross-correlation;
- prewhitening;
- dynamic regression;
- distributed lag models;
- regression with autocorrelated errors.

### Machine learning methods

- datetime feature extraction;
- resampling;
- lagged features;
- rolling-window features;
- cyclical encoding;
- time-based validation;
- gradient boosting regression;
- quantile regression;
- forecast uncertainty estimation.

---

## 27. Final interpretation of the subject

This subject teaches how to move from raw time-indexed data to justified forecasts.

The key intellectual skill is not simply knowing many models. The key skill is knowing **which method is appropriate for which type of time series**, and being able to justify that choice using:

- plots;
- stationarity analysis;
- ACF/PACF;
- decomposition;
- residual diagnostics;
- forecast accuracy;
- leakage-free validation.

For the project, the safest approach is to show a complete workflow:

```text
Understand the data → Explore time patterns → Check stationarity and dependence → Build baseline models → Fit suitable statistical/ML models → Evaluate correctly → Interpret results honestly
```

A strong project should not only produce forecasts. It should explain why the chosen method is valid for the data and what limitations remain.
