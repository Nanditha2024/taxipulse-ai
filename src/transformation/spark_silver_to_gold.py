from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

SILVER_PATH = Path("data/silver_spark/yellow_tripdata_2025-01")
GOLD_PATH = Path("data/gold_spark/daily_revenue")

spark = (
    SparkSession.builder
    .appName("TaxiPulse-Gold-ETL")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

try:
    silver_df = spark.read.parquet(str(SILVER_PATH))

    gold_df = (
        silver_df
        .withColumn("trip_date", F.to_date("tpep_pickup_datetime"))
        .groupBy("trip_date")
        .agg(
            F.round(F.sum("total_amount"), 2).alias("total_revenue"),
            F.count("*").alias("total_trips"),
            F.round(F.avg("fare_amount"), 2).alias("avg_fare"),
            F.round(F.avg("trip_distance"), 2).alias("avg_trip_distance"),
            F.round(F.avg("trip_duration_minutes"), 2).alias(
                "avg_trip_duration_minutes"
            ),
        )
        .orderBy("trip_date")
    )

    gold_df.show(10, truncate=False)

    gold_df.write.mode("overwrite").parquet(str(GOLD_PATH))

    print(f"Spark Gold data saved to: {GOLD_PATH}")

finally:
    spark.stop()