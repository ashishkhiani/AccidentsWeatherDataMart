from db import DatabaseConnection


class AccidentDimensionDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'dimension_pre_stage.accident_dimension'.
    No business logic is allowed here.
    """

    @staticmethod
    def copy_data_from_accident_pre_stage():
        db = DatabaseConnection()

        sql = """INSERT INTO accidents_weather_data_mart.accident_dimension (
                          accident_key,
                          time,
                          environment,
                          environment_flag,
                          light,
                          light_flag,
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
                 SELECT * FROM dimension_pre_stage.accident_dimension_pre_stage"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)