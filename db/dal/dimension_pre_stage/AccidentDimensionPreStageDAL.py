from db import DatabaseConnection


class AccidentDimensionPreStageDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'dimension_pre_stage.weather_dimension_pre_stage'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert(entity):
        """
        Inserts a single entity to the database.
        :param entity: a tuple of the form -> (
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
                no_of_pedestrians)

        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO dimension_pre_stage.accident_dimension_pre_stage (
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
                          no_of_pedestrians) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql_insert, entity)

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
                          no_of_pedestrians) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.executemany(sql_insert, entities)
