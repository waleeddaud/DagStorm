from dagster import Definitions, load_assets_from_modules
from DagStorm.assets.fetch_weather import fetch_weather
from DagStorm.assets.transform_weather import transform_weather_data
from DagStorm.assets.store_weather import store_weather_data
from DagStorm.jobs.weather_job import weather_job
from DagStorm.resource import weather_resource, supabase_resource
all_assets = [fetch_weather, transform_weather_data, store_weather_data]
defs = Definitions(
    assets=all_assets,
    jobs = [weather_job],
    resources={
        "weather_resource": weather_resource,
        "supabase_resource": supabase_resource
    }
)
