# Data Usage and GitHub Storage Policy

## Purpose

Define how public datasets, derived samples, metadata, and future monitoring outputs may be handled in this repository.

## Policy Rules

1. Do not upload large raw datasets to GitHub.
2. Do not upload data that violates source terms.
3. Store download instructions instead of raw official datasets.
4. Store small derived samples only if allowed.
5. Store aggregated monitoring outputs only when privacy-safe and license-safe.
6. Clearly document data source, access date, and transformation steps.
7. Do not use real personal identifiers.
8. Do not attempt to re-identify individuals.
9. Do not claim public data represents the project author's own business data.
10. All derived data must include source attribution.
11. Do not commit large raw official datasets.
12. Use `.gitignore` in later phases to exclude raw datasets.
13. Clearly label derived files.
14. Do not upload restricted files.
15. Do not include personal identifiers.
16. Raw downloaded files should stay local under `data/raw/` and be ignored by Git.
17. Small official sample files may be stored only if source terms allow.
18. Data preparation must happen before metric calculation, alerting, report generation, or UI implementation.

## Recommended Repository Practice

The repository should contain:

* Source links and access notes.
* Data dictionaries and field mapping plans.
* Download instructions.
* Transformation documentation.
* Small privacy-safe derived examples only if source terms allow.
* Source metadata, access date, file version, user guide version, and transformation notes.
* Metadata templates and download logs.

The repository should not contain:

* Full raw public datasets.
* Private financial institution data.
* Real personal identifiers.
* Data that violates source license or redistribution terms.
* Restricted official files.

## Key Principles

* Dataset governance should be documented before coding.
* Privacy and source terms take priority over demonstration convenience.
* Public data must not be misrepresented as proprietary business data.
* Public data and synthetic supplements must be separated and labeled clearly.
* All transformations must be reproducible.
