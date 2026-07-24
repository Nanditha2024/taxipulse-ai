from pathlib import Path
import pandas as pd

FILE = Path("data/raw/yellow_tripdata_2025-01.parquet")

df = pd.read_parquet(FILE)

columns = [
    "passenger_count",
    "RatecodeID",
    "store_and_fwd_flag",
    "congestion_surcharge",
    "Airport_fee"
]

for col in columns:
    print(f"\n{'='*50}")
    print(f"Column: {col}")
    print(f"Missing Values: {df[col].isna().sum():,}")
    print("\nSample Rows:")
    print(df[df[col].isna()].head())