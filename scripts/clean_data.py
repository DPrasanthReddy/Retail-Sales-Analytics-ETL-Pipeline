import pandas as pd

def clean_data(file_path):

    df = pd.read_csv(
        file_path,
        na_values=["", " ", "NULL", "null", "N/A", "na"]
    )

    print("\nDataset Loaded Successfully")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nTotal Missing Values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    return df