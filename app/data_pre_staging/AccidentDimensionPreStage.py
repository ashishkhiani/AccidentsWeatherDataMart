import math, re
from datetime import datetime, time

from db.dal.data_source.CollisionDataOttawaDAL import CollisionDataOttawaDAL
from db.dal.data_source.CollisionDataTorontoDAL import CollisionDataTorontoDAL
from db.dal.dimension_pre_stage.AccidentDimensionPreStageDAL import AccidentDimensionPreStageDAL

from utils.flags import AVAILABLE, ESTIMATED, NOT_AVAILABLE
from utils.utilities import is_null_or_empty, is_estimated, is_missing_or_unavailable
from utils.utilities import ENVIRONMENT, VISIBILITY, ROAD_SURFACE, TRAFFIC_CONTROL, COLLISION_CLASSIFICATION, IMPACT_TYPE
from utils.utilities import parse_ottawa_location

class AccidentDimensionPreStage(object):
    """
    The functionality of this class is to define the business logic necessary
    to populate the accident pre-stage dimension during the data pre-staging phase.

    This class can use any of the DAL classes defined.

    The accident pre-stage dimension contains all the attributes necessary including ones
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
        i = 1
        count = CollisionDataCalgaryDAL.get_count()

        for row in CollisionDataCalgaryDAL.fetch_all():
            entities.append(AccidentDimensionPreStage.handle_raw_calgary_accident_data(row))
            
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




        i = 1
        count = CollisionDataTorontoDAL.get_count()
        # TODO handle Toronto Climate Data
        for row in CollisionDataTorontoDAL.fetch_all():
            entities.append(AccidentDimensionPreStage.handle_raw_toronto_accident_data(row))
            
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

    @staticmethod
    def handle_raw_ottawa_accident_data(row):

        longitude, latitude, street_name, street1, street2 = \
            AccidentDimensionPreStage.handle_accident_data(row, "Ottawa")

        date, time = AccidentDimensionPreStage.handle_ottawa_date_and_time(row['date'], row['time'])

        environment, environment_flag = \
            AccidentDimensionPreStage.handle_ottawa_environment(row['environment'])

        visibility, visibility_flag = \
            AccidentDimensionPreStage.handle_ottawa_light_condition(row['light'])

        road_surface, road_surface_flag = \
            AccidentDimensionPreStage.handle_ottawa_road_surface_condition(row['surface_condition'])

        traffic_control, traffic_control_flag = \
            AccidentDimensionPreStage.handle_ottawa_traffic_condition(row['traffic_control'])
        
        collision_classification, collision_classification_flag = \
            AccidentDimensionPreStage.handle_ottawa_collision_condition(row['collision_classification'])
        
        impact_type, impact_type_flag = \
            AccidentDimensionPreStage.handle_ottawa_impact_condition(row['impact_type'])

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
    def handle_raw_calgary_accident_data(row):

        longitude, latitude, street_name, street1 = \
            AccidentDimensionPreStage.handle_accident_data(row, "Calgary")

        street2 = None

        date, time = AccidentDimensionPreStage.handle_calgary_date_and_time(row['date'])

        environment, environment_flag = None, NOT_AVAILABLE

        visibility, visibility_flag = None, NOT_AVAILABLE

        road_surface, road_surface_flag = None, NOT_AVAILABLE

        traffic_control, traffic_control_flag = None, NOT_AVAILABLE
        
        collision_classification, collision_classification_flag = \
            AccidentDimensionPreStage.handle_calgary_collision_condition(row['collision_classification'])
        
        impact_type, impact_type_flag = None, NOT_AVAILABLE

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
    def handle_raw_toronto_accident_data(row):

        longitude, latitude, street_name, street1 = \
            AccidentDimensionPreStage.handle_accident_data(row, "Toronto")
        street2 = None
        date, time = AccidentDimensionPreStage.handle_toronto_date_and_time(row['date'])

        environment, environment_flag = \
            AccidentDimensionPreStage.handle_toronto_environment(row['visibility'])

        visibility, visibility_flag = \
            AccidentDimensionPreStage.handle_toronto_light_condition(row['light'])

        road_surface, road_surface_flag = \
            AccidentDimensionPreStage.handle_toronto_road_surface_condition(row['rdsfcond'])

        traffic_control, traffic_control_flag = \
            AccidentDimensionPreStage.handle_toronto_traffic_condition(row['traffctl'])
        
        collision_classification, collision_classification_flag = \
            AccidentDimensionPreStage.handle_toronto_collision_condition(row['acclass'])
        
        impact_type, impact_type_flag = \
            AccidentDimensionPreStage.handle_toronto_impact_condition(row['impactype'])

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
    def handle_accident_data(row, city):
        if city == "Ottawa":
            if is_null_or_empty(row['longitude']):
                raise Exception("Longitude is empty/null")
            if is_null_or_empty(row['latitude']):
                raise Exception("Latitude is empty/null")
            if is_null_or_empty(row['location']):
                raise Exception("Location is empty/null")


            longitude = row['longitude']
            latitude = row['latitude']
            street_name, street1, street2 = parse_ottawa_location(row['location'])
            return float(longitude), float(latitude), street_name, street1, street2
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
            street1 = row['street2']

            return float(longitude), float(latitude), street_name, street1
        elif city == "Calgary":
            if is_null_or_empty(row['longitude']):
                raise Exception("Longitude is empty/null")
            if is_null_or_empty(row['latitude']):
                raise Exception("Latitude is empty/null")
            if is_null_or_empty(row['collision_location']):
                raise Exception("Collision location is empty/null")

            longitude = row['longitude']
            latitude = row['latitude']
            street_name, street1, _ = parse_calgary_location(row['collision_location']) # IF WE HAVE STREET2, REPLACE _ WITH IT here and in accident data func.
            return float(longitude), float(latitude), street_name, street1

    @staticmethod
    def handle_ottawa_environment(environment):
        flag = AVAILABLE
        if is_null_or_empty(environment):
            flag = NOT_AVAILABLE
            return None, flag

        env = environment.split('-')
        if env[1].lower().strip() not in ENVIRONMENT:
            raise Exception("{} is an invalid/unknown environment variable".format(env[1]))
        return env[1], flag

    @staticmethod
    def handle_toronto_environment(environment):
        flag = AVAILABLE
        if is_null_or_empty(environment):
            flag = NOT_AVAILABLE
            return None, flag

        if environment.lower().strip() not in ENVIRONMENT:
            raise Exception("{} is an invalid/unknown environment variable".format(environment))
        return environment, flag

    @staticmethod
    def handle_ottawa_light_condition(light):
        flag = AVAILABLE
        if is_null_or_empty(light):
            flag = NOT_AVAILABLE
            return None, flag

        env = light.split('-')
        if env[1].lower().strip() not in VISIBILITY:
            raise Exception("{} is an invalid/unknown visibility variable".format(env[1]))
        return env[1], flag

    @staticmethod
    def handle_toronto_light_condition(light):
        flag = AVAILABLE
        if is_null_or_empty(light):
            flag = NOT_AVAILABLE
            return None, flag

        if light.lower().strip() not in VISIBILITY:
            raise Exception("{} is an invalid/unknown visibility variable".format(light))
        return light, flag

    @staticmethod
    def handle_ottawa_road_surface_condition(surface):
        flag = AVAILABLE
        if is_null_or_empty(surface):
            flag = NOT_AVAILABLE
            return None, flag

        env = surface.split('-')
        if env[1].lower().strip() not in ROAD_SURFACE:
            raise Exception("{} is an invalid/unknown road surface variable".format(env[1]))

        return env[1], flag

    @staticmethod
    def handle_toronto_road_surface_condition(surface):
        flag = AVAILABLE
        if is_null_or_empty(surface):
            flag = NOT_AVAILABLE
            return None, flag

        if surface.lower().strip() not in ROAD_SURFACE:
            raise Exception("{} is an invalid/unknown road surface variable".format(surface))

        return surface, flag

    @staticmethod
    def handle_ottawa_traffic_condition(traffic):
        flag = AVAILABLE
        if is_null_or_empty(traffic):
            flag = NOT_AVAILABLE
            return None, flag

        env = traffic.split('-')
        if env[1].lower().strip() not in TRAFFIC_CONTROL:
            raise Exception("{} is an invalid/unknown traffic control variable".format(env[1]))

        return env[1], flag

    @staticmethod
    def handle_toronto_traffic_condition(traffic):
        flag = AVAILABLE
        if is_null_or_empty(traffic):
            flag = NOT_AVAILABLE
            return None, flag

        if traffic.lower().strip() not in TRAFFIC_CONTROL:
            raise Exception("{} is an invalid/unknown traffic control variable".format(traffic))

        return traffic, flag

    @staticmethod
    def handle_ottawa_collision_condition(collision):
        flag = AVAILABLE
        if is_null_or_empty(collision):
            flag = NOT_AVAILABLE
            return None, flag

        r = re.compile(r"^([^-]+)-")
        env = r.split(collision)

        if env[-1].lower().strip() == "fatal injury":
            env[-1] = "Fatal"

        if env[-1].lower().strip() not in COLLISION_CLASSIFICATION:
            raise Exception("{} is an invalid/unknown collision classification variable".format(env[-1].lower().strip()))

        return env[-1], flag
    
    @staticmethod
    def handle_toronto_collision_condition(collision):
        flag = AVAILABLE
        if is_null_or_empty(collision):
            flag = NOT_AVAILABLE
            return None, flag

        if collision.lower().strip() not in COLLISION_CLASSIFICATION:
            raise Exception("{} is an invalid/unknown collision classification variable".format(collision))

        return collision, flag

    @staticmethod
    def handle_ottawa_impact_condition(impact):
        flag = AVAILABLE
        if is_null_or_empty(impact):
            flag = NOT_AVAILABLE
            return None, flag

        env = impact.split('-')

        if env[1].lower().strip() not in IMPACT_TYPE:
            raise Exception("{} is an invalid/unknown impact variable".format(env[1].lower().strip()))

        return env[1], flag

    @staticmethod
    def handle_toronto_impact_condition(impact):
        flag = AVAILABLE
        if is_null_or_empty(impact):
            flag = NOT_AVAILABLE
            return None, flag

        if impact.lower().strip() not in IMPACT_TYPE:
            raise Exception("{} is an invalid/unknown impact variable".format(impact))

        return impact, flag

    @staticmethod
    def handle_ottawa_date_and_time(date, time):
        if is_null_or_empty(date):
            raise Exception("Date is empty/null")
        if is_null_or_empty(time):
            raise Exception("Time is empty/null")

        return datetime.strptime(date, '%Y-%m-%d').date(), datetime.strptime(time, '%I:%M:%S %p').time()

    @staticmethod
    def handle_calgary_date_and_time(date):
        if is_null_or_empty(date):
            raise Exception("Date is empty/null")

        return datetime.strptime(date, '%Y-%m-%d').date(), time(0,0)

    @staticmethod
    def handle_toronto_date_and_time(date):
        if is_null_or_empty(date):
            raise Exception("Date is empty/null")

        date_time = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        return date_time, date_time

    @staticmethod
    def handle_float_data_and_flag(data, flag):
        if is_null_or_empty(data) or is_missing_or_unavailable(flag):
            return None, NOT_AVAILABLE

        value = round(float(data), 2)

        if is_estimated(flag):  # estimated data
            return value, ESTIMATED

        return value, AVAILABLE
