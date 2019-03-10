from db.DatabaseConnection import DatabaseConnection


class HourDimensionPreStageDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'dimension_pre_stage.hour_dimension_pre_stage'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert(entity):
        """
        Inserts a single entity to the database.
        :param entity: a tuple of the form ->
                (hour_start, hour_end, date,day_of_week, month,year, is_weekend, is_holiday, holiday_name)
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
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql_insert, entity)

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
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.executemany(sql_insert, entities)
