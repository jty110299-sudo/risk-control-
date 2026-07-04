from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


RISK_BAND_ORDER = ["低风险", "中低风险", "中风险", "中高风险", "高风险"]


def generate_predicted_probability(model: Any, df: pd.DataFrame, feature_cols: list[str]) -> np.ndarray:
    if model is None:
        raise ValueError("没有可用模型，请先训练模型。")
    return model.predict_proba(df[feature_cols])[:, 1]


def build_risk_score(probability: float | pd.Series | np.ndarray) -> Any:
    score = np.round((1 - np.asarray(probability)) * 1000).astype(int)
    return int(score) if np.ndim(score) == 0 else score


def assign_risk_band(score: int | float) -> str:
    if score >= 800:
        return "低风险"
    if score >= 650:
        return "中低风险"
    if score >= 500:
        return "中风险"
    if score >= 350:
        return "中高风险"
    return "高风险"


def score_dataset(model: Any, df: pd.DataFrame, feature_cols: list[str]) -> pd.DataFrame:
    probability = generate_predicted_probability(model, df, feature_cols)
    scored = df.copy()
    scored["predicted_probability"] = probability
    scored["risk_score"] = build_risk_score(probability)
    scored["risk_band"] = scored["risk_score"].apply(assign_risk_band)
    scored["risk_rank"] = scored["predicted_probability"].rank(method="first", ascending=False).astype(int)
    return scored


def save_scored_dataset(scored_df: pd.DataFrame, path: str | Path) -> Path:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    scored_df.to_csv(output_path, index=False, encoding="utf-8-sig")
    return output_path
