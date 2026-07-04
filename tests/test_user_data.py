import pandas as pd

from risk_control_agent.user_data import infer_column_types, validate_training_target


def test_missing_target_cannot_train():
    df = pd.DataFrame({"x": [1, 2, 3]})
    result = validate_training_target(df, None)
    assert not result["valid"]


def test_single_class_target_invalid():
    df = pd.DataFrame({"target": [1, 1, 1], "x": [1, 2, 3]})
    result = validate_training_target(df, "target")
    assert not result["valid"]


def test_infer_column_types():
    df = pd.DataFrame({"num": [1, 2], "cat": ["a", "b"]})
    result = infer_column_types(df)
    assert "num" in result["numeric"]
    assert "cat" in result["categorical"]
