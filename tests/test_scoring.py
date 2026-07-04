import numpy as np
import pandas as pd

from risk_control_agent.scoring import assign_risk_band, build_risk_score, score_dataset


class DummyModel:
    def predict_proba(self, X):
        probs = np.linspace(0.1, 0.9, len(X))
        return np.column_stack([1 - probs, probs])


def test_risk_score_range():
    scores = build_risk_score(np.array([0.0, 0.5, 1.0]))
    assert scores.min() >= 0
    assert scores.max() <= 1000


def test_risk_band_assignment():
    assert assign_risk_band(900) == "低风险"
    assert assign_risk_band(200) == "高风险"


def test_score_dataset_outputs_columns():
    df = pd.DataFrame({"x": [1, 2, 3]})
    scored = score_dataset(DummyModel(), df, ["x"])
    assert {"predicted_probability", "risk_score", "risk_band", "risk_rank"}.issubset(scored.columns)
