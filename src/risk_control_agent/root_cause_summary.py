import json
from datetime import datetime, timezone
from pathlib import Path

from risk_control_agent.root_cause import SAFETY_NOTE


PROJECT_PHASE = "Phase 7 - Root Cause Analysis and Segment Contribution Engine"


def summarize_top_contributors(contribution_findings, top_n: int = 5) -> list:
    """Extract top contributors from contribution findings."""
    if not contribution_findings:
        return []
    contributors = contribution_findings.get("top_contributors", [])
    return contributors[:top_n]


def determine_human_confirmation_required(root_cause_result: dict) -> bool:
    """Determine whether human confirmation is required."""
    if root_cause_result.get("human_confirmation_required"):
        return True
    for hint in root_cause_result.get("alert_linked_hints", []):
        if hint.get("human_confirmation_required"):
            return True
        if hint.get("risk_level") in ("Level 3", "Level 4"):
            return True
    warnings = root_cause_result.get("warnings", [])
    return any("high-risk" in str(warning).lower() for warning in warnings)


def build_root_cause_summary(root_cause_result: dict, run_context=None) -> dict:
    """Build structured root cause summary."""
    root_cause_result = root_cause_result or {
        "analysis_status": "skipped_no_input_data",
        "available_inputs": {},
        "metric_change_findings": [],
        "segment_contribution_findings": {"top_contributors": [], "warnings": []},
        "alert_linked_hints": [],
        "warnings": ["No root cause result was provided."],
        "human_confirmation_required": False,
        "safety_note": SAFETY_NOTE,
    }
    contribution_findings = root_cause_result.get("segment_contribution_findings", {})
    return {
        "project_phase": PROJECT_PHASE,
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "analysis_status": root_cause_result.get("analysis_status", "unknown"),
        "available_inputs": root_cause_result.get("available_inputs", {}),
        "top_contributors": summarize_top_contributors(contribution_findings),
        "metric_change_findings": root_cause_result.get("metric_change_findings", []),
        "alert_linked_hints": root_cause_result.get("alert_linked_hints", []),
        "warnings": root_cause_result.get("warnings", []),
        "human_confirmation_required": determine_human_confirmation_required(root_cause_result),
        "safety_note": root_cause_result.get("safety_note", SAFETY_NOTE),
        "run_context": run_context or {},
    }


def save_root_cause_summary(summary: dict, output_path: str | Path) -> Path:
    """Save root cause summary JSON."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2, ensure_ascii=False)
    return path

