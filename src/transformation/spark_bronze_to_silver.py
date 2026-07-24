from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

RAW_PATH = Path("data/raw/yellow_tripdata_2025-01.parquet")
OUTPUT_PATH = Path("data/silver_spark/yellow_tripdata_2025-01")

spark = (
    SparkSession.builder
    .appName("TaxiPulse-Silver-ETL")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

try:
    df = spark.read.parquet(str(RAW_PATH))

    rows_before = df.count()
    print(f"Rows before cleaning: {rows_before:,}")

    silver_df = (
        df
        .filter(F.col("trip_distance") > 0)
        .filter(F.col("fare_amount") > 0)
        .filter(F.col("total_amount") > 0)
        .filter(
            (F.col("tpep_pickup_datetime") >= F.lit("2025-01-01 00:00:00")) &
            (F.col("tpep_pickup_datetime") < F.lit("2025-02-01 00:00:00"))
        )
        .fillna({
            "passenger_count": 1,
            "RatecodeID": 1,
            "store_and_fwd_flag": "N",
            "congestion_surcharge": 0.0,
            "Airport_fee": 0.0,
        })
        .withColumn(
            "trip_duration_minutes",
            (
                F.unix_timestamp("tpep_dropoff_datetime")
                - F.unix_timestamp("tpep_pickup_datetime")
            ) / 60
        )
        .filter(F.col("trip_duration_minutes") > 0)
    )

    rows_after = silver_df.count()

    print(f"Rows after cleaning: {rows_after:,}")
    print(f"Rows removed: {rows_before - rows_after:,}")

    silver_df.write.mode("overwrite").parquet(str(OUTPUT_PATH))

    print(f"Spark Silver data saved to: {OUTPUT_PATH}")

finally:
    spark.stop()