from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.alert_rules import (
    evaluate_absolute_threshold,
    evaluate_operator,
    evaluate_relative_change_from_baseline,
    filter_active_mvp_rules,
)


def test_evaluate_operator_supported_ops():
    assert evaluate_operator(2, ">=", 2)
    assert evaluate_operator(3, ">", 2)
    assert evaluate_operator(1, "<=", 1)
    assert evaluate_operator(1, "<", 2)
    assert evaluate_operator(2, "==", 2)
    assert evaluate_operator(2, "=", 2)
    assert evaluate_operator(2, "!=", 3)


def test_absolute_threshold_triggers():
    row = pd.Series({"monitoring_period": "2024-01", "delinquency_rate": 0.06})
    rule = {
        "rule_id": "R1",
        "rule_name": "test",
        "metric": "delinquency_rate",
        "condition_type": "absolute_threshold",
        "operator": ">=",
        "threshold": 0.05,
        "risk_level": "Level 2",
    }
    assert evaluate_absolute_threshold(row, rule)["triggered"] is True


def test_relative_change_from_baseline_triggers():
    row = pd.Series({"monitoring_period": "2024-01", "metric_relative_change_from_baseline": 0.25})
    rule = {
        "rule_id": "R2",
        "rule_name": "test",
        "metric": "metric",
        "condition_type": "relative_change_from_baseline",
        "operator": ">=",
        "threshold": 0.2,
        "risk_level": "Level 2",
    }
    assert evaluate_relative_change_from_baseline(row, rule)["triggered"] is True


def test_future_not_active_is_filtered_out():
    rules = [{"mvp_applicability": "active_mvp"}, {"mvp_applicability": "future_not_active"}]
    assert len(filter_active_mvp_rules(rules)) == 1


def test_missing_metric_does_not_crash():
    row = pd.Series({"monitoring_period": "2024-01"})
    rule = {"rule_id": "R3", "metric": "missing", "operator": ">=", "threshold": 1}
    result = evaluate_absolute_threshold(row, rule)
    assert result["triggered"] is False
    assert "warning" in result

