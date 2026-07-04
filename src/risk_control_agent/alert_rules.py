from pathlib import Path
from typing import Any, Dict, Iterable, List

import pandas as pd

from risk_control_agent.config import load_yaml_config


def load_alert_rules(config_path: str | Path) -> List[Dict[str, Any]]:
    """Load alert rules from YAML config."""
    config = load_yaml_config(config_path)
    rules = config.get("rules", [])
    if not isinstance(rules, list):
        raise ValueError("Alert rule config must contain a rules list.")
    return rules


def evaluate_operator(value, operator: str, threshold) -> bool:
    """Evaluate a simple comparison operator."""
    if pd.isna(value) or pd.isna(threshold):
        return False
    if operator == ">=":
        return value >= threshold
    if operator == ">":
        return value > threshold
    if operator == "<=":
        return value <= threshold
    if operator == "<":
        return value < threshold
    if operator in ("==", "="):
        return value == threshold
    if operator == "!=":
        return value != threshold
    raise ValueError(f"Unsupported operator: {operator}")


def _period_value(row: pd.Series):
    return row.get("monitoring_period", row.get("date", None))


def _alert_payload(row: pd.Series, rule: Dict[str, Any], observed_value, evidence: str) -> Dict[str, Any]:
    return {
        "rule_id": rule.get("rule_id"),
        "rule_name": rule.get("rule_name"),
        "metric": rule.get("metric"),
        "monitoring_period": _period_value(row),
        "observed_value": observed_value,
        "threshold": rule.get("threshold"),
        "condition_type": rule.get("condition_type"),
        "risk_level": rule.get("risk_level"),
        "human_confirmation_required": bool(rule.get("human_confirmation_required", False)),
        "evidence": evidence,
        "notes": rule.get("notes", ""),
    }


def evaluate_absolute_threshold(row: pd.Series, rule: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate an absolute threshold rule for one row."""
    metric = rule.get("metric")
    if metric not in row:
        return {"triggered": False, "warning": f"Metric missing for rule {rule.get('rule_id')}: {metric}"}
    value = row.get(metric)
    triggered = evaluate_operator(value, rule.get("operator"), rule.get("threshold"))
    return {
        "triggered": triggered,
        "alert": _alert_payload(row, rule, value, f"{metric}={value}") if triggered else None,
    }


def evaluate_relative_change_from_baseline(row: pd.Series, rule: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate a relative-change-from-baseline rule for one row."""
    metric = rule.get("metric")
    baseline_column = f"{metric}_relative_change_from_baseline"
    if baseline_column not in row:
        return {
            "triggered": False,
            "warning": f"Baseline comparison missing for rule {rule.get('rule_id')}: {baseline_column}",
        }
    value = row.get(baseline_column)
    triggered = evaluate_operator(value, rule.get("operator"), rule.get("threshold"))
    return {
        "triggered": triggered,
        "alert": _alert_payload(row, rule, value, f"{baseline_column}={value}") if triggered else None,
    }


def evaluate_rule(row: pd.Series, rule: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate one rule for one monitoring row."""
    if not rule.get("rule_id"):
        return {"triggered": False, "warning": "Rule missing rule_id."}
    condition_type = rule.get("condition_type")
    if condition_type == "absolute_threshold":
        return evaluate_absolute_threshold(row, rule)
    if condition_type == "relative_change_from_baseline":
        return evaluate_relative_change_from_baseline(row, rule)
    return {"triggered": False, "warning": f"Unsupported condition type: {condition_type}"}


def filter_active_mvp_rules(rules: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return only rules marked active for MVP."""
    return [rule for rule in rules if rule.get("mvp_applicability") == "active_mvp"]


def evaluate_rules_for_dataframe(df: pd.DataFrame, rules: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    """Evaluate active rules for all rows and collect alerts plus warnings."""
    triggered_alerts = []
    warnings = []
    for _, row in df.iterrows():
        for rule in rules:
            result = evaluate_rule(row, rule)
            if result.get("warning"):
                warnings.append(result["warning"])
            if result.get("triggered") and result.get("alert"):
                triggered_alerts.append(result["alert"])
    return {"triggered_alerts": triggered_alerts, "warnings": warnings}


def generate_triggered_alerts(df: pd.DataFrame, rules: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    """Filter active MVP rules and evaluate them against a monitoring table."""
    active_rules = filter_active_mvp_rules(rules)
    return evaluate_rules_for_dataframe(df, active_rules)

