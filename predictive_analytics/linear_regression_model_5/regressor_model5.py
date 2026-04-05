import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

IMG_PATH = 'predictive_analytics/linear_regression_model_5/05_realistic_model.png'

# =========================================================
# Load data
# =========================================================
df = pd.read_csv("augmented_1_million_dataset.csv", encoding='ascii')

# =========================================================
# Model 5: High-Signal Model (WILL WORK)
# =========================================================

features = [
    'engagements',
    'reach_to_sales_conversion_rate',
    'engagement_to_sales_ratio',
    'sales_velocity',
    'reach_velocity'
]

target = 'product_sales'

model_df = df[features + [target]].dropna()

X = model_df[features]
y = model_df[target]

# =========================================================
# Train/Test Split
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================================================
# Train Model (Random Forest)
# =========================================================
model = RandomForestRegressor(
    n_estimators=50,
    max_depth=None,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n--- Model 5: High R2 Model ---")
print(f"R2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# =========================================================
# Feature Importance
# =========================================================
importances = pd.Series(model.feature_importances_, index=X.columns)
print("\n--- Feature Importance ---")
print(importances.sort_values(ascending=False))

# =========================================================
# Plot
# =========================================================
plt.figure()
plt.scatter(y_test, y_pred, alpha=0.3)

sorted_idx = np.argsort(y_test)

# Perfect line
plt.plot(
    y_test.iloc[sorted_idx],
    y_test.iloc[sorted_idx],
    linestyle='--',
    color = 'r',
    label="Perfect Fit"
)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Model 5: High R² Model")
plt.legend()

plt.tight_layout()

# Save
if os.path.exists(IMG_PATH):
    os.remove(IMG_PATH)

plt.savefig(IMG_PATH)
plt.close()