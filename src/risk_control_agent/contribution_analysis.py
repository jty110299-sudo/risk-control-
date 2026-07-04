from typing import Iterable, List

import numpy as np
import pandas as pd


def calculate_metric_change(current_value, baseline_value):
    """Calculate current value minus baseline value."""
    if pd.isna(current_value) or pd.isna(baseline_value):
        return np.nan
    return current_value - baseline_value


def calculate_count_increase(current_count, baseline_count):
    """Calculate count increase from baseline to current."""
    return calculate_metric_change(current_count, baseline_count)


def calculate_contribution_share(segment_increase, total_increase):
    """Calculate segment contribution share.

    Returns numpy.nan when total increase is zero or negative. Contribution
    share is an investigation signal, not causal proof.
    """
    if pd.isna(segment_increase) or pd.isna(total_increase) or total_increase <= 0:
        return np.nan
    return segment_increase / total_increase


def validate_contribution_input(df: pd.DataFrame, required_columns: Iterable[str]) -> dict:
    """Validate required columns for contribution analysis."""
    missing = [column for column in required_columns if column not in df.columns]
    return {
        "passed": not missing,
        "errors": [f"Missing required contribution columns: {', '.join(missing)}"] if missing else [],
        "warnings": [],
    }


def build_segment_baseline(
    df: pd.DataFrame,
    period_col: str,
    segment_cols: Iterable[str],
    metric_cols: Iterable[str],
    baseline_periods: Iterable | None = None,
) -> pd.DataFrame:
    """Build baseline metric averages by segment."""
    segment_cols = list(segment_cols)
    metric_cols = list(metric_cols)
    required = [period_col] + segment_cols + metric_cols
    validation = validate_contribution_input(df, required)
    if not validation["passed"]:
        raise ValueError(validation["errors"][0])

    baseline_df = df.copy()
    if baseline_periods is not None:
        baseline_df = baseline_df[baseline_df[period_col].isin(list(baseline_periods))]
    if baseline_df.empty:
        return pd.DataFrame(columns=segment_cols + [f"{metric}_baseline" for metric in metric_cols])

    result = baseline_df.groupby(segment_cols, dropna=False)[metric_cols].mean().reset_index()
    return result.rename(columns={metric: f"{metric}_baseline" for metric in metric_cols})


def calculate_segment_contribution(
    df: pd.DataFrame,
    period_col: str,
    segment_cols: Iterable[str],
    count_metric: str,
    rate_metric: str | None = None,
    baseline_periods: Iterable | None = None,
    current_period=None,
) -> pd.DataFrame:
    """Calculate segment count increase and contribution share.

    Positive segment increases are used by default. If total positive increase
    is zero or negative, contribution_share is returned as numpy.nan.
    """
    segment_cols = list(segment_cols)
    metric_cols: List[str] = [count_metric] + ([rate_metric] if rate_metric else [])
    required = [period_col] + segment_cols + metric_cols
    validation = validate_contribution_input(df, required)
    if not validation["passed"]:
        raise ValueError(validation["errors"][0])
    if df.empty:
        return pd.DataFrame()

    if current_period is None:
        current_period = df[period_col].max()
    current_df = df[df[period_col] == current_period].copy()
    if current_df.empty:
        return pd.DataFrame()

    baseline = build_segment_baseline(df, period_col, segment_cols, metric_cols, baseline_periods)
    merged = current_df.merge(baseline, on=segment_cols, how="left")
    merged["segment_increase"] = merged[count_metric] - merged[f"{count_metric}_baseline"]
    if rate_metric:
        merged["segment_metric_change"] = merged[rate_metric] - merged[f"{rate_metric}_baseline"]
    else:
        merged["segment_metric_change"] = np.nan

    positive_increase = merged["segment_increase"].where(merged["segment_increase"] > 0, 0)
    total_increase = positive_increase.sum()
    if total_increase <= 0:
        merged["contribution_share"] = np.nan
        merged["warning"] = "Total positive increase is zero; contribution share is not meaningful."
    else:
        merged["contribution_share"] = [
            calculate_contribution_share(max(value, 0), total_increase)
            for value in merged["segment_increase"]
        ]
        merged["warning"] = ""

    merged["current_period"] = current_period
    merged["contribution_interpretation"] = (
        "Investigation signal only; not causal proof."
    )
    return merged


def rank_top_contributors(
    contribution_df: pd.DataFrame,
    contribution_col: str = "contribution_share",
    top_n: int = 5,
) -> pd.DataFrame:
    """Return top contributing segments by contribution share."""
    if contribution_df.empty or contribution_col not in contribution_df.columns:
        return pd.DataFrame()
    return (
        contribution_df.sort_values(contribution_col, ascending=False, na_position="last")
        .head(top_n)
        .reset_index(drop=True)
    )

