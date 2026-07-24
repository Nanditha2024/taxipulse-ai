# 🚖 TaxiPulse AI

An end-to-end Data Engineering and Analytics project built using the NYC Yellow Taxi dataset.

## 🚀 Project Overview

TaxiPulse AI demonstrates how raw transportation data can be transformed into business-ready insights using modern data engineering tools.

The project includes:

- Automated data ingestion
- Data profiling and quality validation
- Bronze → Silver → Gold ETL architecture
- Pandas and PySpark data processing
- SQL analytics using DuckDB and Spark SQL
- Business KPI generation

---

## 📊 Dataset

**Dataset:** NYC Yellow Taxi January 2025

| Metric | Value |
|--------|-------|
| Raw Records | 3,475,226 |
| Columns | 20 |
| Duplicate Records | 0 |
| Clean Records | 3,252,469 |
| Removed Records | 222,757 |

---

## 🏗️ Architecture

```text
NYC Taxi Dataset
        │
        ▼
Data Ingestion
        │
        ▼
Raw Layer
        │
        ▼
Data Profiling
        │
        ▼
Silver Layer (Cleaning)
        │
        ▼
Gold Layer (Aggregations)
        │
        ▼
Spark SQL & DuckDB Analytics
        │
        ▼
Business KPIs
```

---

## 🛠️ Technologies

- Python
- Pandas
- PySpark
- Apache Spark SQL
- DuckDB
- Parquet
- Git
- GitHub

---

## 📂 Project Structure

```text
src/
 ├── ingestion/
 ├── quality/
 ├── transformation/
 └── analytics/

reports/
sql/
requirements.txt
README.md
```

---

## ⚙️ Pipeline

### 1. Data Ingestion

Downloads the NYC Taxi dataset.

```bash
python src/ingestion/download_data.py
```

### 2. Data Profiling

Analyzes:

- Missing values
- Data types
- Duplicate records
- Dataset statistics

```bash
python src/quality/profile_raw_data.py
```

### 3. Data Quality Report

Generates a CSV report summarizing data quality.

```bash
python src/quality/data_quality_report.py
```

### 4. Silver Layer (Cleaning)

Performs:

- Invalid record removal
- Missing value handling
- Data standardization

```bash
python src/transformation/bronze_to_silver.py
```

### 5. PySpark ETL

Processes over **3.4 million** records using Spark.

```bash
python src/transformation/spark_bronze_to_silver.py
```

### 6. Gold Layer

Creates daily business KPIs.

```bash
python src/transformation/spark_silver_to_gold.py
```

### 7. SQL Analytics

Runs business queries using Spark SQL and DuckDB.

```bash
python src/analytics/spark_sql_analytics.py
```

---

## 📈 Key Results

- Processed 3.4M+ taxi trips
- Generated daily revenue KPIs
- Identified and cleaned 222K+ invalid records
- Built scalable ETL pipelines using both Pandas and PySpark

---

## ▶️ Setup

```bash
git clone https://github.com/Nanditha2024/taxipulse-ai.git

cd taxipulse-ai

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## 🔮 Next Steps

- Power BI Dashboard
- FastAPI Backend
- Docker
- GitHub Actions CI/CD
- AI-powered Analytics Assistant

---

## 👩‍💻 Author

**Nanditha Rayabharapu**