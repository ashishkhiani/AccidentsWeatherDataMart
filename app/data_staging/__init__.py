from app.data_staging.HourDimension import HourDimension
from app.data_staging.WeatherDimension import WeatherDimension


def populate_dimensions(hour=False, weather=False, accident=False, location=False):

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
        print("Location Dimension successfully populated.")

