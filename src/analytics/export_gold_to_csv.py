from pathlib import Path

import pandas as pd

# Paths
GOLD_FILE = Path("data/gold/daily_revenue.parquet")
OUTPUT_FILE = Path("reports/daily_revenue.csv")

# Read Gold dataset
df = pd.read_parquet(GOLD_FILE)

# Ensure trip_date is a datetime column
df["trip_date"] = pd.to_datetime(df["trip_date"])

# Keep only January 2025
df = df[
    (df["trip_date"] >= pd.Timestamp("2025-01-01"))
    & (df["trip_date"] < pd.Timestamp("2025-02-01"))
].copy()

# Sort by date
df = df.sort_values("trip_date")

# Export dates as YYYY-MM-DD
df["trip_date"] = df["trip_date"].dt.strftime("%Y-%m-%d")

# Create reports folder if it doesn't exist
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Export to CSV
df.to_csv(OUTPUT_FILE, index=False)

print(f"CSV exported successfully to: {OUTPUT_FILE}")
print(f"Rows exported: {len(df)}")
print(df.head())
print(df.tail())