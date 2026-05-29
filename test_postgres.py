from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("Prasanth@2")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/postgres"
)

try:
    with engine.connect() as conn:
        print("Connected!")
        result = conn.exec_driver_sql(
            "SELECT datname FROM pg_database"
        )

        for row in result:
            print(row)

except Exception as e:
    print(e)