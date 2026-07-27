from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "TaxiPulse AI Analytics API"


def test_kpis():
    response = client.get("/api/kpis")
    assert response.status_code == 200

    data = response.json()

    assert "total_revenue" in data
    assert "total_trips" in data
    assert "average_fare" in data
    assert "average_trip_distance" in data

    assert data["total_revenue"] > 0
    assert data["total_trips"] > 0


def test_daily_revenue():
    response = client.get("/api/daily-revenue")
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 31