from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.recommendations import (
    build_operations_recommendations,
    filter_prohibited_recommendations,
    get_recommendations_by_risk_level,
)


RULES = {
    "recommendations_by_risk_level": {
        "Level 2": ["Conduct manual investigation on triggered metrics and related segments."],
        "Level 3": ["Start focused review. Human confirmation is required before any operational change."],
    },
    "recommendations_by_alert_type": {"delinquency_rate": ["Review delinquency movement."]},
    "prohibited_recommendations": ["automatically reject", "automatically reduce credit", "automatically close"],
}


def test_get_recommendations_by_risk_level_level2():
    assert get_recommendations_by_risk_level("Level 2", RULES)


def test_level3_recommendation_contains_human_confirmation():
    recs = build_operations_recommendations({"overall_risk_level": "Level 3"}, rules_config=RULES)
    assert any(item["human_confirmation_required"] for item in recs)


def test_filter_prohibited_recommendations():
    recs = ["Automatically reject users.", "Review abnormal segments."]
    assert filter_prohibited_recommendations(recs, RULES) == ["Review abnormal segments."]


def test_build_operations_recommendations_from_alert_summary():
    recs = build_operations_recommendations(
        {"overall_risk_level": "Level 2", "triggered_alerts": [{"metric": "delinquency_rate"}]},
        rules_config=RULES,
    )
    assert recs


def test_no_input_returns_cautious_recommendation():
    recs = build_operations_recommendations(rules_config=RULES)
    assert "Continue monitoring" in recs[0]["recommendation"]

