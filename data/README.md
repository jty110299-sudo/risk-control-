# Data Directory

## Purpose

This directory defines the future data storage structure for Risk Control Agent.

It is intended to support reproducible, GitHub-safe data preparation for official public datasets, small allowed samples, metadata templates, and later derived monitoring tables.

## Directory Structure

```text
data/
├── README.md
├── raw/
├── external/
├── interim/
├── processed/
├── samples/
│   └── official/
└── metadata/
```

## What Can Be Stored Here

* `data/metadata/`: source metadata templates, download logs, field layout verification checklists, and download instructions.
* `data/samples/official/`: small official sample files only if source terms allow and source, size, access date, and usage are documented.
* `data/samples/`: small license-safe demonstration samples in later phases, if allowed.
* `data/processed/`: derived aggregated monitoring tables in later phases, only when privacy-safe, license-safe, and clearly attributed.

## What Must Not Be Stored Here

* Large full raw Freddie Mac, Fannie Mae, or HMDA datasets committed to GitHub.
* Restricted official files.
* Real personal identifiers.
* Private financial institution data.
* Data that violates source terms.
* Unlabeled synthetic supplements.

## GitHub Upload Policy

Large raw official datasets must not be committed to GitHub.

Raw downloaded files should stay local under `data/raw/` and be ignored by Git.

Small official sample files may be stored only if source terms allow.

Derived small samples may be committed only if license-safe, privacy-safe, clearly attributed, and small enough for GitHub demonstration.

## Official Dataset Policy

All official public data sources must be documented with:

* Dataset name
* Data owner
* Official source link
* Access date
* Download date
* File version
* User guide version
* File layout version
* File size
* Intended project use
* License or terms notes

## Small Sample Policy

Small samples are allowed only when:

* The source is official or clearly documented.
* The file size is manageable.
* Source terms allow local project use.
* The file is not a full large raw dataset.
* The sample is recorded in metadata and download logs.

No official sample files have been downloaded yet.

## Synthetic Supplement Policy

Synthetic supplements must be explicitly labeled.

Synthetic supplements may only be used for missing internal monitoring fields, demo-only abnormal scenarios, or future testing needs.

## Source Attribution Requirement

All public-data-derived files must preserve source attribution and transformation notes. Public datasets must not be described as internal business data.

## Current Status

No full raw official datasets are stored in this repository at this phase.

No official sample files have been downloaded yet.

No final monitoring CSV files have been generated.

