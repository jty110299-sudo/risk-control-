# Data Directory Plan

## Purpose

Design the future data directory structure for Risk Control Agent. This document does not create data files.

## Proposed Future Structure

```text
data/
├── README.md
├── raw/
│   └── .gitkeep
├── external/
│   └── .gitkeep
├── interim/
│   └── .gitkeep
├── processed/
│   └── .gitkeep
├── samples/
│   └── .gitkeep
└── metadata/
    └── .gitkeep
```

## Directory Purpose

| Directory | Purpose | GitHub policy |
| --- | --- | --- |
| `data/raw/` | Future location for original downloaded source files. | Should not be committed if it contains large official datasets. |
| `data/external/` | Future location for third-party reference files or official samples. | Commit only if allowed by source terms and file size is safe. |
| `data/interim/` | Future location for temporary cleaned or joined files. | Usually excluded from GitHub. |
| `data/processed/` | Future location for derived aggregated monitoring tables. | May contain derived aggregated outputs in later phases if privacy-safe and license-safe. |
| `data/samples/` | Future location for small demonstration samples. | May contain small license-safe samples if allowed. |
| `data/metadata/` | Future location for source metadata, field layout notes, and download instructions. | Should be committed when it contains documentation only. |

## Data README Requirements

Future `data/README.md` should explain:

* What files can be stored locally.
* What files can be committed to GitHub.
* Which directories are excluded by `.gitignore`.
* Source attribution requirements.
* Whether files are public-data-derived or synthetic supplements.
* That large raw official datasets should not be committed.

## Current Phase Decision

Phase 3 only creates this directory plan. It does not create the `data/` directory and does not add data files.

If a future phase creates empty directories with `.gitkeep`, it must ensure that no raw data, CSV sample, or restricted file is added without documented source terms and storage policy.

