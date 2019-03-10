import psycopg2.extras

from db import DatabaseConnection
from db.dal.data_source.DataSourceDAL import DataSourceDAL


class StationInventoryDAL(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for READING from 'data_source.station_inventory'.
    No business logic is allowed here.
    """

    @staticmethod
    def fetch_all():
        return DataSourceDAL.fetch_all("""SELECT * FROM data_source.station_inventory""")

    @staticmethod
    def get_count():
        return DataSourceDAL.get_count("""SELECT count(*) FROM data_source.station_inventory""")

    @staticmethod
    def fetch_by_name(name):
        sql = """SELECT * FROM data_source.station_inventory WHERE name = %s"""

        db = DatabaseConnection()

        with db.get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql, (name,))
            return cursor.fetchone()
