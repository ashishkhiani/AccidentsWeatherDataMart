from db import DatabaseConnection


class WeatherDimensionDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'accidents_weather_data_mart.weather_dimension'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert(entity):
        """
        Inserts a single entity to the database.
        :param entity: a tuple of the form -> (
                weather_key,
                station_name,
                longitude,
                latitude,
                elevation,
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
                weather)

        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO accidents_weather_data_mart.weather_dimension (
                          weather_key,
                          station_name, 
                          longitude, 
                          latitude, 
                          elevation, 
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
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql_insert, entity)

    @staticmethod
    def insert_many(entities):
        """
        Insert many entities to the database.
        :param entities: a list of tuples of the form -> [(
                weather_key,
                station_name,
                longitude,
                latitude,
                elevation,
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

        sql_insert = """INSERT INTO accidents_weather_data_mart.weather_dimension (
                          weather_key,
                          station_name, 
                          longitude, 
                          latitude, 
                          elevation, 
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
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.executemany(sql_insert, entities)

    @staticmethod
    def copy_data_from_weather_pre_stage():
        db = DatabaseConnection()

        sql = """INSERT INTO accidents_weather_data_mart.weather_dimension(
                    weather_key, station_name, longitude, latitude, elevation, temperature, 
                    temperature_flag, dew_point_temp, dew_point_temp_flag, relative_humidity, 
                    relative_humidity_flag, wind_direction, wind_direction_flag, wind_speed, 
                    wind_speed_flag, visibility, visibility_flag, station_pressure, station_pressure_flag, 
                    humidex, humidex_flag, wind_chill, wind_chill_flag, weather, weather_flag)
                    
                 SELECT weather_key, station_name, longitude, latitude, elevation, temperature, 
                    temperature_flag, dew_point_temp, dew_point_temp_flag, relative_humidity, 
                    relative_humidity_flag, wind_direction, wind_direction_flag, wind_speed, 
                    wind_speed_flag, visibility, visibility_flag, station_pressure, station_pressure_flag, 
                    humidex, humidex_flag, wind_chill, wind_chill_flag, weather, weather_flag 
                
                FROM dimension_pre_stage.weather_dimension_pre_stage"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
