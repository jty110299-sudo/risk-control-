from typing import Iterable

import pandas as pd


def check_missing_rate(df: pd.DataFrame) -> dict:
    if df.empty:
        return {}
    return {column: float(df[column].isna().mean()) for column in df.columns}


def check_row_count(df: pd.DataFrame) -> dict:
    return {"row_count": int(len(df))}


def check_column_count(df: pd.DataFrame) -> dict:
    return {"column_count": int(len(df.columns))}


def check_duplicate_count(df: pd.DataFrame, key_columns: Iterable[str]) -> dict:
    key_columns = list(key_columns)
    missing = [column for column in key_columns if column not in df.columns]
    if missing:
        return {"duplicate_count": None, "errors": [f"Missing key columns: {', '.join(missing)}"]}
    return {"duplicate_count": int(df.duplicated(subset=key_columns).sum()), "errors": []}


def generate_basic_quality_summary(df: pd.DataFrame, key_columns: Iterable[str] | None = None) -> dict:
    summary = {
        "row_count": check_row_count(df)["row_count"],
        "column_count": check_column_count(df)["column_count"],
        "missing_rate": check_missing_rate(df),
    }
    if key_columns:
        summary["duplicate_check"] = check_duplicate_count(df, key_columns)
    return summary

