from dagster import resource
import sqlalchemy
import requests
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
class WeatherClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def get_weather(self, city: str):
        response = requests.get(
            f"{self.base_url}",
            params={
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            },
        )
        response.raise_for_status()
        return response.json()
@resource()
def weather_resource(_):
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = os.getenv("WEATHER_API_URL")
    if not api_key:
        raise ValueError("Missing WEATHER_API_KEY in environment variables.")
    return WeatherClient(api_key, base_url)

@resource()
def supabase_resource(_):
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    return client
