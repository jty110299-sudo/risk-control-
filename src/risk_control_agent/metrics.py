from typing import Iterable

import numpy as np
import pandas as pd


def safe_divide(numerator, denominator):
    """Divide safely and return numpy.nan when denominator is zero or missing."""
    if denominator is None or pd.isna(denominator) or denominator == 0:
        return np.nan
    return numerator / denominator


def calculate_rate(numerator, denominator):
    """Calculate a rate with zero-denominator protection."""
    return safe_divide(numerator, denominator)


def calculate_absolute_change(current, baseline):
    """Calculate current minus baseline."""
    if pd.isna(current) or pd.isna(baseline):
        return np.nan
    return current - baseline


def calculate_relative_change(current, baseline):
    """Calculate relative change from baseline with zero-denominator protection."""
    if pd.isna(current) or pd.isna(baseline):
        return np.nan
    return safe_divide(current - baseline, baseline)


def validate_metric_columns(df: pd.DataFrame, metric_cols: Iterable[str]) -> dict:
    """Validate that metric columns exist in a DataFrame."""
    missing = [column for column in metric_cols if column not in df.columns]
    return {
        "passed": not missing,
        "errors": [f"Missing metric columns: {', '.join(missing)}"] if missing else [],
        "warnings": [],
    }


def calculate_period_over_period_change(
    df: pd.DataFrame, period_col: str, metric_cols: Iterable[str]
) -> pd.DataFrame:
    """Add period-over-period absolute and relative change columns."""
    validation = validate_metric_columns(df, metric_cols)
    if not validation["passed"]:
        raise ValueError(validation["errors"][0])
    if period_col not in df.columns:
        raise ValueError(f"Missing period column: {period_col}")

    result = df.sort_values(period_col).copy()
    for metric in metric_cols:
        previous = result[metric].shift(1)
        result[f"{metric}_previous_period"] = previous
        result[f"{metric}_absolute_change"] = result[metric] - previous
        result[f"{metric}_relative_change"] = [
            calculate_relative_change(current, baseline)
            for current, baseline in zip(result[metric], previous)
        ]
    return result


def calculate_baseline_average(
    df: pd.DataFrame, metric_cols: Iterable[str], window: int = 3
) -> pd.DataFrame:
    """Add shifted rolling baseline average columns for selected metrics."""
    validation = validate_metric_columns(df, metric_cols)
    if not validation["passed"]:
        raise ValueError(validation["errors"][0])
    result = df.copy()
    for metric in metric_cols:
        result[f"{metric}_baseline_average"] = result[metric].shift(1).rolling(window=window).mean()
    return result


def add_baseline_comparison(
    df: pd.DataFrame, metric_cols: Iterable[str], baseline_window: int = 3
) -> pd.DataFrame:
    """Add baseline average, absolute change, and relative change columns."""
    result = calculate_baseline_average(df, metric_cols, window=baseline_window)
    for metric in metric_cols:
        baseline_col = f"{metric}_baseline_average"
        result[f"{metric}_absolute_change_from_baseline"] = result[metric] - result[baseline_col]
        result[f"{metric}_relative_change_from_baseline"] = [
            calculate_relative_change(current, baseline)
            for current, baseline in zip(result[metric], result[baseline_col])
        ]
    return result

