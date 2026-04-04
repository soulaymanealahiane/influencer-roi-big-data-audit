# Data Cleaning & Feature Engineering Pipeline

## Overview
This repository contains the preprocessing, cleaning, and feature engineering architecture for the Influencer Marketing ROI dataset. The objective of this pipeline is to transform raw interaction counts into normalized, statistically rigorous Key Performance Indicators (KPIs) and advanced benchmarking metrics suitable for enterprise Business Intelligence (Tableau) and predictive regression modeling.

### Data Sources & Project Links
* **Primary Dataset:** [150,000 Influencer Marketing Campaigns ROI Dataset](https://www.kaggle.com/datasets/tfisthis/influencer-marketing-roi-dataset?resource=download)
* **Analysis & Prediction Repo:** [BAI Project: Influencer Marketing ROI](https://www.kaggle.com/code/devraai/influencer-marketing-roi-analysis-and-prediction)

---

## Phase 1: Pre-Computation Cleaning (Mathematical Integrity)
Before any derived metrics or ratios could be computed, the dataset was sanitized to prevent critical mathematical failures during downstream statistical modeling.

* **Denominator Sanitization:** Scanned all foundational denominator columns (`estimated_reach`, `engagements`, and `campaign_duration_days`). Any instances containing a strict value of `0` were systematically replaced with `1`. This proactively prevents `NaN` or `Infinity` errors from breaking algorithms and dashboard calculations.

---

## Phase 2: Engineered KPIs (Dimensionality Expansion)
To transition from raw vanity metrics to normalized performance rates, 6 custom KPIs were engineered. These are segmented into three core evaluation verticals:

### 1. Engagement Analytics
* **`true_engagement_rate`** (`engagements / estimated_reach`)
  * *Purpose:* Measures the exact percentage of the exposed audience that actively interacted with the campaign.
* **`daily_engagement_velocity`** (`engagements / campaign_duration_days`)
  * *Purpose:* Measures interaction momentum, determining how many engagements a campaign generates on average per day.

### 2. Growth & Conversion
* **`reach_to_sales_conversion_rate`** (`product_sales / estimated_reach`)
  * *Purpose:* Measures pure visibility effectiveness—evaluating how well top-of-funnel exposure converts into measurable revenue.
* **`engagement_to_sales_ratio`** (`product_sales / engagements`)
  * *Purpose:* A deep analytic quality check. It verifies if highly engaged users are actually converting, effectively filtering out "vanity" or low-intent engagements.

### 3. Content Effectiveness
* **`sales_velocity`** (`product_sales / campaign_duration_days`)
  * *Purpose:* Measures immediate business impact speed—calculating how fast a specific content format drives actual revenue over time.
* **`reach_velocity`** (`estimated_reach / campaign_duration_days`)
  * *Purpose:* Acts as a proxy for "Virality"—tracking how quickly the content spreads across the platform algorithmically per day.

---

## Phase 3: Advanced Benchmarking (The "Secret Sauce")
To facilitate clean cross-sectional analysis in Tableau and accurate coefficient scaling in Python regression models, three advanced normalization columns were engineered:

* **`benchmark_index_true_engagement_rate`**
  * *Logic:* Compares every single campaign against its specific platform's average engagement rate. 
  * *Usage:* An index of `1.0` means it performed exactly at the platform average. An index of `2.5` means it outperformed the platform baseline by 150%. This is the ultimate normalized comparison metric.
* **`benchmark_index_reach_to_sales_conversion_rate`**
  * *Logic:* Applies the same benchmarking logic as above, but evaluates growth conversion (reach_to_sales_conversion_rate) strictly against platform-specific averages.
* **`is_viral_outlier`** (Boolean)
  * *Logic:* Utilizes the Interquartile Range (IQR) method, specifically applied to the true_engagement_rate metric to algorithmically flag extreme statistical anomalies (`True`/`False`).
  * *Usage:* Crucial for the statistical modeling team to run clean comparisons of means and baseline regressions without extreme viral outliers artificially skewing the $R^2$ or coefficient values.
