1. 150,000 Influencer Marketing Compaigns ROI Dataset; https://www.kaggle.com/datasets/tfisthis/influencer-marketing-roi-dataset?resource=download

2. Analysis & prediction repo: BAI project: https://www.kaggle.com/code/devraai/influencer-marketing-roi-analysis-and-prediction
                                
3. Data Cleaning (Preventing Math Errors)
    Before any metrics could be computed, scanned the denominator columns (estimated_reach, engagements, and campaign_duration_days). Any instances of exactly 0 were replaced with 1 to prevent NaN or infinity errors from breaking statistical computations.



4. The 6 Engineered KPIs (Appended as New Columns)
    added the following 6 normalized KPIs. These transition the raw counts into normalized "rates": ---2 KPIs per EVALUATION---

    ---ENGAGEMENT---

    true_engagement_rate: engagements / estimated_reach
        (Measures the exact percentage of the exposed audience that actively interacted).

    daily_engagement_velocity: engagements / campaign_duration_days
        (Measures interaction momentum: how many engagements a campaign generates on average per day).




    ---GROWTH---

    reach_to_sales_conversion_rate: product_sales / estimated_reach
        (Measures pure visibility effectiveness—how well simple exposure converts into measurable growth/sales).

    engagement_to_sales_ratio: product_sales / engagements
        (A deep analytic check: it verifies if highly engaged users are actually converting, filtering out "vanity" engagements).



    ---CONTENT EFFECTIVENESS---

    sales_velocity: product_sales / campaign_duration_days
        (Measures the immediate business impact speed: how fast the content format drives actual revenue).

    reach_velocity: estimated_reach / campaign_duration_days
        (A proxy for "Virality"—how quickly the content spread across the platform per day).




5. Advanced Benchmarking Normalizations (The "Secret Sauce")---
        To make the job  easy for the Python statistical tests & regression and Tableau dashboards, engineered three additional advanced benchmarking columns:

    benchmark_index_true_engagement_rate: This compares every single row against its specific platform's average engagement rate.
        How to use it: If this index is 1.0, it performed exactly at the platform average. If it is 2.5, it performed 150% better than the average. This is the ultimate "normalized" comparison metric.

    benchmark_index_reach_to_sales_conversion_rate: The same logic as above, but benchmarking growth conversion across the platforms.

    is_viral_outlier: Just like your mid-semester project, I used the Interquartile Range (IQR) method to flag extreme statistical anomalies (True/False).   Your statistical analyst will need this to run clean comparisons of means without outliers skewing their results.