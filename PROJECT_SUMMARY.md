# Risk Control Agent Project Summary

## Project Name

Risk Control Agent

## Chinese Name

智能风控分析工作台

## Current Version

v1.0.0 - Workflow Packaging and GitHub Showcase

## Current Phase

Phase 10 - Agent Workflow Packaging and GitHub Showcase

## Project Positioning

Risk Control Agent 是一个面向金融信贷风控监控场景的本地 MVP 分析工作台，主线是 Credit Risk Monitoring，辅助覆盖 Fraud Risk Indicators。

## Implemented Capabilities

* Public data source strategy
* Data directory and metadata templates
* Data ingestion framework
* Monitoring table construction framework
* Metric calculation utilities
* Rule-based alert engine
* Root Cause Analysis framework
* Segment Contribution analysis framework
* Markdown risk report generation framework
* Streamlit UI Dashboard MVP
* Local full pipeline runner
* Project health check
* GitHub showcase and interview materials

## Not Implemented

* Official sample data actually downloaded and processed
* LLM integration
* Production-grade model training and deployment
* Production database connection
* Automated scheduling
* Authentication and role-based permission
* Production deployment
* Real credit decisioning

## Repository Structure

* `app/`：Streamlit UI Dashboard MVP
* `configs/`：项目配置
* `data/`：数据目录和治理模板
* `docs/`：知识库、产品、技术、展示、架构、面试和发布文档
* `outputs/`：运行日志、预警和报告输出
* `scripts/`：本地流程入口
* `src/`：核心 Python 模块
* `tests/`：单元测试

## How to Run

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
python scripts/project_health_check.py
python scripts/run_full_pipeline.py
streamlit run app/streamlit_app.py
```

## Data Strategy

项目采用 public-dataset-first 策略，优先使用 Freddie Mac、Fannie Mae、HMDA 等官方或权威公开数据源。当前仓库不内置大型官方数据文件，不使用真实个人金融数据。

## Safety Boundary

项目支持用户在本地上传 CSV 后进行 MVP 级二分类模型训练、AUC / KS 评估、轻量调参和风险评分实验，但不包含生产级模型训练、生产模型部署或自动信贷决策。项目不执行真实信贷决策，不自动拒贷、调额、关闭渠道或修改策略。所有高风险建议都需要 Human Confirmation。

## Technical Stack

Python, Streamlit, pandas, numpy, PyYAML, pytest, Markdown, JSON, Mermaid.

## Roadmap

* 准备小型官方样本
* 生成真实 derived outputs
* 优化 UI 视觉
* 扩展 Model Monitoring
* 在严格边界下探索 LLM 报告辅助

## Interview Value

项目展示了风控指标体系、数据治理、规则预警、归因分析、报告生成、Dashboard、日志审计和安全边界意识，适合中文风控实习、数据分析和数据产品面试场景。

## Disclaimer

本项目为学习、作品集和风控分析流程展示项目，不使用真实个人金融数据，不进行真实信贷审批，不构成任何金融机构的实际风控建议。
