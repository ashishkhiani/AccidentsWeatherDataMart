from db import DatabaseConnection


class AccidentDimensionPreStageDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'dimension_pre_stage.accident_dimension'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert(entity):
        """
        Inserts a single entity to the database.
        :param entity: a tuple of the form -> (
                accident_key,
                collision_id,
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
                impact_type_flag)

        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO dimension_pre_stage.accident_dimension_pre_stage (
                          accident_key,
                          time,
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
                          impact_type_flag ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql_insert, entity)

    @staticmethod
    def insert_many(entities):
        """
        Insert many entities to the database.
        :param entities: a list of tuples of the form -> (
                accident_key,
                collision_id,
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
                impact_type_flag)

        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO dimension_pre_stage.accident_dimension_pre_stage (
                          accident_key,
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
                          impact_type_flag ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.executemany(sql_insert, entities)

    @staticmethod
    def copy_data_from_accident_pre_stage():
        db = DatabaseConnection()

        sql = """INSERT INTO accidents_weather_data_mart.location_dimension (
                location_key,
                street_name,
                intersection_1,
                intersection_2,
                longitude,
                latitude,
                city,
                neighbourhood)  
                 SELECT * FROM dimension_pre_stage.location_dimension_pre_stage"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)