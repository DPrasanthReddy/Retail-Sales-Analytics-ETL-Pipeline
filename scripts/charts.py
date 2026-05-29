import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from config import CONNECTION_STRING
import os

os.makedirs("charts", exist_ok=True)

engine = create_engine(CONNECTION_STRING)
engine = create_engine(CONNECTION_STRING)

def country_chart():

    query = """
    SELECT
        "Country",
        SUM("Total Revenue") AS revenue
    FROM sales_data
    GROUP BY "Country"
    ORDER BY revenue DESC
    LIMIT 10;
    """

    df = pd.read_sql(query, engine)

    plt.figure(figsize=(10,5))
    plt.bar(df["Country"], df["revenue"])

    plt.xticks(rotation=45)

    plt.title("Top 10 Countries by Revenue")

    plt.tight_layout()

    plt.savefig("charts/top_countries.png")

    plt.close()

    print("Country chart saved")


def product_chart():

    query = """
    SELECT
        "Item Type",
        SUM("Total Profit") AS profit
    FROM sales_data
    GROUP BY "Item Type"
    ORDER BY profit DESC;
    """

    df = pd.read_sql(query, engine)

    plt.figure(figsize=(10,5))

    plt.bar(df["Item Type"], df["profit"])

    plt.xticks(rotation=45)

    plt.title("Profit by Product")

    plt.tight_layout()

    plt.savefig("charts/top_products.png")

    plt.close()

    print("Product chart saved")
    

def revenue_trend():

    query = """
    SELECT
        DATE_TRUNC('month', "Order Date") AS month,
        SUM("Total Revenue") AS revenue
    FROM sales_data
    GROUP BY month
    ORDER BY month;
    """

    df = pd.read_sql(query, engine)

    plt.figure(figsize=(10,5))

    plt.plot(df["month"], df["revenue"])

    plt.title("Monthly Revenue Trend")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("charts/revenue_trend.png")

    plt.close()

    print("Revenue Trend Chart Saved")