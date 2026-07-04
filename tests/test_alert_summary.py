from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.alert_summary import build_alert_summary, determine_overall_risk_level


def test_determine_overall_risk_level_returns_highest():
    alerts = [{"risk_level": "Level 1"}, {"risk_level": "Level 3"}]
    assert determine_overall_risk_level(alerts) == "Level 3"


def test_build_alert_summary_counts_alerts():
    summary = build_alert_summary([{"risk_level": "Level 2"}])
    assert summary["alert_count"] == 1


def test_high_risk_requires_human_confirmation():
    summary = build_alert_summary([{"risk_level": "Level 3"}])
    assert summary["human_confirmation_required"] is True


def test_safety_note_exists():
    summary = build_alert_summary([])
    assert "safety_note" in summary

