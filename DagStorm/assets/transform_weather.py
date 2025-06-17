from dagster import asset
from DagStorm.models import WeatherData

@asset()
def transform_weather_data(context , fetch_weather : dict) -> WeatherData:
    """
    Transform the raw weather data into a structured WeatherData model.
    """
    if not fetch_weather:
        return None

    transformed_data = WeatherData(
        city=fetch_weather.get("name"),
        country=fetch_weather.get("sys", {}).get("country"),
        temperature=fetch_weather.get("main", {}).get("temp"),
        feels_like=fetch_weather.get("main", {}).get("feels_like"),
        humidity=fetch_weather.get("main", {}).get("humidity"),
        weather_main=fetch_weather.get("weather", [{}])[0].get("main"),
        weather_description=fetch_weather.get("weather", [{}])[0].get("description"),
        wind_speed=fetch_weather.get("wind", {}).get("speed"),
        wind_deg=fetch_weather.get("wind", {}).get("deg"),
        cloudiness=fetch_weather.get("clouds", {}).get("all"),
        timestamp_utc=fetch_weather.get("dt"),
    )
    print("Data " ,transformed_data , type(transformed_data))
    return transformed_data
