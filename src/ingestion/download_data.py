from pathlib import Path
import requests

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet"

OUTPUT = Path("data/raw/yellow_tripdata_2025-01.parquet")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

print("Downloading dataset...")

response = requests.get(URL, timeout=60)
response.raise_for_status()

OUTPUT.write_bytes(response.content)

print("Download completed!")
print(f"Saved to: {OUTPUT}")