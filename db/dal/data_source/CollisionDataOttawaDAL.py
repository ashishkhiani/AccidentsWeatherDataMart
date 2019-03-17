from db.dal.DAL import DAL


class CollisionDataOttawaDAL(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for READING from 'data_source.collision_data_ottawa'.
    No business logic is allowed here.
    """

    @staticmethod
    def fetch_all():
        return DAL.fetch_all("""SELECT * FROM data_source.collision_data_ottawa""")

    @staticmethod
    def get_count():
        return DAL.get_count("""SELECT count(*) FROM data_source.collision_data_ottawa""")

    @staticmethod
    def fetch_all_unique_locations():
        return DAL.fetch_all("""
                     SELECT DISTINCT ON (longitude, latitude) *
                     FROM data_source.collision_data_ottawa
                     GROUP BY id, longitude, latitude""")

    @staticmethod
    def get_locations_count():
        return DAL.get_count("""
                     SELECT COUNT(*) FROM (SELECT DISTINCT ON (longitude, latitude) *
                     FROM data_source.collision_data_ottawa
                     GROUP BY id, longitude, latitude) a;""")

