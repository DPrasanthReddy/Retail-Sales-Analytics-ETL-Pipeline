import pandas as pd
from sqlalchemy import create_engine
from config import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING)

def top_countries():

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

    print("\nTop Countries By Revenue")
    print(df)

def top_products():

    query = """
    SELECT
        "Item Type",
        SUM("Total Profit") AS profit
    FROM sales_data
    GROUP BY "Item Type"
    ORDER BY profit DESC
    LIMIT 10;
    """

    df = pd.read_sql(query, engine)

    print("\nTop Products By Profit")
    print(df)

def revenue_by_region():

    query = """
    SELECT
        "Region",
        SUM("Total Revenue") AS revenue
    FROM sales_data
    GROUP BY "Region"
    ORDER BY revenue DESC;
    """

    df = pd.read_sql(query, engine)

    print("\nRevenue By Region")
    print(df)