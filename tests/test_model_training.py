import importlib.util

import pandas as pd
import pytest

from risk_control_agent.model_training import estimate_training_plan, train_risk_model


pytestmark = pytest.mark.skipif(importlib.util.find_spec("sklearn") is None, reason="scikit-learn not installed")


def test_train_model_rejects_single_class_target():
    df = pd.DataFrame({"target": [1] * 40, "x": list(range(40))})
    result = train_risk_model(df, "target", "Logistic Regression")
    assert result["status"] == "error"


def test_train_model_returns_metrics():
    df = pd.DataFrame(
        {
            "target": [0, 1] * 40,
            "x": list(range(80)),
            "segment": ["a", "b"] * 40,
        }
    )
    result = train_risk_model(df, "target", "Logistic Regression")
    assert result["status"] == "ok"
    assert "auc" in result["metrics"]


@pytest.mark.skipif(importlib.util.find_spec("xgboost") is None, reason="xgboost not installed")
def test_train_xgboost_returns_metrics():
    df = pd.DataFrame(
        {
            "target": [0, 1] * 40,
            "x": list(range(80)),
            "segment": ["a", "b"] * 40,
        }
    )
    result = train_risk_model(df, "target", "XGBoost")
    assert result["status"] == "ok"
    assert result["metrics"]["model_type"] == "XGBoost"


def test_light_tuning_records_best_params():
    df = pd.DataFrame(
        {
            "target": [0, 1] * 40,
            "x": list(range(80)),
            "segment": ["a", "b"] * 40,
        }
    )
    result = train_risk_model(df, "target", "Logistic Regression", enable_tuning=True)
    assert result["status"] == "ok"
    assert result["metrics"]["tuning_enabled"] is True
    assert result["metrics"]["best_params"] is not None


def test_estimate_training_plan_for_xgboost_tuning():
    df = pd.DataFrame(
        {
            "target": [0, 1] * 80,
            "x": list(range(160)),
            "user_id": [f"user_{index}" for index in range(160)],
            "segment": ["a", "b", "c", "d"] * 40,
        }
    )
    plan = estimate_training_plan(df, "target", "XGBoost", training_mode="调参训练")
    assert plan["enable_tuning"] is True
    assert plan["fit_count"] == 24
    assert plan["estimated_seconds"] > 0
    assert "user_id" in plan["high_cardinality_columns"]


def test_train_model_records_sampling_metadata():
    df = pd.DataFrame(
        {
            "target": [0, 1] * 80,
            "x": list(range(160)),
            "segment": ["a", "b"] * 80,
        }
    )
    result = train_risk_model(df, "target", "Logistic Regression", max_training_rows=60, training_mode="快速训练")
    assert result["status"] == "ok"
    assert result["metrics"]["sampled_for_training"] is True
    assert result["metrics"]["training_sample_count"] <= 60
    assert result["metrics"]["original_sample_count"] == 160
    assert result["metrics"]["elapsed_seconds"] >= 0
