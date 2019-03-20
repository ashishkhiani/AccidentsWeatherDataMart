from db.dal.dimension_pre_stage.EventDimensionPreStageDAL import EventDimensionPreStageDAL


class EventDimensionPreStage(object):

    @staticmethod
    def populate():
        """
        Data acquired from https://www.hockey-reference.com/teams/OTT/
        """
        events = [
            # (event_name, event_start_date, event_end_date, event_city)
            ('Hockey - Colorado Avalanche at Ottawa Senators', '2014-10-16', '2014-10-16', 'Ottawa'),
            ('Hockey - New Jersey Devils at Ottawa Senators', '2015-12-30', '2015-12-30', 'Ottawa'),
            ('Winterlude', '2016-01-29', '2016-02-15', 'Ottawa'),
            ('Winterlude', '2017-02-03', '2017-02-20', 'Ottawa'),
            ('Basketball - Miami Heat at Toronto Raptors', '2016-01-22', '2016-01-22', 'Toronto'),
            ('Basketball - Houston Rockets at Toronto Raptors', '2016-03-06', '2016-03-06', 'Toronto'),
            ('Ottawa Tulip Festival', '2015-05-08', '2015-05-18', 'Ottawa'),
            ('Ottawa Tulip Festival', '2016-05-12', '2016-05-23', 'Ottawa')
        ]

        EventDimensionPreStageDAL.insert_many(events)
