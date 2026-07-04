from __future__ import annotations

from pathlib import Path

import streamlit as st

from risk_control_agent.model_training import TRAINING_MODE_CONFIG, estimate_training_plan, save_model, train_risk_model
from risk_control_agent.scoring import save_scored_dataset, score_dataset
from ui_components import render_empty_state, render_metric_card, render_page_title
from ui_state import add_audit_log


def render() -> None:
    render_page_title("风险评估", "训练二分类风控模型，生成 predicted_probability、risk_score 和 risk_band。")
    df = st.session_state.current_dataframe
    if df is None:
        render_empty_state("暂无数据", "请先在“数据接入”页面上传 CSV。")
        return

    render_page_title("A. 模型训练区", "支持 Logistic Regression、Random Forest、Gradient Boosting、XGBoost。")
    columns = df.columns.tolist()
    target_col = st.selectbox("选择 target label", columns, index=columns.index(st.session_state.target_col) if st.session_state.target_col in columns else 0)
    positive_label = st.text_input("正样本含义", value="1", help="MVP 期望 target 已经编码为 0/1；1 表示坏样本。")
    excluded_cols = st.multiselect("排除字段", columns, default=[col for col in [st.session_state.id_col, st.session_state.time_col] if col])
    model_type = st.selectbox("模型类型", ["Logistic Regression", "Random Forest", "Gradient Boosting", "XGBoost"])
    training_mode = st.radio(
        "训练模式",
        list(TRAINING_MODE_CONFIG.keys()),
        horizontal=True,
        help="快速训练用于先看方向；标准训练用于稳定基线；调参训练会自动执行轻量 GridSearchCV。",
    )
    plan = estimate_training_plan(
        df,
        target_col=target_col,
        model_type=model_type,
        exclude_cols=excluded_cols,
        training_mode=training_mode,
    )
    st.session_state.target_col = target_col
    st.session_state.excluded_cols = excluded_cols

    render_page_title("训练计划", "点击训练前先确认预计耗时、训练轮数和样本范围。")
    plan_cols = st.columns(4)
    with plan_cols[0]:
        render_metric_card("预计耗时", plan["estimated_label"], "本地电脑粗略估算", "info")
    with plan_cols[1]:
        render_metric_card("训练轮数", plan["fit_count"], "单次训练或 CV fit 次数", "review")
    with plan_cols[2]:
        render_metric_card("参与训练样本", plan["effective_rows"], f"原始行数 {plan['row_count']}", "info")
    with plan_cols[3]:
        render_metric_card("特征数", plan["feature_count"], "排除字段后", "ready")

    st.caption(plan["mode_label"])
    for warning in plan["warnings"]:
        st.warning(warning)
    if plan["high_cardinality_columns"]:
        st.info("建议排除的高基数字段：" + "、".join(plan["high_cardinality_columns"]))

    button_label = "一键训练并调参" if plan["enable_tuning"] else "一键训练评分模型"
    if st.button(button_label, use_container_width=False):
        result = train_risk_model(
            df,
            target_col=target_col,
            model_type=model_type,
            exclude_cols=excluded_cols,
            enable_tuning=plan["enable_tuning"],
            max_training_rows=plan["max_training_rows"],
            training_mode=training_mode,
        )
        if result["status"] == "ok":
            model_path = save_model(result["model"], Path("models") / "risk_model.joblib")
            st.session_state.trained_model = result["model"]
            st.session_state.model_metrics = result["metrics"]
            st.session_state.feature_cols = result["feature_cols"]
            st.session_state.model_path = str(model_path)
            add_audit_log(
                "train_risk_model",
                "success",
                inputs={"target_col": target_col, "model_type": model_type, "training_mode": training_mode},
                outputs={"model_path": str(model_path), "metrics": result["metrics"]},
            )
            st.success("模型训练完成。")
        else:
            add_audit_log("train_risk_model", "error", inputs={"target_col": target_col}, errors=[result["message"]])
            st.error(result["message"])

    metrics = st.session_state.model_metrics
    if metrics:
        metric_cols = st.columns(5)
        for col, key in zip(metric_cols, ["auc", "ks", "precision", "recall", "f1"]):
            with col:
                render_metric_card(key.upper(), metrics.get(key), "测试集指标", "ready")
        extra_cols = st.columns(4)
        with extra_cols[0]:
            render_metric_card("样本量", metrics.get("sample_count"), "训练可用样本", "info")
        with extra_cols[1]:
            render_metric_card("坏样本率", metrics.get("bad_rate"), "target=1", "warning")
        with extra_cols[2]:
            render_metric_card("训练 / 测试", metrics.get("train_test_split"), "split ratio", "info")
        with extra_cols[3]:
            render_metric_card("模型路径", st.session_state.model_path or "暂无", "models/*.joblib 已忽略", "review")
        runtime_cols = st.columns(4)
        with runtime_cols[0]:
            render_metric_card("训练模式", metrics.get("training_mode"), "本次执行方式", "info")
        with runtime_cols[1]:
            render_metric_card("实际耗时", f"{metrics.get('elapsed_seconds')} 秒", "本机运行结果", "ready")
        with runtime_cols[2]:
            render_metric_card("训练轮数", metrics.get("fit_count"), "包含调参 CV", "review")
        with runtime_cols[3]:
            sampled_label = "已抽样" if metrics.get("sampled_for_training") else "未抽样"
            render_metric_card("样本处理", sampled_label, f"原始 {metrics.get('original_sample_count')} 行", "warning")
        if metrics.get("tuning_enabled"):
            tuning_cols = st.columns(2)
            with tuning_cols[0]:
                render_metric_card("Best CV AUC", metrics.get("best_cv_auc", "暂无"), "GridSearchCV 交叉验证结果", "ready")
            with tuning_cols[1]:
                render_metric_card("Best Params", metrics.get("best_params", "暂无"), "轻量参数搜索结果", "review")

    render_page_title("调参优化怎么做", "当前提供轻量 GridSearchCV；后续可扩展为更完整的模型治理流程。")
    st.markdown(
        """
* 第一阶段：用当前轻量调参比较不同模型的 AUC / KS / Recall。
* 第二阶段：结合坏样本率、业务成本和风险偏好选择阈值，而不是只看 AUC。
* 第三阶段：增加时间外验证集、PSI、score distribution 和分群稳定性。
* 第四阶段：记录参数、训练数据窗口、指标和人工确认意见，形成模型审计记录。

注意：调参只优化分析模型，不代表自动信贷决策；上线策略仍需要人工审批和业务校准。
"""
    )

    render_page_title("B. 风险评分区", "risk_score = round((1 - predicted_probability) * 1000)。分数越低，风险越高。")
    if st.session_state.trained_model is None:
        render_empty_state("暂无模型", "请先训练评分模型。")
        return
    if st.button("生成风险评估", use_container_width=False):
        scored = score_dataset(st.session_state.trained_model, df, st.session_state.feature_cols)
        save_path = save_scored_dataset(scored, "data/processed/scored_dataset.csv")
        st.session_state.scored_dataframe = scored
        add_audit_log("score_dataset", "success", outputs={"path": str(save_path), "rows": len(scored)})
        st.success("risk_score 和 risk_band 已生成。")

    scored = st.session_state.scored_dataframe
    if scored is not None:
        st.dataframe(scored[["predicted_probability", "risk_score", "risk_band", "risk_rank"]].head(20), use_container_width=True)
        band_summary = scored["risk_band"].value_counts().rename_axis("risk_band").reset_index(name="count")
        st.bar_chart(band_summary, x="risk_band", y="count")
