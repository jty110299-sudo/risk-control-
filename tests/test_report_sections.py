from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.report_sections import (
    render_executive_summary,
    render_human_confirmation_items,
    render_overall_risk_level,
    render_root_cause_findings,
    render_triggered_alert_rules,
)


def test_executive_summary_missing_input_not_available():
    assert "Not available" in render_executive_summary()


def test_overall_risk_level_renders_level():
    text = render_overall_risk_level({"overall_risk_level": "Level 2"})
    assert "Level 2" in text


def test_triggered_alert_rules_renders_rule_id():
    text = render_triggered_alert_rules({"triggered_alerts": [{"rule_id": "R1"}]})
    assert "R1" in text


def test_root_cause_findings_uses_investigation_language():
    text = render_root_cause_findings({"metric_change_findings": [{"metric": "x", "change": 1}]})
    assert "not causal proof" in text


def test_human_confirmation_items_detects_required():
    text = render_human_confirmation_items(
        {"triggered_alerts": [{"rule_id": "R1", "human_confirmation_required": True}]}
    )
    assert "human confirmation" in text.lower()

