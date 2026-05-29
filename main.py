from scripts.clean_data import clean_data
from scripts.analysis import (
    top_countries,
    top_products,
    revenue_by_region
)

from scripts.charts import (
    country_chart,
    product_chart
)

from scripts.generate_report import generate_report

FILE_PATH = "data/sales_data.csv"

# Uncomment only first time
# from scripts.load_to_postgres import load_data
# df = clean_data(FILE_PATH)
# load_data(df)

top_countries()
top_products()
revenue_by_region()

country_chart()
product_chart()

generate_report()

from scripts.charts import (
    country_chart,
    product_chart,
    revenue_trend
)

country_chart()
product_chart()
revenue_trend()