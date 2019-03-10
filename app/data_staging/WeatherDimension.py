from datetime import datetime
from db.dal.data_source.ClimateDataCalgaryDAL import ClimateDataCalgaryDAL
from db.dal.data_source.ClimateDataOttawaDAL import ClimateDataOttawaDAL
from db.dal.data_source.ClimateDataTorontoDAL import ClimateDataTorontoDAL
from db.dal.data_source.StationInventoryDAL import StationInventoryDAL
from utils.flags import AVAILABLE, ESTIMATED, NOT_AVAILABLE
from utils.utilities import is_null_or_empty, is_estimated, is_missing_or_unavailable


class WeatherDimension(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the weather dimension during the data staging phase.

    This class can use any of the DAL classes defined.
    """

    @staticmethod
    def populate():
        entities = []

        for row in ClimateDataCalgaryDAL.fetch_all():
            entities.append(WeatherDimension.handle_raw_climate_data(row))

            if len(entities) == 500:
                # connect weather to hour in relations table
                # insert batch of entities into db
                entities.clear()

        # for row in ClimateDataOttawaDAL.fetch_all():
        #     entities.append(WeatherDimension.handle_climate_data(row))
        #
        # for row in ClimateDataTorontoDAL.fetch_all():
        #     entities.append(WeatherDimension.handle_climate_data(row))
        print(entities)

    @staticmethod
    def handle_raw_climate_data(row):
        station_name, longitude, latitude, elevation = WeatherDimension.handle_station_data(row['station_name'])
        date = WeatherDimension.handle_date_time(row['date_time'])

        temperature, temperature_flag = \
            WeatherDimension.handle_float_data_and_flag(row['temp_c'], row['temp_flag'])

        dew_point_temp, dew_point_temp_flag = \
            WeatherDimension.handle_float_data_and_flag(row['dew_point_temp_c'], row['dew_point_temp_flag'])

        relative_humidity, relative_humidity_flag =\
            WeatherDimension.handle_float_data_and_flag(row['rel_hum_percent'], row['rel_hum_flag'])

        wind_direction, wind_direction_flag =\
            WeatherDimension.handle_float_data_and_flag(row['wind_dir_10s_deg'], row['wind_dir_flag'])

        wind_speed, wind_speed_flag =\
            WeatherDimension.handle_float_data_and_flag(row['wind_spd_km_h'], row['wind_spd_flag'])

        visibility, visibility_flag =\
            WeatherDimension.handle_float_data_and_flag(row['visibility_km'], row['visibility_flag'])

        station_pressure, station_pressure_flag = \
            WeatherDimension.handle_float_data_and_flag(row['stn_press_kpa'], row['stn_press_flag'])

        humidex, humidex_flag = \
            WeatherDimension.handle_float_data_and_flag(row['hmdx'], row['hmdx_flag'])

        wind_chill, wind_chill_flag =\
            WeatherDimension.handle_float_data_and_flag(row['wind_chill'], row['wind_chill_flag'])

        entity = (station_name,
                  longitude,
                  latitude,
                  date,
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
                  wind_chill_flag)

        return entity

    @staticmethod
    def handle_station_data(station_name):
        if is_null_or_empty(station_name):
            raise Exception("Station name is empty/null")

        station_data = StationInventoryDAL.fetch_by_name(station_name)
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
    def connect_weather_to_hour(weather_key, hour_key, date_time):
        pass
