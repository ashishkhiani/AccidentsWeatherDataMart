from db import DatabaseConnection


class AccidentHourRelationDAL(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for reading and writing to 'relations.weather_hour_relation'.
    No business logic is allowed here.
    """

    @staticmethod
    def connect_accident_hour_dimension():
        db = DatabaseConnection()

        sql = """INSERT INTO relations.accident_hour_relation (accident_key, hour_key)
                 SELECT A.accident_key, H.hour_key
                 FROM dimension_pre_stage.accident_dimension_pre_stage A, dimension_pre_stage.hour_dimension_pre_stage H
                 WHERE date_trunc('hour', A.date + A.time + INTERVAL '30 minute') = H.date + H.hour_start;"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
