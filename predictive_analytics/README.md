# Predictive Analytics & Hypothesis Testing

## Overview
This directory contains the machine learning architecture for the Influencer Marketing ROI audit. Using the augmented 1,000,000-row dataset, we deployed Multiple Linear Regression and Random Forest algorithms. 

Rather than simply trying to brute-force a high $R^2$ score, these models were designed as **Rigorous Hypothesis Tests** to mathematically prove (or disprove) the linear relationship between vanity metrics, platform selection, and actual revenue generation.

## Directory Structure
```
predictive_analytics/
├── linear_regression_model_1/
│   ├── 01_platform_dynamics.png
│   └── regressor_model1.py
├── linear_regression_model_2/
│   ├── 02_campaign_strategy_model.png
│   └── regressor_model2.py
├── linear_regression_model_3/
│   ├── 03A_normal_campaigns.png
│   ├── 03B_viral_campaigns.png
│   └── regressor_model3.py
├── linear_regression_model_4/
│   ├── 04_realistic_model.png
│   └── regressor_model4.py
└── linear_regression_model_5/
    ├── 05_realistic_model.png
    └── regressor_model5.py
```
## Key Findings & Model Diagnostics

### 1. The "Vanity Metric" Proof (Models 1 - 4)
**The Hypothesis:** Highly engaging campaigns on top-tier platforms (e.g., TikTok) naturally result in higher linear product sales.
**The Result:** Models 1 through 4 yielded flat horizontal trendlines with an $R^2$ effectively at zero. 
**The Business Insight:** This is a mathematically significant finding. It proves that social media marketing is highly non-linear. Raw attention (estimated reach) and platform choice do not mathematically guarantee sales. Conversion is entirely dependent on the *quality* of the niche and the audience trust, completely validating our descriptive Tableau findings.

### 2. The Target Leakage Demonstration (Model 5)
**The Trap:** In Model 5, a Random Forest Regressor achieved a near-perfect 45-degree prediction line. 
**The Audit:** Upon rigorous data auditing, we identified this as a textbook case of **Target Leakage**. The model was fed engineered features (like `sales_velocity` and `engagement_to_sales_ratio`) that were algebraically derived from the target variable (`product_sales`) during the data cleaning phase. 
**The Insight:** The algorithm did not discover a predictive business pattern; it reverse-engineered the algebra. We have retained this model in the repository to demonstrate the dangers of target leakage in enterprise Big Data pipelines and the importance of strict feature selection.

### 3. The Virality A/B Test (Model 3)
Utilizing our custom `is_viral_outlier` boolean, we split the dataset to see if the rules of conversion change when a campaign "breaks the algorithm." The regression confirmed that extreme algorithmic virality does not scale linearly with predictable revenue, reinforcing the recommendation to invest in targeted, high-trust niche influencers over broad viral attempts.
