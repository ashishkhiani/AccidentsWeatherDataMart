from db import DatabaseConnection


class AccidentFactDAL(object):

    @staticmethod
    def populate():
        db = DatabaseConnection()

        sql = """INSERT INTO accidents_weather_data_mart.accident_fact(
                    hour_key, 
                    location_key, 
                    accident_key,
                    weather_key,
                    is_fatal,
                    is_intersection
                 )
                 SELECT AH.hour_key, AL.location_key, AH.accident_key, WL.weather_key, false, false
                 FROM relations.accident_hour_relation AH, 
                      relations.accident_location_relation AL, 
                      relations.weather_hour_relation WH,
                      relations.weather_location_relation WL
                 WHERE AL.accident_key = AH.accident_key
                 AND AH.hour_key = WH.hour_key
                 AND WH.weather_key = WL.weather_key
                 AND AL.location_key = WL.location_key"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
