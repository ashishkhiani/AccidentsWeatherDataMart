from db import DatabaseConnection


class LocationDimensionPreStageDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'dimension_pre_stage.location_dimension_pre_stage'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert(entity):
        """
        Inserts a single entity to the database.
        :param entity: a tuple of the form -> (
                street_name,
                intersection_1,
                intersection_2,
                longitude,
                latitude,
                city,
                neighbourhood)

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
                neighbourhood)
                        VALUES (%s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql_insert, entity)

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
                neighbourhood])

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
                neighbourhood) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.executemany(sql_insert, entities)
