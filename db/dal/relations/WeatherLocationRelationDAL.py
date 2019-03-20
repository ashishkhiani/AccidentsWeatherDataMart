from db import DatabaseConnection
from db.dal.DAL import DAL
from psycopg2.extras import execute_values


class WeatherLocationRelationDAL(object):

    @staticmethod
    def get_distinct_locations_and_time_information():
        sql = """
                    SELECT
                      AL.location_key, L.city, L.latitude, L.longitude, H.date, H.hour_start
                    
                    FROM
                      relations.accident_hour_relation AH,
                      relations.accident_location_relation AL,
                      relations.weather_hour_relation WH,
                      dimension_pre_stage.location_dimension_pre_stage L,
                      dimension_pre_stage.hour_dimension_pre_stage H
                    
                    WHERE
                      AH.accident_key = AL.accident_key
                      AND AH.hour_key = WH.hour_key
                      AND AL.location_key = L.location_key
                      AND AH.hour_key = H.hour_key
                    
                    GROUP BY
                      AL.location_key, L.city, L.latitude, L.longitude, H.date, H.hour_start
              """

        return DAL.fetch_all(sql)

    @staticmethod
    def get_distinct_locations_and_time_information_count():
        sql = """SELECT count(*) FROM (
                    SELECT
                      AL.location_key, L.city, L.latitude, L.longitude, H.date, H.hour_start
                    
                    FROM
                      relations.accident_hour_relation AH,
                      relations.accident_location_relation AL,
                      relations.weather_hour_relation WH,
                      dimension_pre_stage.location_dimension_pre_stage L,
                      dimension_pre_stage.hour_dimension_pre_stage H
                    
                    WHERE
                      AH.accident_key = AL.accident_key
                      AND AH.hour_key = WH.hour_key
                      AND AL.location_key = L.location_key
                      AND AH.hour_key = H.hour_key
                    
                    GROUP BY
                      AL.location_key, L.city, L.latitude, L.longitude, H.date, H.hour_start) C
              """

        return DAL.get_count(sql)

    @staticmethod
    def connect_weather_to_location_dimension():
        db = DatabaseConnection()

        sql = """INSERT INTO relations.weather_location_relation (weather_key, location_key)
                 SELECT W.weather_key, T.location_key
                 FROM dimension_pre_stage.weather_dimension_pre_stage W, relations.weather_location_temp_relation T
                 WHERE W.station_name = T.station_name AND W.date = T.date AND W.time = T.time;"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)

    @staticmethod
    def insert_many_temp(entities):

        db = DatabaseConnection()

        sql_insert = """INSERT INTO relations.weather_location_temp_relation (station_name, location_key, date, time) 
                        VALUES %s;"""

        with db.get_connection().cursor() as cursor:
            execute_values(cur=cursor, sql=sql_insert, argslist=entities)
