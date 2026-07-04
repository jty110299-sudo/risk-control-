# Credit Risk and Fraud Risk

## Purpose

Clarify the difference between credit risk and fraud risk so later monitoring logic can keep the project scope focused.

## Credit Risk

### Definition

Credit risk is the risk that a borrower or account fails to meet repayment obligations.

### Typical Scenarios

* Increase in overdue users.
* Increase in bad accounts after observation windows mature.
* Deterioration concentrated in a channel, product, region, score band, or customer segment.

### Common Metrics

* `overdue_rate`
* `first_payment_default_rate`
* `bad_rate`
* `approval_rate`
* `manual_review_rate`

### Common Abnormal Patterns

* Bad rate rises while approval rate also rises.
* A specific channel has a segment bad rate far above the portfolio average.
* Score distribution shifts toward lower-score bands.
* Model performance drops from baseline.

## Fraud Risk

### Definition

Fraud risk is the risk of intentional deception, identity misuse, or coordinated abnormal behavior affecting applications or accounts.

### Typical Scenarios

* Sudden increase in fraud-rule hits.
* Concentrated abnormal activity in a channel or region.
* Increased confirmed fraud cases relative to application volume.

### Common Metrics

* `fraud_rate`
* `rule_hit_rate`
* `intercept_rate`
* `false_positive_rate`

### Common Abnormal Patterns

* Single-day fraud indicator increase.
* Rule hit concentration in a newly changed channel.
* Intercept rate changes that do not match confirmed risk outcomes.

## Difference Between Credit Risk and Fraud Risk

| Dimension | Credit risk | Fraud risk |
| --- | --- | --- |
| Main concern | Repayment ability and willingness over time. | Intentional deception or abnormal application behavior. |
| Observation window | Often requires repayment performance over time. | May appear early through application and behavior signals. |
| First project priority | Main focus. | Auxiliary monitoring only. |

## Scope of This Project

Main focus: credit risk monitoring.

Auxiliary coverage: fraud risk indicators.

This project does not include advanced fraud network analysis, device-fingerprint engineering, or operational fraud investigation details.

