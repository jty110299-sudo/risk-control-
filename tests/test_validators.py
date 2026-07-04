import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_control_agent.validators import (
    validate_no_duplicate_keys,
    validate_non_empty_dataframe,
    validate_required_columns,
)


def test_validate_required_columns_passes():
    df = pd.DataFrame({"a": [1], "b": [2]})
    result = validate_required_columns(df, ["a", "b"])
    assert result["passed"] is True
    assert result["errors"] == []


def test_validate_non_empty_dataframe_fails_for_empty():
    result = validate_non_empty_dataframe(pd.DataFrame())
    assert result["passed"] is False
    assert result["errors"]


def test_validate_no_duplicate_keys_detects_duplicates():
    df = pd.DataFrame({"loan_id": ["x", "x"], "period": ["2024-01", "2024-01"]})
    result = validate_no_duplicate_keys(df, ["loan_id", "period"])
    assert result["passed"] is False
    assert "duplicate" in result["errors"][0]
