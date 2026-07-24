from pathlib import Path
import pandas as pd

SILVER = Path("data/silver/yellow_tripdata_2025-01.parquet")
GOLD = Path("data/gold/daily_revenue.parquet")

df = pd.read_parquet(SILVER)

# Create trip date
df["trip_date"] = df["tpep_pickup_datetime"].dt.date

# Aggregate revenue by day
daily_revenue = (
    df.groupby("trip_date")
      .agg(
          total_revenue=("total_amount", "sum"),
          total_trips=("VendorID", "count"),
          avg_fare=("fare_amount", "mean"),
          avg_trip_distance=("trip_distance", "mean"),
      )
      .reset_index()
)

GOLD.parent.mkdir(parents=True, exist_ok=True)
daily_revenue.to_parquet(GOLD, index=False)

print(daily_revenue.head())
print("\nGold table saved to:", GOLD)
