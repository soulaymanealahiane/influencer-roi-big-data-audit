import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

IMG_PATH = 'predictive_analytics/linear_regression_model_4/04_realistic_model.png'

# =========================================================
# Dataset loading
# =========================================================
data_path = "augmented_1_million_dataset.csv"
df = pd.read_csv(data_path, encoding='ascii', delimiter=',')

# =========================================================
# Feature Engineering (🔥 HIGH IMPACT)
# =========================================================
df['engagement_volume'] = df['estimated_reach'] * df['true_engagement_rate']
df['engagement_per_day'] = df['engagements'] / df['campaign_duration_days']
df['reach_per_day'] = df['estimated_reach'] / df['campaign_duration_days']

# Avoid division issues
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# =========================================================
# Model 4: Realistic / Causal Model
# =========================================================

features = [
    'estimated_reach',
    'engagements',
    'true_engagement_rate',
    'daily_engagement_velocity',
    'campaign_duration_days',
    'engagement_volume',
    'engagement_per_day',
    'reach_per_day'
]

categorical = [
    'platform',
    'campaign_type',
    'influencer_category'
]

target = 'product_sales'

# Combine all needed columns
model_df = df[features + categorical + [target]].dropna()

# -------- One-hot encoding (clean) --------
dummies = pd.get_dummies(
    model_df[categorical],
    drop_first=True
)

# Combine features
X = pd.concat([
    model_df[features],
    dummies
], axis=1)

y = model_df[target]

# =========================================================
# Train/Test Split
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================================================
# Train Model
# =========================================================
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predictions
y_pred = lr_model.predict(X_test)

# Metrics
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# =========================================================
# Output Results
# =========================================================
print(f"\n--- Model 4: Realistic / Causal Model ---")
print(f"Features used: {list(X.columns)}")
print(f"R2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# =========================================================
# Coefficients
# =========================================================
coeffs = pd.Series(lr_model.coef_, index=X.columns)
print("\n--- Coefficients ---")
print(coeffs.sort_values(ascending=False))

# =========================================================
# Plot: Actual vs Predicted with Trendline
# =========================================================
plt.figure()

# Scatter
plt.scatter(y_test, y_pred, alpha=0.3)

# Sort for clean lines
sorted_idx = np.argsort(y_test)

# Trendline
z = np.polyfit(y_test, y_pred, 1)
p = np.poly1d(z)
plt.plot(
    y_test.iloc[sorted_idx],
    p(y_test.iloc[sorted_idx]),
    label="Trendline"
)

# Perfect fit line
plt.plot(
    y_test.iloc[sorted_idx],
    y_test.iloc[sorted_idx],
    linestyle='--',
    label="Perfect Fit"
)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Model 4: Realistic / Causal Model")
plt.legend()

plt.tight_layout()

# Save (safe overwrite)
if os.path.exists(IMG_PATH):
    os.remove(IMG_PATH)

plt.savefig(IMG_PATH)
plt.close()