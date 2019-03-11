from db.dal.data_mart.HourDimensionDAL import HourDimensionDAL


class HourDimension(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the hour dimension during the data staging phase.

    This class can use any of the DAL classes defined.
    """

    @staticmethod
    def populate():
        HourDimensionDAL.copy_data_from_hour_pre_stage()

