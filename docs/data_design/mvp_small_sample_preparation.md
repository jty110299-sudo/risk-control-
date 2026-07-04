# MVP Small Sample Preparation

## Purpose

Define how a small MVP sample should be prepared in a later phase.

## Why MVP Sample Is Needed

The MVP sample should allow the project to demonstrate monitoring-table construction, metric calculation, alert logic, report generation, and future UI display without relying on full production-scale data.

## Why Full Raw Dataset Is Not Needed for MVP

The MVP sample should support monitoring-table construction, not full production-scale modeling.

Full raw datasets can be large, difficult to store safely, and unnecessary for first-version demonstration.

## Candidate Sample Options

* Official sample file if available.
* One small time window.
* One vintage cohort.
* One geography or segment if supported.
* Derived aggregated monitoring table.

## Recommended MVP Sample Strategy

Start with an official sample file if Freddie Mac provides a small, license-safe file. If not, define a narrow time window or vintage cohort and derive aggregated monitoring tables locally without committing raw data.

## Sample Acceptance Criteria

* Official source is documented.
* Source terms allow use.
* File size is manageable.
* File layout version is verified.
* Metadata and download log are complete.
* No real personal identifiers are included.
* The sample can support at least basic monitoring-table construction.

## Minimum Fields Required

Minimum fields should support:

* Reporting period.
* Loan or record identifier suitable for aggregation.
* Origination or static dimensions.
* Performance status.
* Delinquency or default proxy field if available.
* Segment fields such as score band, LTV band, product, geography, or cohort if available.

## Risk Metrics That MVP Sample Should Support

* Loan count by period.
* Delinquency or overdue-style rate.
* Bad-rate proxy if definition is documented.
* Segment-level performance rate.
* Segment contribution to risk movement.

## Metrics Excluded from MVP

* `manual_review_rate`
* `rule_hit_rate`
* `fraud_rate`
* Production model AUC or KS unless a later modeling scope is defined.
* Internal strategy-rule metrics.

## Synthetic Supplement Conditions

Synthetic supplements may be used only for missing internal monitoring fields or demo-only abnormal scenarios. They must be clearly labeled and separated from public-data-derived fields.

## How to Document Sample Construction

Document:

* Source file name.
* Source link.
* Access and download dates.
* File version.
* User guide and file layout versions.
* Sampling logic.
* Filtering logic.
* Aggregation logic.
* Output file names.
* Source attribution.

## How to Avoid GitHub Data Bloat

* Do not commit large raw files.
* Use `.gitignore` to exclude raw and interim data.
* Commit only small derived samples if allowed.
* Prefer metadata, instructions, and aggregated examples over raw data.

