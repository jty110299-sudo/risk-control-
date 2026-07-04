from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from risk_control_agent.config import load_data_paths
from risk_control_agent.io_utils import ensure_directory
from risk_control_agent.run_logger import create_run_log, save_run_log


PROJECT_PHASE = "Phase 6 - Risk Metric Calculation and Alert Rule Engine"
NO_PROCESSED_MESSAGE = (
    "No processed monitoring table found. Please run scripts/build_monitoring_tables.py "
    "after preparing an official sample file."
)


def main() -> int:
    paths = load_data_paths()
    ensure_directory(paths["logs_dir"])
    ensure_directory(PROJECT_ROOT / "outputs" / "alerts")
    processed_path = paths["processed_data_dir"] / "daily_risk_metrics_mvp.csv"

    if not processed_path.exists():
        print(NO_PROCESSED_MESSAGE)
        log = create_run_log(
            run_name="run_alert_engine",
            status="skipped_no_processed_data",
            messages=[NO_PROCESSED_MESSAGE],
            project_phase=PROJECT_PHASE,
        )
        log_path = save_run_log(log, paths["logs_dir"])
        print(f"Run log saved to: {log_path}")
        return 0

    try:
        import pandas as pd
        from risk_control_agent.alert_rules import generate_triggered_alerts, load_alert_rules
        from risk_control_agent.alert_summary import build_alert_summary, save_alert_summary
        from risk_control_agent.metrics import add_baseline_comparison

        df = pd.read_csv(processed_path)
        metric_cols = [
            column for column in [
                "observed_loan_count",
                "delinquency_rate",
                "serious_delinquency_rate",
            ] if column in df.columns
        ]
        df_with_baseline = add_baseline_comparison(df, metric_cols, baseline_window=3)
        rules = load_alert_rules("configs/risk_alert_rules.yaml")
        evaluation = generate_triggered_alerts(df_with_baseline, rules)
        summary = build_alert_summary(
            evaluation["triggered_alerts"],
            warnings=evaluation.get("warnings", []),
        )
        output_path = PROJECT_ROOT / "outputs" / "alerts" / "risk_alert_summary_mvp.json"
        save_alert_summary(summary, output_path)
        log = create_run_log(
            run_name="run_alert_engine",
            status="success",
            messages=[f"Alert summary saved to: {output_path}"],
            output_path=str(output_path),
            project_phase=PROJECT_PHASE,
        )
        save_run_log(log, paths["logs_dir"])
        print(f"Alert summary saved to: {output_path}")
        return 0
    except Exception as exc:
        message = f"Alert engine failed: {exc}"
        print(message)
        log = create_run_log(
            run_name="run_alert_engine",
            status="failed_alert_engine",
            messages=[message],
            project_phase=PROJECT_PHASE,
        )
        log_path = save_run_log(log, paths["logs_dir"])
        print(f"Run log saved to: {log_path}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
