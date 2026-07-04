# System Architecture

## 1. Data Layer

* 作用：记录官方公开数据源策略、目录结构和数据治理规则。
* 对应代码或文档：`docs/data_design/`、`data/README.md`、`.gitignore`
* 输入：Freddie Mac、Fannie Mae、HMDA 等官方样本或说明。
* 输出：数据源记录、metadata、download log。
* 当前实现状态：目录和文档已实现，官方样本未内置。

## 2. Data Ingestion Layer

* 作用：读取官方样本并构建 MVP monitoring tables。
* 对应代码或文档：`src/risk_control_agent/monitoring_tables.py`、`scripts/build_monitoring_tables.py`
* 输入：官方样本文件。
* 输出：`data/processed/daily_risk_metrics_mvp.csv`、`segment_risk_metrics_mvp.csv`
* 当前实现状态：框架已实现；无输入时优雅跳过。

## 3. Metric Calculation Layer

* 作用：计算 bad_rate、delinquency_rate 等风控指标。
* 对应代码或文档：`src/risk_control_agent/metrics.py`、`configs/metric_definitions.yaml`
* 输入：monitoring tables。
* 输出：指标结果。
* 当前实现状态：MVP utilities 已实现。

## 4. Alert Rule Engine

* 作用：基于 Risk Alert Rules 识别风险异常。
* 对应代码或文档：`src/risk_control_agent/alert_rules.py`、`scripts/run_alert_engine.py`
* 输入：daily monitoring table。
* 输出：`outputs/alerts/risk_alert_summary_mvp.json`
* 当前实现状态：规则化引擎已实现；不执行业务动作。

## 5. Root Cause Analysis Layer

* 作用：生成分群贡献和归因线索。
* 对应代码或文档：`src/risk_control_agent/root_cause.py`、`contribution_analysis.py`
* 输入：monitoring tables、alert summary。
* 输出：`outputs/alerts/root_cause_summary_mvp.json`
* 当前实现状态：框架已实现；贡献不是因果证明。

## 6. Report Generation Layer

* 作用：生成 Markdown risk report。
* 对应代码或文档：`src/risk_control_agent/report_generator.py`、`scripts/generate_risk_report.py`
* 输入：alert summary、root cause summary。
* 输出：`outputs/reports/risk_analysis_report_mvp.md`
* 当前实现状态：确定性报告框架已实现；无输入时不生成伪造报告。

## 7. UI Dashboard Layer

* 作用：展示状态、预警、归因、报告和日志，触发白名单脚本。
* 对应代码或文档：`app/streamlit_app.py`
* 输入：outputs、data processed、run logs。
* 输出：本地 Streamlit 页面。
* 当前实现状态：MVP 已实现；不是生产系统。

## 8. Audit and Logging Layer

* 作用：记录脚本运行状态、输出路径、跳过原因和异常信息。
* 对应代码或文档：`src/risk_control_agent/run_logger.py`、`outputs/logs/`
* 输入：各阶段脚本运行结果。
* 输出：JSON run logs。
* 当前实现状态：已实现。

## 9. Safety and Governance Layer

* 作用：约束数据、报告、UI、发布和面试展示边界。
* 对应代码或文档：`AGENT_DEVELOPMENT_RULES.md`、`docs/release/`
* 输入：项目实现状态和发布检查。
* 输出：安全边界、检查清单、展示口径。
* 当前实现状态：已实现。
