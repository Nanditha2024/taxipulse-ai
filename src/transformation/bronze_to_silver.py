from pathlib import Path
import pandas as pd

RAW = Path("data/raw/yellow_tripdata_2025-01.parquet")
SILVER = Path("data/silver/yellow_tripdata_2025-01.parquet")

df = pd.read_parquet(RAW)

print("Rows before cleaning:", len(df))

# Convert pickup datetime
df["tpep_pickup_datetime"] = pd.to_datetime(
    df["tpep_pickup_datetime"],
    errors="coerce"
)

# Keep only January 2025 pickup dates
df = df[
    (df["tpep_pickup_datetime"] >= "2025-01-01")
    & (df["tpep_pickup_datetime"] < "2025-02-01")
].copy()

# Remove impossible trips
df = df[df["trip_distance"] > 0]
df = df[df["fare_amount"] > 0]
df = df[df["total_amount"] > 0]

# Fill missing values
df["passenger_count"] = df["passenger_count"].fillna(1)
df["RatecodeID"] = df["RatecodeID"].fillna(1)
df["store_and_fwd_flag"] = df["store_and_fwd_flag"].fillna("N")
df["congestion_surcharge"] = df["congestion_surcharge"].fillna(0)
df["Airport_fee"] = df["Airport_fee"].fillna(0)

SILVER.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(SILVER, index=False)

print("Rows after cleaning:", len(df))
print("Silver dataset saved:", SILVER)