from pydantic import BaseModel, Field
from typing import Optional

class WeatherData(BaseModel):
    city: str
    country: str
    temperature: float
    feels_like: float
    humidity: int
    weather_main: str
    weather_description: str
    wind_speed: float
    wind_deg: int
    cloudiness: int
    timestamp_utc: int  