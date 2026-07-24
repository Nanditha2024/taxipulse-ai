from pathlib import Path
import duckdb

GOLD_FILE = Path("data/gold/daily_revenue.parquet")

connection = duckdb.connect()

connection.execute(
    f"""
    CREATE OR REPLACE VIEW daily_revenue AS
    SELECT *
    FROM read_parquet('{GOLD_FILE.as_posix()}')
    """
)

queries = {
    "Daily Revenue": """
        SELECT
            trip_date,
            ROUND(total_revenue, 2) AS total_revenue
        FROM daily_revenue
        ORDER BY trip_date
        LIMIT 10
    """,

    "Highest Revenue Day": """
        SELECT
            trip_date,
            ROUND(total_revenue, 2) AS total_revenue
        FROM daily_revenue
        ORDER BY total_revenue DESC
        LIMIT 1
    """,

    "Overall KPIs": """
        SELECT
            SUM(total_trips) AS total_trips,
            ROUND(SUM(total_revenue), 2) AS total_revenue,
            ROUND(AVG(avg_fare), 2) AS average_daily_fare,
            ROUND(AVG(avg_trip_distance), 2) AS average_trip_distance
        FROM daily_revenue
    """,
}

for name, query in queries.items():
    print(f"\n===== {name.upper()} =====")
    result = connection.execute(query).fetchdf()
    print(result.to_string(index=False))

connection.close()