from sqlalchemy import create_engine
from config import CONNECTION_STRING

def load_data(df):

    engine = create_engine(CONNECTION_STRING)

    df.to_sql(
        "sales_data",
        engine,
        if_exists="replace",
        index=False
    )

    print("\nData Loaded Successfully Into PostgreSQL")