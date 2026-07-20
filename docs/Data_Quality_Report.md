# Data Quality Report

## 1. Dataset Summary

| Item | Result |
|---|---:|
| Customer records | 2,240 |
| Columns | 30 |
| Expected data level | One row per customer |
| Duplicate customer IDs | 0 |
| Exact duplicate rows | 0 |
| Latest-campaign responders | 334 |
| Latest-campaign response rate | 14.91% |
| Customer registration dates | 30 July 2012 to 29 June 2014 |

The dataset is suitable for exploratory customer and campaign analysis after the issues below are handled and documented.

## 2. Checks Performed

- Checked the number of rows and columns.
- Checked whether customer ID is complete and unique.
- Checked for exact duplicate rows.
- Checked missing values in every column.
- Reviewed customer registration dates.
- Reviewed the values used in education, marital status, campaign acceptance, response, and complaint fields.
- Checked numerical columns for negative values and unusually high or low values.
- Compared `Age` with `Year_Birth`.
- Checked for columns that contain only one value.

## 3. Main Findings

| Finding | Evidence | Why it matters | Severity | Recommended action |
|---|---|---|---|---|
| Missing income values | 24 of 2,240 records (1.07%) have no income value. | Income-based charts and groups may exclude these customers or give incomplete results. | Medium | Keep the records, label missing income clearly, and document how they are treated in each analysis. |
| Unusually high ages | Three customers have birth years of 1893, 1899, or 1900, producing ages above 120. | These values can distort age averages and age-group comparisons. | Medium | Flag the records and exclude them only from age-based analysis unless a correction rule is agreed. |
| Extreme income value | One customer has an income of 666,666, while 99% of recorded incomes are below 94,459. | This value can strongly affect average income and chart scale. | Medium | Check the record separately and use median, bands, or clearly documented outlier treatment where appropriate. |
| Uncommon marital-status labels | `Alone` (3), `Absurd` (2), and `YOLO` (2) appear in seven records (0.31%). | Very small or unclear categories can make charts difficult to understand. | Low | Keep the original data, but consider grouping these values into `Other` for reporting and document the rule. |
| Constant columns | `Z_CostContact` is always 3 and `Z_Revenue` is always 11. | Columns with one value cannot explain differences between customers. | Low | Exclude these columns from charts and segmentation while keeping them in the original dataset. |

## 4. Checks That Passed

- All 2,240 customer IDs are present and unique.
- No exact duplicate rows were found.
- No missing customer registration dates were found.
- Campaign acceptance, latest response, and complaint fields contain valid binary values of 0 and 1.
- No negative values were found in the reviewed income, spending, purchase-count, recency, household, or age fields.
- All `Age` values match `2024 - Year_Birth`; however, the three unusually old customers still require review.
- Education values are consistently recorded in five categories.

## 5. Effect on the Planned Analysis

The identified issues do not prevent the project from continuing. They mainly affect income-based and age-based comparisons. The original dataset should remain unchanged, while any exclusions, replacements, or grouping rules should be applied in the analysis layer and recorded in the project documentation.

## 6. Recommended Data-Preparation Rules

1. Keep the original dataset as a read-only source file.
2. Do not remove the 24 customers with missing income from analyses that do not use income.
3. Create a visible `Missing/Not Available` group when income bands are used.
4. Flag the three age records above 120 before creating age-based charts.
5. Review the income value of 666,666 separately before calculating averages.
6. Group very small marital-status labels into `Other` only for reporting, while retaining their original values in the source data.
7. Exclude the two constant columns from analysis because they do not add useful information.
8. Record every data-treatment decision so dashboard calculations can be explained and repeated.

## 7. Overall Data-Quality Assessment

**Status: Suitable for analysis with minor preparation.**

The dataset has a clear customer-level structure, unique IDs, no duplicate rows, and very limited missing data. A small number of unusual age, income, and marital-status values should be handled carefully, but they do not make the dataset unusable for this portfolio project.

