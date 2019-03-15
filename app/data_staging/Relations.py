from db.dal.relations.AccidentHourRelationDAL import AccidentHourRelationDAL
from db.dal.relations.AccidentLocationRelationDAL import AccidentLocationRelationDAL
from db.dal.relations.WeatherHourRelationDAL import WeatherHourRelationDAL


class Relations(object):

    @staticmethod
    def create_weather_hour_relation():
        WeatherHourRelationDAL.connect_weather_hour_dimension()

    @staticmethod
    def create_weather_location_relation():
        print("Not yet implemented")

    @staticmethod
    def create_accident_hour_relation():
        AccidentHourRelationDAL.connect_accident_hour_dimension()

    @staticmethod
    def create_accident_location_relation():
        AccidentLocationRelationDAL.connect_accident_location_dimension()
