import os
import pandas as pd

BASE_PATH = r"..\operations_analytics_and_risk_monitoring\data\raw"

def explore_file(file_path):
    print("\n" + "="*100)
    print(f"FILE: {file_path}")
    print("="*100)

    try:
        df = pd.read_csv(file_path, encoding="latin1")

        print("\nShape:", end=" ")
        print(df.shape)

        print("\nColumns:", end=" ")
        print(df.columns.tolist())

        print("\nInfo:", end=" ")
        print(df.info())

        print("\nMissing Values:", end=" ")
        print(df.isnull().sum().sort_values(ascending=False).head(10))

        print("\nSample Data:", end=" ")
        print(df.head(3))

    except Exception as e:
        print(f"Error reading file: {e}")


def scan_folders(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                explore_file(file_path)


if __name__ == "__main__":
    scan_folders(BASE_PATH)


'''
Observations: 

1. Business/Revenue is the dataset Superstore Sales Data.The Superstore dataset contains 9,994 records with 21 structured columns covering orders, customers, products, and financial metrics such as sales, profit, and discount. The data is clean with no missing values and includes well-defined categorical and numerical fields across regions, product categories, and customer segments. Date fields (Order Date and Ship Date) are stored as strings and require conversion for time-series analysis.

Conclusion:
This dataset serves as a complete business intelligence layer, enabling revenue analysis, profit tracking, customer segmentation, and regional performance insights. It is well-suited for KPI dashboards, SQL-based analytics, and time-series forecasting in Power BI.

2. Operations/Risk is the dataset Azure Maintenance. This dataset consists of multiple interconnected tables including machine telemetry (876,100 records), error logs, failure events, maintenance records, and machine metadata. All tables are clean with no missing values, and are linked via machineID and timestamps. The dataset captures real-world industrial machine behavior such as voltage, vibration, pressure, and rotation metrics.

Conclusion:
This dataset represents an operational monitoring system, suitable for anomaly detection, predictive maintenance modeling, and system health scoring. It enables time-series analysis and failure prediction, simulating enterprise-level infrastructure monitoring similar to cloud or industrial IoT systems.

3. Product/Behavior is the dataset Ecommerce Behavior. This dataset is large-scale, containing over 109 million user interaction records across two months (October and November). It includes event-level data such as product views, cart actions, purchases, user sessions, pricing, and product metadata. Significant missing values exist in category_code and brand, and the dataset requires sampling or filtering due to its size (multi-GB memory footprint).

Conclusion:
This dataset represents a user behavior and product analytics system, enabling funnel analysis (view → cart → purchase), customer journey tracking, and engagement modeling. It is highly suitable for conversion rate analysis and behavioral segmentation but requires optimization techniques such as sampling or time-based filtering for practical processing.

'''