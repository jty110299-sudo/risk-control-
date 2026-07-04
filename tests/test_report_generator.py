from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.report_generator import (
    build_report_context,
    generate_markdown_report,
    generate_report_manifest,
    validate_report_inputs,
)


def test_validate_report_inputs_without_input_cannot_generate():
    assert validate_report_inputs()["can_generate"] is False


def test_generate_markdown_report_contains_executive_summary():
    context = build_report_context({"overall_risk_level": "Level 1", "alert_count": 0})
    report = generate_markdown_report(context, {"report_name": "Test Report"}, {})
    assert "Executive Summary" in report


def test_generate_markdown_report_contains_safety_note():
    context = build_report_context({"overall_risk_level": "Level 1", "alert_count": 0})
    report = generate_markdown_report(context, {"safety_notes": ["Safety Note Text"]}, {})
    assert "Safety Note" in report


def test_generate_markdown_report_contains_footer_disclaimer():
    context = build_report_context({"overall_risk_level": "Level 1", "alert_count": 0})
    report = generate_markdown_report(context, {"footer_disclaimer": "Footer Disclaimer Text"}, {})
    assert "Footer Disclaimer Text" in report


def test_generate_report_manifest_records_status_and_inputs():
    manifest = generate_report_manifest("report.md", "success", ["alert_summary"])
    assert manifest["status"] == "success"
    assert manifest["inputs_used"] == ["alert_summary"]


def test_no_input_does_not_generate_report():
    assert validate_report_inputs()["can_generate"] is False

