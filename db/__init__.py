from db.DatabaseConnection import DatabaseConnection
from db.config import config
from utils.stations import WEATHER_STATIONS, OTTAWA_STATIONS, TORONTO_STATIONS


def init_schemas():
    _get_postgres_version()
    _create_schemas()


def _get_postgres_version():
    db = DatabaseConnection()

    with db.get_connection().cursor() as cursor:
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print('PostgreSQL database version: ' + db_version[0])


def _create_schemas():
    print("Initializing schemas...")
    db = DatabaseConnection()
    connection = db.get_connection()

    with connection.cursor() as cursor:
        with open("db/sql/schemas.sql", "r") as f:
            sql = f.read()
            cursor.execute(sql)

    print("Schemas successfully created.")


class DataSource(object):

    data_source_files = config(section='data_source_files')

    raw_station_inventory_file = data_source_files.get('raw_station_inventory_file')

    collision_data_ottawa_2014 = data_source_files.get('collision_data_ottawa_2014')
    collision_data_ottawa_2015 = data_source_files.get('collision_data_ottawa_2015')
    collision_data_ottawa_2016 = data_source_files.get('collision_data_ottawa_2016')
    collision_data_ottawa_2017 = data_source_files.get('collision_data_ottawa_2017')
    # collision_data_calgary = data_source_files.get('collision_data_calgary')
    collision_data_toronto = data_source_files.get('collision_data_toronto')

    climate_data_alberta_1 = data_source_files.get('climate_data_alberta_1')
    climate_data_alberta_2 = data_source_files.get('climate_data_alberta_2')
    climate_data_alberta_3 = data_source_files.get('climate_data_alberta_3')
    climate_data_alberta_4 = data_source_files.get('climate_data_alberta_4')
    climate_data_alberta_5 = data_source_files.get('climate_data_alberta_5')
    climate_data_alberta_6 = data_source_files.get('climate_data_alberta_6')

    climate_data_ontario_1 = data_source_files.get('climate_data_ontario_1')
    climate_data_ontario_2 = data_source_files.get('climate_data_ontario_2')
    climate_data_ontario_3 = data_source_files.get('climate_data_ontario_3')
    climate_data_ontario_4 = data_source_files.get('climate_data_ontario_4')
    climate_data_ontario_5 = data_source_files.get('climate_data_ontario_5')
    climate_data_ontario_6 = data_source_files.get('climate_data_ontario_6')

    def __init__(self,
                 populate_ontario_climate_data=False,
                 populate_alberta_climate_data=False,
                 # populate_calgary_climate_data=False,
                 populate_ottawa_climate_data=False,
                 populate_toronto_climate_data=False,
                 # populate_calgary_collision_data=False,
                 populate_ottawa_collision_data=False,
                 populate_toronto_collision_data=False,
                 populate_raw_station_inventory_data=False,
                 populate_station_inventory_data=False):

        # POPULATE CLIMATE DATA
        self.populate_ontario_climate_data = populate_ontario_climate_data
        self.populate_alberta_climate_data = populate_alberta_climate_data
        # self.populate_calgary_climate_data = populate_calgary_climate_data
        self.populate_ottawa_climate_data = populate_ottawa_climate_data
        self.populate_toronto_climate_data = populate_toronto_climate_data

        # POPULATE COLLISION DATA
        # self.populate_calgary_collision_data = populate_calgary_collision_data
        self.populate_ottawa_collision_data = populate_ottawa_collision_data
        self.populate_toronto_collision_data = populate_toronto_collision_data

        # POPULATE STATION INVENTORY DATA
        self.populate_raw_station_inventory_data = populate_raw_station_inventory_data
        self.populate_station_inventory_data = populate_station_inventory_data

    def populate(self):

        if self.populate_ottawa_collision_data:
            self.populate_ottawa_collision_table()

        # if self.populate_calgary_collision_data:
        #     self.populate_calgary_collision_table()

        if self.populate_toronto_collision_data:
            self.populate_toronto_collision_table()

        if self.populate_ontario_climate_data:
            self.populate_ontario_climate_table()

        if self.populate_alberta_climate_data:
            self.populate_alberta_climate_table()

        # if self.populate_calgary_climate_data:
        #     self.populate_calgary_climate_table()

        if self.populate_ottawa_climate_data:
            self.populate_ottawa_climate_table()

        if self.populate_toronto_climate_data:
            self.populate_toronto_climate_table()

        if self.populate_raw_station_inventory_data:
            self.populate_raw_station_inventory_table()

        if self.populate_station_inventory_data:
            self.populate_station_inventory_table()

    def populate_ottawa_collision_table(self):
        print("Populating data_source.collision_data_ottawa...")

        sql = """COPY data_source.collision_data_ottawa(
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
                                    no_of_pedestrians)
                                 FROM STDIN CSV HEADER NULL ''"""

        self.copy_data_from_csv(self.collision_data_ottawa_2014, sql)
        self.copy_data_from_csv(self.collision_data_ottawa_2015, sql)
        self.copy_data_from_csv(self.collision_data_ottawa_2016, sql)
        self.copy_data_from_csv(self.collision_data_ottawa_2017, sql)

        print("data_source.collision_data_ottawa successfully populated.")

    # def populate_calgary_collision_table(self):
    #     print("Populating data_source.collision_data_calgary...")
    #
    #     sql = """COPY data_source.collision_data_calgary(
    #                                 date,
    #                                 collision_location,
    #                                 collision_severity,
    #                                 comm_name,
    #                                 comm_code,
    #                                 latitude,
    #                                 longitude,
    #                                 point,
    #                                 "4a3i-ccfj",
    #                                 "4b54-tmc4",
    #                                 "p8tp-5dkv",
    #                                 "kxmf-bzkv")
    #                              FROM STDIN CSV HEADER NULL ''"""
    #
    #     self.copy_data_from_csv(self.collision_data_calgary, sql)
    #
    #     print("data_source.collision_data_calgary successfully populated.")

    def populate_toronto_collision_table(self):
        print("Populating data_source.collision_data_toronto...")

        sql = """COPY data_source.collision_data_toronto(
                                    x, y, index_, accnum, year, date, time, hour, street1, street2, "offset",
                                    road_class, district, latitude, longitude, loccoord, accloc, traffctl,
                                    visibility, light, rdsfcond, acclass, impactype, invtype, invage, injury, fatal_no,
                                    initdir, vehtype, manoeuver, drivact, drivcond, pedtype, pedact, pedcond, 
                                    cyclistype, cycact, cyccond, pedestrian, cyclist, automobile, motorcycle, truck, 
                                    trsn_city_veh, emerg_veh, passenger, speeding, ag_driv, redlight, alcohol, 
                                    disability, division, ward_name, ward_id, hood_id, hood_name, fid)
                                 FROM STDIN CSV HEADER NULL ''"""

        self.copy_data_from_csv(self.collision_data_toronto, sql)

        print("data_source.collision_data_toronto successfully populated.")

    def populate_ontario_climate_table(self):
        print("Populating data_source.climate_data_ontario...")

        sql = """COPY data_source.climate_data_ontario(
                                    date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                                    dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                                    wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                                    stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                                    weather, station_name, province)
                                 FROM STDIN CSV HEADER NULL ''"""

        self.copy_data_from_csv(self.climate_data_ontario_1, sql)
        print(self.climate_data_ontario_1 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_ontario_2, sql)
        print(self.climate_data_ontario_2 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_ontario_3, sql)
        print(self.climate_data_ontario_3 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_ontario_4, sql)
        print(self.climate_data_ontario_4 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_ontario_5, sql)
        print(self.climate_data_ontario_5 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_ontario_6, sql)
        print(self.climate_data_ontario_6 + " successfully inserted into db")

        print("data_source.climate_data_ontario successfully populated.")

    def populate_alberta_climate_table(self):
        print("Populating data_source.climate_data_alberta...")

        sql = """COPY data_source.climate_data_alberta(
                                    date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                                    dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                                    wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                                    stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                                    weather, station_name, province)
                                 FROM STDIN CSV HEADER NULL ''"""

        self.copy_data_from_csv(self.climate_data_alberta_1, sql)
        print(self.climate_data_alberta_1 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_alberta_2, sql)
        print(self.climate_data_alberta_2 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_alberta_3, sql)
        print(self.climate_data_alberta_3 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_alberta_4, sql)
        print(self.climate_data_alberta_4 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_alberta_5, sql)
        print(self.climate_data_alberta_5 + " successfully inserted into db")

        self.copy_data_from_csv(self.climate_data_alberta_6, sql)
        print(self.climate_data_alberta_6 + " successfully inserted into db")

        print("data_source.climate_data_alberta successfully populated.")

    # def populate_calgary_climate_table(self):
    #     print("Populating data_source.climate_data_calgary...")
    #
    #     sql = """CREATE TABLE data_source.climate_data_calgary AS
    #              SELECT * FROM data_source.climate_data_alberta
    #              WHERE station_name in %s"""
    #
    #     self.create_filtered_stations_table(sql, CALGARY_STATIONS)
    #
    #     print("data_source.climate_data_calgary successfully populated.")

    def populate_ottawa_climate_table(self):
        print("Populating data_source.climate_data_ottawa...")

        sql = """CREATE TABLE data_source.climate_data_ottawa AS
                 SELECT * FROM data_source.climate_data_ontario
                 WHERE station_name in %s"""

        self.create_filtered_stations_table(sql, OTTAWA_STATIONS)

        print("data_source.climate_data_ottawa successfully populated.")

    def populate_toronto_climate_table(self):
        print("Populating data_source.climate_data_toronto...")

        sql = """CREATE TABLE data_source.climate_data_toronto AS
                 SELECT * FROM data_source.climate_data_ontario
                 WHERE station_name in %s"""

        self.create_filtered_stations_table(sql, TORONTO_STATIONS)

        print("data_source.climate_data_toronto successfully populated.")

    def populate_raw_station_inventory_table(self):
        print("Populating data_source.raw_station_inventory...")

        sql = """COPY data_source.raw_station_inventory(name, latitude, longitude, elevation) 
                 FROM STDIN CSV HEADER NULL ''"""

        self.copy_data_from_csv(self.raw_station_inventory_file, sql)

        print("data_source.raw_station_inventory successfully populated.")

    def populate_station_inventory_table(self):
        print("Populating data_source.station_inventory...")

        sql = """CREATE TABLE data_source.station_inventory AS
                 SELECT DISTINCT ON (name) * FROM data_source.raw_station_inventory
                 WHERE name in %s"""

        self.create_filtered_stations_table(sql, WEATHER_STATIONS)

        print("data_source.station_inventory successfully populated.")

    @staticmethod
    def create_filtered_stations_table(sql, stations):
        db = DatabaseConnection()
        connection = db.get_connection()

        with connection.cursor() as cursor:
            cursor.execute(sql, (stations,))

    @staticmethod
    def copy_data_from_csv(file_path, sql):
        db = DatabaseConnection()
        connection = db.get_connection()

        with connection.cursor() as cursor:
            with open(file_path) as f:
                cursor.copy_expert(file=f, sql=sql)
