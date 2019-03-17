from db import DatabaseConnection


class LocationDimensionDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'accidents_weather_data_mart.location_dimension'.
    No business logic is allowed here.
    """

    @staticmethod
    def copy_data_from_location_pre_stage():
        db = DatabaseConnection()

        sql = """INSERT INTO accidents_weather_data_mart.location_dimension (
                    location_key,
                    street_name,
                    intersection_1,
                    intersection_2,
                    longitude,
                    latitude,
                    city,
                    neighbourhood,
                    is_intersection)  
                 SELECT * FROM dimension_pre_stage.location_dimension_pre_stage"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
