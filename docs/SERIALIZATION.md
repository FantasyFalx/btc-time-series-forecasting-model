**Task**
Serialize the already-trained ARIMA time series forecasting model in the Jupyter notebook using the `joblib` Python package.

**Context**

* `./pipeline/model_training.ipynb`
* `./src/main.py`
* `pyproject.toml`

**Constraints**

* Do not read files outside the context list.
* Do not generate unnecessary code or unneeded library imports.
* Do not retrain the model in `./src/main.py`.
* Do not create cloud resources or deployment environments.
* Do not generate Dockerfiles.

**Directions**

1. Read the files specified in the context path.
2. In `./pipeline/model_training.ipynb`, add a `joblib` import and serialize the already-trained `full_model` in the Model Serialization cell.
3. Create a `prod_model` directory and save the serialized model within it.
4. Run the notebook serialization cell to dump the in-memory trained model.
5. Retry steps 2–4 if errors occur, notifying the user if failures exceed three attempts.
6. In `./src/main.py`, load the serialized model from `prod_model` with `joblib.load`. Do not refit ARIMA.

**Output**

* Deployment-ready BTC time series forecasting model.
