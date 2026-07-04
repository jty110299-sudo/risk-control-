from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


SAFETY_NOTE = "归因结果是排查线索，不是因果证明；最终结论需要人工确认。"


def get_global_feature_importance(model: Any, feature_names: list[str] | None = None) -> pd.DataFrame:
    if model is None:
        return pd.DataFrame(columns=["feature", "importance", "direction"])
    estimator = _get_estimator(model)
    names = feature_names or _get_feature_names(model)
    if hasattr(estimator, "coef_"):
        return get_logistic_regression_coefficients(model, names)
    if hasattr(estimator, "feature_importances_"):
        return get_tree_feature_importance(model, names)
    return pd.DataFrame(columns=["feature", "importance", "direction"])


def get_logistic_regression_coefficients(model: Any, feature_names: list[str] | None = None) -> pd.DataFrame:
    estimator = _get_estimator(model)
    coefficients = np.ravel(getattr(estimator, "coef_", []))
    names = feature_names or _get_feature_names(model)
    names = _align_names(names, len(coefficients))
    frame = pd.DataFrame({"feature": names, "importance": np.abs(coefficients), "coefficient": coefficients})
    frame["direction"] = frame["coefficient"].apply(lambda value: "风险升高" if value > 0 else "风险降低")
    return frame.sort_values("importance", ascending=False).reset_index(drop=True)


def get_tree_feature_importance(model: Any, feature_names: list[str] | None = None) -> pd.DataFrame:
    estimator = _get_estimator(model)
    importances = np.ravel(getattr(estimator, "feature_importances_", []))
    names = _align_names(feature_names or _get_feature_names(model), len(importances))
    frame = pd.DataFrame({"feature": names, "importance": importances, "direction": "模型重要性"})
    return frame.sort_values("importance", ascending=False).reset_index(drop=True)


def generate_reason_codes_for_record(
    model: Any,
    record: pd.Series | dict[str, Any],
    reference_df: pd.DataFrame,
    top_n: int = 5,
) -> list[dict[str, Any]]:
    record_series = pd.Series(record)
    numeric_cols = reference_df.select_dtypes(include=["number"]).columns
    importances = get_global_feature_importance(model)
    importance_map = dict(zip(importances["feature"], importances["importance"])) if not importances.empty else {}
    reasons: list[dict[str, Any]] = []
    for column in numeric_cols:
        if column not in record_series or pd.isna(record_series[column]):
            continue
        mean_value = reference_df[column].mean()
        std_value = reference_df[column].std() or 1
        z_score = abs(float(record_series[column] - mean_value) / std_value)
        weight = max([importance for feature, importance in importance_map.items() if feature.endswith(str(column))] or [1.0])
        reasons.append(
            {
                "feature": column,
                "record_value": float(record_series[column]),
                "reference_mean": float(mean_value),
                "reason_strength": round(float(z_score * weight), 6),
                "note": "与总体均值差异较大，结合模型重要性作为 reason code 线索。",
            }
        )
    return sorted(reasons, key=lambda item: item["reason_strength"], reverse=True)[:top_n]


def build_segment_risk_summary(
    df: pd.DataFrame,
    segment_col: str,
    score_col: str = "risk_score",
    target_col: str | None = None,
) -> pd.DataFrame:
    if segment_col not in df.columns or score_col not in df.columns:
        return pd.DataFrame()
    high_risk = df[score_col] < 350
    working = df.copy()
    working["_high_risk"] = high_risk.astype(int)
    aggregations = {
        "sample_count": (segment_col, "count"),
        "avg_risk_score": (score_col, "mean"),
        "high_risk_ratio": ("_high_risk", "mean"),
    }
    if target_col and target_col in df.columns:
        aggregations["bad_rate"] = (target_col, "mean")
    summary = working.groupby(segment_col, dropna=False).agg(**aggregations).reset_index()
    overall_score = df[score_col].mean()
    summary["score_gap_vs_overall"] = summary["avg_risk_score"] - overall_score
    return summary.sort_values(["high_risk_ratio", "sample_count"], ascending=[False, False]).reset_index(drop=True)


def rank_risky_segments(segment_summary: pd.DataFrame) -> pd.DataFrame:
    if segment_summary.empty:
        return segment_summary
    return segment_summary.sort_values(["high_risk_ratio", "sample_count"], ascending=[False, False]).reset_index(drop=True)


def build_attribution_summary(
    model: Any,
    scored_df: pd.DataFrame,
    target_col: str | None = None,
    segment_col: str | None = None,
) -> dict[str, Any]:
    global_importance = get_global_feature_importance(model).head(15)
    segment_summary = build_segment_risk_summary(scored_df, segment_col, target_col=target_col) if segment_col else pd.DataFrame()
    return {
        "global_feature_importance": global_importance.to_dict("records"),
        "segment_summary": segment_summary.to_dict("records"),
        "safety_note": SAFETY_NOTE,
    }


def _get_estimator(model: Any) -> Any:
    return model.named_steps["model"] if hasattr(model, "named_steps") and "model" in model.named_steps else model


def _get_feature_names(model: Any) -> list[str]:
    try:
        preprocessor = model.named_steps["preprocess"]
        return preprocessor.get_feature_names_out().tolist()
    except Exception:
        return []


def _align_names(names: list[str], length: int) -> list[str]:
    if len(names) == length:
        return names
    return [f"feature_{index}" for index in range(length)]
