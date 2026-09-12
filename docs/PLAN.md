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
3. Explore and visualize the time series data to identify noise, trend, seasonal, and cyclical components. (Done)
    - 3.1: Write planning document for cleaning and visulization. (Done)   
    - 3.3: Execute the planning document. (Done)
    - 3.4: Analyze visulizations to determine what model will need to be used. (Done) 
    - 3.5: Choose model. (Done)
4. Train the selected model—SARIMA, ARIMA, or exponential smoothing—based on exploratory analysis. (Done)
5. Validate the model with historical backtesting to assess loss function performance. (Done)
6. Iterate training and validation (steps 4 and 5) until the desired losls threshold is achieved. (Done)
7. Deploy the finalized model. .(IP) 
    7.1: Ask ai what packages could be used to serialize the ml model. (IP)
        - Selected job lib packaging. 
    7.2: Use package to seriazlize the model. (Done)
        - Create a prompt md file that directs agent to serialize the model 
        and prep it for deployment. (Done) 
    7.3: Run a test forecast of the serialized model. (Done) 
    7.4: Deploy the model. ()
## Remove this item. 
9. Create comprehensive documentation (README), and publish the project to GitHub, Discord channels, and LinkedIn for public showcasing.
10. Prepare and distribute the model for public download.

## Output: 
- A time series model trained to forecast Bitcoin price data.

