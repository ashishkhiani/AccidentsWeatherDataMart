from psycopg2.extras import execute_values

from db import DatabaseConnection


class LocationDimensionPreStageDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'dimension_pre_stage.location_dimension_pre_stage'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert_many(entities):
        """
        Inserts a single entity to the database.
        :param entities: a tuple of the form -> ([
                street_name,
                intersection_1,
                intersection_2,
                longitude,
                latitude,
                city,
                neighbourhood,
                is_intersection])

        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO dimension_pre_stage.location_dimension_pre_stage (
                          street_name,
                          intersection_1,
                          intersection_2,
                          longitude,
                          latitude,
                          city,
                          neighbourhood,
                          is_intersection) 
                        VALUES %s;"""

        with db.get_connection().cursor() as cursor:
            execute_values(cur=cursor, sql=sql_insert, argslist=entities)
