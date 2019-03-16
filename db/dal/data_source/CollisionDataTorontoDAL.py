from db.dal.DAL import DAL


class CollisionDataTorontoDAL(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for READING from 'data_source.collision_data_toronto'.
    No business logic is allowed here.
    """

    @staticmethod
    def fetch_all():
        return DAL.fetch_all("""SELECT * FROM data_source.collision_data_toronto""")

    @staticmethod
    def get_count():
        return DAL.get_count("""SELECT count(*) FROM data_source.collision_data_toronto""")
