from typing import Iterable, List

import pandas as pd


def _result(passed: bool, errors: List[str] | None = None, warnings: List[str] | None = None) -> dict:
    return {
        "passed": passed,
        "errors": errors or [],
        "warnings": warnings or [],
    }


def validate_required_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> dict:
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        return _result(False, [f"Missing required columns: {', '.join(missing)}"])
    return _result(True)


def validate_non_empty_dataframe(df: pd.DataFrame) -> dict:
    if df is None or df.empty:
        return _result(False, ["DataFrame is empty."])
    return _result(True)


def validate_date_or_period_column(df: pd.DataFrame, column_name: str) -> dict:
    if column_name not in df.columns:
        return _result(False, [f"Date or period column not found: {column_name}"])
    if df[column_name].isna().all():
        return _result(False, [f"Date or period column contains only missing values: {column_name}"])
    return _result(True)


def validate_numeric_columns(df: pd.DataFrame, numeric_columns: Iterable[str]) -> dict:
    errors = []
    for column in numeric_columns:
        if column not in df.columns:
            errors.append(f"Numeric column not found: {column}")
        elif not pd.api.types.is_numeric_dtype(df[column]):
            errors.append(f"Column is not numeric: {column}")
    return _result(not errors, errors)


def validate_no_duplicate_keys(df: pd.DataFrame, key_columns: Iterable[str]) -> dict:
    key_columns = list(key_columns)
    missing = [column for column in key_columns if column not in df.columns]
    if missing:
        return _result(False, [f"Duplicate key validation missing columns: {', '.join(missing)}"])
    duplicate_count = int(df.duplicated(subset=key_columns).sum())
    if duplicate_count:
        return _result(False, [f"Found {duplicate_count} duplicate key rows."])
    return _result(True)

