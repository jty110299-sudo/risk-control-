from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd


def save_uploaded_file(uploaded_file: Any, output_dir: str | Path) -> Path:
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    original_name = Path(getattr(uploaded_file, "name", "uploaded.csv")).name
    safe_name = "".join(char if char.isalnum() or char in {".", "_", "-"} else "_" for char in original_name)
    output_path = directory / f"{timestamp}_{safe_name}"
    output_path.write_bytes(uploaded_file.getvalue())
    return output_path


def load_user_dataset(path: str | Path) -> pd.DataFrame:
    file_path = Path(path)
    if file_path.suffix.lower() != ".csv":
        raise ValueError("MVP 当前仅支持 CSV 文件。")
    return pd.read_csv(file_path)


def infer_column_types(df: pd.DataFrame) -> dict[str, list[str]]:
    numeric_cols = df.select_dtypes(include=["number", "bool"]).columns.tolist()
    datetime_cols = [
        col
        for col in df.columns
        if col not in numeric_cols and _looks_like_datetime(df[col])
    ]
    categorical_cols = [
        col
        for col in df.columns
        if col not in numeric_cols and col not in datetime_cols
    ]
    return {
        "numeric": numeric_cols,
        "categorical": categorical_cols,
        "datetime": datetime_cols,
    }


def calculate_missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        pd.DataFrame(
            {
                "column": df.columns,
                "missing_count": [int(df[col].isna().sum()) for col in df.columns],
                "missing_rate": [round(float(df[col].isna().mean()), 6) for col in df.columns],
            }
        )
        .sort_values("missing_rate", ascending=False)
        .reset_index(drop=True)
    )


def get_basic_dataset_profile(df: pd.DataFrame) -> dict[str, Any]:
    column_types = infer_column_types(df)
    missing_summary = calculate_missing_summary(df)
    return {
        "row_count": int(len(df)),
        "column_count": int(len(df.columns)),
        "numeric_count": len(column_types["numeric"]),
        "categorical_count": len(column_types["categorical"]),
        "datetime_count": len(column_types["datetime"]),
        "missing_column_count": int((missing_summary["missing_count"] > 0).sum()),
        "column_types": column_types,
    }


def validate_training_target(df: pd.DataFrame, target_col: str | None) -> dict[str, Any]:
    if not target_col:
        return {"valid": False, "message": "请选择 target label 后才能训练 supervised credit risk model。"}
    if target_col not in df.columns:
        return {"valid": False, "message": f"target label 不存在：{target_col}"}
    non_null = df[target_col].dropna()
    unique_values = non_null.unique().tolist()
    if len(unique_values) < 2:
        return {"valid": False, "message": "target label 只有一个类别，不能训练二分类风险模型。"}
    return {
        "valid": True,
        "message": "target label 可用于二分类训练。",
        "unique_values": unique_values,
        "non_null_count": int(len(non_null)),
    }


def _looks_like_datetime(series: pd.Series) -> bool:
    if series.dropna().empty:
        return False
    sample = series.dropna().astype(str).head(50)
    parsed = pd.to_datetime(sample, errors="coerce")
    return bool(parsed.notna().mean() >= 0.8)
