from __future__ import annotations

from pathlib import Path
from typing import Any


DEFAULT_SECTIONS = [
    "summary",
    "data_overview",
    "model_results",
    "risk_distribution",
    "attribution",
    "recommendations",
    "human_confirmation",
    "limitations",
    "disclaimer",
]


def build_user_report_context(
    dataset_profile: dict[str, Any] | None = None,
    model_metrics: dict[str, Any] | None = None,
    risk_band_summary: list[dict[str, Any]] | None = None,
    attribution_summary: dict[str, Any] | None = None,
    recommendations: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    return {
        "dataset_profile": dataset_profile or {},
        "model_metrics": model_metrics or {},
        "risk_band_summary": risk_band_summary or [],
        "attribution_summary": attribution_summary or {},
        "recommendations": recommendations or [],
    }


def generate_user_markdown_report(context: dict[str, Any], selected_sections: list[str] | None = None) -> str:
    sections = selected_sections or DEFAULT_SECTIONS
    lines = ["# Risk Control Agent 风险分析报告", ""]
    if "summary" in sections:
        lines += ["## 报告摘要", "本报告基于用户上传数据、模型评分结果和规则化建议生成，供风控分析复核使用。", ""]
    if "data_overview" in sections:
        profile = context.get("dataset_profile", {})
        lines += [
            "## 数据概览",
            f"* 样本量：{profile.get('row_count', '暂无')}",
            f"* 特征数：{profile.get('column_count', '暂无')}",
            f"* 存在缺失的字段数：{profile.get('missing_column_count', '暂无')}",
            "",
        ]
    if "model_results" in sections:
        metrics = context.get("model_metrics", {})
        lines += [
            "## 模型训练结果",
            f"* AUC：{metrics.get('auc', '暂无')}",
            f"* KS：{metrics.get('ks', '暂无')}",
            f"* Precision：{metrics.get('precision', '暂无')}",
            f"* Recall：{metrics.get('recall', '暂无')}",
            f"* F1：{metrics.get('f1', '暂无')}",
            "",
        ]
    if "risk_distribution" in sections:
        lines += ["## 风险评分分布", "风险分层结果以 `risk_score` 和 `risk_band` 为准，模型输出仅用于分析辅助。", ""]
        for row in context.get("risk_band_summary", []):
            lines.append(f"* {row.get('risk_band')}: {row.get('count')} ({row.get('ratio')})")
        lines.append("")
    if "attribution" in sections:
        lines += ["## 归因分析结果", "归因结果是模型解释和分群排查线索，不是因果证明。", ""]
        for row in context.get("attribution_summary", {}).get("global_feature_importance", [])[:10]:
            lines.append(f"* {row.get('feature')}: {row.get('importance')}")
        lines.append("")
    if "recommendations" in sections:
        lines += ["## 智能建议", ""]
        for item in context.get("recommendations", []):
            lines.append(f"* [{item.get('level')}] {item.get('recommendation')}")
        lines.append("")
    if "human_confirmation" in sections:
        lines += ["## 人工确认事项", "所有高风险建议、策略调整和业务动作都需要人工确认。", ""]
    if "limitations" in sections:
        lines += ["## 限制说明", "本报告依赖上传数据质量、标签口径和模型配置；不代表真实授信审批结论。", ""]
    if "disclaimer" in sections:
        lines += [
            "## 免责声明",
            "本项目为学习、作品集和风控分析流程展示项目，不执行真实信贷审批，不构成任何金融机构的实际风控建议。",
            "",
        ]
    return "\n".join(lines)


def save_user_report(markdown_text: str, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown_text, encoding="utf-8")
    return path
