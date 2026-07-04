# MVP Sample Construction Plan

## Purpose of MVP Sample

The MVP sample should support credit risk monitoring, trend analysis, segment comparison, and report generation without requiring full raw dataset storage in GitHub.

MVP sample should be small enough for local development and GitHub demonstration, but rich enough to support risk monitoring, trend analysis, segment comparison, and report generation.

## Why Full Raw Dataset Is Not Required for MVP

The MVP only needs enough data to demonstrate the monitoring workflow, field mapping, aggregation logic, and report structure. Full raw datasets can be large, difficult to store, and unnecessary for first-version validation.

## Candidate Sample Size Strategy

Future sampling should target a small, manageable file or derived table size. Candidate approaches:

* Use an official sample file if available and source terms allow.
* Use one or a few selected origination quarters.
* Use a limited reporting-period window.
* Use a documented random sample only after source terms and field layout are reviewed.
* Prefer aggregated monitoring tables for GitHub demonstration.

## Candidate Time-Window Strategy

Candidate time windows:

* A recent but stable historical period.
* A limited range of monthly performance periods.
* A window long enough to show delinquency and trend behavior.
* A window with documented start and end dates.

The selected period must be documented before processing.

## Candidate Segment Strategy

Candidate segment dimensions may include:

* Origination period.
* Product or loan purpose if available.
* Property type if available.
* Geography if available and safe.
* Credit score band if available.
* Loan-to-value band if available.
* Delinquency or performance status band.

Segments should be selected based on public fields and privacy-safe aggregation.

## Constructing Aggregated Monitoring Tables

Future derived tables may be built by:

1. Selecting documented source files.
2. Understanding raw file layout.
3. Mapping source fields to monitoring fields.
4. Filtering to the MVP sample window.
5. Aggregating by period and segment.
6. Calculating supported metrics.
7. Excluding unsupported metrics or labeling synthetic supplements.
8. Preserving source metadata and transformation notes.

No sample files were generated in Phase 3 or Phase 4.

Phase 4 prepares metadata templates, download instructions, and quality checklists. Sample construction begins only after source terms, file size, and file layout are verified.

## Preserving Source Attribution

Every derived table should include or be accompanied by:

* Source dataset name.
* Source URL.
* Access date.
* File version or release notes.
* User guide version.
* Field layout version.
* Transformation summary.

## Fields That Can Be Derived from Public Data

Depending on confirmed Freddie Mac or Fannie Mae fields, public data may support:

* Loan counts.
* Monthly performance status.
* Delinquency or overdue-style indicators.
* Default or bad-rate-style proxies with documented definitions.
* Segment-level performance metrics.
* Score-band or LTV-band distributions if fields are available.

HMDA may support:

* Application count.
* Approval or denial action distribution.
* Geography-level application patterns.
* Product and institution-level application monitoring.

## Fields Excluded from MVP

Fields should be excluded from MVP if they cannot be derived from public data:

* Internal manual review rate.
* Internal strategy rule hit rate.
* Fraud strategy outcome.
* Production model score.
* Internal approval policy changes.

## Fields That May Require Synthetic Supplement Later

Synthetic supplements may be considered later for:

* `manual_review_rate`
* `rule_hit_rate`
* `fraud_rate`
* Strategy-rule outcomes.
* Demo-only abnormal scenarios.

All synthetic fields must be explicitly labeled.

## Quality Checks Before Using the Sample

Before any MVP sample is used:

* Confirm source terms.
* Confirm file layout.
* Confirm field definitions.
* Check missingness and value ranges.
* Check duplicate records.
* Check reporting period consistency.
* Validate aggregation counts.
* Document all exclusions and transformations.
* Confirm GitHub safety before committing any derived sample.
