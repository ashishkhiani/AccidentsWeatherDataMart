from app.data_staging.HourDimension import HourDimension
from app.data_staging.WeatherDimension import WeatherDimension
from app.data_staging.LocationDimension import LocationDimension
from app.data_staging.Relations import Relations


def populate_dimensions_data_mart(hour=False, weather=False, accident=False, location=False):

    if hour:
        print("Populating Hour Dimension...")
        HourDimension.populate()
        print("Hour Dimension successfully populated.")

    if weather:
        print("Populating Weather Dimension...")
        WeatherDimension.populate()
        print("Weather Dimension successfully populated.")

    if accident:
        print("Populating Accident Dimension...")
        print("Accident Dimension successfully populated.")

    if location:
        print("Populating Location Dimension...")
        LocationDimension.populate()
        print("Location Dimension successfully populated.")


def create_relations(weather_hour=False, weather_location=False, accident_hour=False, accident_location=False):

    if weather_hour:
        print("Creating Weather-Hour relation...")
        Relations.create_weather_hour_relation()
        print("Weather-Hour relation successfully created.")

    if weather_location:
        print("Creating Weather-Location relation...")
        print("Weather-Location relation successfully created.")

    if accident_hour:
        print("Creating Accident-Hour relation...")
        print("Accident-Hour relation successfully created.")

    if accident_location:
        print("Creating Accident-Location relation...")
        print("Accident-Location relation successfully created.")
