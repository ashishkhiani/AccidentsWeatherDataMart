import math
from datetime import datetime

from db.dal.data_source.ClimateDataCalgaryDAL import ClimateDataCalgaryDAL
from db.dal.data_source.ClimateDataOttawaDAL import ClimateDataOttawaDAL
from db.dal.data_source.ClimateDataTorontoDAL import ClimateDataTorontoDAL
from db.dal.data_source.StationInventoryDAL import StationInventoryDAL
from db.dal.dimension_pre_stage.WeatherDimensionPreStageDAL import WeatherDimensionPreStageDAL
from utils.flags import AVAILABLE, ESTIMATED, NOT_AVAILABLE
from utils.utilities import is_null_or_empty, is_estimated, is_missing_or_unavailable


class WeatherDimensionPreStage(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the weather pre-stage dimension during the data pre-staging phase.

    This class can use any of the DAL classes defined.

    The weather pre-stage dimension contains all the attributes necessary including ones
    that will help connect with other dimensions
    """

    @staticmethod
    def populate():
        station_inventory = dict()

        for station in StationInventoryDAL.fetch_all():
            station_inventory[station['name']] = {
                'longitude': station['longitude'],
                'latitude': station['latitude'],
                'elevation': station['elevation']
            }

        # Calgary Climate Data
        print("Populating dimension_pre_stage.weather_dimension_pre_stage with Calgary data...")
        WeatherDimensionPreStage.populate_helper(
            count=ClimateDataCalgaryDAL.get_count(),
            data=ClimateDataCalgaryDAL.fetch_all(),
            station_inventory=station_inventory
        )
        print("Successfully populated Calgary data in dimension_pre_stage.weather_dimension_pre_stage.")

        # Ottawa Climate Data
        print("Populating dimension_pre_stage.weather_dimension_pre_stage with Ottawa data...")
        WeatherDimensionPreStage.populate_helper(
            count=ClimateDataOttawaDAL.get_count(),
            data=ClimateDataOttawaDAL.fetch_all(),
            station_inventory=station_inventory
        )
        print("Successfully populated Ottawa data in dimension_pre_stage.weather_dimension_pre_stage.")

        # Toronto Climate Data
        print("Populating dimension_pre_stage.weather_dimension_pre_stage with Toronto data...")
        WeatherDimensionPreStage.populate_helper(
            count=ClimateDataTorontoDAL.get_count(),
            data=ClimateDataTorontoDAL.fetch_all(),
            station_inventory=station_inventory
        )
        print("Successfully populated Toronto data in dimension_pre_stage.weather_dimension_pre_stage.")

    @staticmethod
    def populate_helper(count, data, station_inventory):
        entities = []

        i = 1
        for row in data:
            entities.append(WeatherDimensionPreStage.handle_raw_climate_data(row, station_inventory))

            if len(entities) == 500:  # insert entities into db in batches of 500
                WeatherDimensionPreStageDAL.insert_many(entities)
                entities.clear()  # clear list to free up memory
                print("Completed batch " + str(i) + " of " + str(math.ceil(count / 500)))
                i += 1

        if len(entities) > 0:  # insert any remaining records into db
            WeatherDimensionPreStageDAL.insert_many(entities)
            entities.clear()
            print("Completed batch " + str(i) + " of " + str(math.ceil(count / 500)))

    @staticmethod
    def handle_raw_climate_data(row, station_inventory):

        station_name, longitude, latitude, elevation = \
            WeatherDimensionPreStage.handle_station_data(row['station_name'], station_inventory)

        date_time = WeatherDimensionPreStage.handle_date_time(row['date_time'])

        temperature, temperature_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['temp_c'], row['temp_flag'])

        dew_point_temp, dew_point_temp_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['dew_point_temp_c'], row['dew_point_temp_flag'])

        relative_humidity, relative_humidity_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['rel_hum_percent'], row['rel_hum_flag'])

        wind_direction, wind_direction_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['wind_dir_10s_deg'], row['wind_dir_flag'])

        wind_speed, wind_speed_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['wind_spd_km_h'], row['wind_spd_flag'])

        visibility, visibility_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['visibility_km'], row['visibility_flag'])

        station_pressure, station_pressure_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['stn_press_kpa'], row['stn_press_flag'])

        humidex, humidex_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['hmdx'], row['hmdx_flag'])

        wind_chill, wind_chill_flag = \
            WeatherDimensionPreStage.handle_float_data_and_flag(row['wind_chill'], row['wind_chill_flag'])

        weather, weather_flag = WeatherDimensionPreStage.handle_weather(row['weather'])

        entity = (station_name,
                  longitude,
                  latitude,
                  elevation,
                  date_time.date(),
                  date_time.time(),
                  temperature,
                  temperature_flag,
                  dew_point_temp,
                  dew_point_temp_flag,
                  relative_humidity,
                  relative_humidity_flag,
                  wind_direction,
                  wind_direction_flag,
                  wind_speed,
                  wind_speed_flag,
                  visibility,
                  visibility_flag,
                  station_pressure,
                  station_pressure_flag,
                  humidex,
                  humidex_flag,
                  wind_chill,
                  wind_chill_flag,
                  weather,
                  weather_flag)

        return entity

    @staticmethod
    def handle_station_data(station_name, station_inventory):
        if is_null_or_empty(station_name):
            raise Exception("Station name is empty/null")

        if station_name not in station_inventory:
            raise Exception("Station name does not exist in station inventory")

        station_data = station_inventory.get(station_name)

        longitude = station_data['longitude']
        latitude = station_data['latitude']
        elevation = station_data['elevation']

        if is_null_or_empty(longitude) or is_null_or_empty(latitude):
            raise Exception("Longitude/Latitude is empty/null")

        if is_null_or_empty(elevation):
            raise Exception("Elevation is empty/null")

        return station_name, round(float(longitude), 2), round(float(latitude), 2), round(float(elevation), 2)

    @staticmethod
    def handle_date_time(date_time):
        if is_null_or_empty(date_time):
            raise Exception("Date is empty/null")

        return datetime.strptime(date_time, '%Y-%m-%d %H:%M')

    @staticmethod
    def handle_float_data_and_flag(data, flag):
        if is_null_or_empty(data) or is_missing_or_unavailable(flag):
            return None, NOT_AVAILABLE

        value = round(float(data), 2)

        if is_estimated(flag):  # estimated data
            return value, ESTIMATED

        return value, AVAILABLE

    @staticmethod
    def handle_weather(weather):
        if is_null_or_empty(weather) or is_missing_or_unavailable(weather):
            return None, NOT_AVAILABLE

        if is_estimated(weather):
            return weather, ESTIMATED

        return weather, AVAILABLE
