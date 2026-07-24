from pathlib import Path

from pyspark.sql import SparkSession

GOLD_PATH = Path("data/gold_spark/daily_revenue")

spark = (
    SparkSession.builder
    .appName("TaxiPulse-Spark-SQL-Analytics")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

try:
    gold_df = spark.read.parquet(str(GOLD_PATH))

    gold_df.createOrReplaceTempView("daily_revenue")

    print("\n=== Overall KPIs ===")

    spark.sql("""
        SELECT
            SUM(total_trips) AS total_trips,
            ROUND(SUM(total_revenue), 2) AS total_revenue,
            ROUND(AVG(avg_fare), 2) AS average_daily_fare,
            ROUND(AVG(avg_trip_distance), 2) AS average_trip_distance,
            ROUND(AVG(avg_trip_duration_minutes), 2)
                AS average_trip_duration_minutes
        FROM daily_revenue
    """).show(truncate=False)

    print("\n=== Top 5 Revenue Days ===")

    spark.sql("""
        SELECT
            trip_date,
            total_revenue,
            total_trips,
            avg_fare
        FROM daily_revenue
        ORDER BY total_revenue DESC
        LIMIT 5
    """).show(truncate=False)

    print("\n=== Highest Trip Volume Days ===")

    spark.sql("""
        SELECT
            trip_date,
            total_trips,
            total_revenue
        FROM daily_revenue
        ORDER BY total_trips DESC
        LIMIT 5
    """).show(truncate=False)

finally:
    spark.stop()