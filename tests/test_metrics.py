from pathlib import Path
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.metrics import (
    add_baseline_comparison,
    calculate_absolute_change,
    calculate_relative_change,
    safe_divide,
)


def test_safe_divide_normal():
    assert safe_divide(4, 2) == 2


def test_safe_divide_zero_denominator_returns_nan():
    assert np.isnan(safe_divide(4, 0))


def test_calculate_absolute_change():
    assert calculate_absolute_change(5, 3) == 2


def test_calculate_relative_change():
    assert calculate_relative_change(12, 10) == 0.2


def test_add_baseline_comparison_adds_columns():
    df = pd.DataFrame({"period": [1, 2, 3, 4], "metric": [1.0, 2.0, 3.0, 6.0]})
    result = add_baseline_comparison(df, ["metric"], baseline_window=2)
    assert "metric_baseline_average" in result.columns
    assert "metric_relative_change_from_baseline" in result.columns

