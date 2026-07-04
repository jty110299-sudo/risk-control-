from pathlib import Path
import sys

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.contribution_analysis import (
    calculate_contribution_share,
    calculate_count_increase,
    calculate_segment_contribution,
    rank_top_contributors,
)


def test_calculate_count_increase():
    assert calculate_count_increase(10, 6) == 4


def test_calculate_contribution_share():
    assert calculate_contribution_share(2, 10) == 0.2


def test_calculate_contribution_share_zero_total_returns_nan():
    assert np.isnan(calculate_contribution_share(2, 0))


def test_calculate_segment_contribution_outputs_increase_and_share():
    df = pd.DataFrame(
        {
            "monitoring_period": ["p1", "p1", "p2", "p2"],
            "segment_type": ["channel", "channel", "channel", "channel"],
            "segment_value": ["A", "B", "A", "B"],
            "delinquent_loan_count": [2, 1, 5, 2],
            "delinquency_rate": [0.02, 0.01, 0.05, 0.02],
        }
    )
    result = calculate_segment_contribution(
        df,
        "monitoring_period",
        ["segment_type", "segment_value"],
        "delinquent_loan_count",
        "delinquency_rate",
        baseline_periods=["p1"],
        current_period="p2",
    )
    assert "segment_increase" in result.columns
    assert "contribution_share" in result.columns


def test_rank_top_contributors_returns_top_n():
    df = pd.DataFrame({"contribution_share": [0.1, 0.5, 0.2]})
    result = rank_top_contributors(df, top_n=2)
    assert len(result) == 2
    assert result.iloc[0]["contribution_share"] == 0.5


def test_missing_required_columns_errors():
    df = pd.DataFrame({"monitoring_period": ["p1"]})
    with pytest.raises(ValueError, match="Missing required contribution columns"):
        calculate_segment_contribution(df, "monitoring_period", ["segment_type"], "count")

