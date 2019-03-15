from db import DatabaseConnection


class AccidentLocationRelationDAL(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for reading and writing to 'connect_accident_hour_dimension'.
    No business logic is allowed here.
    """

    @staticmethod
    def connect_accident_hour_dimension():
        db = DatabaseConnection()

        sql = """INSERT INTO relations.accident_location_relation (accident_key, location_key)
                 SELECT A.accident_key, L.location_key
                 FROM dimension_pre_stage.accident_dimension_pre_stage A, 
                      dimension_pre_stage.location_dimension_pre_stage L
                 WHERE L.latitude = A.longitude AND L.latitude = A.latitude"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
