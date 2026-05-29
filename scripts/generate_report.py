from sqlalchemy import create_engine
import pandas as pd
import os

from config import CONNECTION_STRING

os.makedirs("reports", exist_ok=True)

engine = create_engine(CONNECTION_STRING)

def generate_report():

    summary_query = """
    SELECT
        COUNT(*) AS orders,
        SUM("Total Revenue") AS revenue,
        SUM("Total Profit") AS profit
    FROM sales_data;
    """

    country_query = """
    SELECT
        "Country",
        SUM("Total Revenue") revenue
    FROM sales_data
    GROUP BY "Country"
    ORDER BY revenue DESC
    LIMIT 1;
    """

    product_query = """
    SELECT
        "Item Type",
        SUM("Total Profit") profit
    FROM sales_data
    GROUP BY "Item Type"
    ORDER BY profit DESC
    LIMIT 1;
    """

    summary = pd.read_sql(summary_query, engine)
    country = pd.read_sql(country_query, engine)
    product = pd.read_sql(product_query, engine)

    with open("reports/sales_report.txt", "w") as file:

        file.write("RETAIL SALES ANALYTICS REPORT\n")
        file.write("="*50 + "\n\n")

        file.write(f"Total Orders : {summary['orders'][0]}\n")
        file.write(f"Total Revenue : {summary['revenue'][0]:,.2f}\n")
        file.write(f"Total Profit : {summary['profit'][0]:,.2f}\n\n")

        file.write(
            f"Top Country : {country['Country'][0]}\n"
        )

        file.write(
            f"Top Product : {product['Item Type'][0]}\n"
        )

    print("Detailed Report Generated")