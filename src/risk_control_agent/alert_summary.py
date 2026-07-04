import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List

from risk_control_agent.risk_levels import get_max_risk_level, is_high_risk


PROJECT_PHASE = "Phase 6 - Risk Metric Calculation and Alert Rule Engine"
SAFETY_NOTE = (
    "Risk Control Agent provides monitoring and analysis support only. "
    "Final decisions require human review and approval."
)


def summarize_alert_counts(triggered_alerts: Iterable[dict]) -> dict:
    """Count triggered alerts by risk level."""
    counts = {}
    for alert in triggered_alerts:
        level = alert.get("risk_level", "Level 0")
        counts[level] = counts.get(level, 0) + 1
    return counts


def determine_overall_risk_level(triggered_alerts: Iterable[dict]) -> str:
    """Determine the maximum risk level among triggered alerts."""
    levels = [alert.get("risk_level", "Level 0") for alert in triggered_alerts]
    return get_max_risk_level(levels)


def build_alert_summary(triggered_alerts: List[dict], warnings: List[str] | None = None) -> dict:
    """Build a structured alert summary."""
    overall_risk_level = determine_overall_risk_level(triggered_alerts)
    return {
        "project_phase": PROJECT_PHASE,
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "overall_risk_level": overall_risk_level,
        "alert_count": len(triggered_alerts),
        "alert_count_by_level": summarize_alert_counts(triggered_alerts),
        "human_confirmation_required": any(
            alert.get("human_confirmation_required", False) or is_high_risk(alert.get("risk_level", "Level 0"))
            for alert in triggered_alerts
        ),
        "triggered_alerts": triggered_alerts,
        "warnings": warnings or [],
        "safety_note": SAFETY_NOTE,
    }


def save_alert_summary(summary: dict, output_path: str | Path) -> Path:
    """Save alert summary JSON."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2, ensure_ascii=False)
    return path

