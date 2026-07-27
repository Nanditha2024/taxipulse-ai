from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="TaxiPulse AI Analytics API",
    description="REST API for NYC Yellow Taxi business metrics",
    version="1.0.0",
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "reports" / "daily_revenue.csv"


def load_data() -> pd.DataFrame:
    """Load and validate the Gold-layer CSV."""
    if not DATA_FILE.exists():
        raise HTTPException(
            status_code=500,
            detail="Gold dataset not found. Run the ETL and CSV export first.",
        )

    df = pd.read_csv(DATA_FILE, parse_dates=["trip_date"])

    required_columns = {
        "trip_date",
        "total_revenue",
        "total_trips",
        "avg_fare",
        "avg_trip_distance",
    }

    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        raise HTTPException(
            status_code=500,
            detail=f"Missing required columns: {sorted(missing_columns)}",
        )

    return df


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "TaxiPulse AI Analytics API",
        "documentation": "/docs",
    }


@app.get("/api/kpis")
def get_kpis() -> dict[str, float | int]:
    df = load_data()

    return {
        "total_revenue": round(float(df["total_revenue"].sum()), 2),
        "total_trips": int(df["total_trips"].sum()),
        "average_fare": round(float(df["avg_fare"].mean()), 2),
        "average_trip_distance": round(
            float(df["avg_trip_distance"].mean()), 2
        ),
    }


@app.get("/api/daily-revenue")
def get_daily_revenue() -> list[dict]:
    df = load_data().sort_values("trip_date")

    return [
        {
            "trip_date": row.trip_date.strftime("%Y-%m-%d"),
            "total_revenue": round(float(row.total_revenue), 2),
            "total_trips": int(row.total_trips),
        }
        for row in df.itertuples()
    ]


@app.get("/api/top-revenue-days")
def get_top_revenue_days(limit: int = 5) -> list[dict]:
    if limit < 1 or limit > 31:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 31.",
        )

    df = (
        load_data()
        .nlargest(limit, "total_revenue")
        .sort_values("total_revenue", ascending=False)
    )

    return [
        {
            "trip_date": row.trip_date.strftime("%Y-%m-%d"),
            "total_revenue": round(float(row.total_revenue), 2),
            "total_trips": int(row.total_trips),
        }
        for row in df.itertuples()
    ]