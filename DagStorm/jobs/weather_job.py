from dagster import define_asset_job

weather_job = define_asset_job(
    name= "weather_job",
    selection = [
        'fetch_weather',
        'transform_weather_data',
        'store_weather_data'
    ]
)