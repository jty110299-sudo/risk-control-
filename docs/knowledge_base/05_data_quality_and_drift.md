# Data Quality and Drift Monitoring

## Purpose

Define data quality and drift checks that must precede strong business conclusions in future Agent analysis.

## Core Principle

If data quality is abnormal, the Agent should avoid making strong business conclusions before data validation.

如果数据质量异常，Agent 不应在数据校验前给出强业务结论。

## Monitoring Items

| Issue | Meaning | Risk to analysis | Investigation direction |
| --- | --- | --- | --- |
| Missing rate increase | Required fields become more often empty. | Metrics and model inputs may be biased. | Check upstream source, schema, ingestion logic. |
| Outlier increase | Extreme values increase unexpectedly. | Averages, score inputs, and segment metrics may distort. | Check value ranges, unit changes, duplicate records. |
| Data delay | Expected data arrives late. | Current-day metrics may be understated. | Check refresh time, source availability, batch status. |
| Duplicate records | Same event or user appears more than expected. | Counts and rates may be inflated. | Check primary keys and deduplication rules. |
| Schema change | Columns are added, removed, renamed, or typed differently. | Calculation logic may fail or misread fields. | Review data contract changes. |
| Field definition change | Meaning of a field changes while name remains the same. | Historical comparison becomes unreliable. | Confirm business definition and mapping. |
| Sample size abnormal change | Record count differs materially from baseline. | Rate stability and representativeness may weaken. | Decompose by channel, product, region. |
| Feature drift | Feature distribution changes from baseline. | Model behavior may become less reliable. | Review CSI, feature means, missingness. |
| Score distribution drift | Score bands shift from baseline. | Risk ranking and approval mix may change. | Review PSI and score-band migration. |
| Population mix change | Composition changes by channel, product, region, or customer type. | Portfolio-level metrics may mask segment shifts. | Segment decomposition. |
| Channel traffic shift | Traffic mix moves between acquisition channels. | Risk changes may reflect mix rather than segment deterioration. | Compare channel volume and bad rate. |

## Key Principles

* Data validation should precede strong interpretation.
* Data issues must be disclosed in future reports.
* Drift is a signal for investigation, not proof of outcome deterioration.
* Segment analysis is required when population mix changes.

