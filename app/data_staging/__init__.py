from app.data_staging.HourDimension import HourDimension


def populate_dimensions():
    print("Populating hour dimension...")
    HourDimension.populate()
    print("Hour Dimension successfully populated.")
