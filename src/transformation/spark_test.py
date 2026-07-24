from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("TaxiPulseAI")
    .master("local[*]")
    .getOrCreate()
)

print("=" * 50)
print("Spark Version:", spark.version)
print("Spark is running successfully!")
print("=" * 50)

spark.stop()