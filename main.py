from scripts.clean_data import clean_data
from scripts.load_to_postgres import load_data

from scripts.analysis import (
    top_countries,
    top_products,
    revenue_by_region
)

from scripts.charts import (
    country_chart,
    product_chart,
    revenue_trend
)

from scripts.generate_report import generate_report

FILE_PATH = "data/sales_data.csv"

# ETL Pipeline
df = clean_data(FILE_PATH)
load_data(df)

# Analytics
top_countries()
top_products()
revenue_by_region()

# Visualizations
country_chart()
product_chart()
revenue_trend()

# Report
generate_report()

print("\nProject Completed Successfully!")