# 🌦️ Weather Data Pipeline with Dagster + Supabase

This project is a simple **ETL (Extract, Transform, Load)** pipeline that:

1. **Fetches weather data** from the OpenWeatherMap API.
2. **Transforms** it into a structured format.
3. **Stores** it into a **Supabase PostgreSQL database**.

It uses **Dagster** for orchestrating the pipeline and **SQLAlchemy** to interact with Supabase.

---

## 🔧 Tech Stack

- [Dagster](https://dagster.io/) - Workflow orchestration
- [OpenWeatherMap API](https://openweathermap.org/api) - Weather data source
- [Supabase](https://supabase.com/) - PostgreSQL cloud database
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python ORM for DB interaction

---

## 📦 Pipeline Stages

### ✅ 1. Fetch Weather Data

- Pulls live weather data for a specified city using OpenWeatherMap API.
- Extracts useful fields like temperature, humidity, pressure, and timestamp.

### ✅ 2. Transform Data

- Converts raw JSON response into a structured `WeatherData` model.
- Ensures data types are consistent (e.g., float for temperature, datetime for timestamp).

### ✅ 3. Store in Supabase

- Uses SQLAlchemy with PostgreSQL dialect to `UPSERT` the data.
- Conflict key: `timestamp_utc` to avoid duplicates.
- Writes to a `weather_data` table hosted on Supabase.

---

## 📁 Project Structure

```bash
.
├── DagStorm/
│   ├── models.py          # Defines the WeatherData Pydantic model
│   ├── resources.py       # Supabase connection resource
│   ├── ops/               # Dagster ops and assets
│   └── ...
├── weather_job.py         # Dagster job definition
├── README.md              # This file
├── .env                   # Contains SUPABASE_URI and API keys
└── ...
