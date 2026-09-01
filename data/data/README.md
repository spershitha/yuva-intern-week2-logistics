# Dataset Information

## Dataset Used

This project uses the **Brazilian E-Commerce Public Dataset by Olist**.

The dataset contains anonymized information about orders, customers, sellers, products, payments, reviews, and delivery dates from an e-commerce platform in Brazil.

## Purpose

The dataset is used to demonstrate data collection, cleaning, and preprocessing techniques for logistics analysis.

## Relevant Logistics Information

The `olist_orders_dataset.csv` file contains important order and delivery-related fields such as:

- Order purchase timestamp
- Order approval timestamp
- Order delivery to carrier date
- Order delivery to customer date
- Estimated delivery date

These fields can be used to calculate delivery duration and identify late deliveries.

## Preprocessing Performed

The Python script in this repository demonstrates:

1. Checking dataset structure and information
2. Identifying missing values
3. Checking duplicate records
4. Converting date columns into datetime format
5. Calculating delivery duration
6. Identifying late deliveries
7. Detecting delivery-time outliers using the IQR method
8. Standardizing numerical delivery-duration values

## Source

Brazilian E-Commerce Public Dataset by Olist, available through Kaggle.

The raw dataset is not uploaded to this repository because it contains multiple large CSV files. Users can download the dataset separately and place the required CSV files inside this `data` folder.
