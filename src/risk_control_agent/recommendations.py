from pathlib import Path

from risk_control_agent.config import load_yaml_config


def load_recommendation_rules(config_path: str | Path) -> dict:
    """Load recommendation rules from YAML."""
    return load_yaml_config(config_path)


def get_recommendations_by_risk_level(overall_risk_level, rules_config) -> list:
    """Return configured recommendations for a risk level."""
    return list(rules_config.get("recommendations_by_risk_level", {}).get(overall_risk_level, []))


def get_recommendations_by_alerts(triggered_alerts, rules_config) -> list:
    """Return configured recommendations based on triggered alert metrics."""
    recommendations = []
    by_type = rules_config.get("recommendations_by_alert_type", {})
    for alert in triggered_alerts or []:
        recommendations.extend(by_type.get(alert.get("metric"), []))
    return recommendations


def filter_prohibited_recommendations(recommendations, rules_config) -> list:
    """Filter recommendations containing prohibited phrases."""
    prohibited = [phrase.lower() for phrase in rules_config.get("prohibited_recommendations", [])]
    allowed = []
    for recommendation in recommendations:
        lowered = recommendation.lower()
        if not any(phrase in lowered for phrase in prohibited):
            allowed.append(recommendation)
    return allowed


def mark_human_confirmation_required(recommendations, overall_risk_level=None) -> list:
    """Mark high-risk recommendations as requiring human confirmation."""
    high_risk = overall_risk_level in ("Level 3", "Level 4")
    marked = []
    for recommendation in recommendations:
        marked.append(
            {
                "recommendation": recommendation,
                "human_confirmation_required": high_risk or "human confirmation" in recommendation.lower(),
            }
        )
    return marked


def build_operations_recommendations(alert_summary=None, root_cause_summary=None, rules_config=None) -> list:
    """Build investigation-oriented operations recommendations."""
    rules_config = rules_config or {}
    if not alert_summary and not root_cause_summary:
        return [
            {
                "recommendation": "Continue monitoring when no alert or root cause evidence is available.",
                "human_confirmation_required": False,
            }
        ]
    overall_risk_level = (alert_summary or {}).get("overall_risk_level", "Level 0")
    recommendations = []
    recommendations.extend(get_recommendations_by_risk_level(overall_risk_level, rules_config))
    recommendations.extend(get_recommendations_by_alerts((alert_summary or {}).get("triggered_alerts", []), rules_config))
    if root_cause_summary and root_cause_summary.get("top_contributors"):
        recommendations.append("Review abnormal segments as investigation priorities, not causal proof.")
    recommendations = filter_prohibited_recommendations(recommendations, rules_config)
    return mark_human_confirmation_required(recommendations, overall_risk_level)

