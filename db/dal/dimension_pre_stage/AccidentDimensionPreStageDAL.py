from psycopg2.extras import execute_values

from db import DatabaseConnection


class AccidentDimensionPreStageDAL(object):
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
                id,
                collision_id,
                location,
                longitude,
                latitude,
                date,
                time,
                environment,
                environment_flag,
                light,
                light_flag,
                surface_condition,
                surface_condition,
                traffic_control,
                traffic_control_flag,
                traffic_control_condition,
                traffic_control_condition_flag,
                collision_classification,
                collision_classification_flag,
                impact_type,
                impact_type_flag,
                no_of_pedestrians)]

        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO dimension_pre_stage.accident_dimension_pre_stage (
                          longitude,
                          latitude,
                          date,
                          time,
                          street_name,
                          street1,
                          street2,
                          environment,
                          environment_flag,
                          road_surface,
                          road_surface_flag,
                          traffic_control,
                          traffic_control_flag,
                          visibility,
                          visibility_flag,
                          collision_classification,
                          collision_classification_flag,
                          impact_type,
                          impact_type_flag) 
                        VALUES %s"""

        with db.get_connection().cursor() as cursor:
            execute_values(cur=cursor, sql=sql_insert, argslist=entities)
