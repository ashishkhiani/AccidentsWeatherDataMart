from db.dal.data_mart.AccidentDimensionDAL import AccidentDimensionDAL


class AccidentDimension(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the accident dimension during the data staging phase.

    This class can use any of the DAL classes defined.
    """

    @staticmethod
    def populate():
        AccidentDimensionDAL.copy_data_from_accident_pre_stage()

