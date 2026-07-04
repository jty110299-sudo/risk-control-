# Public Dataset Acquisition Plan

## Purpose

Define how Risk Control Agent should acquire official public datasets in future phases without downloading full large raw datasets during Phase 3 or Phase 4.

## Dataset Acquisition Principles

* Public official datasets are preferred over fully synthetic data.
* The MVP should use a small, manageable, license-safe, GitHub-safe sample or derived monitoring table.
* Large raw public datasets should not be committed to GitHub.
* Dataset source, access date, file version, user guide version, and transformation logic must be documented.
* If a field cannot be derived from public data, it should be excluded from MVP or clearly marked as synthetic supplement.
* The project should not use real personal identifiers.
* The project should not attempt to re-identify individuals.
* The project should not claim the public dataset represents the author's own business data.
* All derived datasets must preserve source attribution.
* The Agent remains a monitoring and analysis assistant, not an autonomous credit decision engine.

## Primary Candidate Dataset

Freddie Mac Single-Family Loan-Level Dataset is the MVP primary candidate.

Reasons:

* Official public data source.
* Contains loan-level origination data.
* Contains monthly performance data.
* Suitable for credit performance monitoring, delinquency status analysis, risk migration, and segment-level risk analysis.
* Provides user guide, file layout, release notes, and related documentation.

Future phases must confirm the active user guide, release notes, file layout, and disclosure change version before processing.

## Backup Candidate Dataset

Fannie Mae Single-Family Loan Performance Data is the alternative primary or backup candidate.

Reasons:

* Official public data source.
* Contains acquisition data and performance data.
* Suitable for mortgage credit performance monitoring.
* Can support analysis similar to Freddie Mac if Freddie Mac access, documentation, or field layout constraints become unsuitable.

## Auxiliary Dataset

CFPB / FFIEC HMDA Data is the auxiliary dataset.

It is suitable for application volume, approval and denial action, product type, geography, and institution-level analysis. It is not suitable as the sole primary data source for bad-rate, overdue-rate, delinquency, or monthly loan performance analysis.

## What Will Be Downloaded in Future Phases

Future phases may download:

* Official user guides.
* Official file layout documents.
* Official sample files, if provided and allowed.
* Small, documented extracts or samples if source terms allow.
* Derived aggregated monitoring tables if privacy-safe and license-safe.

In Phase 4, no official sample files were downloaded. The project prepares directory structure, metadata templates, and manual download instructions first.

## What Will Not Be Downloaded

The project should not download full large Freddie Mac, Fannie Mae, or HMDA datasets during Phase 3.

The project should not download restricted files, private financial institution data, or files whose terms do not allow portfolio use.

## Large Raw Data GitHub Policy

The project should not commit large raw public datasets to GitHub. Instead, it should store download instructions, source metadata, field mapping documents, and small derived samples only when allowed.

## Version and Access-Date Tracking

Every future dataset use should document:

* Source name.
* Source URL.
* Access date.
* File version or release date if available.
* User guide version.
* File layout version.
* Transformation logic.
* Derived file creation date.

## Manual Download vs Scripted Download Policy

Manual download is preferred for early MVP setup because it forces review of source terms and documentation.

Scripted download should be considered only after:

* Source terms allow automated access.
* The source file version is documented.
* Large raw files are excluded from GitHub.
* Download paths and credentials are not committed.

## Phase 4 Preparation Requirements

Before any future download:

* Complete `data/metadata/dataset_metadata_template.md`.
* Complete or copy `data/metadata/download_log_template.md`.
* Complete `data/metadata/field_layout_verification_checklist.md`.
* Confirm `.gitignore` excludes large raw and interim files.
* Confirm whether the file is a full dataset, official sample, or derived extract.

## Risk and Compliance Notes

Public datasets may still be privacy-modified or subject to redistribution terms. The project must not attempt re-identification, must preserve source attribution, and must not present public data as proprietary internal business data.
