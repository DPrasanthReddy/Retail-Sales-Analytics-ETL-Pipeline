from urllib.parse import quote_plus

DB_USER = "postgres"
DB_PASSWORD = quote_plus("Prasanth@2")

DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "salesdb"

CONNECTION_STRING = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)