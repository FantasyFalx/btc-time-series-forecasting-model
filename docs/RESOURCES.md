# Resources

- https://www.coingecko.com/en/coins/bitcoin/historical_data?start=2025-09-04&end=2026-09-04


## How to fix model: 
While a 3.66% MAPE looks impressive on paper, the chart highlights a classic pitfall in applying standard ARIMA models to financial time series.

**Key Insights from the Visual**

* **Lag/Flatline Prediction:** The red forecast line simply slopes slightly downward from the split point (~$61,000 to ~$60,000), completely missing the actual market dynamic (the blue line, which immediately bounced upward toward $66,000 before fluctuating).
* **The "Naïve Persistence" Trap:** Financial asset prices often follow a random walk. A basic ARIMA model usually predicts a near-flat line (or a straight continuation of the immediate trend).
* **Why the MAPE is 3.66%:** Because the forecast horizon is very short (5 days) and the absolute price level of Bitcoin is high (~$60,000 to $65,000), a prediction error of $2,000–$3,000 yields a low percentage error (~3%–5%). However, the model gets the **direction (sign of return)** wrong—predicting a drop while the market moved up.

**Key Recommendations**

* **Directional Accuracy Metric:** Evaluate your model using **Mean Directional Accuracy (MDA)** alongside MAPE to see if it correctly predicts whether the price goes up or down.
* **Stationarity & Differencing:** Ensure you are modeling stationary log-returns ($\ln(P_t / P_{t-1})$) rather than raw closing prices ($P_t$). Forecasting prices directly often causes ARIMA to act like a persistence model ($Y_{t+1} \approx Y_t$).
* **Baseline Benchmark:** Compare your ARIMA performance against a naïve baseline model (e.g., predicting tomorrow's price equals today's price). If ARIMA doesn't outperform the naïve model, it isn't adding predictive value.

