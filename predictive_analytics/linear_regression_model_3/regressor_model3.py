import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

IMG_PATH_NORMAL = 'predictive_analytics/linear_regression_model_3/03A_normal_campaigns.png'
IMG_PATH_VIRAL = 'predictive_analytics/linear_regression_model_3/03B_viral_campaigns.png'

# =========================================================
# Dataset loading
# =========================================================
data_path = "augmented_1_million_dataset.csv"
df = pd.read_csv(data_path, encoding='ascii', delimiter=',')

# =========================================================
# Common setup
# =========================================================
features = [
    'estimated_reach',
    'true_engagement_rate',
    'campaign_duration_days'
]
target = 'product_sales'

# =========================================================
# Function to train + evaluate model
# =========================================================
def run_model(data, label, img_path):
    
    model_df = data[features + [target]].dropna()

    X = model_df[features]
    y = model_df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"\n--- Model 3 ({label}) ---")
    print(f"R2 Score: {r2:.4f}")
    print(f"RMSE: {rmse:.4f}")

    # Coefficients
    coeffs = pd.Series(model.coef_, index=X.columns)
    print("\nCoefficients:")
    print(coeffs)

    # =====================================================
    # Plot
    # =====================================================
    plt.figure()
    plt.scatter(y_test, y_pred, alpha=0.3)

    sorted_idx = np.argsort(y_test)

    # Trendline
    z = np.polyfit(y_test, y_pred, 1)
    p = np.poly1d(z)
    plt.plot(
        y_test.iloc[sorted_idx],
        p(y_test.iloc[sorted_idx]),
        label="Trendline"
    )

    # Perfect line
    plt.plot(
        y_test.iloc[sorted_idx],
        y_test.iloc[sorted_idx],
        linestyle='--',
        label="Perfect Fit"
    )

    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title(f"Model 3 ({label})")
    plt.legend()
    plt.tight_layout()

    # Save
    if os.path.exists(img_path):
        os.remove(img_path)

    plt.savefig(img_path)
    plt.close()


# =========================================================
# Run 3A: Normal campaigns (NOT viral)
# =========================================================
normal_df = df[df['is_viral_outlier'] == False]

run_model(normal_df, "Normal Campaigns", IMG_PATH_NORMAL)


# =========================================================
# Run 3B: Viral campaigns
# =========================================================
viral_df = df[df['is_viral_outlier'] == True]

run_model(viral_df, "Viral Campaigns", IMG_PATH_VIRAL)