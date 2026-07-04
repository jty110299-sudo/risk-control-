# Demo Walkthrough

## 1. 安装依赖

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 2. 运行健康检查

```bash
python scripts/project_health_check.py
```

检查结果会保存到 `outputs/logs/project_health_check_*.json`。

## 3. 运行完整 pipeline

```bash
python scripts/run_full_pipeline.py
```

该脚本会按顺序运行监控表构建、风险预警、归因分析和 Markdown report 生成。当前没有官方样本文件时，部分步骤会 skipped，但不应崩溃。

## 4. 运行 Streamlit UI

```bash
streamlit run app/streamlit_app.py
```

打开浏览器中的本地地址即可体验 Risk Control Agent Console。

## 5. 查看 Alert Summary

在 UI 中进入“风险预警”，或查看：

```text
outputs/alerts/risk_alert_summary_mvp.json
```

如果文件不存在，页面会显示空状态提示。

## 6. 查看 Root Cause Summary

在 UI 中进入“归因分析”，或查看：

```text
outputs/alerts/root_cause_summary_mvp.json
```

归因结果是调查线索，不是因果证明。

## 7. 查看 Markdown Report

在 UI 中进入“报告中心”，或查看：

```text
outputs/reports/risk_analysis_report_mvp.md
```

如果没有 alert summary / root cause summary，报告脚本不会生成伪造报告。

## 8. 查看 Run Logs

在 UI 中进入“运行日志与审计”，或查看：

```text
outputs/logs/*.json
```

## 9. 当前没有官方样本文件时会看到什么

项目不会内置大型官方数据文件。没有官方样本时，数据构建、预警、归因和报告步骤会按既有逻辑跳过，并写入 run log。UI 会显示中文空状态和下一步建议。

## 10. 准备官方样本文件后的预期流程

用户需要根据 `docs/data_design/freddie_mac_download_instructions.md` 准备官方样本。准备完成后，可重新运行：

```bash
python scripts/run_full_pipeline.py
streamlit run app/streamlit_app.py
```

届时 UI 会展示由真实输入流程生成的 derived outputs。
