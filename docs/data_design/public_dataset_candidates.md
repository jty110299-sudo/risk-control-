# Public Dataset Candidates

## Purpose

Compare official public datasets that may support future Risk Control Agent monitoring demonstrations.

## Candidate 1: Fannie Mae Single-Family Loan Performance Data

### Overview

Fannie Mae provides loan performance data for a portion of its single-family mortgage loans. The dataset is relevant for credit performance monitoring and mortgage loan behavior analysis.

### Official Link

https://capitalmarkets.fanniemae.com/credit-risk-transfer/single-family-credit-risk-transfer/fannie-mae-single-family-loan-performance-data

### Data Owner

Fannie Mae.

### Data Content

The source includes loan performance data and documentation for single-family mortgage loans. Public materials indicate that the offering includes loan origination or static fields and monthly performance fields.

### Suitable Project Use Cases

* Credit Risk Monitoring for mortgage loan performance.
* Delinquency or default trend monitoring after field definitions are confirmed.
* Vintage, segment, and cohort-style analysis.
* Loan performance aggregation into monitoring tables.

### What Metrics Can Be Derived

* Delinquency-related metrics, subject to field mapping.
* Bad-rate style metrics, subject to documented outcome definition.
* Segment-level performance metrics.
* Population or cohort shifts based on available origination fields.

### What Metrics Cannot Be Derived

* Application approval or denial rates.
* Internal manual review rate.
* Internal strategy rule hit rate.
* Confirmed fraud rate, unless a relevant public field is verified.

### Limitations

The data is mortgage-specific and may not represent all consumer credit products. It may not include full application funnel information or internal risk strategy fields. Source terms and file layouts must be reviewed before any data acquisition.

### Access Notes

Use official download instructions and documentation only. Do not upload large raw files to GitHub.

### Recommendation

Suitable as a primary dataset candidate for loan performance and credit risk monitoring.

## Candidate 2: Freddie Mac Single-Family Loan-Level Dataset

### Overview

Freddie Mac provides a public single-family loan-level dataset containing loan origination and monthly performance data for covered loans.

### Official Link

https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset

### Data Owner

Freddie Mac.

### Data Content

The dataset contains loan-level origination data and monthly performance data. Official documentation describes coverage, file layouts, user guidance, and interpretation notes.

### Suitable Project Use Cases

* Primary Credit Risk Monitoring demonstration.
* Delinquency, default, and loss-related monitoring after field confirmation.
* Segment risk analysis by loan, borrower, property, or acquisition fields that are available in the public layout.
* Cohort and vintage performance review.

### What Metrics Can Be Derived

* Delinquency-related metrics.
* Bad-rate or default-style metrics if definitions are documented.
* Loss-related metrics if relevant fields are used.
* Segment contribution metrics.
* Feature distribution and drift-style monitoring from public fields.

### What Metrics Cannot Be Derived

* Full application funnel approval or denial rates.
* Internal manual review rates.
* Internal rule hit rates.
* Fraud strategy outcomes.

### Limitations

The dataset is specific to Freddie Mac covered loans and is not a full lending application dataset. It may not represent all mortgage or credit populations. Terms of use, privacy rules, and documentation must be reviewed before use.

### Access Notes

Use the official Freddie Mac dataset page and user guide. Dataset download access may be provided through Freddie Mac systems referenced by the official resource page.

### Recommendation

Suitable as a primary dataset candidate for loan performance and credit risk monitoring.

## Candidate 3: CFPB / FFIEC HMDA Data

### Overview

HMDA data provides public mortgage application and lending activity information. It is useful for application, approval, denial, loan, borrower, property, geography, and lender field analysis.

### Official Link

https://www.consumerfinance.gov/data-research/hmda/

### Data Owner

CFPB and FFIEC public HMDA data infrastructure.

### Data Content

HMDA contains loan application records and action taken information, with borrower, loan, property, geography, and lender fields subject to public disclosure and privacy modifications.

### Suitable Project Use Cases

* Application volume monitoring.
* Approval and denial monitoring.
* Segment analysis by geography, lender, product, loan purpose, or borrower attributes where appropriate and privacy-safe.
* Auxiliary data source for application-stage monitoring.

### What Metrics Can Be Derived

* Application count.
* Approval or denial rates based on action taken fields.
* Segment-level application and action distribution.
* Population mix changes across public HMDA dimensions.

### What Metrics Cannot Be Derived

* Post-origination delinquency or default performance.
* Internal manual review rate.
* Internal strategy rule hit rate.
* Confirmed fraud rate.
* Model monitoring metrics without a separate modeling scope.

### Limitations

HMDA is application and lending activity data, not monthly loan performance data. Public files may be privacy-modified. It should not be used to claim repayment performance or default monitoring without another outcome source.

### Access Notes

Use CFPB and FFIEC official pages or the HMDA Platform. Do not upload full public raw data files to GitHub.

### Recommendation

Suitable as an auxiliary dataset for application and approval monitoring.

## Candidate Ranking

1. Freddie Mac Single-Family Loan-Level Dataset - MVP primary candidate.
2. Fannie Mae Single-Family Loan Performance Data - alternative primary / backup.
3. CFPB / FFIEC HMDA - auxiliary application and approval dataset.
4. Synthetic supplements only for internal strategy-rule metrics or fraud indicators that public data cannot provide.

## Ranking Rationale

Freddie Mac is ranked first because it is an official public dataset with loan-level origination and monthly performance data, making it well aligned with the first MVP goal of credit performance monitoring.

Fannie Mae is ranked second because it also provides official acquisition and performance data suitable for credit risk monitoring, but the MVP should choose one primary source first to reduce field mapping and processing complexity.

HMDA is ranked third because it is highly useful for application, approval, denial, product, geography, and institution-level monitoring. However, HMDA is not a monthly loan performance dataset and should not be the only primary source for bad-rate or overdue-rate monitoring.
