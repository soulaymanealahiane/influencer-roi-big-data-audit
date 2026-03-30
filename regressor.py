# Import necessary libraries and suppress warnings
import warnings
warnings.filterwarnings('ignore')

import math
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')  # Ensuring non-interactive plotting backend
import matplotlib.pyplot as plt

import seaborn as sns

# For prediction
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Set plot style 
sns.set_theme(style='whitegrid')

# Load the dataset
data_path = r"C:\Users\pc\OneDrive - Al Akhawayn University in Ifrane\Desktop\BAI Final Project\cleaned_dataset.csv"
df = pd.read_csv(data_path, encoding='ascii', delimiter=',')

# Convert start_date and end_date columns to datetime types
date_cols = ['start_date', 'end_date']
for col in date_cols:
    try:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    except Exception as e:
        print(f"Error converting {col}: {e}")

# ---------------------------------------------------------
# VISUALIZATION 1: Categorical Countplots
# ---------------------------------------------------------
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.countplot(data=df, x='platform')
plt.title('Distribution of Platforms')

plt.subplot(1, 2, 2)
sns.countplot(data=df, x='campaign_type')
plt.title('Distribution of Campaign Types')
plt.xticks(rotation=45, ha='right') 

plt.tight_layout()
plt.savefig('01_categorical_distributions.png') 
plt.close()

# ---------------------------------------------------------
# VISUALIZATION 2: Correlation Heatmap 
# ---------------------------------------------------------
numeric_df = df.select_dtypes(include=[np.number])

if numeric_df.shape[1] >= 4:
    plt.figure(figsize=(14, 10)) 
    corr = numeric_df.corr()
    
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 8})
    plt.xticks(rotation=45, ha='right')
    plt.title('Correlation Heatmap of Numeric Features', pad=20)
    
    plt.tight_layout()
    plt.savefig('02_correlation_heatmap.png') 
    plt.close()

# ---------------------------------------------------------
# VISUALIZATION 3: Pair Plot (Targeted Core Metrics Only)
# ---------------------------------------------------------
core_metrics = [
    'engagements', 
    'estimated_reach', 
    'product_sales', 
    'true_engagement_rate', 
    'reach_to_sales_conversion_rate'
]

valid_core_metrics = [col for col in core_metrics if col in numeric_df.columns]

sns.pairplot(df[valid_core_metrics], diag_kind='kde', height=2.5)
plt.suptitle('Pair Plot of Core Business Metrics', y=1.02)
plt.savefig('03_pair_plot.png') 
plt.close()

# ---------------------------------------------------------
# VISUALIZATION 4: Dynamic Histograms 
# ---------------------------------------------------------
numeric_features = numeric_df.columns
n_features = len(numeric_features)
grid_cols = 3
grid_rows = math.ceil(n_features / grid_cols) 

plt.figure(figsize=(18, 5 * grid_rows))

for i, col in enumerate(numeric_features, 1):
    plt.subplot(grid_rows, grid_cols, i)
    sns.histplot(numeric_df[col], kde=True, bins=30)
    plt.title(f'{col}')

plt.tight_layout(pad=3.0)
plt.savefig('04_numeric_histograms.png') 
plt.close()

# =========================================================
# MACHINE LEARNING MODEL 1: RAW METRICS
# =========================================================
features_raw = ['engagements', 'estimated_reach', 'campaign_duration_days']
target = 'product_sales'

model_df_raw = df[features_raw + [target]].dropna()
X_raw = model_df_raw[features_raw]
y_raw = model_df_raw[target]

X_train_raw, X_test_raw, y_train_raw, y_test_raw = train_test_split(X_raw, y_raw, test_size=0.2, random_state=42)

lr_model_raw = LinearRegression()
lr_model_raw.fit(X_train_raw, y_train_raw)
y_pred_raw = lr_model_raw.predict(X_test_raw)

r2_raw = r2_score(y_test_raw, y_pred_raw)
rmse_raw = np.sqrt(mean_squared_error(y_test_raw, y_pred_raw))

print(f"\n--- Model 1: Raw Metrics Regression ---")
print(f"Features used: {features_raw}")
print(f"R2 Score: {r2_raw:.4f}")
print(f"RMSE: {rmse_raw:.4f}")

# ---------------------------------------------------------
# VISUALIZATION 5: Regression Scatter Plot (Model 1)
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(y_test_raw, y_pred_raw, alpha=0.5)
plt.xlabel('Actual Product Sales')
plt.ylabel('Predicted Product Sales')
plt.title('Model 1: Actual vs. Predicted Sales (Raw Metrics)')

axis_min_raw = min(y_test_raw.min(), y_pred_raw.min())
axis_max_raw = max(y_test_raw.max(), y_pred_raw.max())
plt.plot([axis_min_raw, axis_max_raw], [axis_min_raw, axis_max_raw], ls="--", c="red")

plt.tight_layout()
plt.savefig('05_regression_scatter.png') 
plt.close()


# =========================================================
# MACHINE LEARNING MODEL 2: ENGINEERED KPIs
# =========================================================
# We strictly exclude KPIs derived from sales to prevent Data Leakage cheating
features_kpi = ['true_engagement_rate', 'daily_engagement_velocity', 'reach_velocity']

model_df_kpi = df[features_kpi + [target]].dropna()
X_kpi = model_df_kpi[features_kpi]
y_kpi = model_df_kpi[target]

X_train_kpi, X_test_kpi, y_train_kpi, y_test_kpi = train_test_split(X_kpi, y_kpi, test_size=0.2, random_state=42)

lr_model_kpi = LinearRegression()
lr_model_kpi.fit(X_train_kpi, y_train_kpi)
y_pred_kpi = lr_model_kpi.predict(X_test_kpi)

r2_kpi = r2_score(y_test_kpi, y_pred_kpi)
rmse_kpi = np.sqrt(mean_squared_error(y_test_kpi, y_pred_kpi))

print(f"\n--- Model 2: Engineered KPIs Regression ---")
print(f"Features used: {features_kpi}")
print(f"R2 Score: {r2_kpi:.4f}")
print(f"RMSE: {rmse_kpi:.4f}")

# ---------------------------------------------------------
# VISUALIZATION 6: Regression Scatter Plot (Model 2)
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
# Using a different color (orange) to distinguish the second model
plt.scatter(y_test_kpi, y_pred_kpi, alpha=0.5, color='darkorange')
plt.xlabel('Actual Product Sales')
plt.ylabel('Predicted Product Sales')
plt.title('Model 2: Actual vs. Predicted Sales (Engineered KPIs)')

axis_min_kpi = min(y_test_kpi.min(), y_pred_kpi.min())
axis_max_kpi = max(y_test_kpi.max(), y_pred_kpi.max())
plt.plot([axis_min_kpi, axis_max_kpi], [axis_min_kpi, axis_max_kpi], ls="--", c="red")

plt.tight_layout()
plt.savefig('06_regression_kpis_scatter.png') 
plt.close()

print("\nAll 6 visualizations have been successfully saved as PNG files.")