from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from risk_control_agent.config import load_data_paths
from risk_control_agent.io_utils import ensure_directory, find_candidate_input_files
from risk_control_agent.run_logger import create_run_log, save_run_log


NO_INPUT_MESSAGE = (
    "No official sample files found. Please follow "
    "docs/data_design/freddie_mac_download_instructions.md before running data ingestion."
)


def main() -> int:
    paths = load_data_paths()
    ensure_directory(paths["processed_data_dir"])
    ensure_directory(paths["logs_dir"])

    input_files = find_candidate_input_files(paths["official_sample_dir"])
    if not input_files:
        print(NO_INPUT_MESSAGE)
        log = create_run_log(
            run_name="build_monitoring_tables",
            status="skipped_no_input_data",
            messages=[NO_INPUT_MESSAGE],
        )
        log_path = save_run_log(log, paths["logs_dir"])
        print(f"Run log saved to: {log_path}")
        return 0

    input_file = input_files[0]
    messages = [f"Found input file: {input_file}"]
    try:
        from risk_control_agent.io_utils import read_csv_safely
        from risk_control_agent.monitoring_tables import build_daily_risk_metrics_from_performance
        from risk_control_agent.quality_checks import generate_basic_quality_summary

        df = read_csv_safely(input_file)
        quality_summary = generate_basic_quality_summary(df)
        messages.append(f"Quality summary: {quality_summary}")
        table = build_daily_risk_metrics_from_performance(df)
        output_path = paths["processed_data_dir"] / "daily_risk_metrics_mvp.csv"
        table.to_csv(output_path, index=False)
        messages.append(f"Monitoring table saved to: {output_path}")
        log = create_run_log(
            run_name="build_monitoring_tables",
            status="success",
            messages=messages,
            output_path=str(output_path),
        )
        save_run_log(log, paths["logs_dir"])
        print(f"Monitoring table saved to: {output_path}")
        return 0
    except Exception as exc:
        message = f"Monitoring table construction failed: {exc}"
        print(message)
        messages.append(message)
        log = create_run_log(
            run_name="build_monitoring_tables",
            status="failed_validation_or_processing",
            messages=messages,
        )
        log_path = save_run_log(log, paths["logs_dir"])
        print(f"Run log saved to: {log_path}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
