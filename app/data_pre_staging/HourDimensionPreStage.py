import datetime

import holidays

from db.dal.dimension_pre_stage.HourDimensionPreStageDAL import HourDimensionPreStageDAL
from utils.flags import NOT_AVAILABLE


class HourDimensionPreStage(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the hour dimension during the data pre-staging phase.

    This class can use any of the DAL classes defined.
    """

    @staticmethod
    def populate():
        """
        Does a historic load into the hour pre-stage dimension
        :return: None
        """

        d1 = datetime.date(2007, 1, 1)  # start date
        d2 = datetime.date(2017, 12, 31)  # end date

        delta = d2 - d1  # timedelta

        entities = []

        for i in range(delta.days + 1):
            date = d1 + datetime.timedelta(i)
            day_of_week = date.strftime("%A")
            month = date.strftime("%B")
            year = date.year
            is_weekend = HourDimensionPreStage.is_weekend(day_of_week)
            is_holiday, holiday_name = HourDimensionPreStage.is_holiday(date)

            for j in range(24):
                hour_start = datetime.time(j, 0, 0, 0)
                hour_end = datetime.time(j, 59, 59, 0)

                entity = (hour_start,
                          hour_end,
                          date,
                          day_of_week,
                          month,
                          year,
                          is_weekend,
                          is_holiday,
                          holiday_name)

                entities.append(entity)

        HourDimensionPreStageDAL.insert_many(entities)

    @staticmethod
    def is_weekend(day):
        """
        Determines whether a given day is the weekend.
        :param day: A string that represents the name of the day.
        :return: True if day is weekend, False otherwise
        """
        if day == 'Friday' or day == 'Saturday' or day == 'Sunday':
            return True

        return False

    @staticmethod
    def is_holiday(date):
        """
        Determines whether a given date is a Canadian Holiday
        :param date: Datetime object
        :return: True if date is a Canadian Holiday, False otherwise
        """
        canada_holidays = holidays.Canada()  # TODO handle province specific holidays
        if date in canada_holidays:
            return True, canada_holidays.get(date)

        return False, NOT_AVAILABLE
