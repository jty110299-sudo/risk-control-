# Fannie Mae Backup Plan

## Purpose

Define how Fannie Mae Single-Family Loan Performance Data may serve as an alternative primary or backup dataset.

## Why Fannie Mae Is a Backup or Alternative Primary Dataset

Fannie Mae provides an official public loan performance dataset with acquisition and performance data. It is suitable for mortgage credit performance monitoring and can support similar analysis to Freddie Mac if it is selected as the primary source.

## Expected Data Components

### Acquisition Data

Acquisition data is expected to include static loan-level fields at origination or delivery, such as loan, borrower, product, and property characteristics, subject to official documentation.

### Performance Data

Performance data is expected to include monthly loan performance records, delinquency or status fields, and other performance-related fields, subject to official documentation.

## Suitable Use Cases

* Mortgage credit performance monitoring.
* Delinquency trend analysis.
* Segment-level risk comparison.
* Vintage or cohort analysis.
* Backup MVP source if Freddie Mac field layout, access, or sampling constraints are not suitable.

## Limitations

* Mortgage-specific data, not consumer finance, credit card, or online lending data.
* May not include application approval or denial funnel information.
* May not include internal strategy rule hits, manual review results, or fraud strategy outcomes.
* Access terms, file sizes, data dictionary, and usage limitations must be checked before use.

## Access and Usage Considerations

Before using Fannie Mae data, future phases should confirm:

* Official source page.
* FAQ or data dictionary version.
* File layout.
* Download process.
* Data size.
* Redistribution and GitHub storage restrictions.
* Required source attribution.

## Comparison with Freddie Mac

| Dimension | Freddie Mac | Fannie Mae |
| --- | --- | --- |
| Recommended role | MVP primary candidate | Alternative primary / backup |
| Data type | Loan-level origination and monthly performance | Acquisition and performance data |
| Main use | Credit performance monitoring | Credit performance monitoring |
| MVP complexity | Chosen first to reduce scope | Use if Freddie Mac is unsuitable |
| Field mapping | Requires current file layout confirmation | Requires current file layout confirmation |

## When to Choose Fannie Mae Instead of Freddie Mac

Choose Fannie Mae if:

* Freddie Mac access becomes unsuitable.
* Freddie Mac documentation or file layout is not convenient for MVP.
* Fannie Mae provides a clearer or smaller official sample for the selected use case.
* Fannie Mae terms better support GitHub-safe demonstration.

## Mapping Notes for Monitoring Tables

Fannie Mae may support:

* `daily_risk_metrics.csv` as period-level aggregated risk metrics, likely monthly rather than daily.
* `segment_risk_metrics.csv` using acquisition fields and performance outcomes.
* `score_distribution.csv` if score fields are available and documented.
* `feature_drift_metrics.csv` for selected public fields.

Fannie Mae likely does not support:

* `strategy_rule_metrics.csv`
* Internal manual review metrics.
* Internal fraud strategy metrics.
* Production model monitoring metrics without later modeling scope.

