# Data Augmentation Pipeline: Scaling to 1 Million Rows

## Overview
This repository contains the data engineering pipeline designed to scale an Influencer Marketing ROI dataset from its original 150,000 records to 1,000,000 rows. The goal of this augmentation is to provide a massive, robust dataset for downstream multiple linear regression modeling and enterprise-level Business Intelligence (Tableau) visualizations.

Scaling tabular data for regression requires strict adherence to the original statistical distribution. Generating purely random data would destroy the linear correlations (and thus, the predictive power) of the dataset. Therefore, this pipeline utilizes a hybrid approach of **Bootstrapping** and **Vectorized Gaussian Noise Injection**.

## Implemented Augmentation Architecture

To generate 850,000 synthetic rows while maintaining mathematical integrity, the pipeline segments the dataset by datatype and applies specific statistical treatments to each.

### 1. Bootstrapping (Categorical & Structural Baseline)
For non-continuous variables (e.g., `platform`, `influencer_category`, `campaign_type`), altering the data mathematically is impossible. 
* **The Mechanism:** The algorithm utilizes **Resampling with Replacement** (Bootstrapping). It randomly draws 850,000 rows from the clean, original 150,000-row dataset to create a new baseline matrix.
* **The Benefit:** This guarantees that the macro-level categorical proportions (e.g., the ratio of YouTube to TikTok campaigns, or Fashion to Tech influencers) remain exactly identical to the real-world sample.

### 2. Vectorized Gaussian Noise Injection (Continuous Variables)
If we only used Bootstrapping, the regression model would overfit on the exact duplicate numerical values. To prevent this, we inject mathematical variance into continuous metrics (e.g., `estimated_reach`, `engagements`, engineered velocities).
* **The Mechanism:** For the bootstrapped numerical columns, the algorithm generates a matrix of random noise drawn from a standard normal distribution $\mathcal{N}(0, 1)$. 
* **The Formula:** This noise is scaled proportionately by the standard deviation ($\sigma$) of each specific column, multiplied by a strict threshold parameter (`noise_std = 0.01`). 
    * $New\_Value = Original\_Value + [\mathcal{N}(0, 1) \times \sigma \times 0.01]$
* **The Benefit:** This creates "new" numerical data points that vary slightly from the originals (a 1% variance threshold). It breaks exact duplication while strictly preserving the variance, mean, and covariance structure required for accurate Ordinary Least Squares (OLS) regression.

---

## Architectural Trade-offs & Bypassed Techniques

During the design phase, multiple advanced augmentation techniques were evaluated. The following methods were deliberately bypassed to prioritize computational scalability and data integrity at the 1-million-row scale:

* **SMOGN (Synthetic Minority Over-Sampling Technique for Regression):** While excellent for interpolating skewed target variables, SMOGN relies on K-Nearest Neighbor (KNN) distance calculations. At a scale of generating 850,000 rows, the algorithmic time complexity $\mathcal{O}(n^2)$ results in severe memory bottlenecks and potential local hardware crashes. Vectorized noise achieves a similar continuous variance at a fraction of the computational cost.
* **Categorical Permutation:** Occasional swapping of categories between similar rows was considered to create slight variations in non-numerical data. This was bypassed because, without complex cluster-bounding, it risks generating illogical feature combinations that could introduce artificial bias into the downstream categorical regression models.

---

## Pre-Augmentation Feature Selection (Dimensionality Reduction)
To ensure the noise injection targets only highly predictive signals:
* **Handling Temporal Data:** Date columns (`start_date`, `end_date`) are explicitly dropped prior to augmentation. Specific timestamps lack linear correlation with engagement KPIs and risk introducing target leakage or requiring arbitrary date imputation.
* **Missing Values:** Any row containing `NaN` values in critical columns is dropped prior to augmentation to prevent the algorithm from mathematically multiplying errors.

## Setup and Execution

### Prerequisites
Ensure you have the following Python libraries installed:
```bash
pip install pandas numpy
```
### Running the Script
1. Place your cleaned base dataset in the same directory as the script.
2. Open `augment_pipeline.py` and update the `INPUT_FILE` variable in the configuration section to match your exact file name.
3. Execute the pipeline via your terminal:

```bash
python augment_pipeline.py
```

### Console Logging
The script utilizes Python's `logging` module to provide real-time console readouts detailing ingestion counts, `NaN` drops, noise injection execution, and the final 1,000,000-row export status.

## Downstream Integration
This augmented dataset is specifically engineered to feed into two analytical branches:
* **Predictive Modeling:** The 1 million rows support independent, categorical regression models (e.g., Platform Dynamics, Campaign Strategy, and Outlier/Virality testing) without risking target leakage. 
* **Business Intelligence:** The preserved categorical integrity allows for seamless integration into Tableau dashboards for benchmarking across platforms, influencer niches, and campaign types.
