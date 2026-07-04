from __future__ import annotations

from typing import Any


PROHIBITED_TERMS = ["自动拒贷", "自动调额", "自动关闭渠道", "自动修改策略", "自动拉黑", "自动认定欺诈"]


def generate_data_quality_recommendations(profile: dict[str, Any]) -> list[dict[str, Any]]:
    recommendations = []
    if profile.get("missing_column_count", 0) > 0:
        recommendations.append(_rec("需要排查", "存在缺失字段，建议先确认缺失是否集中在关键风险变量。", False))
    if profile.get("row_count", 0) < 100:
        recommendations.append(_rec("观察", "样本量较小，模型指标可能不稳定。", False))
    return recommendations or [_rec("观察", "当前数据质量未发现明显阻断项。", False)]


def generate_model_recommendations(metrics: dict[str, Any]) -> list[dict[str, Any]]:
    recommendations = []
    auc = metrics.get("auc")
    ks = metrics.get("ks")
    if auc is not None and auc < 0.6:
        recommendations.append(_rec("需要排查", "AUC 偏低，建议检查标签口径、特征质量和样本时间窗口。", False))
    if ks is not None and ks < 0.2:
        recommendations.append(_rec("需要排查", "KS 偏低，建议复核模型区分能力。", False))
    if metrics.get("bad_rate", 0) > 0.3:
        recommendations.append(_rec("需要人工确认", "坏样本率较高，建议人工复核样本定义和风险分层。", True))
    return recommendations or [_rec("观察", "模型表现暂无明显异常，仍需结合业务口径复核。", False)]


def generate_risk_band_recommendations(risk_band_summary: list[dict[str, Any]]) -> list[dict[str, Any]]:
    high_risk_rows = [row for row in risk_band_summary if row.get("risk_band") == "高风险"]
    if high_risk_rows and high_risk_rows[0].get("ratio", 0) > 0.2:
        return [_rec("高优先级人工复核", "高风险样本占比较高，建议优先复核高风险分层样本。", True)]
    return [_rec("观察", "风险分层占比未触发高优先级复核条件。", False)]


def generate_attribution_recommendations(attribution_summary: dict[str, Any]) -> list[dict[str, Any]]:
    if attribution_summary.get("segment_summary"):
        return [_rec("需要排查", "存在可排序的高风险分群，建议结合业务口径进行排查。", False)]
    if attribution_summary.get("global_feature_importance"):
        return [_rec("观察", "已生成模型特征重要性，可作为原因排查入口。", False)]
    return [_rec("观察", "暂无足够归因结果，建议先完成评分或选择分群字段。", False)]


def generate_next_step_recommendations(context: dict[str, Any]) -> list[dict[str, Any]]:
    recommendations = []
    if not context.get("has_data"):
        recommendations.append(_rec("观察", "请先在数据接入页上传 CSV。", False))
    if context.get("has_data") and not context.get("has_model") and context.get("has_target"):
        recommendations.append(_rec("需要排查", "数据包含 target，可进入风险评估页训练二分类模型。", False))
    if context.get("has_score") and not context.get("has_report"):
        recommendations.append(_rec("观察", "已生成 score，可进入报告撰写页生成分析报告。", False))
    return recommendations or [_rec("观察", "当前流程可以继续完善可视化、归因和报告。", False)]


def filter_prohibited_actions(recommendations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    filtered = []
    for recommendation in recommendations:
        text = str(recommendation.get("recommendation", ""))
        if any(term in text for term in PROHIBITED_TERMS):
            continue
        filtered.append(recommendation)
    return filtered


def _rec(level: str, recommendation: str, human_confirmation_required: bool) -> dict[str, Any]:
    return {
        "level": level,
        "recommendation": recommendation,
        "human_confirmation_required": human_confirmation_required,
        "boundary": "建议仅用于风控分析辅助，不执行自动业务动作。",
    }
