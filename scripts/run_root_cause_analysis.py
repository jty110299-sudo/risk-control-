from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from risk_control_agent.config import load_data_paths, load_yaml_config
from risk_control_agent.io_utils import ensure_directory
from risk_control_agent.run_logger import create_run_log, save_run_log


PROJECT_PHASE = "Phase 7 - Root Cause Analysis and Segment Contribution Engine"
NO_INPUT_MESSAGE = (
    "No monitoring tables or alert summary found. Please run previous phases before root cause analysis."
)


def _read_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    paths = load_data_paths()
    ensure_directory(paths["logs_dir"])
    ensure_directory(PROJECT_ROOT / "outputs" / "alerts")

    daily_path = paths["processed_data_dir"] / "daily_risk_metrics_mvp.csv"
    segment_path = paths["processed_data_dir"] / "segment_risk_metrics_mvp.csv"
    alert_path = PROJECT_ROOT / "outputs" / "alerts" / "risk_alert_summary_mvp.json"
    output_path = PROJECT_ROOT / "outputs" / "alerts" / "root_cause_summary_mvp.json"

    if not daily_path.exists() and not segment_path.exists() and not alert_path.exists():
        print(NO_INPUT_MESSAGE)
        log = create_run_log(
            run_name="run_root_cause_analysis",
            status="skipped_no_input_data",
            messages=[NO_INPUT_MESSAGE],
            project_phase=PROJECT_PHASE,
        )
        log_path = save_run_log(log, paths["logs_dir"])
        print(f"Run log saved to: {log_path}")
        return 0

    try:
        import pandas as pd
        from risk_control_agent.root_cause import run_root_cause_analysis
        from risk_control_agent.root_cause_summary import build_root_cause_summary, save_root_cause_summary

        daily_df = pd.read_csv(daily_path) if daily_path.exists() else None
        segment_df = pd.read_csv(segment_path) if segment_path.exists() else None
        alert_summary = _read_json(alert_path) if alert_path.exists() else None
        config = load_yaml_config("configs/root_cause_analysis.yaml")

        result = run_root_cause_analysis(
            daily_df=daily_df,
            segment_df=segment_df,
            alert_summary=alert_summary,
            config=config,
        )
        summary = build_root_cause_summary(result)
        save_root_cause_summary(summary, output_path)
        log = create_run_log(
            run_name="run_root_cause_analysis",
            status=summary["analysis_status"],
            messages=[f"Root cause summary saved to: {output_path}"],
            output_path=str(output_path),
            project_phase=PROJECT_PHASE,
        )
        save_run_log(log, paths["logs_dir"])
        print(f"Root cause summary saved to: {output_path}")
        return 0
    except Exception as exc:
        message = f"Root cause analysis failed: {exc}"
        print(message)
        log = create_run_log(
            run_name="run_root_cause_analysis",
            status="failed_root_cause_analysis",
            messages=[message],
            project_phase=PROJECT_PHASE,
        )
        log_path = save_run_log(log, paths["logs_dir"])
        print(f"Run log saved to: {log_path}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

