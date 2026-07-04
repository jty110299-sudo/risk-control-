from pathlib import Path
from typing import Any, Dict

import pandas as pd

from risk_control_agent.config import load_yaml_config
from risk_control_agent.contribution_analysis import (
    calculate_segment_contribution,
    rank_top_contributors,
    validate_contribution_input,
)


SAFETY_NOTE = (
    "Root cause findings are investigation leads, not causal proof. "
    "Final decisions require human review and approval."
)


def load_root_cause_config(config_path: str | Path) -> Dict[str, Any]:
    """Load root cause configuration."""
    return load_yaml_config(config_path)


def validate_root_cause_inputs(daily_df=None, segment_df=None, alert_summary=None) -> dict:
    """Validate which root cause inputs are available."""
    return {
        "daily_df": daily_df is not None and not getattr(daily_df, "empty", True),
        "segment_df": segment_df is not None and not getattr(segment_df, "empty", True),
        "alert_summary": bool(alert_summary),
    }


def generate_metric_change_findings(daily_df: pd.DataFrame, config: Dict[str, Any]) -> list:
    """Generate simple metric change findings from the latest available periods."""
    if daily_df is None or daily_df.empty:
        return []
    period_col = config.get("period_column", "monitoring_period")
    target_metrics = config.get("target_metrics", {})
    metrics = [
        target_metrics.get("primary_rate_metric", "delinquency_rate"),
        target_metrics.get("serious_rate_metric", "serious_delinquency_rate"),
    ]
    available_metrics = [metric for metric in metrics if metric in daily_df.columns]
    if period_col not in daily_df.columns or not available_metrics:
        return []

    sorted_df = daily_df.sort_values(period_col)
    latest = sorted_df.iloc[-1]
    previous = sorted_df.iloc[-2] if len(sorted_df) >= 2 else None
    findings = []
    for metric in available_metrics:
        finding = {
            "metric": metric,
            "monitoring_period": latest.get(period_col),
            "current_value": latest.get(metric),
            "previous_value": previous.get(metric) if previous is not None else None,
            "change": (latest.get(metric) - previous.get(metric)) if previous is not None else None,
            "interpretation": "Metric change is a monitoring signal, not causal proof.",
        }
        findings.append(finding)
    return findings


def generate_segment_contribution_findings(segment_df: pd.DataFrame, config: Dict[str, Any]) -> dict:
    """Generate segment contribution findings from segment monitoring data."""
    if segment_df is None or segment_df.empty:
        return {"top_contributors": [], "warnings": ["Segment monitoring table is missing."]}

    period_col = config.get("period_column", "monitoring_period")
    segment_cfg = config.get("segment_columns", {})
    segment_cols = [segment_cfg.get("segment_type", "segment_type"), segment_cfg.get("segment_value", "segment_value")]
    target_metrics = config.get("target_metrics", {})
    count_metric = target_metrics.get("primary_count_metric", "delinquent_loan_count")
    rate_metric = target_metrics.get("primary_rate_metric", "delinquency_rate")
    required = [period_col] + segment_cols + [count_metric]
    validation = validate_contribution_input(segment_df, required)
    if not validation["passed"]:
        return {"top_contributors": [], "warnings": validation["errors"]}

    contribution = calculate_segment_contribution(
        segment_df,
        period_col=period_col,
        segment_cols=segment_cols,
        count_metric=count_metric,
        rate_metric=rate_metric if rate_metric in segment_df.columns else None,
    )
    top_n = config.get("contribution_settings", {}).get("top_n_segments", 5)
    top = rank_top_contributors(contribution, top_n=top_n)
    return {
        "top_contributors": top.to_dict(orient="records"),
        "warnings": sorted(set(str(value) for value in contribution.get("warning", []) if str(value))),
    }


def link_alerts_to_root_cause_hints(alert_summary: dict, contribution_findings=None) -> list:
    """Create alert-linked investigation hints without claiming causality."""
    if not alert_summary:
        return []
    hints = []
    for alert in alert_summary.get("triggered_alerts", []):
        hints.append(
            {
                "rule_id": alert.get("rule_id"),
                "metric": alert.get("metric"),
                "risk_level": alert.get("risk_level"),
                "hint": "Review related metric movement and segment contribution. This is not causal proof.",
                "human_confirmation_required": bool(alert.get("human_confirmation_required", False)),
            }
        )
    if contribution_findings and contribution_findings.get("top_contributors"):
        hints.append(
            {
                "rule_id": None,
                "metric": "segment_contribution",
                "risk_level": alert_summary.get("overall_risk_level", "Level 0"),
                "hint": "Top contributing segments may guide investigation priority.",
                "human_confirmation_required": False,
            }
        )
    return hints


def run_root_cause_analysis(daily_df=None, segment_df=None, alert_summary=None, config=None) -> dict:
    """Run the first root cause framework over available inputs."""
    config = config or {}
    available_inputs = validate_root_cause_inputs(daily_df, segment_df, alert_summary)
    warnings = []
    if not any(available_inputs.values()):
        return {
            "analysis_status": "skipped_no_input_data",
            "available_inputs": available_inputs,
            "metric_change_findings": [],
            "segment_contribution_findings": {"top_contributors": [], "warnings": []},
            "alert_linked_hints": [],
            "warnings": ["No daily, segment, or alert summary input was available."],
            "human_confirmation_required": False,
            "safety_note": SAFETY_NOTE,
        }

    metric_findings = generate_metric_change_findings(daily_df, config) if available_inputs["daily_df"] else []
    contribution_findings = (
        generate_segment_contribution_findings(segment_df, config)
        if available_inputs["segment_df"]
        else {"top_contributors": [], "warnings": ["Segment data unavailable; contribution analysis skipped."]}
    )
    warnings.extend(contribution_findings.get("warnings", []))
    alert_hints = link_alerts_to_root_cause_hints(alert_summary, contribution_findings)
    human_confirmation = any(hint.get("human_confirmation_required", False) for hint in alert_hints)
    return {
        "analysis_status": "completed_with_available_inputs",
        "available_inputs": available_inputs,
        "metric_change_findings": metric_findings,
        "segment_contribution_findings": contribution_findings,
        "alert_linked_hints": alert_hints,
        "warnings": warnings,
        "human_confirmation_required": human_confirmation,
        "safety_note": SAFETY_NOTE,
    }

