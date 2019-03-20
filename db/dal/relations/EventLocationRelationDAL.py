from db import DatabaseConnection


class EventLocationRelationDAL(object):

    @staticmethod
    def connect_event_location_dimension():
        db = DatabaseConnection()

        sql = """INSERT INTO relations.event_location_relation (event_key, location_key)
                 SELECT E.event_key, L.location_key
                 FROM dimension_pre_stage.event_dimension_pre_stage E, 
                      dimension_pre_stage.location_dimension_pre_stage L
                 WHERE E.city = L.city"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
