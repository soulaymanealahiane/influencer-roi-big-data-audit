import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv('original_dataset.csv')

# Convert start_date and end_date columns to datetime types
date_cols = ['start_date', 'end_date']
for col in date_cols:
    try:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    except Exception as e:
        print(f"Error converting {col}: {e}")

# 2. Data Cleaning: Prevent Division by Zero
# If any of these are 0, replace with 1 to avoid infinite values during division
cols_to_protect = ['estimated_reach', 'engagements', 'campaign_duration_days']
for col in cols_to_protect:
    df[col] = df[col].replace(0, 1)

# 3. Engineer the 6 Core Normalized KPIs

# --- ENGAGEMENT KPIs ---
# KPI 1: True Engagement Rate (Interaction Quality)
df['true_engagement_rate'] = (df['engagements'] / df['estimated_reach']).round(6)

# KPI 2: Daily Engagement Velocity (Interaction Momentum)
df['daily_engagement_velocity'] = (df['engagements'] / df['campaign_duration_days']).round(2)

# --- GROWTH KPIs ---
# KPI 3: Reach-to-Sales Conversion Rate (Visibility to Growth)
df['reach_to_sales_conversion_rate'] = (df['product_sales'] / df['estimated_reach']).round(6)

# KPI 4: Engagement-to-Sales Ratio (Interaction to Growth)
df['engagement_to_sales_ratio'] = (df['product_sales'] / df['engagements']).round(6)

# --- CONTENT EFFECTIVENESS KPIs ---
# KPI 5: Sales Velocity (Business Impact Speed)
df['sales_velocity'] = (df['product_sales'] / df['campaign_duration_days']).round(2)

# KPI 6: Virality / Reach Velocity (Content Spread Speed)
df['reach_velocity'] = (df['estimated_reach'] / df['campaign_duration_days']).round(2)


# 4. Advanced Benchmarking Feature Engineering (Platform-Wise Normalization)
# To make benchmarking incredibly easy for the Tableau/Stats team, 
# we calculate how each campaign performs RELATIVE to its specific platform's average.
# An index > 1.0 means it outperformed the platform average. < 1.0 means it underperformed.

platforms = df['platform'].unique()

for metric in ['true_engagement_rate', 'reach_to_sales_conversion_rate']:
    # Calculate the platform average for the metric
    platform_avg = df.groupby('platform')[metric].transform('mean')
    
    # Create the benchmark index column
    index_col_name = f'benchmark_index_{metric}'
    df[index_col_name] = (df[metric] / platform_avg).round(3)

# 5. Outlier Flagging (Just like the Mid-Semester Project)
# Flagging highly viral engagement anomalies so the statistical analyst can filter them if needed.
Q1 = df['true_engagement_rate'].quantile(0.25)
Q3 = df['true_engagement_rate'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR

df['is_viral_outlier'] = np.where(df['true_engagement_rate'] > upper_bound, True, False)

# 6. Save the fully prepared dataset
output_file = 'cleaned_dataset.csv'
df.to_csv(output_file, index=False)

print(f"Data processing complete! Saved to {output_file}")
print("\n--- New Dataset Shape ---")
print(df.shape)
print("\n--- New Columns Available for Analysts ---")
print(df.columns.tolist())
print("\n--- Snapshot of KPI Data ---")
print(df[['platform', 'true_engagement_rate', 'reach_to_sales_conversion_rate', 'benchmark_index_true_engagement_rate']].head())
