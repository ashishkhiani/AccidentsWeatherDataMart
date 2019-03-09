from db.dal.data_source.ClimateDataCalgaryDAL import ClimateDataCalgaryDAL
from db.dal.data_source.ClimateDataOttawaDAL import ClimateDataOttawaDAL
from db.dal.data_source.ClimateDataTorontoDAL import ClimateDataTorontoDAL


class WeatherDimension(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the weather dimension during the data staging phase.

    This class can use any of the DAL classes defined.
    """

    @staticmethod
    def populate():
        for row in ClimateDataCalgaryDAL.fetch_all():
            # handle row
            continue

        for row in ClimateDataOttawaDAL.fetch_all():
            # handle row
            continue

        for row in ClimateDataTorontoDAL.fetch_all():
            # handle row
            continue
