import psycopg2.extras

from db import DatabaseConnection


class DataSourceDAL(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for READING from 'data_source'.
    No business logic is allowed here.
    """

    @staticmethod
    def fetch_all(sql):
        db = DatabaseConnection()

        with db.get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql)

            while True:
                results = cursor.fetchmany(500)
                if not results:
                    break
                for result in results:
                    yield result

    @staticmethod
    def fetch_one(sql):
        db = DatabaseConnection()

        with db.get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql)
            return cursor.fetchone()

    @staticmethod
    def get_count(sql):
        db = DatabaseConnection()

        with db.get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql)
            return cursor.fetchone()['count']
