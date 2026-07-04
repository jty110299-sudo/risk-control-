import pandas as pd
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.monitoring_tables import build_daily_risk_metrics_from_performance


def test_build_daily_risk_metrics_counts_observed_loans():
    df = pd.DataFrame(
        {
            "loan_id": ["a", "b", "c"],
            "reporting_period": ["2024-01", "2024-01", "2024-02"],
            "current_loan_delinquency_status": [0, 1, 3],
        }
    )
    result = build_daily_risk_metrics_from_performance(df)
    jan = result[result["monitoring_period"] == "2024-01"].iloc[0]
    assert jan["observed_loan_count"] == 2


def test_build_daily_risk_metrics_calculates_delinquency_rate():
    df = pd.DataFrame(
        {
            "loan_id": ["a", "b"],
            "reporting_period": ["2024-01", "2024-01"],
            "current_loan_delinquency_status": [0, 1],
        }
    )
    result = build_daily_risk_metrics_from_performance(df)
    assert result.iloc[0]["delinquency_rate"] == 0.5


def test_build_daily_risk_metrics_missing_required_columns_errors():
    df = pd.DataFrame({"loan_id": ["a"]})
    with pytest.raises(ValueError, match="Missing required performance columns"):
        build_daily_risk_metrics_from_performance(df)
