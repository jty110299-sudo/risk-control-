from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def read_uploaded_csv(uploaded_file: Any) -> pd.DataFrame | None:
    if uploaded_file is None:
        return None
    try:
        return pd.read_csv(uploaded_file)
    except Exception:
        return None


def summarize_columns(dataframe: pd.DataFrame) -> list[dict[str, Any]]:
    summary: list[dict[str, Any]] = []
    for column in dataframe.columns:
        series = dataframe[column]
        summary.append(
            {
                "column": column,
                "dtype": str(series.dtype),
                "missing_count": int(series.isna().sum()),
                "missing_rate": round(float(series.isna().mean()), 4),
                "unique_count": int(series.nunique(dropna=True)),
            }
        )
    return summary


def compute_auc_ks(
    dataframe: pd.DataFrame,
    label_column: str,
    score_column: str,
    positive_label: int | float | str = 1,
    higher_score_means_higher_risk: bool = True,
) -> dict[str, Any]:
    working = dataframe[[label_column, score_column]].dropna().copy()
    if working.empty:
        return {"status": "error", "message": "标签列或 score 列没有可计算数据。"}

    working["_label"] = (working[label_column].astype(str) == str(positive_label)).astype(int)
    working["_score"] = pd.to_numeric(working[score_column], errors="coerce")
    working = working.dropna(subset=["_score"])
    if not higher_score_means_higher_risk:
        working["_score"] = -working["_score"]

    positive_count = int(working["_label"].sum())
    negative_count = int(len(working) - positive_count)
    if positive_count == 0 or negative_count == 0:
        return {
            "status": "error",
            "message": "AUC / KS 需要同时包含正样本和负样本。",
            "sample_count": int(len(working)),
            "positive_count": positive_count,
            "negative_count": negative_count,
        }

    ranks = working["_score"].rank(method="average")
    rank_sum_positive = float(ranks[working["_label"] == 1].sum())
    auc = (rank_sum_positive - positive_count * (positive_count + 1) / 2) / (positive_count * negative_count)

    sorted_frame = working.sort_values("_score", ascending=False)
    cumulative_positive = sorted_frame["_label"].cumsum() / positive_count
    cumulative_negative = (1 - sorted_frame["_label"]).cumsum() / negative_count
    ks = float(np.max(np.abs(cumulative_positive - cumulative_negative)))

    return {
        "status": "ok",
        "sample_count": int(len(working)),
        "positive_count": positive_count,
        "negative_count": negative_count,
        "auc": round(float(auc), 6),
        "ks": round(ks, 6),
        "label_column": label_column,
        "score_column": score_column,
        "positive_label": positive_label,
        "score_direction": "higher_score_means_higher_risk"
        if higher_score_means_higher_risk
        else "lower_score_means_higher_risk",
    }
