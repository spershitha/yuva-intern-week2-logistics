import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ==========================================
# YUVA INTERN - WEEK 2
# Logistics Data Cleaning and Preprocessing
# Dataset: Olist Brazilian E-Commerce
# ==========================================

# 1. Load the Olist orders dataset
orders = pd.read_csv("data/olist_orders_dataset.csv")

# 2. Display basic information
print("Dataset Shape:", orders.shape)
print("\nDataset Information:")
print(orders.info())

# 3. Check missing values
print("\nMissing Values:")
print(orders.isnull().sum())

# 4. Check duplicate records
print("\nDuplicate Records:", orders.duplicated().sum())

# 5. Convert date columns to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )

# 6. Remove exact duplicate rows
orders = orders.drop_duplicates()

# 7. Calculate delivery duration in days
orders["delivery_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.total_seconds() / (24 * 3600)

# 8. Identify late deliveries
orders["is_late"] = (
    orders["order_delivered_customer_date"]
    > orders["order_estimated_delivery_date"]
).astype("Int64")

# 9. Detect delivery-duration outliers using IQR
q1 = orders["delivery_days"].quantile(0.25)
q3 = orders["delivery_days"].quantile(0.75)

iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

orders["delivery_outlier"] = (
    (orders["delivery_days"] < lower_limit)
    | (orders["delivery_days"] > upper_limit)
)

# 10. Standardize delivery duration
valid_delivery = orders[["delivery_days"]].dropna()

scaler = StandardScaler()

orders.loc[
    valid_delivery.index,
    "delivery_days_scaled"
] = scaler.fit_transform(valid_delivery)

# 11. Final validation
print("\nFinal Dataset Shape:", orders.shape)

print("\nRemaining Missing Values:")
print(orders.isnull().sum())

print("\nPreprocessing completed successfully!")
