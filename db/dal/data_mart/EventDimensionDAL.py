from db.DatabaseConnection import DatabaseConnection


class EventDimensionDAL(object):

    @staticmethod
    def copy_data_from_event_pre_stage():
        db = DatabaseConnection()

        sql = """INSERT INTO accidents_weather_data_mart.event_dimension(event_key, name)   
                 SELECT event_key, name FROM dimension_pre_stage.event_dimension_pre_stage"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
