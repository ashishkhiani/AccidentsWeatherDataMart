from app.data_pre_staging.EventDimensionPreStage import EventDimensionPreStage
from app.data_pre_staging.HourDimensionPreStage import HourDimensionPreStage
from app.data_pre_staging.WeatherDimensionPreStage import WeatherDimensionPreStage
from app.data_pre_staging.AccidentDimensionPreStage import AccidentDimensionPreStage
from app.data_pre_staging.LocationDimensionPreStage import LocationDimensionPreStage


def populate_dimensions_pre_stage(hour=False, weather=False, accident=False, location=False, event=False):

    if hour:
        print("Populating Hour pre-stage Dimension...")
        HourDimensionPreStage.populate()
        print("Hour pre-stage Dimension successfully populated.")

    if weather:
        print("Populating Weather pre-stage Dimension...")
        WeatherDimensionPreStage.populate()
        WeatherDimensionPreStage.handle_null_values()
        print("Weather pre-stage Dimension successfully populated.")

    if accident:
        print("Populating Accident pre-stage Dimension...")
        AccidentDimensionPreStage.populate()
        print("Accident pre-stage Dimension successfully populated.")

    if location:
        print("Populating Location pre-stage Dimension...")
        LocationDimensionPreStage.populate()
        print("Location pre-stage Dimension successfully populated.")

    if event:
        print("Populating Event pre-stage Dimension...")
        EventDimensionPreStage.populate()
        print("Event pre-stage Dimension successfully populated.")

