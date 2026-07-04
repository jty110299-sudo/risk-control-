# Data Schema Blueprint

## Purpose

Define future monitoring data table designs. This document describes schemas only and does not generate data.

Phase 2 changes the data strategy to public datasets first. Synthetic data is no longer the primary data source and may only supplement fields that official public datasets do not provide.

## Planned Tables

| Table | Purpose | Grain | Key columns | Example fields | Public Data Support | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `daily_risk_metrics.csv` | Track overall risk metrics. | One row per reporting period. | `date` or `reporting_period` | `application_count`, `approval_rate`, `overdue_rate`, `bad_rate`, `fraud_rate` | Partially supported by public data; requires derived aggregation. | Loan performance data may support delinquency and bad-rate style metrics. HMDA may support application and action metrics. Fraud rate likely requires synthetic supplement or exclusion from MVP. |
| `segment_risk_metrics.csv` | Track metrics by segment. | One row per period and segment. | `date`, `segment_type`, `segment_value` | `channel`, `product`, `region`, `score_band`, `bad_rate` | Partially supported by public data; requires derived aggregation. | Public fields may support product, geography, loan characteristics, and score or risk-band proxies depending on dataset. |
| `model_monitoring_metrics.csv` | Track model performance. | One row per period and model version. | `date`, `model_id`, `model_version` | `auc`, `ks`, `precision`, `recall`, `f1`, `lift` | Requires future modeling workflow; optional for MVP. | Public data can provide labels and features for later model experiments, but Phase 2 does not build models. |
| `score_distribution.csv` | Track score-band population movement. | One row per period and score band. | `date`, `score_band` | `user_count`, `user_share`, `bad_count`, `bad_rate` | Partially supported if public data includes credit score or model-derived score bands; requires derived aggregation. | Model-derived score bands require later code and should not be claimed in Phase 2. |
| `feature_drift_metrics.csv` | Track feature stability. | One row per period and feature. | `date`, `feature_name` | `missing_rate`, `mean_value`, `psi`, `csi` | Partially supported by public data; requires derived aggregation. | PSI and CSI can be calculated later from public fields if baseline windows are defined. |
| `strategy_rule_metrics.csv` | Track rule hit and review behavior. | One row per period and rule. | `date`, `rule_id` | `rule_hit_count`, `rule_hit_rate`, `intercept_rate`, `false_positive_rate` | Requires synthetic supplement or excluded from MVP. | Public mortgage datasets generally do not contain internal strategy-rule hits, manual review queues, or fraud strategy outcomes. |

## Key Principles

* Official or authoritative public datasets should be used first.
* Public datasets usually require field interpretation, cleaning, aggregation, and metric construction before they can serve as Agent inputs.
* Synthetic supplements must be explicitly labeled.
* No real customer identifiers are allowed.
* Schema definitions must support metric traceability and report reproducibility.
