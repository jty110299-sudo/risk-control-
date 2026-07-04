# Freddie Mac MVP Field Plan

## Purpose

Design how Freddie Mac Single-Family Loan-Level Dataset may serve as the MVP primary data source.

## Why Freddie Mac Is Recommended as MVP Primary Candidate

Freddie Mac is recommended because it is an official public dataset with loan-level origination data and monthly performance data. It is suitable for demonstrating credit risk monitoring, delinquency status analysis, risk migration, segment comparison, and portfolio-style monitoring.

Freddie Mac data is mortgage loan-level data. It is suitable for demonstrating credit risk monitoring, but it does not represent consumer finance, credit card, or online lending scenarios.

## Expected Raw Data Components

Phase 4 does not process Freddie Mac files. The following field plan remains a design target until the official user guide, file layout, release notes, and selected sample file are verified.

### Origination / Static Data

Expected to include loan-level attributes captured at origination or acquisition, such as loan characteristics, borrower or risk attributes, property characteristics, and origination timing fields, subject to the official file layout.

### Monthly Performance Data

Expected to include monthly loan performance records, performance status, balance-related fields, and termination or delinquency-related fields, subject to the official file layout.

### Possible Loss-Related Data

Loss-related data may be available for some terminated or default-related records. Future phases must verify field definitions and limitations before using any loss-related metrics.

## Candidate Fields for Credit Risk Monitoring

Candidate fields should be selected only after confirming the current file layout:

* Reporting period.
* Loan identifier or anonymized record key.
* Origination period.
* Original loan amount or balance.
* Credit score or risk-band field if available.
* Loan-to-value style field if available.
* Loan purpose.
* Property type.
* Occupancy status.
* Geography or region field if available and privacy-safe.
* Current loan status.
* Delinquency status.
* Zero balance or termination status.

## Candidate Dimensions

* Origination cohort.
* Reporting period.
* Product or loan purpose.
* LTV band.
* Credit score band.
* Geography or region.
* Property type.
* Delinquency status.

## Candidate Performance Status Fields

Future mapping may use:

* Current loan status.
* Current delinquency status.
* Months delinquent or delinquency indicator if available.
* Zero balance code if available.
* Current unpaid principal balance if available.

Field names must follow the official file layout selected in Phase 4 or later.

## Candidate Delinquency / Default Proxy Fields

Possible proxies:

* 30+ delinquency indicator.
* 60+ delinquency indicator.
* 90+ delinquency indicator.
* Serious delinquency indicator.
* Default or zero-balance status where documented.
* Loss-related status where documented.

Proxy definitions must be documented before metric calculation.

## Candidate Derived Metrics

* Loan count by reporting period.
* Delinquency rate by reporting period.
* Serious delinquency or bad-rate proxy.
* Segment delinquency rate.
* Segment contribution to risk increase.
* Vintage or cohort performance trend.
* Score-band or LTV-band migration.
* Population mix shift.

## Fields Not Available from Freddie Mac

Freddie Mac public data is not expected to provide:

* Application approval or denial outcomes.
* Manual review results.
* Internal strategy rule hits.
* Fraud strategy outcomes.
* Production model scores.
* Internal policy changes.
* Consumer finance, credit card, or online lending-specific fields.

## Fields Requiring Exclusion or Synthetic Supplement

The following should be excluded from MVP or clearly marked as synthetic supplement if used later:

* `manual_review_rate`
* `rule_hit_rate`
* `fraud_rate`
* Strategy intercept result.
* False positive rate for internal fraud rules.
* Production model monitoring metrics tied to internal model versions.

## Mapping to Future Agent Monitoring Tables

| Future table | Support level | Mapping note |
| --- | --- | --- |
| `daily_risk_metrics.csv` | Requires Derived Aggregation | Source performance is likely monthly; MVP should use reporting period rather than true daily monitoring. |
| `segment_risk_metrics.csv` | Supported / Requires Derived Aggregation | Use origination/static fields as dimensions and monthly performance fields as outcomes. |
| `model_monitoring_metrics.csv` | Excluded from MVP | Requires later modeling workflow and label definition. |
| `score_distribution.csv` | Partially Supported | Possible if public credit score or score-band fields are confirmed. |
| `feature_drift_metrics.csv` | Partially Supported | Possible for public origination fields after baseline windows are defined. |
| `strategy_rule_metrics.csv` | Requires Synthetic Supplement / Excluded from MVP | Internal rule hits and review outcomes are not available. |

## Phase 4 Verification Gate

Before Phase 5 ingestion:

* Confirm whether Pre-July 2026 or Effective July 2026 layout applies.
* Confirm origination file layout.
* Confirm monthly performance file layout.
* Confirm delimiter, encoding, header behavior, and missing value encoding.
* Confirm whether official sample files match the selected layout.
* Record the user guide version, file layout version, release notes, file name, and file size.
