from db.dal.data_mart.LocationDimensionDAL import LocationDimensionDAL


class LocationDimension(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the location dimension during the data staging phase.

    This class can use any of the DAL classes defined.
    """

    @staticmethod
    def populate():
        LocationDimensionDAL.copy_data_from_location_pre_stage()

