from db.DatabaseConnection import DatabaseConnection


class HourDimensionDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'accidents_weather_data_mart.hour_dimension'.
    No business logic is allowed here.
    """

    @staticmethod
    def copy_data_from_hour_pre_stage():
        db = DatabaseConnection()

        sql = """INSERT INTO accidents_weather_data_mart.hour_dimension(
                    hour_key, 
                    hour_start, 
                    hour_end, 
                    date, 
                    day_of_week, 
                    month, 
                    year, 
                    is_weekend, 
                    is_holiday, 
                    holiday_name) 
                 SELECT * FROM dimension_pre_stage.hour_dimension_pre_stage"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
