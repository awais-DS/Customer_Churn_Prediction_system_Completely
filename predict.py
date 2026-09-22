from pathlib import Path
import joblib
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "model.pkl"
model = joblib.load(MODEL_PATH)

def predict(inp: dict):
    df = pd.DataFrame([inp])
    label = int(model.predict(df)[0])              # 1 = churn, 0 = stay
    score = float(model.predict_proba(df)[0, 1])   # churn risk score
    return label, score