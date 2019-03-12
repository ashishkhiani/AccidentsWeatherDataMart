from db.DatabaseConnection import DatabaseConnection


class HourDimensionDAL(object):
    """
    This functionality of this class is to interact with the database.
    All methods defined in the class must be solely responsible
    for reading and writing to 'accidents_weather_data_mart.hour_dimension'.
    No business logic is allowed here.
    """

    @staticmethod
    def insert(entity):
        """
        Inserts a single entity to the database.
        :param entity: a tuple of the form ->
                (hour_key, hour_start, hour_end, date,day_of_week, month,year, is_weekend, is_holiday, holiday_name)
        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO accidents_weather_data_mart.hour_dimension (
                            hour_key,
                            hour_start, 
                            hour_end, 
                            date, 
                            day_of_week, 
                            month, 
                            year, 
                            is_weekend, 
                            is_holiday, 
                            holiday_name) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql_insert, entity)

    @staticmethod
    def insert_many(entities):
        """
        Insert many entities at once to the database.
        :param entities: a list of tuples of the form ->
                [(hour_key, hour_start, hour_end, date,day_of_week, month,year, is_weekend, is_holiday, holiday_name)]
        :return: None
        """
        db = DatabaseConnection()

        sql_insert = """INSERT INTO accidents_weather_data_mart.hour_dimension (
                            hour_key,
                            hour_start, 
                            hour_end, 
                            date, 
                            day_of_week, 
                            month, 
                            year, 
                            is_weekend, 
                            is_holiday, 
                            holiday_name) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        with db.get_connection().cursor() as cursor:
            cursor.executemany(sql_insert, entities)

    @staticmethod
    def copy_data_from_hour_pre_stage():
        db = DatabaseConnection()

        sql = """INSERT INTO accidents_weather_data_mart.hour_dimension(
                    hour_key, 
                    hour_start, 
                    hour_end, 
                    date, 
                    day_of_week, 
                    month, 
                    year, 
                    is_weekend, 
                    is_holiday, 
                    holiday_name) 
                 SELECT * FROM dimension_pre_stage.hour_dimension_pre_stage"""

        with db.get_connection().cursor() as cursor:
            cursor.execute(sql)
