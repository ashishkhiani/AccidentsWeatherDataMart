from db import DatabaseConnection


class WeatherHourRelationDAL(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for reading and writing to 'relations.weather_hour_relation'.
    No business logic is allowed here.
    """

    @staticmethod
    def connect_weather_hour_dimension():
        db = DatabaseConnection()

        sql = """INSERT INTO relations.weather_hour_relation (weather_key, hour_key)
                 SELECT W.weather_key, H.hour_key
                 FROM dimension_pre_stage.weather_dimension_pre_stage W, 
                      dimension_pre_stage.hour_dimension_pre_stage H
                 WHERE W.date = H.date AND H.hour_start <= W.time AND W.time <= H.hour_end"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
