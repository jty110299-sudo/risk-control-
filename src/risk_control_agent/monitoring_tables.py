from typing import Dict, Iterable

import pandas as pd


def _mapping(config: Dict | None) -> Dict[str, str]:
    if not config:
        return {
            "loan_id": "loan_id",
            "reporting_period": "reporting_period",
            "delinquency_status": "current_loan_delinquency_status",
        }
    return {
        "loan_id": config.get("loan_id", "loan_id"),
        "reporting_period": config.get("reporting_period", "reporting_period"),
        "delinquency_status": config.get(
            "delinquency_status", "current_loan_delinquency_status"
        ),
    }


def _validate_performance_columns(df: pd.DataFrame, config: Dict | None = None) -> Dict[str, str]:
    columns = _mapping(config)
    missing = [value for value in columns.values() if value not in df.columns]
    if missing:
        raise ValueError(
            "Missing required performance columns for monitoring table construction: "
            + ", ".join(missing)
        )
    return columns


def build_daily_risk_metrics_from_performance(
    df: pd.DataFrame, config: Dict | None = None
) -> pd.DataFrame:
    """Build the first minimal period-level risk monitoring table.

    This logic must be verified against the official data dictionary before
    production-like use. Delinquency is currently treated as status > 0, and
    serious delinquency is treated as status >= 3, both as candidate MVP logic.
    """
    if df.empty:
        return pd.DataFrame()
    columns = _validate_performance_columns(df, config)
    work = df[[columns["loan_id"], columns["reporting_period"], columns["delinquency_status"]]].copy()
    work["_delinquency_status_numeric"] = pd.to_numeric(
        work[columns["delinquency_status"]], errors="coerce"
    ).fillna(0)
    grouped = work.groupby(columns["reporting_period"], dropna=False)
    result = grouped.agg(
        observed_loan_count=(columns["loan_id"], "nunique"),
        delinquent_loan_count=("_delinquency_status_numeric", lambda series: int((series > 0).sum())),
        serious_delinquent_loan_count=(
            "_delinquency_status_numeric",
            lambda series: int((series >= 3).sum()),
        ),
    ).reset_index()
    result = result.rename(columns={columns["reporting_period"]: "monitoring_period"})
    result["delinquency_rate"] = (
        result["delinquent_loan_count"] / result["observed_loan_count"]
    )
    result["serious_delinquency_rate"] = (
        result["serious_delinquent_loan_count"] / result["observed_loan_count"]
    )
    return result[
        [
            "monitoring_period",
            "observed_loan_count",
            "delinquent_loan_count",
            "delinquency_rate",
            "serious_delinquent_loan_count",
            "serious_delinquency_rate",
        ]
    ]


def build_segment_risk_metrics_from_performance(
    df: pd.DataFrame, segment_columns: Iterable[str], config: Dict | None = None
) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    columns = _validate_performance_columns(df, config)
    segment_columns = list(segment_columns)
    missing_segments = [column for column in segment_columns if column not in df.columns]
    if missing_segments:
        raise ValueError(f"Missing segment columns: {', '.join(missing_segments)}")
    outputs = []
    for segment_column in segment_columns:
        work = df[
            [
                columns["loan_id"],
                columns["reporting_period"],
                columns["delinquency_status"],
                segment_column,
            ]
        ].copy()
        work["_delinquency_status_numeric"] = pd.to_numeric(
            work[columns["delinquency_status"]], errors="coerce"
        ).fillna(0)
        grouped = work.groupby([columns["reporting_period"], segment_column], dropna=False)
        result = grouped.agg(
            observed_loan_count=(columns["loan_id"], "nunique"),
            delinquent_loan_count=("_delinquency_status_numeric", lambda series: int((series > 0).sum())),
        ).reset_index()
        result = result.rename(
            columns={
                columns["reporting_period"]: "monitoring_period",
                segment_column: "segment_value",
            }
        )
        result.insert(1, "segment_type", segment_column)
        result["delinquency_rate"] = result["delinquent_loan_count"] / result["observed_loan_count"]
        outputs.append(result)
    return pd.concat(outputs, ignore_index=True) if outputs else pd.DataFrame()


def build_score_distribution_placeholder(df: pd.DataFrame, config: Dict | None = None) -> pd.DataFrame:
    return pd.DataFrame()


def build_model_monitoring_placeholder(df: pd.DataFrame, config: Dict | None = None) -> pd.DataFrame:
    return pd.DataFrame()


def build_feature_drift_placeholder(df: pd.DataFrame, config: Dict | None = None) -> pd.DataFrame:
    return pd.DataFrame()


def build_strategy_rule_placeholder(df: pd.DataFrame, config: Dict | None = None) -> pd.DataFrame:
    return pd.DataFrame()

