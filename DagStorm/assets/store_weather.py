from dagster import asset

from sqlalchemy import Table, MetaData, insert
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.engine import Engine
from typing import Dict, Any
from DagStorm.models import WeatherData
from supabase import create_client
import os 
from dotenv import load_dotenv
load_dotenv()

@asset(required_resource_keys={"supabase_resource"})
def store_weather_data(context, transform_weather_data: WeatherData):
    """
    Store the transformed weather data into Supabase.
    """
    if not transform_weather_data:
        context.log.warning("No transformed weather data to store.")
        return

    try:
        supabase = context.resources.supabase_resource
        supabase.table("weather_data").insert(transform_weather_data.model_dump()).execute()
        context.log.info(f"Stored weather data for {transform_weather_data.city} in Supabase.")
    except Exception as e:
        context.log.error(f"Exception occurred while storing weather data: {str(e)}")

