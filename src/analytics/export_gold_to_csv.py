from pathlib import Path
import pandas as pd

# Paths
GOLD_FILE = Path("data/gold/daily_revenue.parquet")
OUTPUT_FILE = Path("reports/daily_revenue.csv")

# Read Gold dataset
df = pd.read_parquet(GOLD_FILE)

# Create reports folder if it doesn't exist
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Export to CSV
df.to_csv(OUTPUT_FILE, index=False)

print(f"CSV exported successfully to: {OUTPUT_FILE}")
print(df.head())