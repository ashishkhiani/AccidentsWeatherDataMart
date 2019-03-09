from db import DatabaseConnection


class WeatherHourRelation(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for reading and writing to 'relations.weather_hour_relation'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert(weather_key, hour_key):
        """
        Stores the relationship between the weather and hour dimension
        :param weather_key: surrogate key of the weather dimension
        :param hour_key: surrogate key of the hour dimension
        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO relations.weather_hour_relation (weather_key, hour_key) VALUES (%s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql_insert, (weather_key, hour_key))
