from db import DatabaseConnection


class EventHourRelationDAL(object):

    @staticmethod
    def connect_event_hour_dimension():
        db = DatabaseConnection()

        sql = """INSERT INTO relations.event_hour_relation (event_key, hour_key)
                 SELECT E.event_key, H.hour_key
                 FROM dimension_pre_stage.event_dimension_pre_stage E, 
                      dimension_pre_stage.hour_dimension_pre_stage H
                 WHERE E.start_date = H.date OR E.end_date = H.date"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
