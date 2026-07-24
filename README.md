# Retail Analytics: Predicting Customer Responses and Optimizing Promotions

## Project Overview

This business analytics project examines how customer characteristics, spending, purchase activity, and earlier campaign acceptance relate to response in the latest marketing campaign. The goal is to help the marketing team prioritize stronger customer segments for the next promotion.

## Interactive Dashboard

[Open the interactive campaign response dashboard](https://retail-promotion-response-dashboard.arpit2432.chatgpt.site)

The dashboard has no global filters, so the KPI cards and core campaign-history view always show the complete customer population. Two chart-specific controls support focused analysis without changing the rest of the dashboard:

- A dropdown switches the response comparison between age, income, and spending.
- An age-group selector applies only to the preferred purchase-channel chart.

### KPI widgets

- Latest campaign responders
- Latest campaign non-responders
- Customers who accepted at least one previous campaign
- Total customers

### Dashboard visuals

1. Latest response likelihood by number of previous campaigns accepted
2. Latest response and previous acceptance by age, income, or spending
3. Preferred purchase channel: web, store, catalogue, or tied channels
4. Product-category spending: latest responders vs non-responders
5. Latest response rate by recency
6. Latest and previous campaign response by customer tenure cohort

The dashboard displays the exact Low, Medium, High, and Very High spending-band definitions beside the spending view.

The recommendation panel connects these findings to future campaign decisions:

- who to prioritize using previous response history and recency;
- what to promote using product-category spending;
- where to deliver the offer using preferred purchase channel; and
- how to adapt loyalty or welcome messaging using customer tenure.

The source version is available at [`dashboard/index.html`](dashboard/index.html). It is a self-contained interactive HTML file and can also be downloaded and opened in a browser.

## Main Findings

- Previous campaign acceptance is the strongest historical prioritization signal. Latest response increased from 8.2% among customers with no earlier acceptance to 31.1% after one, 50.6% after two, and 79.5% after three previous acceptances.
- Very-high-spending customers recorded a 30.0% latest response rate, compared with 5.5% among low-spending customers.
- Customers purchasing within 30 days had a 23.9% latest response rate, compared with 5.6% among customers whose last purchase was more than 90 days ago.
- Latest responders spent more on average than non-responders in every product category, with the largest absolute differences in wine and meat.
- Customers who joined in 2012 had a higher latest response rate than the 2013 and 2014 join-year cohorts; tenure should be treated as a supporting loyalty signal.
- The 70K–100K income band had a 27.9% latest response rate; income should still be used with other behavior signals.
- Age differences were smaller, and the 18–30 segment contained only ten customers, so age should be treated as a supporting factor.

## Recommended Actions

- Prioritize customers who accepted one or more earlier campaigns.
- Within that audience, give additional priority to high spenders and recently engaged customers.
- Match the offer to the product categories responders value most and deliver it through the customer's preferred purchase channel.
- Use loyalty-led messaging for established customers and welcome or education-led offers for newer customers.
- Use age and income only as supporting segmentation factors.
- Test the prioritized audience against a control group before scaling the campaign.
- Track response rate, conversion value, and campaign cost in future campaigns to validate targeting effectiveness.

These findings describe historical response patterns and should not be presented as guaranteed predictions or as a validated machine-learning model.

## Repository Contents

```text
├── dashboard/
│   └── index.html
├── data/
│   └── marketing_campaign.xlsx
├── docs/
│   ├── Business_Requirements_Document.md
│   └── Data_Quality_Report.md
└── README.md
```

## Data Notes

- Dataset grain: one row per customer
- Customer records: 2,240
- Cleaned columns: 28
- Missing income values are retained as `Null` and shown as `Missing` in the dashboard.
- Ages above 100 are retained but shown as `Invalid/Unknown` for age-based analysis.
- `Alone`, `YOLO`, and `Absurd` marital-status values were grouped as `Others`.
- Constant columns `Z_CostContact` and `Z_Revenue` were removed.

## Tools Used

- Excel for limited source-data cleaning
- Tableau concepts for KPI and segmentation design
- HTML, CSS, and JavaScript for the interactive portfolio dashboard
