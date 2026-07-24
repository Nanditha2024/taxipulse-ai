from pathlib import Path
import pandas as pd

FILE = Path("data/raw/yellow_tripdata_2025-01.parquet")

df = pd.read_parquet(FILE)

report = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isnull().sum().values,
    "Missing %": (df.isnull().mean() * 100).round(2).values
})

print(report)

report.to_csv("reports/data_quality_report.csv", index=False)

print("\nReport saved to reports/data_quality_report.csv")

