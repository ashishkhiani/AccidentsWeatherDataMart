from db.dal.data_mart.AccidentFactDAL import AccidentFactDAL


class AccidentFact(object):

    @staticmethod
    def populate():
        AccidentFactDAL.populate()
        AccidentFact.check_condition_integrity()

    @staticmethod
    def check_condition_integrity():
        data = AccidentFactDAL.fetch_conditions()

        for row in data:

            if row['environment'] is None:
                row['environment'] = ''
            environment = row['environment'].lower()
            if row['road_surface'] is None:
                row['road_surface'] = ''
            road_surface = row['road_surface'].lower()
            if row['weather'] is None:
                row['weather'] = ''
            weather = row['weather'].lower()

            accident_condition = AccidentFact.check_accident_precipitation(environment, road_surface)
            weather_condition = AccidentFact.check_weather_precipitation(weather)

            if accident_condition == weather_condition:
                update_value = True
            else:
                update_value = False

            AccidentFactDAL.update_condition_integrity(row['fact_id'], update_value)

    @staticmethod
    def check_accident_precipitation(environment, road_surface):

        road_surface_list = ['ice', 'loose snow', 'mud', 'packed snow',
                             'slush', 'spilled liquid', 'wet']

        if 'rain' in environment or 'snow' in environment or 'fog' in environment:
            return True

        for condition in road_surface_list:
            if road_surface == condition:
                return True

        return False

    @staticmethod
    def check_weather_precipitation(weather):
        if 'rain' in weather or 'drizzle' in weather or 'ice' in weather or 'haze' in weather or 'snow' in weather or 'fog' in weather or 'thunderstorm' in weather:
            return True
        else:
            return False
