from db.dal.DAL import DAL


class StationInventoryDAL(object):
    """
    This functionality of this class is to interact with the database.
    ALl methods defined in the class must be solely responsible
    for READING from 'data_source.station_inventory'.
    No business logic is allowed here.
    """

    @staticmethod
    def fetch_all():
        return DAL.fetch_all("""SELECT * FROM data_source.station_inventory""")
