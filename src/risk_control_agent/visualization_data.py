from __future__ import annotations

import pandas as pd


def get_numeric_distribution(df: pd.DataFrame, column: str) -> pd.DataFrame:
    values = pd.to_numeric(df[column], errors="coerce").dropna()
    return pd.DataFrame({"value": values})


def get_categorical_top_values(df: pd.DataFrame, column: str, top_n: int = 10) -> pd.DataFrame:
    return (
        df[column]
        .astype("object")
        .fillna("缺失")
        .value_counts()
        .head(top_n)
        .rename_axis(column)
        .reset_index(name="count")
    )


def get_missing_rate_ranking(df: pd.DataFrame) -> pd.DataFrame:
    return (
        pd.DataFrame({"column": df.columns, "missing_rate": [float(df[col].isna().mean()) for col in df.columns]})
        .sort_values("missing_rate", ascending=False)
        .reset_index(drop=True)
    )


def get_risk_band_summary(df: pd.DataFrame) -> pd.DataFrame:
    if "risk_band" not in df.columns:
        return pd.DataFrame(columns=["risk_band", "count", "ratio"])
    summary = df["risk_band"].value_counts().rename_axis("risk_band").reset_index(name="count")
    summary["ratio"] = summary["count"] / len(df)
    return summary


def get_score_distribution(df: pd.DataFrame) -> pd.DataFrame:
    if "risk_score" not in df.columns:
        return pd.DataFrame(columns=["risk_score"])
    return pd.DataFrame({"risk_score": pd.to_numeric(df["risk_score"], errors="coerce").dropna()})


def get_target_by_risk_band(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    if "risk_band" not in df.columns or target_col not in df.columns:
        return pd.DataFrame(columns=["risk_band", "sample_count", "bad_rate"])
    return (
        df.groupby("risk_band", dropna=False)[target_col]
        .agg(sample_count="count", bad_rate="mean")
        .reset_index()
    )
