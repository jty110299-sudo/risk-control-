# Risk Control Agent

## 项目简介

Risk Control Agent 是一个面向金融信贷风控监控场景的智能风控分析助手。第一版以 Credit Risk Monitoring 为主，Fraud Risk Indicators 为辅。项目目标是在本地分析流程中读取监控指标、识别风险异常、定位贡献因素、生成风险分析报告，并通过中文优先的界面帮助风控分析人员查看结果和触发已有脚本。

当前项目已经进入 Phase 10: Agent Workflow Packaging and GitHub Showcase。项目现在包含完整本地 MVP 链路、第一版本地 Streamlit UI Dashboard、GitHub 展示材料和面试材料。

当前 UI 已完成 v1.0.1 - UI Design System and Dashboard Redesign：项目新增 `DESIGN.md`，Streamlit UI 已按统一设计系统重构为中文优先的深色金融风控工作台风格。该 UI 仍然是本地 MVP，不伪造数据，不接入 LLM，不执行自动业务动作，也不代表生产系统。

当前 UI 已进一步进入 v2.0.0 - Product-grade Risk Control Agent Workbench：工作台支持用户上传 CSV、自动识别字段、选择 target label、训练二分类风险模型、生成 `risk_score` 和 `risk_band`、交互式可视化、新版归因分析、规则化智能建议和交互式报告撰写。该能力仍然是本地分析工作台，不接入 LLM，不执行自动业务动作，不构成真实金融建议。

需要明确的是：当前项目仍没有内置大型官方数据，没有 LLM 接入，也不是生产级风控系统。项目支持用户在本地上传 CSV 后进行 MVP 级二分类模型训练、AUC / KS 评估、轻量调参和风险评分实验，但不包含生产级模型训练、生产模型部署或自动信贷决策。项目不执行真实信贷审批，不自动拒贷、自动调额、自动关闭渠道或自动修改策略。

## 当前项目阶段

当前阶段：Phase 10 - Agent Workflow Packaging and GitHub Showcase

已完成：

* Phase 1: Risk Control Knowledge Base Construction
* Phase 2: Public Dataset Research and Data Source Design
* Phase 3: Public Dataset Acquisition Plan and MVP Data Sample Construction
* Phase 4: Public Dataset Download Instructions and Small Sample Preparation
* Phase 5: MVP Data Ingestion and Monitoring Table Construction
* Phase 6: Risk Metric Calculation and Alert Rule Engine
* Phase 7: Root Cause Analysis and Segment Contribution Engine
* Phase 8: Risk Report Generation Framework
* Phase 9: Streamlit UI Dashboard MVP
* Phase 10: Agent Workflow Packaging and GitHub Showcase

当前项目包含本地完整流程入口、项目健康检查、Streamlit UI Dashboard MVP、GitHub 展示文档、架构图、面试讲解稿、简历 bullet、Q&A bank 和发布前检查清单。没有输入数据或前序输出时，脚本和 UI 会显示空状态提示，不会伪造数据、图表、风险结论或报告。

尚未完成：

* LLM integration
* Production-grade model training and deployment
* Production database connection
* Automated scheduling
* Authentication and role-based permission
* Production deployment
* Real credit decisioning

## 项目定位

Risk Control Agent 不是自动信贷决策系统，而是风控监控与分析助手。

它可以帮助风控分析人员在本地 MVP 流程中完成：

* 日常风险指标监控
* 信用风险变化分析
* 辅助 Fraud Risk Indicators 观察
* Model Monitoring 与 Data Stability 状态查看
* 数据质量与特征漂移检查的规划展示
* Segment Contribution 与 Root Cause Analysis 查看
* Markdown report 预览与下载
* run log 审计查看
* 触发已有本地分析脚本

所有高风险建议都需要 Human Confirmation。Agent 不负责最终业务决策。

## 项目不会做什么

本项目不会：

* 自动拒贷
* 自动放款
* 自动调整授信额度
* 自动修改生产风控策略
* 自动上线或下线模型
* 自动关闭渠道
* 自动拉黑用户
* 使用真实个人金融数据
* 绕过人工审批
* 对个人用户直接做欺诈定性

## 第一版业务边界

第一版主线是 Credit Risk Monitoring，也就是信用风险监控。

辅助覆盖 Fraud Risk Indicators，也就是反欺诈风险指标观察。反欺诈内容在当前项目中仅作为辅助指标方向，不展开复杂欺诈网络、设备指纹或黑产实战细节。

## Streamlit UI Dashboard

本项目包含本地 Streamlit UI Dashboard MVP：

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

UI 名称：

* Risk Control Agent Console
* 智能风控分析工作台

UI 语言中文为主，保留必要英文专业术语，例如 Alert Summary、Root Cause Analysis、Segment Contribution、Model Monitoring、Data Stability、Human Confirmation、AUC、KS、PSI、bad_rate、monitoring table、run log 和 Markdown report。

UI 设计系统：

* `DESIGN.md`：根目录设计系统说明。
* `app/ui_theme.py`：颜色、风险等级、全局 CSS、cards 和 badges helper。
* `app/ui_components.py`：统一 cards、badges、empty states、safety banner、report viewer 和 run log table。

UI 可以：

* 上传 CSV 并进行字段识别和缺失率分析
* 基于有效 target label 训练二分类风控模型
* 支持 Logistic Regression、Random Forest、Gradient Boosting 和 XGBoost
* 支持轻量 GridSearchCV 调参，以 AUC 作为优化目标，并在训练前展示预计耗时、训练轮数、参与训练样本数和特征数
* 生成 `predicted_probability`、`risk_score`、`risk_band`
* 展示 AUC、KS、Precision、Recall、F1
* 进行交互式数据可视化
* 展示模型归因、样本 reason codes 和分群归因
* 生成规则化智能建议
* 撰写并下载 Markdown / HTML 风险分析报告
* 展示当前会话操作审计

UI 不会：

* 伪造数据或风险结论
* 下载大型官方数据集
* 接入 LLM
* 执行生产级模型训练、自动化 AutoML 或模型上线
* 连接生产系统
* 执行自动业务动作
* 自动保存用户上传的敏感数据
* 将模型输出作为真实信贷决策

## 项目目录结构

* `app/`：Streamlit UI Dashboard MVP
* `configs/`：路径、字段映射、指标、预警、归因、报告和建议配置
* `data/`：数据准备目录，目前不包含大型原始数据
* `docs/knowledge_base/`：金融风控知识库
* `docs/product_design/`：产品定位、用户场景、工作流和 UI 设计
* `docs/technical_design/`：各阶段技术设计文档
* `docs/showcase/`：GitHub 展示材料
* `docs/architecture/`：系统架构说明和 Mermaid 图
* `docs/interview/`：面试讲解稿、简历 bullet 和 Q&A
* `docs/release/`：上传说明和发布前检查清单
* `outputs/`：保存预警、报告和运行日志
* `scripts/`：本地分析脚本
* `src/`：核心 Python 模块
* `tests/`：单元测试
* `README.md`：项目说明
* `PROJECT_LOG.md`：项目建设日志
* `CHANGELOG.md`：版本变化记录
* `SOURCES.md`：资料来源记录
* `AGENT_DEVELOPMENT_RULES.md`：后续开发规则

## 核心知识库内容

* `00_knowledge_base_index.md`：知识库总览。
* `01_risk_control_overview.md`：金融风控整体概念和 Agent 角色边界。
* `02_credit_and_fraud_risk.md`：信用风险与反欺诈风险边界。
* `03_risk_metrics_dictionary.md`：业务风险指标字典。
* `04_model_monitoring_dictionary.md`：AUC、KS、PSI 等模型监控指标字典。
* `05_data_quality_and_drift.md`：数据质量与漂移监控说明。
* `06_risk_alert_rules.md`：Risk Alert Rules 与风险等级设计。
* `07_root_cause_analysis_playbook.md`：Root Cause Analysis 分析路径。
* `08_risk_report_standard.md`：风险报告标准。
* `09_ops_advice_policy.md`：运维建议边界。
* `10_agent_safety_boundary.md`：Agent 安全边界与 Human Confirmation 原则。

## 运行说明

安装运行依赖：

```bash
pip install -r requirements.txt
```

安装测试依赖：

```bash
pip install -r requirements-dev.txt
```

运行项目健康检查：

```bash
python scripts/project_health_check.py
```

运行完整本地 pipeline：

```bash
python scripts/run_full_pipeline.py
```

启动本地 UI：

```bash
streamlit run app/streamlit_app.py
```

构建 MVP monitoring table：

```bash
python scripts/build_monitoring_tables.py
```

运行风险预警：

```bash
python scripts/run_alert_engine.py
```

运行归因分析：

```bash
python scripts/run_root_cause_analysis.py
```

生成 Markdown 风险分析报告：

```bash
python scripts/generate_risk_report.py
```

运行测试：

```bash
python -m pytest
```

如果没有官方样本、processed monitoring table、alert summary 或 root cause summary，相关脚本会优雅跳过并写入 run log，不会生成伪造输出。

## 展示材料入口

* `PROJECT_SUMMARY.md`
* `docs/showcase/project_showcase_overview.md`
* `docs/showcase/demo_walkthrough.md`
* `docs/interview/interview_talk_track.md`
* `docs/interview/resume_bullets.md`
* `docs/release/github_upload_guide.md`

## Roadmap

| 阶段 | 内容 | 状态 |
| --- | --- | --- |
| Phase 1 | 金融风控知识库建设 | 已完成 |
| Phase 2 | 官方公开数据源调研与数据源设计 | 已完成 |
| Phase 3 | 公开数据获取方案与 MVP 样本构建方案 | 已完成 |
| Phase 4 | Public Dataset Download Instructions and Small Sample Preparation | 已完成 |
| Phase 5 | MVP Data Ingestion and Monitoring Table Construction | 已完成 |
| Phase 6 | Risk Metric Calculation and Alert Rule Engine | 已完成 |
| Phase 7 | Root Cause Analysis and Segment Contribution Engine | 已完成 |
| Phase 8 | Risk Report Generation Framework | 已完成 |
| Phase 9 | Streamlit UI Dashboard | 已完成 |
| Phase 10 | Agent Workflow Packaging and GitHub Showcase | 已完成 |

## 安全与治理原则

* 风险结论必须基于指标、规则或明确假设。
* 报告必须区分事实、推测和建议。
* 高风险建议必须标注需要人工确认。
* 所有模拟数据必须明确标注为 synthetic data。
* 不处理真实个人金融数据。
* 不执行真实信贷决策。
* 不输出无证据的因果判断。
* UI 只能触发白名单本地脚本，不能执行任意用户命令。
* UI 必须清楚说明当前是本地 MVP dashboard，不是生产系统。

## 免责声明

本项目为学习、作品集和风控分析流程展示项目，不使用真实个人金融数据，不进行真实信贷审批，不构成任何金融机构的实际风控建议。项目中的阈值、指标和规则用于演示风控监控逻辑，真实业务中需要结合历史样本、业务口径、风险偏好和监管要求进行校准。
