# 📈 Influencer Marketing ROI: Big Data Audit & Predictive Engine

## 📊 Live Interactive Dashboards
**[View the Executive Performance Dashboards on Tableau Public ↗](https://public.tableau.com/views/influencer-roi-big-data-audit/InfluencerCategoryDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

*(Note: The dashboards are hosted on Tableau Public to handle the 1,000,000-row augmented dataset without requiring local software installation. Click the link above for full interactivity and filtering.)*

---

## 📌 Executive Summary
This repository contains an end-to-end Business Analytics and Data Engineering pipeline designed to audit social media performance. The core objective of this project is to mathematically separate "vanity metrics" (raw reach, basic engagements) from true business drivers (revenue conversion, algorithmic velocity). 

By scaling an initial dataset of 150,000 campaigns to a robust 1,000,000-row synthetic population, this project deploys custom feature engineering, visual benchmarking, and rigorous predictive hypothesis testing to uncover the structural efficiencies of different social media platforms, campaign formats, and influencer niches.

## 🏗️ Project Architecture & Pipeline

### Phase 1: Data Engineering (`/Data Engineering`)
To ensure statistical significance and prepare the data for downstream machine learning without target leakage, a strict three-step engineering pipeline was implemented in Python:
1. **Data Loading:** Safe ingestion and validation of the raw 150k campaign dataset.
2. **Data Cleaning & Feature Engineering:** Mathematical sanitization to prevent division-by-zero errors, followed by the creation of 6 normalized Key Performance Indicators (KPIs) categorized by *Engagement*, *Growth*, and *Content Effectiveness*. Advanced Boolean flags (`is_viral_outlier`) and platform-specific `benchmark_index` features were engineered for cross-sectional analysis.
3. **Data Augmentation:** Scaled the dataset to 1,000,000 rows utilizing a hybrid approach of **Bootstrapping** (to preserve categorical proportions) and **Vectorized Gaussian Noise Injection** (to create continuous variance while preserving OLS regression integrity). Dates were explicitly dropped to prevent time-drift.

### Phase 2: Descriptive Analytics (`/Descriptive Analytics`)
Built entirely in Tableau using the augmented 1M-row dataset, this phase translates complex engineered KPIs into executive-ready business intelligence. 
* **Platform Benchmarking:** Proves which platforms generate the highest absolute conversion ratios, holding raw reach equal.
* **Campaign Strategy:** Visualizes "Optimal Campaign Duration" via decay curves, proving that peak engagement momentum is exhausted within 2–4 days.
* **Influencer Niche Analysis:** Utilizes a custom 4-quadrant scatter plot to isolate "vanity niches" (high engagement, low sales) from high-efficiency converting niches.

### Phase 3: Predictive Analytics (`/predictive_analytics`)
Rather than brute-forcing high $R^2$ scores, we deployed Multiple Linear Regression and Random Forest algorithms as **Rigorous Hypothesis Tests**:
* **The Vanity Metric Proof:** Models 1-4 successfully proved that social media marketing is highly non-linear. Raw attention and platform choice *do not* mathematically guarantee sales ($R^2 \approx 0$), validating the need for targeted, niche-specific conversion strategies.
* **The Virality A/B Test:** Sliced the dataset using our `is_viral_outlier` feature to prove that extreme algorithmic virality breaks standard conversion logic. 
* **Target Leakage Demonstration:** Model 5 intentionally demonstrates the dangers of target leakage in enterprise ML pipelines by feeding the algorithm features algebraically derived from the target variable.

### Phase 4: Deliverables (`/Deliverables`)
* **Synthesis Report:** A rigorous, 2-page academic and strategic summary of the audit's findings.
* **Executive Pitch Deck:** An interactive HTML presentation designed to guide a 20-minute data-driven strategy briefing.

---

## 📂 Repository Structure
```text
influencer-roi-big-data-audit/
├── Data Engineering/
│   ├── Data Augmentation/
│   │   ├── README.md
│   │   ├── augmented_1_million_dataset_sample.csv
│   │   └── augmenter_pipeline.py
│   ├── Data Cleaning/
│   │   ├── README.md
│   │   ├── cleaned_dataset_sample.csv
│   │   └── data_cleaner.py
│   └── Data Loading/
│       ├── README.md
│       ├── data_downloader.py
│       └── original_raw_dataset_sample.csv
├── Descriptive Analytics/
│   ├── README.md
├── predictive_analytics/
│   ├── README.md
│   ├── linear_regression_model_1/
│   ├── linear_regression_model_2/
│   ├── linear_regression_model_3/
│   ├── linear_regression_model_4/
│   └── linear_regression_model_5/
└── Deliverables/
    ├── synthesis_report.docx
    └── presentation_deck.html
