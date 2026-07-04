# Public Dataset Strategy

## Purpose

Define the Phase 2 data strategy for Risk Control Agent.

Risk Control Agent will use official or authoritative public datasets as the primary data foundation whenever possible.

Synthetic data will only be used as a clearly labeled supplement when public datasets do not contain required internal monitoring fields.

## Why Public Datasets Are Preferred

Official or authoritative public datasets provide more realistic structures, field definitions, time windows, and data limitations than a fully synthetic dataset. For a credit risk monitoring portfolio project, public datasets can better demonstrate how an analyst works with imperfect but credible source data.

Public datasets should be used for realistic credit risk monitoring demonstrations.

## Why Fully Synthetic Data Is Not Ideal as the Main Data Source

Fully synthetic data can make demonstrations easy to control, but it may hide important real-world issues:

* Public data often has missing fields, privacy modifications, and source-specific definitions.
* Loan performance data often requires careful time-window interpretation.
* Application data and post-origination performance data may live in different sources.
* A realistic monitoring system must document source limitations before coding.

## Public Dataset First Principle

The project prioritizes official or authoritative public datasets.

Public raw data should be treated as the foundation for field mapping, data cleaning design, aggregation planning, and future MVP monitoring tables.

## When Synthetic Supplements Are Allowed

Synthetic data is allowed only when public data does not contain necessary internal monitoring fields, such as:

* Strategy rule hit results.
* Manual review queue or review decision fields.
* Internal fraud strategy outcomes.
* Demo-only abnormal scenarios.
* Unit testing inputs in later coding phases.

Any synthetic fields or synthetic scenarios must be clearly labeled.

## Dataset Selection Criteria

Candidate datasets should be evaluated by:

* Official source and source owner.
* Documentation quality.
* Availability of origination or application fields.
* Availability of monthly performance or outcome fields.
* Ability to derive credit risk monitoring metrics.
* Privacy modification and usage restrictions.
* Suitability for GitHub portfolio demonstration.
* Limitations that must be disclosed before coding.

## Dataset Governance Principles

* All dataset sources must be recorded in `SOURCES.md`.
* Dataset limitations must be documented before coding.
* The project must not use real personal financial data.
* The project must not attempt to identify individuals.
* Derived monitoring tables must preserve source attribution.
* Public-data-derived metrics must be separated from synthetic supplements.

## GitHub Storage Policy

The project must not upload large raw datasets to GitHub.

The repository should store dataset download instructions, metadata, field mapping plans, and small derived samples only if license, privacy, and source terms allow.

## Privacy and Compliance Considerations

Public datasets may still contain sensitive or privacy-modified information. The project should avoid re-identification attempts, avoid unnecessary row-level publishing, and prefer aggregated monitoring outputs for demonstration.

## Final Recommendation for Phase 2

Use Freddie Mac or Fannie Mae loan performance data as the primary candidate for loan performance and credit risk monitoring. Use HMDA as an auxiliary dataset for application and approval monitoring. Use synthetic supplements only for internal strategy-rule metrics or fraud indicators that public data cannot provide.

## Phase 3 MVP Data Source Recommendation

For Phase 3 planning, the recommended MVP primary candidate is Freddie Mac Single-Family Loan-Level Dataset.

Rationale:

* It is an official public dataset.
* It includes loan-level origination data.
* It includes monthly performance data.
* It is suitable for demonstrating post-origination credit performance monitoring, delinquency status analysis, risk migration, and segment risk analysis.
* It provides user guide, file layout, release notes, and sample-related resources that can support reproducible field mapping.

Fannie Mae Single-Family Loan Performance Data remains the alternative primary or backup source. HMDA remains an auxiliary dataset for application and approval monitoring.

Large raw public datasets should not be committed to GitHub. Phase 3 designs the acquisition and sampling plan only.
