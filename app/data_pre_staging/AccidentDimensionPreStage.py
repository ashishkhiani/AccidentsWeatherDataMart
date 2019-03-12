import math
from datetime import datetime

from db.dal.data_source.ClimateDataCalgaryDAL import CollisionDataOttawaDAL
from db.dal.data_source.ClimateDataCalgaryDAL import CollisionDataTorontoDAL
from db.dal.data_source.ClimateDataCalgaryDAL import CollisionDataCalgaryDAL

from utils.flags import AVAILABLE, ESTIMATED, NOT_AVAILABLE
from utils.utilities import is_null_or_empty, is_estimated, is_missing_or_unavailable


class AccidentDimensionPreStage(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the weather pre-stage dimension during the data pre-staging phase.

    This class can use any of the DAL classes defined.

    The weather pre-stage dimension contains all the attributes necessary including ones
    that will help connect with other dimensions
    """

    @staticmethod
    def populate():
        entities = []
        accidents = dict()
"""
(id,
collision_id,
location,
x,
y,
longitude,
latitude,
date,
time,
environment,
light,
surface_condition,
traffic_control,
traffic_control_condition,
collision_classification,
impact_type,
no_of_pedestrians)"""

        for accident in CollisionDataOttawaDAL.fetch_all():
            accident[accident['id']] = {
                'longitude': accident['longitude'],
                'latitude': accident['latitude'],
                'location': accident['location'],
            }

        i = 1
        count = CollisionDataOttawaDAL.get_count()
        for row in CollisionDataOttawaDAL.fetch_all():
            entities.append(AccidentDimensionPreStage.handle_raw_climate_data(row, accident))

            if len(entities) == 500:  # insert entities into db in batches of 500
                # TODO insert into weather dimension pre-stage table
                entities.clear()  # clear list to free up memory
                print("Completed batch " + str(i) + " of " + str(math.ceil(count/500)))
                i += 1

        if len(entities) > 0:  # insert any remaining records into db
            # TODO insert into weather dimension pre-stage table
            entities.clear()
            print("Completed batch " + str(i) + " of " + str(math.ceil(count / 500)))

        # TODO handle Calgary Climate Data

        # TODO handle Toronto Climate Data

    @staticmethod
    def handle_raw_accident_data(row, accidents):

        id, longitude, latitude, location = \
            AccidentDimensionPreStage.handle_accident_data(row['id'], accidents)

        collision_id, x, y = \
            row["COLLISION_ID"], row["X"], row["Y"]

        date = AccidentDimensionPreStage.handle_date_time(row['date'], row['time'])

        environment, environment_flag  = \
            AccidentDimensionPreStage.handle_id_condition(row['light'])

        light, light_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['light'])

        surface_condition, surface_condition_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['surface_condition'])

        traffic_control, traffic_control_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['traffic_control'])

        traffic_control_condition, traffic_control_condition_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['traffic_control_condition'])
        
        collision_classification, collision_classification_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['collision_classification'])
        
        impact_type, impact_type_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['impact_type'])

        no_of_pedestrians = \
            row["no_of_pedestrians"]

        entity = (id,
                  collision_id,
                  location,
                  longitude,
                  latitude,
                  date,
                  time,
                  environment,
                  environment_flag,
                  light,
                  light_flag,
                  surface_condition,
                  surface_condition,
                  traffic_control,
                  traffic_control_flag,
                  traffic_control_condition,
                  traffic_control_condition_flag,
                  collision_classification,
                  collision_classification_flag,
                  impact_type,
                  impact_type_flag,
                  no_of_pedestrians)

        return entity

    @staticmethod
    def handle_accident_data(accident_id, accidents):
        if is_null_or_empty(accident_id):
            raise Exception("Station name is empty/null")

        if accident_id not in accidents:
            raise Exception("Station name does not exist in station inventory")

        accident_data = accidents.get(accident_id)

        longitude = accident_data['longitude']
        latitude = accident_data['latitude']
        location = accident_data['location']

        if is_null_or_empty(longitude) or is_null_or_empty(latitude):
            raise Exception("Longitude/Latitude is empty/null")

        if is_null_or_empty(location):
            raise Exception("Elevation is empty/null")

        

        return accident_id, round(float(longitude), 2), round(float(latitude), 2), round(float(location), 2)


    @staticmethod
    def handle_id_condition(id_cond):
        flag = AVAILABLE
        if is_null_or_empty(id_cond):
            flag = NOT_AVAILABLE

        env = id_cond.split('-')
        return env[1], flag

    @staticmethod
    def handle_date_and_time(date, time):
        if is_null_or_empty(date):
            raise Exception("Date is empty/null")
        if is_null_or_empty(time):
            raise Exception("Time is empty/null")

        return datetime.strptime(date+" "+time, '%Y-%m-%d %I:%M:%S %p')

    @staticmethod
    def handle_float_data_and_flag(data, flag):
        if is_null_or_empty(data) or is_missing_or_unavailable(flag):
            return None, NOT_AVAILABLE

        value = round(float(data), 2)

        if is_estimated(flag):  # estimated data
            return value, ESTIMATED

        return value, AVAILABLE