# FTMS Project V2

## Description
You should produce forecasts for the time series using smoothing, decomposition and statistical models. Write a report of your analysis explaining carefully what you have done and why you have done it. Your report should include the following elements.

1.     A discussion of the features of the time series.

2.     Analysis and forecasts using smoothing methods and decomposition methods.  All the details of the analysis must be given, namely

o   the estimation results for the smoothing methods must be shown;

o   the components of the time series - Trend-cycle, Seasonal, Error must be shown;

o   the seasonally adjusted data must be found.

3.     Building an ARIMA (SARIMA) model:

o   explain any transformations and differencing used;

o   describe the methodology used to create a short-list of appropriate ARIMA models; do not forget diagnostic checking that should include ACF/PACF graphs as well as the Ljung-Box test;

o   include discussion of AIC values as well as results from applying the models to a test-set.

4.     Compare the forecasting results obtained using the different approaches. Which method do you think gives the better forecasts? Explain with reference to the test-set comparing your forecasts with the actual numbers. Obtain 95% prediction intervals where applicable. How well did you do?

5.     Obtain out-of-sample point and 95% prediction intervals using the different approaches.

6.     Discuss the benefits and limitations of the models for your data.

Include tables and graphs in the text as close as possible to where you reference them. Graphs should be properly labelled, including appropriate units of measurement. You are free to use techniques such as cross-validation (for time series) and bootstrap.  Do not forget to state clearly the source of your data set.

**Unit root tests like ADF, PP or KPSS are not meant for seasonal data**

**Be careful with applying Ljung-Box test- you must specify the correct number of degrees of freedom**

The report must include a Declaration of Authenticity see the files under Declaration of Authenticity.

## Project structure

- `src/` — código Python
- `00_DATA/` — dados locais (não versionados)
- `01_OUTPUTS/` — resultados gerados (não versionados)
- `02_REPORTS/` — relatórios e documentos finais

## Como executar o projeto

```bash
python -m venv venv
pip install -r requirements.txt