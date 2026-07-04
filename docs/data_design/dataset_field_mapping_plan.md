# Dataset Field Mapping Plan

## Purpose

Design the future mapping from official public datasets to Risk Control Agent monitoring tables.

Official public datasets are usually not ready-made daily risk monitoring reports. They require field interpretation, cleaning, aggregation, and metric construction before they can be used as Agent inputs.

## Data Layers

### 1. Public Raw Data Layer

This layer stores source metadata and raw-field definitions from official public datasets. Large raw datasets should not be uploaded to GitHub.

Expected sources:

* Fannie Mae Single-Family Loan Performance Data.
* Freddie Mac Single-Family Loan-Level Dataset.
* CFPB / FFIEC HMDA Data.

### 2. Cleaned Loan-Level Layer

This future layer would normalize selected fields, apply documented filters, handle missing values, and align reporting periods. Phase 2 does not implement this layer.

### 3. Aggregated Monitoring Layer

This future layer would aggregate cleaned records into monitoring tables such as daily or monthly risk metrics, segment metrics, score distributions, and feature stability tables.

### 4. Agent Input Layer

This future layer would provide small, documented monitoring tables to Risk Control Agent. The Agent should consume aggregated or privacy-safe inputs, not large raw source files.

## Future Monitoring Table Mapping

| Future table | Public dataset support | Fields that can be derived | Fields that may require synthetic supplement | MVP status |
| --- | --- | --- | --- | --- |
| `daily_risk_metrics.csv` | Freddie Mac or Fannie Mae for performance metrics; HMDA for application/action metrics. | Application count from HMDA; delinquency or bad-rate style metrics from loan performance data after definition. | Fraud rate, manual review rate, internal strategy-rule metrics. | Required for MVP, with unsupported fields excluded or labeled. |
| `segment_risk_metrics.csv` | Freddie Mac, Fannie Mae, and HMDA may support segment aggregation. | Segment counts, performance rates, application action rates, geography or product mix. | Internal channel labels, manual review results, fraud strategy outputs. | Required for MVP. |
| `model_monitoring_metrics.csv` | Public data may provide features and labels for later modeling, but not ready-made model metrics. | Future AUC, KS, precision, recall after a modeling phase. | Internal model version, production score, production decision logs. | Optional; exclude from MVP unless modeling scope is defined. |
| `score_distribution.csv` | Public credit score or derived score fields may support score bands if available. | Score-band counts, shares, and outcome rates after mapping. | Internal model scores or scorecards. | Optional for MVP unless source score fields are confirmed. |
| `feature_drift_metrics.csv` | Public datasets can support drift metrics for selected public fields. | Missing rate, distribution shift, PSI or CSI after baseline definition. | Internal-only features not present in public data. | Optional for MVP. |
| `strategy_rule_metrics.csv` | Public data usually does not support internal strategy rules. | None, unless generic public-field proxy rules are explicitly designed later. | Rule hit rate, intercept rate, false positive rate, manual review outcomes. | Requires synthetic supplement or excluded from MVP. |

## Unsupported Internal Monitoring Fields

If public data cannot support `fraud_rate`, `rule_hit_rate`, or `manual_review_rate`, the field must be marked:

```text
Requires synthetic supplement or excluded from MVP.
```

## Key Principles

* Public raw data should remain separate from derived monitoring tables.
* Every derived metric must trace back to source fields and transformation notes.
* Any synthetic supplement must be explicitly labeled.
* Dataset limitations must be documented before coding.

## Freddie Mac MVP Mapping Priority

Freddie Mac should be the first MVP mapping target.

### Future Monitoring Tables Prioritized from Freddie Mac

| Future table | Freddie Mac support level | MVP note |
| --- | --- | --- |
| `daily_risk_metrics.csv` | Requires Derived Aggregation | Use monthly performance periods rather than daily granularity if the raw source is monthly. |
| `segment_risk_metrics.csv` | Supported / Requires Derived Aggregation | Use origination/static fields as dimensions and performance fields as outcomes. |
| `score_distribution.csv` | Partially Supported | Use public credit score or risk-band fields if available and documented. |
| `feature_drift_metrics.csv` | Partially Supported | Use selected public origination fields and compare distributions across time windows. |
| `model_monitoring_metrics.csv` | Excluded from MVP | Requires a later modeling scope and label definition. |
| `strategy_rule_metrics.csv` | Requires Synthetic Supplement or Excluded from MVP | Internal rule hits and manual review outcomes are not available from Freddie Mac public data. |

### Field Source Categories

Fields expected from loan origination / static data:

* Loan amount or balance at origination.
* Original loan-to-value style fields if available.
* Credit score or borrower risk attributes if available.
* Loan purpose, property type, occupancy, channel, geography, or product dimensions if available.
* Origination or acquisition period fields.

Fields expected from monthly performance data:

* Reporting period.
* Current loan status or delinquency status.
* Remaining balance or current performance-related measures.
* Zero balance or termination-related fields if available.
* Loss-related fields if available and suitable for the selected sample.

### Derived Metrics

Metrics requiring aggregation:

* Loan count by reporting period.
* Delinquency or overdue-style rate.
* Bad-rate or default-style proxy, if the definition is documented.
* Segment-level delinquency or bad-rate proxy.
* Score-band or risk-band migration.
* Population mix by selected dimensions.

### Fields Not Available from Freddie Mac

Freddie Mac public loan-level data is not expected to provide:

* Application approval or denial results.
* Internal manual review outcomes.
* Internal strategy rule hits.
* Fraud strategy decisions.
* Production model scores or model versions.
* Consumer finance, credit card, or online lending business fields.

### MVP Exclusion and Synthetic Supplement Rules

Fields such as `manual_review_rate`, `rule_hit_rate`, and `fraud_rate` should be excluded from the MVP unless a clearly labeled synthetic supplement is introduced later.

Synthetic supplements must not be mixed with public data without labeling and source separation.
