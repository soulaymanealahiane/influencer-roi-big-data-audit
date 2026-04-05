import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

IMG_PATH = 'predictive_analytics/linear_regression_model_1/01_platform_dynamics.png'

# =========================================================
# Dataset loading
# =========================================================
data_path = "augmented_1_million_dataset.csv"
df = pd.read_csv(data_path, encoding='ascii', delimiter=',')

# =========================================================
# Model 1: Platform Dynamics (IMPROVED)
# =========================================================

features = [
    'estimated_reach',
    'true_engagement_rate',
    'daily_engagement_velocity'
]
target = 'product_sales'

# Include platform column
model_df = df[features + ['platform'] + [target]].dropna()

# -------- One-hot encode platform (FIXED CLEANLY) --------
platform_dummies = pd.get_dummies(
    model_df['platform'],
    prefix='is',
    drop_first=True   # 🔥 avoids dummy trap automatically
)

# Combine features
X = pd.concat([
    model_df[features],
    platform_dummies
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
print(f"\n--- Model 1: Platform Dynamics Regression ---")
print(f"Features used: {list(X.columns)}")
print(f"R2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# =========================================================
# Coefficients
# =========================================================
coeffs = pd.Series(lr_model.coef_, index=X.columns)
print("\n--- Coefficients ---")
print(coeffs)

# =========================================================
# Plot: Actual vs Predicted with Trendline (IMPROVED)
# =========================================================
plt.figure()

# Scatter
plt.scatter(y_test, y_pred, alpha=0.3)

# Sort values for clean lines
sorted_idx = np.argsort(y_test)

# Trendline
z = np.polyfit(y_test, y_pred, 1)
p = np.poly1d(z)
plt.plot(
    y_test.iloc[sorted_idx],
    p(y_test.iloc[sorted_idx]),
    label="Trendline"
)

# Perfect prediction line
plt.plot(
    y_test.iloc[sorted_idx],
    y_test.iloc[sorted_idx],
    linestyle='--',
    label="Perfect Fit"
)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales with Trendline")
plt.legend()

plt.tight_layout()

# Safe overwrite
if os.path.exists(IMG_PATH):
    os.remove(IMG_PATH)

plt.savefig(IMG_PATH)
plt.close()