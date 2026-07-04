# Risk Control Agent Console

## Purpose

Risk Control Agent Console 是 Risk Control Agent 的本地 Streamlit UI Dashboard MVP，用于展示已有风控监控输出、运行日志和 Markdown report，并触发项目中已经存在的本地分析脚本。

## How to run the Streamlit app

```bash
streamlit run app/streamlit_app.py
```

## Required dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` 中包含 `streamlit`。开发测试依赖可通过以下命令安装：

```bash
pip install -r requirements-dev.txt
```

## Expected project structure

UI 会读取以下项目目录中的现有文件：

* `data/processed/`
* `outputs/alerts/`
* `outputs/reports/`
* `outputs/logs/`
* `scripts/`

## What the UI can show

* 数据准备状态
* Alert Summary
* Root Cause Analysis
* Segment Contribution
* Model Monitoring 与 Data Stability 的当前规划状态
* Markdown report
* run log

## What the UI cannot do

* 不生成或伪造数据
* 不训练模型
* 不接入 LLM API
* 不连接生产数据库
* 不执行真实信贷决策
* 不自动拒贷、调额、关闭渠道或修改策略

## Empty-state behavior

如果没有数据或前序输出，UI 会显示中文空状态提示和下一步建议，而不会伪造风险结果、图表或报告。

## Safety boundary

Risk Control Agent 仅用于风险监控、分析辅助和作品集展示。所有最终业务决策都需要人工审核与确认。
