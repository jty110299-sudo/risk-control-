# Risk Alert Rules

## Purpose

Define illustrative alert levels and example rules for future synthetic monitoring design.

## Risk Levels

| Level | Name | Meaning |
| --- | --- | --- |
| Level 0 | Normal | No material abnormality detected. |
| Level 1 | Watch | Mild change requiring closer monitoring. |
| Level 2 | Medium Risk | Abnormal change requiring manual investigation. |
| Level 3 | High Risk | Significant abnormality requiring focused risk review. |
| Level 4 | Critical Risk | Severe issue requiring human-approved emergency response. |

## Example Rules

| Rule | Level |
| --- | --- |
| `bad_rate` compared with 7-day average increases by more than 20%. | Level 2 |
| `bad_rate` compared with 7-day average increases by more than 40%. | Level 3 |
| `overdue_rate` increases for 3 consecutive days. | Level 2 |
| `fraud_rate` single-day increase exceeds 30%. | Level 3 |
| `approval_rate` single-day decrease exceeds 15%. | Level 2 |
| `PSI >= 0.25`. | Level 3 |
| AUC drops by more than 0.05 from baseline. | Level 2 |
| KS drops by more than 0.05 from baseline. | Level 2 |
| Segment `bad_rate` exceeds overall `bad_rate` by 1.5x. | Level 3 |
| Severe data quality issue. | At least Level 2 |

## Disclaimer

All thresholds in this demo project are illustrative and should be calibrated based on real business history, sample size, risk appetite, and regulatory requirements.

## Key Principles

* Risk level must cite triggered rules.
* Alert rules should be explainable and auditable.
* Level 3 and Level 4 recommendations require human confirmation.

## v0.6.0 Rule Engine Implementation Notes

The current v0.6.0 implementation provides the first configurable rule engine.

* Rule thresholds are for demonstration only.
* Rules must cite metric evidence.
* High-risk rules must require human confirmation.
* The rule engine does not automatically execute strategy actions.
* Risk level output is not a final business decision.
* Rule configuration lives in `configs/risk_alert_rules.yaml`.
* Future rules may be documented but must be marked `future_not_active` until supported.
