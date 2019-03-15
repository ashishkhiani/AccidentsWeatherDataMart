import math
import re

from geopy import distance

from db.dal.data_source.CollisionDataCalgaryDAL import CollisionDataCalgaryDAL
from db.dal.data_source.CollisionDataOttawaDAL import CollisionDataOttawaDAL
from db.dal.data_source.CollisionDataTorontoDAL import CollisionDataTorontoDAL
from db.dal.dimension_pre_stage.LocationDimensionPreStageDAL import LocationDimensionPreStageDAL
from utils.utilities import is_null_or_empty


class LocationDimensionPreStage(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the location pre-stage dimension during the data pre-staging phase.
    This class can use any of the DAL classes defined.
    The location pre-stage dimension contains all the attributes necessary including ones
    that will help connect with other dimensions
    """

    @staticmethod
    def populate():

        # Calgary Location Data
        print("Populating dimension_pre_stage.location_dimension_pre_stage with Calgary data...")
        LocationDimensionPreStage.populate_helper(
            count=CollisionDataCalgaryDAL.get_count(),
            data=CollisionDataCalgaryDAL.fetch_all(),
            city="Calgary"
        )
        print("Successfully populated Calgary data in dimension_pre_stage.location_dimension_pre_stage.")

        # Ottawa Location Data
        print("Populating dimension_pre_stage.location_dimension_pre_stage with Ottawa data...")
        LocationDimensionPreStage.populate_helper(
            count=CollisionDataOttawaDAL.get_count(),
            data=CollisionDataOttawaDAL.fetch_all(),
            city="Ottawa"
        )
        print("Successfully populated Ottawa data in dimension_pre_stage.location_dimension_pre_stage.")

        # Toronto Location Data
        print("Populating dimension_pre_stage.location_dimension_pre_stage with Toronto data...")
        LocationDimensionPreStage.populate_helper(
            count=CollisionDataTorontoDAL.get_count(),
            data=CollisionDataTorontoDAL.fetch_all(),
            city="Toronto"
        )
        print("Successfully populated Toronto data in dimension_pre_stage.location_dimension_pre_stage.")

    @staticmethod
    def populate_helper(count, data, city):
        entities = []

        i = 1
        for row in data:
            entities.append(LocationDimensionPreStage.handle_raw_collision_data(row, city))

            if len(entities) == 500:  # insert entities into db in batches of 500
                LocationDimensionPreStageDAL.insert_many(entities)
                entities.clear()  # clear list to free up memory
                print("Completed batch " + str(i) + " of " + str(math.ceil(count / 500)))
                i += 1

        if len(entities) > 0:  # insert any remaining records into db
            LocationDimensionPreStageDAL.insert_many(entities)
            entities.clear()
            print("Completed batch " + str(i) + " of " + str(math.ceil(count / 500)))

    @staticmethod
    def handle_raw_collision_data(row, city):
        if city == "Ottawa":
            return LocationDimensionPreStage.handle_raw_ottawa_location_data(row)
        elif city == "Toronto":
            return LocationDimensionPreStage.handle_raw_toronto_location_data(row)
        elif city == "Calgary":
            return LocationDimensionPreStage.handle_raw_calgary_location_data(row)

    @staticmethod
    def handle_raw_ottawa_location_data(row):

        longitude, latitude, street_name, intersection_1, intersection_2 = \
            LocationDimensionPreStage.handle_location_data(row, "Ottawa")

        city = 'Ottawa'

        neighbourhood = None

        entity = (street_name,
                  intersection_1,
                  intersection_2,
                  longitude,
                  latitude,
                  city,
                  neighbourhood)

        return entity

    @staticmethod
    def handle_raw_calgary_location_data(row):

        longitude, latitude, street_name, intersection_1 = \
            LocationDimensionPreStage.handle_location_data(row, "Calgary")

        intersection_2 = None

        city = 'Calgary'

        neighbourhood = None

        entity = (street_name,
                  intersection_1,
                  intersection_2,
                  longitude,
                  latitude,
                  city,
                  neighbourhood)

        return entity

    @staticmethod
    def handle_raw_toronto_location_data(row):

        longitude, latitude, street_name, intersection_1, neighbourhood = \
            LocationDimensionPreStage.handle_location_data(row, "Toronto")

        intersection_2 = None

        city = 'Toronto'

        entity = (street_name,
                  intersection_1,
                  intersection_2,
                  longitude,
                  latitude,
                  city,
                  neighbourhood)

        return entity

    @staticmethod
    def handle_location_data(row, city):
        if city == "Ottawa":
            if is_null_or_empty(row['longitude']):
                raise Exception("Longitude is empty/null")
            if is_null_or_empty(row['latitude']):
                raise Exception("Latitude is empty/null")
            if is_null_or_empty(row['location']):
                raise Exception("Location is empty/null")

            longitude = row['longitude']
            latitude = row['latitude']
            street_name, intersection_1, intersection_2 = LocationDimensionPreStage.parse_ottawa_location(
                row['location'])

            return float(longitude), float(latitude), street_name, intersection_1, intersection_2

        elif city == "Toronto":
            if is_null_or_empty(row['longitude']):
                raise Exception("Longitude is empty/null")
            if is_null_or_empty(row['latitude']):
                raise Exception("Latitude is empty/null")
            if is_null_or_empty(row['street1']):
                raise Exception("Street name is empty/null")

            longitude = row['longitude']
            latitude = row['latitude']
            street_name = row['street1']
            intersection_1 = row['street2']
            neighbourhood = row['district']

            return float(longitude), float(latitude), street_name, intersection_1, neighbourhood

        elif city == "Calgary":
            if is_null_or_empty(row['longitude']):
                raise Exception("Longitude is empty/null")
            if is_null_or_empty(row['latitude']):
                raise Exception("Latitude is empty/null")
            if is_null_or_empty(row['collision_location']):
                raise Exception("Collision location is empty/null")

            longitude = row['longitude']
            latitude = row['latitude']
            street_name, intersection_1 = LocationDimensionPreStage.parse_calgary_location(
                 row['collision_location'])  

            return float(longitude), float(latitude), street_name, intersection_1

    @staticmethod
    def parse_ottawa_location(street_string):
        parsed_streets = []
        if '@' in street_string:
            parsed_streets = street_string.split('@')
            parsed_streets[1] = parsed_streets[1].lstrip()
            parsed_streets.append(None)
        elif '&' in street_string:
            temp_parsed_streets = street_string.split("btwn")
            parsed_intersection = temp_parsed_streets[1].split('&', 1)
            parsed_streets.append(temp_parsed_streets[0])
            parsed_streets = parsed_streets + parsed_intersection
            parsed_streets[1] = parsed_streets[1].lstrip()
            parsed_streets[2] = parsed_streets[2].lstrip()
        else:
            parsed_streets.append(street_string)
            parsed_streets.append(None)
            parsed_streets.append(None)

        return parsed_streets

    @staticmethod
    def parse_calgary_location(street_string):
        if '&' in street_string:
            parsed_streets = street_string.split('&')
            parsed_streets[0] = parsed_streets[0].lstrip()
            parsed_streets[1] = parsed_streets[1].lstrip()
        else:
            street_string = re.sub('\s+', ' ', street_string)
            parsed_streets = re.findall("[\d| ]*[\D| ]*", street_string)
            parsed_streets[0] = parsed_streets[0].rstrip()
            parsed_streets.pop()
            if len(parsed_streets) == 1:
                parsed_streets.append(None)

        return parsed_streets

    @staticmethod
    def get_closest_weather_station(latitude, longitude, station_inventory):
        min_distance = float('inf')
        closest_station = None

        for station, station_data in station_inventory.items():

            d = distance.distance(
                (latitude, longitude),
                (float(station_data['latitude']), float(station_data['longitude']))
            )

            if d < min_distance:
                min_distance = d
                closest_station = station

        return closest_station
