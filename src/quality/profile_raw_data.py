from pathlib import Path
import pandas as pd

FILE_PATH = Path("data/raw/yellow_tripdata_2025-01.parquet")

print("Loading dataset...")

df = pd.read_parquet(FILE_PATH)

print("\n===== DATASET INFO =====")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== FIRST 5 ROWS =====")
print(df.head())