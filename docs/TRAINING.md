## Task
Create code to train and validate an ARIMA model on BTC year-over-year price 
data with the minimal amount of loss while avoiding high bias. 
## Context
- Notebook: `./pipeline/model_training.ipynb`
- Train/test split:
  - 75% for training
  - 25% for validation
- Model type: ARIMA
- Data: Time series BTC daily price data
- Read the top-line comments in each cell to understand what code blocks are required.

## Do Not
- Read any file sources besides the notebook path.
- Import unnecessary libraries that contain other time series models.
- Output code under the serialization markdown header. 

## Directions
1. Read over the notebook structure to determine the stages already completed for model development.
2. Identify code cells and markdown headers to understand where to generate code for model training/ validation.
3. Extract the training/validation split from the base dataset stored in the notebook.
4. Difference the training data in its respective cell.
5. Insert code for user for matplotlib and seaborn to generate ACF/PACF plots so the developer can see which hyperparameters to use.
6. Insert code for the user to train the model in its respective cell.
7. Output code in a cell for the user to run a forecast.
8. Insert code that plots the original time series against the forecasted data. Original data should be blue; forecasted data should be orange.
9. Inserts code that outputs the loss functions of the trained model on the validation set.

## Output
Cleanly structured code cells that allow a developer to train and retrain a model after the initial training and validation steps.