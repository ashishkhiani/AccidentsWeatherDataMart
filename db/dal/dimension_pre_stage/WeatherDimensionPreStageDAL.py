from psycopg2.extras import execute_values

from db import DatabaseConnection


class WeatherDimensionPreStageDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'dimension_pre_stage.weather_dimension_pre_stage'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert_many(entities):
        """
        Insert many entities to the database.
        :param entities: a list of tuples of the form -> [(
                station_name,
                longitude,
                latitude,
                elevation,
                date,
                time,
                temperature,
                dew_point_temp,
                relative_humidity,
                wind_direction,
                wind_speed,
                wind_speed_flag,
                visibility,
                station_pressure,
                humidex,
                wind_chill,
                wind_chill_flag,
                weather)]

        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO dimension_pre_stage.weather_dimension_pre_stage (
                          station_name, 
                          longitude, 
                          latitude, 
                          elevation, 
                          date,
                          time,
                          temperature, 
                          temperature_flag, 
                          dew_point_temp, 
                          dew_point_temp_flag, 
                          relative_humidity, 
                          relative_humidity_flag, 
                          wind_direction, 
                          wind_direction_flag, 
                          wind_speed, 
                          wind_speed_flag, 
                          visibility, 
                          visibility_flag, 
                          station_pressure, 
                          station_pressure_flag, 
                          humidex, 
                          humidex_flag, 
                          wind_chill, 
                          wind_chill_flag, 
                          weather, 
                          weather_flag) 
                        VALUES %s"""

        with db.get_connection().cursor() as cursor:
            execute_values(cur=cursor, sql=sql_insert, argslist=entities)

    @staticmethod
    def update_temperature_nulls():
        """
            Update all temperature pre-stage values
        """


        db = DatabaseConnection()

        sql_update = \
            """
            UPDATE dimension_pre_stage.weather_dimension_pre_stage as W 
            SET W.temperature_flag = 'estimated'
            SET W.temperature = av.temp
            FROM (select date, AVG(temperature) as temp
                from dimension_pre_stage.weather_dimension_pre_stage
                group by date) as av
            WHERE
             W.date = av.date AND W.temperature IS NULL
        """

        with db.get_connection().cursor() as cursor:
            execute_values(cur=cursor, sql=sql_update)

    @staticmethod
    def update_weather_nulls():
        """
            Update all weather values
        """


        db = DatabaseConnection()

        sql_update = \
            """
            UPDATE dimension_pre_stage.weather_dimension_pre_stage as W
            SET W.weather_flag = 'estimated'
            SET W.weather = av.weath
            FROM (SELECT date, weather as weath, COUNT(weather) AS cnt
                    FROM dimension_pre_stage.weather_dimension_pre_stage
                    GROUP BY date, weather 
                    ORDER BY cnt DESC
                    LIMIT 1) as av
            WHERE
             W.date = av.date AND W.weather IS NULL
        """

        with db.get_connection().cursor() as cursor:
            execute_values(cur=cursor, sql=sql_update)