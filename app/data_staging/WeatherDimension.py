from db.dal.data_mart.WeatherDimensionDAL import WeatherDimensionDAL


class WeatherDimension(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the weather dimension during the data staging phase.

    This class can use any of the DAL classes defined.
    """

    @staticmethod
    def populate():
        print("Populating accidents_weather_data_mart.weather_dimension")
        WeatherDimensionDAL.copy_data_from_weather_pre_stage()
        print("Successfully populated accidents_weather_data_mart.weather_dimension")

