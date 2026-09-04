# Bitcoin Time Series Analysis ML Project (High Level)

## Description: 
- Planning document for the BTC time series analysis model.

## Steps: 
1. Determine the optimal time series granularity to model (Done). 
    - Options considered: Minute, hour, day, week, month, and yearly.
    - 1.1. Examine BTC charts to assess forecastability for a starter project (Done).
    - 1.2. After exploration, select base time series data for training.
        - Outcome: Daily Data selected for short-term forecasting.
2. Select a source for BTC price data.
    - 2.1. Use AI or manual search to identify 3 potential data sources providing BTC daily price up to the present date. (Done)
    - 2.2. Evaluate these sources to determine ease of integration.
    - 2.3. Choose the best data source and obtain the data via API or CSV download to the data folder. (Done)
3. Explore and visualize the time series data to identify noise, trend, seasonal, and cyclical components. (IP)
    - 3.1: Write planning document for cleaning and visulization.   
    - 3.3: Execute the planning document. 
    - 3.4: Analyze visulizations to determine what model will need to be used. 
    - 3.5: Choose model. 
4. Train the selected model—SARIMA, ARIMA, or exponential smoothing—based on exploratory analysis.
5. Validate the model with historical backtesting to assess loss function performance.
6. Iterate training and validation (steps 4 and 5) until the desired loss threshold is achieved.
7. Package and deploy the finalized model to a cloud environment.
8. Run the model on live data to evaluate real-world accuracy.
9. Create comprehensive documentation (README), and publish the project to GitHub, Discord channels, and LinkedIn for public showcasing.
10. Prepare and distribute the model for public download.

## Output: 
- A time series model trained to forecast Bitcoin price data.

