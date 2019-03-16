from psycopg2.extras import execute_values

from db.DatabaseConnection import DatabaseConnection


class HourDimensionPreStageDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'dimension_pre_stage.hour_dimension_pre_stage'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert_many(entities):
        """
        Insert many entities at once to the database.
        :param entities: a list of tuples of the form ->
                [(hour_start, hour_end, date,day_of_week, month,year, is_weekend, is_holiday, holiday_name)]
        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO dimension_pre_stage.hour_dimension_pre_stage (
                            hour_start, 
                            hour_end, 
                            date, 
                            day_of_week, 
                            month, 
                            year, 
                            is_weekend, 
                            is_holiday, 
                            holiday_name) 
                        VALUES %s"""

        with db.get_connection().cursor() as cursor:
            execute_values(cur=cursor, sql=sql_insert, argslist=entities)
