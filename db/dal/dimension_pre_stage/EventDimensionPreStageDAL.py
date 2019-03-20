from psycopg2.extras import execute_values

from db import DatabaseConnection


class EventDimensionPreStageDAL(object):

    @staticmethod
    def insert_many(entities):

        db = DatabaseConnection()

        sql_insert = """INSERT INTO dimension_pre_stage.event_dimension_pre_stage (
                          name, 
                          start_date, 
                          end_date, 
                          city) 
                        VALUES %s;"""

        with db.get_connection().cursor() as cursor:
            execute_values(cur=cursor, sql=sql_insert, argslist=entities)
