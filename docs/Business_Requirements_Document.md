**BUSINESS REQUIREMENTS DOCUMENT**

**Retail Promotion Response  
Optimization Dashboard**

Understanding customer response to improve retail promotions

| **Project sponsor / manager** | Saurabh                                             |
|-------------------------------|-----------------------------------------------------|
| **Prepared by**               | Business Analyst, PromoScope Insights               |
| **Submission date**           | 20 July 2026                                        |
| **Document status**           | Draft                                               |
| **Version**                   | 1.0                                                 |
| **Data source**               | Marketing campaign dataset (2,240 customer records) |

# 1. Executive Summary

PromoScope Insights will develop an analytical dashboard to explain
which customer segments respond to retail promotions and how response
differs by demographic, household, spending, and purchasing-channel
characteristics. The solution will provide evidence-based insights and
an interpretable propensity view to help marketing teams target future
promotions more efficiently and improve campaign return on investment.

# 2. Project Objectives

- Measure key campaign results, including total customers, responders,
  non-responders, response rate, and acceptance of previous campaigns.

- Identify customer groups with higher and lower response rates based on
  age, education, marital status, income, household details, recency,
  spending, and purchase behavior.

- Use past campaign and customer behavior to identify the main factors
  linked with response and highlight customers who may be more likely
  to respond to future promotions.

- Create an interactive dashboard that allows users to filter results
  and compare customer groups, response rates, spending, and purchase
  channels.

- Provide clear recommendations for future promotions, supported by
  dashboard findings and important data limitations.

# 3. Project Scope

## 3.1 In Scope

- Review the provided customer and campaign dataset and check it for
  missing, duplicate, or unusual values.

- Analyze customer details such as age, education, marital status,
  income, household composition, registration date, and recency.

- Study product spending, web visits, deal purchases, and purchases made
  through web, catalog, and store channels.

- Compare acceptance of previous campaigns with response to the latest
  campaign.

- Calculate important measures such as total customers, responders,
  non-responders, and response rate.

- Create useful customer groups, such as age and income bands, to
  compare response patterns.

- Build an interactive dashboard and summarize the main findings and
  recommendations for future promotions.

## 3.2 Out of Scope

- Running or managing an actual marketing campaign.

- Connecting the dashboard to a live CRM or other business system.

- Collecting new customer information or using outside data.

- Making changes to product prices, discounts, or campaign content.

- Calculating the actual financial return because campaign cost and
  profit data are not available.

- Automatically sending promotions to customers.

# 4. Stakeholders and Responsibilities

| **Stakeholder**            | **Responsibility**                                                                             |
|----------------------------|------------------------------------------------------------------------------------------------|
| Project Manager — Saurabh  | Approves the scope, reviews progress, and accepts the final project.                           |
| Business Analyst           | Defines requirements, analyzes business needs, reviews findings, and prepares recommendations. |
| Marketing Manager          | Explains campaign needs and checks whether the findings are useful for future promotions.      |
| Data Analyst               | Checks the data, performs the analysis, and supports the calculation of results.               |
| BI Developer               | Creates the dashboard, filters, charts, and calculations.                                      |
| Data Privacy Officer       | Ensures customer data is used and shared responsibly.                                          |
| Senior Marketing Executive | Reviews the final insights and makes campaign-related decisions.                               |

# 5. Business Requirements

Priority levels: High = essential; Medium = important; Low = optional
enhancement.

| **ID** | **Priority** | **Requirement**                                                                                                                 | **Purpose**                                                          |
|--------|--------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| BR-01  | High         | Check and prepare the supplied customer and campaign data, documenting how missing or unusual values are handled.               | Make sure the analysis is reliable and easy to reproduce.            |
| BR-02  | High         | Calculate total customers, responders, non-responders, response rate, and acceptance results for previous campaigns.            | Provide a clear summary of campaign performance.                     |
| BR-03  | High         | Compare response across customer details, including age, education, marital status, income, household composition, and recency. | Identify customer groups with different response patterns.           |
| BR-04  | High         | Compare response with product spending and purchases made through web, catalog, store, and deal channels.                       | Understand how spending and purchase behavior relate to response.    |
| BR-05  | High         | Create an interactive dashboard with filters and show both customer count and response rate when comparing groups.              | Make the dashboard easy to explore and avoid misleading comparisons. |
| BR-06  | Medium       | Compare acceptance across previous campaigns and the latest campaign using clear labels.                                        | Understand how campaign response has differed across campaigns.      |
| BR-07  | Medium       | Summarize the main findings and recommend customer groups for future campaign testing.                                          | Support better targeting decisions without overstating the results.  |
| BR-08  | Low          | Provide short instructions explaining the dashboard filters and measures.                                                       | Help users understand and reuse the dashboard.                       |

# 6. Constraints and Assumptions

## 6.1 Constraints

- The project uses only the provided dataset of 2,240 customer records.

- The data is historical and may not represent current customer
  behavior.

- Campaign cost, profit, offer details, and control-group data are not
  available.

- The project does not have access to a live CRM or other company
  systems.

- Missing or unusual values may limit some parts of the analysis.

## 6.2 Assumptions

- Each customer ID represents one customer.

- Response represents acceptance of the latest campaign.

- AcceptedCmp1 to AcceptedCmp5 represent five separate earlier
  campaigns.

- The spending and income fields use the same currency, although the
  currency is not stated.

- The available data is sufficient to identify general response
  patterns.

# 7. Cost–Benefit Analysis

Exact financial values cannot be calculated because employee costs,
campaign costs, sales profit, and expected improvement are not provided.
Therefore, this section describes the expected costs and benefits in
simple business terms.

## 7.1 Expected Costs

| **Cost**        | **Description**                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Time and effort | Time spent on data review, analysis, dashboard creation, testing, and documentation. |
| Software        | Possible cost of dashboard or analytics software, depending on the tools used.       |
| Maintenance     | Time required to update the dashboard if new data becomes available.                 |

## 7.2 Expected Benefits

- Better targeting — helps the marketing team focus on customer groups
  that show stronger response.

- Time savings — reduces repeated manual analysis by using a reusable
  dashboard.

- Clearer decisions — provides one place to compare response, customer
  groups, spending, and purchase behavior.

- Lower promotion waste — may reduce unnecessary promotion spending by
  avoiding very broad targeting.

- Future improvement — provides useful ideas that can be tested in
  future campaigns.

## 7.3 Overall Assessment

The project is expected to offer a favorable, low-cost analytical
benefit because it uses an existing dataset and produces reusable
decision support. However, monetary ROI must remain unclaimed until
campaign cost, margin, and controlled outcome data are available.
