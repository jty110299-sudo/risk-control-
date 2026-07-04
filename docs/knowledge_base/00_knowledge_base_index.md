# Knowledge Base Index

## Purpose

This knowledge base serves Risk Control Agent development. It is not a general finance textbook. It is a set of constraints, definitions, analysis standards, reporting rules, and safety boundaries for later implementation.

## Scope

The first version focuses on credit risk monitoring. Fraud-risk indicators are included only as auxiliary signals.

## File Map

| File | Responsibility |
| --- | --- |
| `01_risk_control_overview.md` | Defines the financial risk control context and the Agent role. |
| `02_credit_and_fraud_risk.md` | Distinguishes credit risk from fraud risk and defines project scope. |
| `03_risk_metrics_dictionary.md` | Defines business risk monitoring metrics and formulas. |
| `04_model_monitoring_dictionary.md` | Defines model monitoring metrics and report language. |
| `05_data_quality_and_drift.md` | Defines data quality, drift, and validation principles. |
| `06_risk_alert_rules.md` | Defines illustrative alert levels and rule examples. |
| `07_root_cause_analysis_playbook.md` | Defines root-cause analysis paths and contribution logic. |
| `08_risk_report_standard.md` | Defines report structure and writing rules. |
| `09_ops_advice_policy.md` | Defines allowed and disallowed operations advice. |
| `10_agent_safety_boundary.md` | Defines what the Agent can and must not do. |

## Key Principles

* Later code development must follow the metric definitions, alert rules, report standards, and safety boundaries in this knowledge base.
* All risk conclusions must be based on data, rules, or explicit assumptions.
* High-risk recommendations must be marked: Requires human confirmation. / 需要人工确认。
* The Agent must not claim causality without sufficient evidence.

