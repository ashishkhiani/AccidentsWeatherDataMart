from db.dal.data_mart.EventDimensionDAL import EventDimensionDAL


class EventDimension(object):

    @staticmethod
    def populate():
        EventDimensionDAL.copy_data_from_event_pre_stage()

