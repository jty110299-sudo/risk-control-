from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.root_cause_summary import (
    build_root_cause_summary,
    determine_human_confirmation_required,
    summarize_top_contributors,
)


def test_build_root_cause_summary_has_project_phase():
    result = {"analysis_status": "skipped_no_input_data"}
    summary = build_root_cause_summary(result)
    assert "project_phase" in summary


def test_summarize_top_contributors_extracts_top():
    findings = {"top_contributors": [{"segment": "A"}, {"segment": "B"}]}
    assert summarize_top_contributors(findings, top_n=1) == [{"segment": "A"}]


def test_determine_human_confirmation_required_for_high_risk_hint():
    result = {"alert_linked_hints": [{"risk_level": "Level 3"}], "warnings": []}
    assert determine_human_confirmation_required(result) is True


def test_safety_note_exists():
    summary = build_root_cause_summary({})
    assert "safety_note" in summary


def test_empty_input_keeps_skipped_status():
    summary = build_root_cause_summary({"analysis_status": "skipped_no_input_data"})
    assert summary["analysis_status"] == "skipped_no_input_data"

