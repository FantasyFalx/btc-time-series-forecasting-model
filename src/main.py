"""Load the ARIMA model serialized from pipeline/model_training.ipynb."""

from pathlib import Path

import joblib

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "arima_btc.joblib"


if __name__ == "__main__":
    model = joblib.load(MODEL_PATH)
    print(f"Loaded serialized model from {MODEL_PATH}")
    print(type(model).__name__, model.model.order)
