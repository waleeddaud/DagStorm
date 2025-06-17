from dagster import asset
import requests

@asset(required_resource_keys={"weather_resource"})
def fetch_weather(context) -> dict:
    try:
        client = context.resources.weather_resource
        city = "Lahore"
        data = client.get_weather(city)
        context.log.info(f"Fetched weather data for {city}: {data}")
        return data
    except Exception as e:
        context.log.error(f"Exception occured while fetching weather {str(e)}")