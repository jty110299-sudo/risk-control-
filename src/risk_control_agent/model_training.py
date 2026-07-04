from __future__ import annotations

from pathlib import Path
from typing import Any
import math
import time

import numpy as np
import pandas as pd


MIN_TRAINING_ROWS = 30
TRAINING_MODE_CONFIG = {
    "快速训练": {"enable_tuning": False, "max_training_rows": 5000, "label": "适合先看 AUC / KS 是否有基本区分度"},
    "标准训练": {"enable_tuning": False, "max_training_rows": 20000, "label": "适合样本量适中时做较稳定的基线模型"},
    "调参训练": {"enable_tuning": True, "max_training_rows": 10000, "label": "一键执行轻量参数搜索，耗时会明显增加"},
}
MODEL_BASE_SECONDS_PER_1000_ROWS = {
    "Logistic Regression": 1.0,
    "Random Forest": 4.0,
    "Gradient Boosting": 5.0,
    "XGBoost": 6.0,
}


def prepare_training_data(df: pd.DataFrame, target_col: str, exclude_cols: list[str] | None = None) -> tuple[pd.DataFrame, pd.Series, list[str]]:
    excluded = set(exclude_cols or [])
    excluded.add(target_col)
    feature_cols = [col for col in df.columns if col not in excluded]
    if not feature_cols:
        raise ValueError("没有可用于训练的特征字段。")
    working = df[feature_cols + [target_col]].dropna(subset=[target_col]).copy()
    y = working[target_col]
    if y.nunique(dropna=True) < 2:
        raise ValueError("target label 只有一个类别，不能训练二分类风险模型。")
    return working[feature_cols], y, feature_cols


def train_logistic_regression(X_train: pd.DataFrame, y_train: pd.Series):
    sklearn = _require_sklearn()
    pipeline = _build_preprocess_pipeline(sklearn, "logistic_regression")
    return pipeline.fit(X_train, y_train)


def train_random_forest(X_train: pd.DataFrame, y_train: pd.Series):
    sklearn = _require_sklearn()
    pipeline = _build_preprocess_pipeline(sklearn, "random_forest")
    return pipeline.fit(X_train, y_train)


def train_gradient_boosting(X_train: pd.DataFrame, y_train: pd.Series):
    sklearn = _require_sklearn()
    pipeline = _build_preprocess_pipeline(sklearn, "gradient_boosting")
    return pipeline.fit(X_train, y_train)


def train_xgboost(X_train: pd.DataFrame, y_train: pd.Series):
    sklearn = _require_sklearn()
    pipeline = _build_preprocess_pipeline(sklearn, "xgboost")
    return pipeline.fit(X_train, y_train)


def evaluate_binary_classifier(model: Any, X_test: pd.DataFrame, y_test: pd.Series) -> dict[str, Any]:
    sklearn = _require_sklearn()
    y_score = model.predict_proba(X_test)[:, 1]
    y_pred = (y_score >= 0.5).astype(int)
    return {
        "auc": round(float(sklearn["roc_auc_score"](y_test, y_score)), 6),
        "ks": round(float(calculate_ks(y_test, y_score)), 6),
        "precision": round(float(sklearn["precision_score"](y_test, y_pred, zero_division=0)), 6),
        "recall": round(float(sklearn["recall_score"](y_test, y_pred, zero_division=0)), 6),
        "f1": round(float(sklearn["f1_score"](y_test, y_pred, zero_division=0)), 6),
        "test_sample_count": int(len(y_test)),
    }


def calculate_ks(y_true: pd.Series | np.ndarray, y_score: pd.Series | np.ndarray) -> float:
    frame = pd.DataFrame({"y_true": y_true, "y_score": y_score}).dropna()
    positives = int(frame["y_true"].sum())
    negatives = int(len(frame) - positives)
    if positives == 0 or negatives == 0:
        return 0.0
    frame = frame.sort_values("y_score", ascending=False)
    cumulative_positive = frame["y_true"].cumsum() / positives
    cumulative_negative = (1 - frame["y_true"]).cumsum() / negatives
    return float(np.max(np.abs(cumulative_positive - cumulative_negative)))


def train_risk_model(
    df: pd.DataFrame,
    target_col: str,
    model_type: str,
    exclude_cols: list[str] | None = None,
    test_size: float = 0.3,
    random_state: int = 42,
    enable_tuning: bool = False,
    max_training_rows: int | None = None,
    training_mode: str | None = None,
) -> dict[str, Any]:
    try:
        started_at = time.perf_counter()
        sklearn = _require_sklearn()
        if len(df) < MIN_TRAINING_ROWS:
            return {"status": "error", "message": f"样本量过少，至少需要 {MIN_TRAINING_ROWS} 行。"}
        original_sample_count = int(len(df))
        working_df = _sample_for_training(df, target_col, max_training_rows, random_state)
        X, y_raw, feature_cols = prepare_training_data(working_df, target_col, exclude_cols)
        y = pd.Series(y_raw).astype(int)
        if y.nunique(dropna=True) < 2:
            return {"status": "error", "message": "target label 只有一个类别，不能训练二分类风险模型。"}
        X_train, X_test, y_train, y_test = sklearn["train_test_split"](
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
        if model_type == "Logistic Regression":
            model = train_logistic_regression(X_train, y_train)
        elif model_type == "Random Forest":
            model = train_random_forest(X_train, y_train)
        elif model_type == "Gradient Boosting":
            model = train_gradient_boosting(X_train, y_train)
        elif model_type == "XGBoost":
            model = train_xgboost(X_train, y_train)
        else:
            return {"status": "error", "message": f"不支持的模型类型：{model_type}"}
        tuning_result = None
        if enable_tuning:
            tuning_result = tune_model_pipeline(model, X_train, y_train, model_type)
            model = tuning_result["best_model"]
        metrics = evaluate_binary_classifier(model, X_test, y_test)
        bad_rate = round(float(y.mean()), 6)
        elapsed_seconds = round(float(time.perf_counter() - started_at), 3)
        fit_count = calculate_fit_count(model_type, enable_tuning)
        return {
            "status": "ok",
            "model": model,
            "metrics": {
                **metrics,
                "sample_count": int(len(y)),
                "original_sample_count": original_sample_count,
                "training_sample_count": int(len(y)),
                "sampled_for_training": original_sample_count > int(len(y)),
                "max_training_rows": max_training_rows,
                "bad_rate": bad_rate,
                "train_test_split": f"{round(1 - test_size, 2)} / {round(test_size, 2)}",
                "model_type": model_type,
                "tuning_enabled": enable_tuning,
                "training_mode": training_mode or ("调参训练" if enable_tuning else "标准训练"),
                "fit_count": fit_count,
                "elapsed_seconds": elapsed_seconds,
                "best_params": tuning_result.get("best_params") if tuning_result else None,
                "best_cv_auc": tuning_result.get("best_cv_auc") if tuning_result else None,
            },
            "feature_cols": feature_cols,
        }
    except ImportError as exc:
        return {"status": "error", "message": str(exc)}
    except ValueError as exc:
        return {"status": "error", "message": str(exc)}


def estimate_training_plan(
    df: pd.DataFrame,
    target_col: str,
    model_type: str,
    exclude_cols: list[str] | None = None,
    training_mode: str = "快速训练",
) -> dict[str, Any]:
    mode_config = TRAINING_MODE_CONFIG.get(training_mode, TRAINING_MODE_CONFIG["快速训练"])
    enable_tuning = bool(mode_config["enable_tuning"])
    max_training_rows = mode_config["max_training_rows"]
    excluded = set(exclude_cols or [])
    excluded.add(target_col)
    feature_cols = [col for col in df.columns if col not in excluded]
    row_count = int(len(df))
    effective_rows = min(row_count, int(max_training_rows)) if max_training_rows else row_count
    fit_count = calculate_fit_count(model_type, enable_tuning)
    high_cardinality_columns = _detect_high_cardinality_columns(df, feature_cols)
    seconds = _estimate_training_seconds(model_type, effective_rows, len(feature_cols), fit_count, high_cardinality_columns)
    return {
        "training_mode": training_mode,
        "model_type": model_type,
        "enable_tuning": enable_tuning,
        "max_training_rows": max_training_rows,
        "row_count": row_count,
        "effective_rows": effective_rows,
        "feature_count": len(feature_cols),
        "fit_count": fit_count,
        "estimated_seconds": seconds,
        "estimated_label": format_duration_estimate(seconds),
        "mode_label": mode_config["label"],
        "high_cardinality_columns": high_cardinality_columns,
        "suggested_exclude_cols": sorted(set(exclude_cols or []) | set(high_cardinality_columns)),
        "warnings": _build_training_plan_warnings(row_count, effective_rows, high_cardinality_columns, enable_tuning),
    }


def calculate_fit_count(model_type: str, enable_tuning: bool) -> int:
    if not enable_tuning:
        return 1
    grid = _get_tuning_grid(model_type)
    if not grid:
        return 1
    combinations = math.prod(len(values) for values in grid.values())
    return int(combinations * 3)


def format_duration_estimate(seconds: float) -> str:
    if seconds < 10:
        return "< 10 秒"
    if seconds < 60:
        return f"约 {int(math.ceil(seconds / 10) * 10)} 秒"
    minutes = int(math.ceil(seconds / 60))
    if minutes <= 3:
        return f"约 {minutes} 分钟"
    return f"可能超过 {minutes} 分钟"


def save_model(model: Any, path: str | Path) -> Path:
    joblib = _require_joblib()
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)
    return output_path


def load_model(path: str | Path) -> Any:
    joblib = _require_joblib()
    return joblib.load(path)


def _build_preprocess_pipeline(sklearn: dict[str, Any], model_type: str):
    numeric_features_selector = sklearn["make_column_selector"](dtype_include=np.number)
    categorical_features_selector = sklearn["make_column_selector"](dtype_exclude=np.number)
    numeric_transformer = sklearn["Pipeline"](
        steps=[("imputer", sklearn["SimpleImputer"](strategy="median")), ("scaler", sklearn["StandardScaler"]())]
    )
    categorical_transformer = sklearn["Pipeline"](
        steps=[
            ("imputer", sklearn["SimpleImputer"](strategy="most_frequent")),
            ("onehot", sklearn["OneHotEncoder"](handle_unknown="ignore")),
        ]
    )
    preprocessor = sklearn["ColumnTransformer"](
        transformers=[
            ("num", numeric_transformer, numeric_features_selector),
            ("cat", categorical_transformer, categorical_features_selector),
        ]
    )
    if model_type == "logistic_regression":
        estimator = sklearn["LogisticRegression"](max_iter=1000)
    elif model_type == "random_forest":
        estimator = sklearn["RandomForestClassifier"](n_estimators=120, random_state=42, min_samples_leaf=5)
    elif model_type == "gradient_boosting":
        estimator = sklearn["GradientBoostingClassifier"](random_state=42)
    elif model_type == "xgboost":
        estimator = _build_xgboost_classifier()
    else:
        raise ValueError(f"不支持的模型类型：{model_type}")
    return sklearn["Pipeline"](steps=[("preprocess", preprocessor), ("model", estimator)])


def tune_model_pipeline(model: Any, X_train: pd.DataFrame, y_train: pd.Series, model_type: str) -> dict[str, Any]:
    sklearn = _require_sklearn()
    param_grid = _get_tuning_grid(model_type)
    if not param_grid:
        return {"best_model": model, "best_params": {}, "best_cv_auc": None}
    search = sklearn["GridSearchCV"](
        estimator=model,
        param_grid=param_grid,
        scoring="roc_auc",
        cv=3,
        n_jobs=1,
        error_score="raise",
    )
    search.fit(X_train, y_train)
    return {
        "best_model": search.best_estimator_,
        "best_params": search.best_params_,
        "best_cv_auc": round(float(search.best_score_), 6),
    }


def _get_tuning_grid(model_type: str) -> dict[str, list[Any]]:
    if model_type == "Logistic Regression":
        return {"model__C": [0.1, 1.0, 3.0]}
    if model_type == "Random Forest":
        return {"model__n_estimators": [80, 160], "model__max_depth": [None, 5], "model__min_samples_leaf": [3, 8]}
    if model_type == "Gradient Boosting":
        return {"model__n_estimators": [80, 140], "model__learning_rate": [0.03, 0.08], "model__max_depth": [2, 3]}
    if model_type == "XGBoost":
        return {
            "model__n_estimators": [80, 140],
            "model__max_depth": [2, 4],
            "model__learning_rate": [0.03, 0.08],
        }
    return {}


def _estimate_training_seconds(
    model_type: str,
    row_count: int,
    feature_count: int,
    fit_count: int,
    high_cardinality_columns: list[str],
) -> float:
    base = MODEL_BASE_SECONDS_PER_1000_ROWS.get(model_type, 4.0)
    row_factor = max(row_count, MIN_TRAINING_ROWS) / 1000
    feature_factor = 1 + min(feature_count, 80) / 80
    cardinality_factor = 1 + min(len(high_cardinality_columns), 5) * 0.35
    return round(max(3.0, base * row_factor * feature_factor * cardinality_factor * max(fit_count, 1)), 1)


def _detect_high_cardinality_columns(df: pd.DataFrame, feature_cols: list[str]) -> list[str]:
    high_cardinality_columns = []
    row_count = max(len(df), 1)
    for col in feature_cols:
        series = df[col]
        if pd.api.types.is_numeric_dtype(series):
            continue
        unique_count = int(series.nunique(dropna=True))
        unique_ratio = unique_count / row_count
        looks_like_identifier = any(token in col.lower() for token in ["id", "uuid", "phone", "mobile", "name"])
        if unique_count >= 50 or unique_ratio >= 0.5 or looks_like_identifier:
            high_cardinality_columns.append(col)
    return high_cardinality_columns


def _build_training_plan_warnings(
    row_count: int,
    effective_rows: int,
    high_cardinality_columns: list[str],
    enable_tuning: bool,
) -> list[str]:
    warnings = []
    if row_count > effective_rows:
        warnings.append(f"当前模式会抽样 {effective_rows} 行参与训练，避免本地训练时间过长。")
    if high_cardinality_columns:
        warnings.append("检测到高基数字段，建议排除 ID、姓名、手机号等不稳定字段。")
    if enable_tuning:
        warnings.append("调参训练会执行多轮交叉验证，AUC / KS 更有参考性，但耗时明显增加。")
    return warnings


def _sample_for_training(
    df: pd.DataFrame,
    target_col: str,
    max_training_rows: int | None,
    random_state: int,
) -> pd.DataFrame:
    if not max_training_rows or len(df) <= max_training_rows:
        return df.copy()
    valid = df.dropna(subset=[target_col]).copy()
    counts = valid[target_col].value_counts()
    if counts.empty:
        return valid.head(max_training_rows).copy()
    sampled_parts = []
    remaining = int(max_training_rows)
    for index, (label, count) in enumerate(counts.items()):
        if index == len(counts) - 1:
            sample_size = min(int(count), remaining)
        else:
            sample_size = max(1, int(round(max_training_rows * int(count) / len(valid))))
            sample_size = min(int(count), sample_size, remaining)
        remaining -= sample_size
        sampled_parts.append(valid[valid[target_col] == label].sample(n=sample_size, random_state=random_state))
    sampled = pd.concat(sampled_parts).sample(frac=1, random_state=random_state)
    if len(sampled) > max_training_rows:
        sampled = sampled.sample(n=max_training_rows, random_state=random_state)
    return sampled.reset_index(drop=True)


def _build_xgboost_classifier() -> Any:
    try:
        from xgboost import XGBClassifier
    except ImportError as exc:
        raise ImportError("缺少 xgboost。请先运行 pip install -r requirements.txt。") from exc
    return XGBClassifier(
        n_estimators=120,
        max_depth=3,
        learning_rate=0.05,
        subsample=0.9,
        colsample_bytree=0.9,
        eval_metric="logloss",
        random_state=42,
        n_jobs=1,
    )


def _require_sklearn() -> dict[str, Any]:
    try:
        from sklearn.compose import ColumnTransformer, make_column_selector
        from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
        from sklearn.impute import SimpleImputer
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score
        from sklearn.model_selection import GridSearchCV, train_test_split
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import OneHotEncoder, StandardScaler
    except ImportError as exc:
        raise ImportError("缺少 scikit-learn。请先运行 pip install -r requirements.txt。") from exc
    return locals()


def _require_joblib():
    try:
        import joblib
    except ImportError as exc:
        raise ImportError("缺少 joblib。请先运行 pip install -r requirements.txt。") from exc
    return joblib
