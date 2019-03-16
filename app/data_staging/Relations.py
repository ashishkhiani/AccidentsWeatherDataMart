import math

from app.data_pre_staging import LocationDimensionPreStage
from db.dal.data_source.StationInventoryDAL import StationInventoryDAL
from db.dal.relations.AccidentHourRelationDAL import AccidentHourRelationDAL
from db.dal.relations.AccidentLocationRelationDAL import AccidentLocationRelationDAL
from db.dal.relations.WeatherHourRelationDAL import WeatherHourRelationDAL
from db.dal.relations.WeatherLocationRelationDAL import WeatherLocationRelationDAL
from utils.stations import OTTAWA_STATIONS, TORONTO_STATIONS


class Relations(object):

    @staticmethod
    def create_weather_hour_relation():
        WeatherHourRelationDAL.connect_weather_hour_dimension()

    @staticmethod
    def create_weather_location_relation():
        ottawa_stn, toronto_stn = Relations.fetch_station_inventory()

        # Fetch location data
        station_location_pairs = Relations.connect_location_to_weather_station(ottawa_stn=ottawa_stn,
                                                                               toronto_stn=toronto_stn)

        # Connect weather station to weather data
        WeatherLocationRelationDAL.insert_many_temp(station_location_pairs)
        WeatherLocationRelationDAL.connect_weather_to_location_dimension()

    @staticmethod
    def fetch_station_inventory():
        # calgary_stn = dict()
        ottawa_stn = dict()
        toronto_stn = dict()

        for station in StationInventoryDAL.fetch_all():
            station_name = station['name']

            if station_name in OTTAWA_STATIONS:
                ottawa_stn[station_name] = {
                    'longitude': station['longitude'],
                    'latitude': station['latitude'],
                    'city': 'Ottawa'
                }

            elif station_name in TORONTO_STATIONS:
                toronto_stn[station_name] = {
                    'longitude': station['longitude'],
                    'latitude': station['latitude'],
                    'city': 'Toronto'
                }

            # elif station_name in CALGARY_STATIONS:
            #     calgary_stn[station_name] = {
            #         'longitude': station['longitude'],
            #         'latitude': station['latitude'],
            #         'city': 'Calgary'
            #     }

        return ottawa_stn, toronto_stn

    @staticmethod
    def connect_location_to_weather_station(ottawa_stn, toronto_stn):
        station_location_pairs = []

        batch_num = 1
        i = 0

        data = WeatherLocationRelationDAL.get_distinct_locations_and_time_information()
        count = WeatherLocationRelationDAL.get_distinct_locations_and_time_information_count()

        for _object in data:

            if _object['city'] == 'Ottawa':
                closest_station = LocationDimensionPreStage.get_closest_weather_station(
                    latitude=_object['latitude'],
                    longitude=_object['longitude'],
                    station_inventory=ottawa_stn)

            elif _object['city'] == 'Toronto':
                closest_station = LocationDimensionPreStage.get_closest_weather_station(
                    latitude=_object['latitude'],
                    longitude=_object['longitude'],
                    station_inventory=toronto_stn)

            # elif _object['city'] == 'Calgary':
            #     closest_station = LocationDimensionPreStage.get_closest_weather_station(
            #         latitude=_object['latitude'],
            #         longitude=_object['longitude'],
            #         station_inventory=calgary_stn)

            else:
                raise Exception(_object['city'] + " is not supported.")

            # Connect location to weather station
            station_location_pairs.append((closest_station,
                                           _object['location_key'],
                                           _object['date'],
                                           _object['hour_start']))

            if i == 500:
                print("Completed batch " + str(batch_num) + " of " + str(math.ceil(count / 500)))
                batch_num += 1
                i = 0

            i += 1

        if i > 0:
            print("Completed batch " + str(batch_num) + " of " + str(math.ceil(count / 500)))

        return station_location_pairs

    @staticmethod
    def create_accident_hour_relation():
        AccidentHourRelationDAL.connect_accident_hour_dimension()

    @staticmethod
    def create_accident_location_relation():
        AccidentLocationRelationDAL.connect_accident_location_dimension()
