# Freddie Mac Download Instructions

## Purpose

Define safe, reproducible download instructions for Freddie Mac Single-Family Loan-Level Dataset resources.

## Why Freddie Mac Is MVP Primary Candidate

Freddie Mac remains the MVP primary candidate because it is an official public source with loan-level origination data, monthly performance data, user guide resources, file layout resources, release notes, and sample-related resources.

## Official Source Page

https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset

## Required Documents to Read Before Downloading

Review the following official resources before downloading any data file:

* General User Guide
* File Layout
* FAQ
* Release Notes
* Disclosure change resources
* Sample files if available

The official page may include both Pre-July 2026 and Effective July 2026 resources. Future phases must confirm which version applies to the selected sample or dataset.

## Recommended Download Order

1. Read the official dataset page.
2. Read the General User Guide.
3. Read the File Layout.
4. Read the FAQ.
5. Read the Release Notes.
6. Review disclosure changes and file header resources.
7. Only then consider official sample files or a small allowed sample.

## What to Download First

Future phases may download:

* User guide PDF.
* File layout spreadsheet.
* Release notes PDF.
* Official sample files, only if size, source terms, and intended use are verified.

## What Not to Download First

Do not download or commit the full Freddie Mac dataset before confirming file size, file layout, usage terms, and MVP sample strategy.

Do not download large raw files into the repository for exploratory analysis.

## Storage Location Recommendation

* Official small sample files, if allowed: `data/samples/official/`
* Large raw files, if downloaded locally in a later phase: `data/raw/` and ignored by Git
* Source metadata and download logs: `data/metadata/`
* Documentation and instructions: `docs/data_design/`

## Metadata Recording Requirement

Before using any downloaded file, record:

* Dataset name
* Source link
* Access date
* Download date
* File name
* File size
* File version
* User guide version
* File layout version
* Storage path
* License / terms notes
* Intended project use

## GitHub Restriction

Large raw official datasets must not be committed to GitHub.

Only small official samples or derived samples may be committed if source terms allow and metadata is complete.

## Field Layout Verification Requirement

No data processing should begin until the field layout verification checklist is complete.

## Next-Step Decision Tree

1. If source terms are unclear, do not download; document manual review needed.
2. If file size is large, do not commit; store locally only if needed later.
3. If official sample files are small and allowed, download only after metadata fields are prepared.
4. If no sample files are suitable, write manual download instructions and continue with field mapping design.
5. If layout version is uncertain, stop before processing.

