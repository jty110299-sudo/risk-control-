# Metric Calculation Plan

## Purpose

Define future metric calculation formulas and logic. This document does not include code.

Phase 2 prioritizes official or authoritative public datasets. Metric availability depends on source fields, reporting windows, privacy modifications, and license terms.

## Planned Calculations

| Metric | Formula | Denominator definition | Notes |
| --- | --- | --- | --- |
| `approval_rate` | `approved_count / application_count` | All applications in the observation period. | Compare against baseline and prior day. |
| `rejection_rate` | `rejected_count / application_count` | All applications in the observation period. | Should reconcile with approval and review categories where applicable. |
| `manual_review_rate` | `manual_review_count / application_count` | All applications in the observation period. | Useful for operational workload and borderline-risk signals. |
| `overdue_rate` | `overdue_users / due_users` | Users with payments due in the observation window. | Observation window must be consistent. |
| `bad_rate` | `bad_count / total_observed_users` | Users with completed performance observation window. | Must avoid immature-window distortion. |
| `fraud_rate` | `fraud_cases / application_count` | All applications in the observation period. | Fraud labels may be delayed. |
| `rule_hit_rate` | `rule_hit_count / application_count` | All applications in the observation period. | Should be analyzed by rule and segment. |
| PSI | `sum((current_share - baseline_share) * ln(current_share / baseline_share))` | Distribution buckets with current and baseline shares. | Bucket definitions must remain stable. |
| AUC change | `current_auc - baseline_auc` | Not a rate denominator. | Negative values indicate performance drop. |
| KS change | `current_ks - baseline_ks` | Not a rate denominator. | Negative values indicate weaker separation. |
| Segment contribution | `segment_bad_increase / total_bad_increase` | Total bad-count increase across included segments. | Requires comparable baseline and current windows. |

## Key Principles

* Formulas must define denominators.
* Baseline windows must be documented.
* Segment calculations must reconcile to portfolio totals where possible.
* Future implementation must distinguish public-data-derived metrics from synthetic supplements.
* Metrics unsupported by public data should be marked `Requires synthetic supplement or excluded from MVP`.

## Public Dataset Support

| Metric area | Freddie Mac / Fannie Mae loan performance data | HMDA data | Phase 2 recommendation |
| --- | --- | --- | --- |
| Delinquency-related metrics | Likely supported through monthly performance fields and loan status fields. | Not suitable for post-origination performance. | Include in MVP design if field definitions are confirmed. |
| `overdue_rate` | Likely supported after mapping delinquency or performance status fields. | Not supported as repayment performance. | Candidate MVP metric from loan performance data. |
| `bad_rate` | Potentially supported using delinquency, default, disposition, or loss-related definitions after careful labeling. | Not supported as post-origination bad outcome. | Candidate MVP metric if the bad definition is documented. |
| Application volume | Not the main strength; loan performance data covers acquired or purchased loans, not all applications. | Supported through loan application records. | Use HMDA as auxiliary source. |
| `approval_rate` / `rejection_rate` | Not suitable for full application funnel monitoring. | Supported through action taken / approval / denial information. | Use HMDA as auxiliary source. |
| `manual_review_rate` | Not typically available. | Not typically available as an internal workflow field. | Requires synthetic supplement or excluded from MVP. |
| `fraud_rate` | Likely not supported by official public mortgage performance data. | Likely not supported as confirmed fraud outcome. | Requires synthetic supplement or excluded from MVP. |
| `rule_hit_rate` | Not available because internal risk strategy-rule results are not public. | Not available. | Requires synthetic supplement or excluded from MVP. |
| PSI / distribution drift | Possible after deriving stable buckets from public fields. | Possible for application population fields if comparable periods are defined. | Include as future derived metric, not Phase 2 implementation. |
| AUC / KS change | Requires later model development and labels. | Requires later model development and outcome labels; HMDA action status is not equivalent to credit default. | Optional later phase, excluded from MVP unless modeling scope is defined. |
| Segment contribution | Can be derived from aggregated bad or delinquency changes by segment. | Can be derived for application or action outcomes by segment. | Candidate MVP logic after field mapping. |

## Phase 6 Implementation Status

Implemented or supported as framework:

* Safe rate calculation.
* Absolute change.
* Relative change.
* Baseline average.
* Period-over-period comparison.
* `delinquency_rate` if monitoring table exists.
* `serious_delinquency_rate` if monitoring table exists.

Future work:

* `bad_rate` from appropriate performance outcome.
* PSI.
* AUC / KS monitoring.
* Model monitoring metrics.
* Fraud indicators if data source supports them or synthetic supplement is approved.

## Phase 7 Contribution Metrics

Phase 7 supports contribution-style metrics:

| Metric | Meaning |
| --- | --- |
| `segment_count_increase` | Current segment count minus baseline segment count. |
| `segment_metric_change` | Current segment rate or metric minus baseline segment rate or metric. |
| `segment_contribution_share` | Positive segment increase divided by total positive increase. |
| `top_contributor_rank` | Segment ranking based on contribution share. |

Key constraints:

* `contribution_share` is calculated from positive segment increases.
* `contribution_share` is an investigation signal, not causality.
* Contribution requires a segment-level monitoring table.
* Contribution should not be calculated when total increase is less than or equal to 0.
