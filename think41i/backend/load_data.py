import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def load_csv(csv_file, table_name):
    df = pd.read_csv(f"data/{csv_file}")
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"✅ Loaded {csv_file} into {table_name}")

if __name__ == "__main__":
    load_csv("distribution_centers.csv", "distribution_centers")
    load_csv("users.csv", "users")
    # Repeat for other CSV files
