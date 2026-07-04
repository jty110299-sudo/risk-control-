from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from risk_control_agent.config import load_data_paths, load_yaml_config
from risk_control_agent.io_utils import ensure_directory
from risk_control_agent.report_generator import (
    build_report_context,
    generate_markdown_report,
    generate_report_manifest,
    load_json_if_exists,
    save_markdown_report,
    save_report_manifest,
    validate_report_inputs,
)
from risk_control_agent.run_logger import create_run_log, save_run_log


PROJECT_PHASE = "Phase 8 - Risk Report Generation"
NO_REPORT_INPUTS_MESSAGE = (
    "No alert summary or root cause summary found. Please run previous phases before generating a risk report."
)


def main() -> int:
    paths = load_data_paths()
    ensure_directory(paths["logs_dir"])
    reports_dir = PROJECT_ROOT / "outputs" / "reports"
    ensure_directory(reports_dir)

    alert_path = PROJECT_ROOT / "outputs" / "alerts" / "risk_alert_summary_mvp.json"
    root_cause_path = PROJECT_ROOT / "outputs" / "alerts" / "root_cause_summary_mvp.json"
    alert_summary = load_json_if_exists(alert_path)
    root_cause_summary = load_json_if_exists(root_cause_path)
    validation = validate_report_inputs(alert_summary, root_cause_summary)

    if not validation["can_generate"]:
        print(NO_REPORT_INPUTS_MESSAGE)
        log = create_run_log(
            run_name="generate_risk_report",
            status="skipped_no_report_inputs",
            messages=[NO_REPORT_INPUTS_MESSAGE],
            project_phase=PROJECT_PHASE,
        )
        log_path = save_run_log(log, paths["logs_dir"])
        print(f"Run log saved to: {log_path}")
        return 0

    try:
        template = load_yaml_config("configs/report_template.yaml")
        recommendations = load_yaml_config("configs/recommendation_rules.yaml")
        context = build_report_context(alert_summary, root_cause_summary)
        markdown = generate_markdown_report(context, template, recommendations)
        report_path = reports_dir / template.get("output_filename", "risk_analysis_report_mvp.md")
        save_markdown_report(markdown, report_path)
        manifest = generate_report_manifest(report_path, "success", validation["inputs_used"], validation["warnings"])
        manifest_path = reports_dir / "risk_analysis_report_manifest_mvp.json"
        save_report_manifest(manifest, manifest_path)
        log = create_run_log(
            run_name="generate_risk_report",
            status="success",
            messages=[f"Risk report saved to: {report_path}", f"Manifest saved to: {manifest_path}"],
            output_path=str(report_path),
            project_phase=PROJECT_PHASE,
        )
        save_run_log(log, paths["logs_dir"])
        print(f"Risk report saved to: {report_path}")
        return 0
    except Exception as exc:
        message = f"Risk report generation failed: {exc}"
        print(message)
        log = create_run_log(
            run_name="generate_risk_report",
            status="failed_report_generation",
            messages=[message],
            project_phase=PROJECT_PHASE,
        )
        log_path = save_run_log(log, paths["logs_dir"])
        print(f"Run log saved to: {log_path}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

