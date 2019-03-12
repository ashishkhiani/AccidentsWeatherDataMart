import math
from datetime import datetime

from db.dal.data_source.ClimateDataCalgaryDAL import CollisionDataOttawaDAL
from db.dal.data_source.ClimateDataCalgaryDAL import CollisionDataTorontoDAL
from db.dal.data_source.ClimateDataCalgaryDAL import CollisionDataCalgaryDAL
from db.dal.dimension_pre_stage.AccidentDimensionPreStageDAL import AccidentDimensionPreStageDAL

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
        

        i = 1
        count = CollisionDataOttawaDAL.get_count()

        for row in CollisionDataOttawaDAL.fetch_all():
            entities.append(AccidentDimensionPreStage.handle_raw_ottawa_accident_data(row))

            if len(entities) == 500:  # insert entities into db in batches of 500
                AccidentDimensionPreStageDAL.insert_many(entities)
                entities.clear()  # clear list to free up memory
                print("Completed batch " + str(i) + " of " + str(math.ceil(count/500)))
                i += 1

        if len(entities) > 0:  # insert any remaining records into db
            # TODO insert into weather dimension pre-stage table
            AccidentDimensionPreStageDAL.insert_many(entities)
            entities.clear()
            print("Completed batch " + str(i) + " of " + str(math.ceil(count / 500)))

        # TODO handle Calgary Climate Data

        # TODO handle Toronto Climate Data

    @staticmethod
    def handle_raw_ottawa_accident_data(row):

        longitude, latitude, street_name, street1, street2 = \
            AccidentDimensionPreStage.handle_accident_data(row)

        date, time = AccidentDimensionPreStage.handle_date_time(row['date'], row['time'])

        environment, environment_flag  = \
            AccidentDimensionPreStage.handle_id_condition(row['environment'])

        visibility, visibility_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['light'])

        road_surface, road_surface_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['surface_condition'])

        traffic_control, traffic_control_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['traffic_control'])
        
        collision_classification, collision_classification_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['collision_classification'])
        
        impact_type, impact_type_flag = \
            AccidentDimensionPreStage.handle_id_condition(row['impact_type'])

        entity = (longitude,
                  latitude,
                  date,
                  time,
                  street_name,
                  street1,
                  street2,
                  environment,
                  environment_flag,
                  road_surface,
                  road_surface_flag,
                  traffic_control,
                  traffic_control_flag,
                  visibility,
                  visibility_flag,
                  collision_classification,
                  collision_classification_flag,
                  impact_type,
                  impact_type_flag)

        return entity

    @staticmethod
    def handle_accident_data(row):
        if is_null_or_empty(row):
            raise Exception("Row is empty/null")

        longitude = row['longitude']
        latitude = row['latitude']
        street_name = row['street_name']
        street1 = row['street1']
        street2 = row['street2']

        if is_null_or_empty(longitude) or is_null_or_empty(latitude):
            raise Exception("Longitude/Latitude is empty/null")

        if is_null_or_empty(street_name):
            raise Exception("Main street name is empty/null")

        return round(float(longitude), 2), round(float(latitude), 2), street_name, street1, street2


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

        return datetime.strftime(date, '%Y-%m-%d'), datetime.strptime(time, '%I:%M:%S %p')

    @staticmethod
    def handle_float_data_and_flag(data, flag):
        if is_null_or_empty(data) or is_missing_or_unavailable(flag):
            return None, NOT_AVAILABLE

        value = round(float(data), 2)

        if is_estimated(flag):  # estimated data
            return value, ESTIMATED

        return value, AVAILABLE