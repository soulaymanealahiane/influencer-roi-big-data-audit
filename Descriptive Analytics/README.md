# Descriptive Analytics & Executive Benchmarking

## Overview
This directory houses the visual performance audit for the Influencer Marketing ROI project. Built entirely in Tableau using the augmented 1,000,000-row dataset, these interactive dashboards translate complex, engineered Key Performance Indicators (KPIs) into actionable, executive-ready insights. 

The primary objective of this phase is to move beyond raw vanity metrics (likes, followers) and visually benchmark structural marketing efficiency across platforms, content strategies, and influencer niches.

## Directory Contents
* `dashboard1.twbx`: Platform Performance Dashboard
* `dashboard2.twbx`: Campaign Type Performance Dashboard
* `dashboard3.twbx`: Influencer Category Performance Dashboard

## Dashboard Architecture & Analysis

### 1. Platform Performance Dashboard (`dashboard1.twbx`)
**Objective:** Evaluate the baseline ROI efficiency and content virality native to different social media platforms (Instagram, TikTok, Twitter, YouTube), holding raw reach equal.

* **Top Performing Platforms by Conversion:** A ranked bar chart identifying which platforms generate the highest absolute `engagement_to_sales_ratio`.
* **The Decay Curve (Optimal Campaign Duration):** Plots `Daily Engagement Velocity` against `Campaign Duration Days` to visualize momentum drop-off, mathematically proving that peak engagement is exhausted within the first 2–4 days of a campaign.
* **The Vanity Filter (Performance Map):** A 4-quadrant scatter plot mapping `True Engagement Rate` against `Engagement to Sales Ratio`. This visually isolates platforms that drive pure attention versus those that successfully funnel that attention into revenue.
* **Performance vs. Benchmark:** A dual-bar visualization utilizing custom engineered indices to highlight which platforms overperform or underperform the aggregate baseline (Index > 1.0) for both reach and conversion.

### 2. Campaign Type Performance Dashboard (`dashboard2.twbx`)
**Objective:** Determine the most effective content format (e.g., Giveaways, Product Launches, Event Promotions) for maximizing both immediate revenue and algorithmic spread.

* **Format Efficiency Ranking:** Highlights which campaign structures lead to the highest absolute conversion rates, proving that formats like Event Promotions and Product Launches are superior for bottom-funnel sales.
* **Engagement vs. Conversion Matrix:** Maps content types to reveal strategic trade-offs. For example, it visualizes how "Giveaways" generate massive top-funnel engagement but often fail to match the revenue efficiency of targeted "Brand Awareness" pushes.
* **Duration Optimization:** Applies the decay curve specifically to campaign types to ensure marketing budgets aren't wasted on prolonged, low-momentum active days.

### 3. Influencer Category Performance Dashboard (`dashboard3.twbx`)
**Objective:** Uncover the deepest layer of audience trust by benchmarking which specific influencer niches (Tech, Beauty, Gaming, Travel, etc.) actually convert their followers' attention into measurable growth.

* **Niche Conversion Leaders:** Identifies categories like "Tech" and "Gaming" as the strongest drivers of direct sales, regardless of their total market share.
* **Isolating Vanity Niches:** The performance scatter plot explicitly separates highly engaging but poorly converting categories (like Fashion and Travel) from high-efficiency categories. This is a critical tool for budget reallocation.
* **Baseline Underperformance Tracking:** Exposes exactly how many influencer categories mathematically underperform the cross-industry benchmark, ensuring future campaigns are targeted only at highly efficient niches.

## Strategic Value
These dashboards bridge the gap between heavy data engineering and business strategy. By visualizing the custom benchmarking indices (`benchmark_index_true_engagement_rate`, `benchmark_index_reach_to_sales_conversion_rate`), stakeholders can immediately identify areas of budget waste and reallocate resources toward mathematically proven combinations of platforms, formats, and niches.
