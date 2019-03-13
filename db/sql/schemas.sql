/* SCHEMA DEFINITIONS */

CREATE SCHEMA IF NOT EXISTS accidents_weather_data_mart;
CREATE SCHEMA IF NOT EXISTS dimension_pre_stage;
CREATE SCHEMA IF NOT EXISTS relations;
CREATE SCHEMA IF NOT EXISTS data_source;

/* DATA SOURCE TABLES */

CREATE TABLE IF NOT EXISTS data_source.climate_data_ontario (
  id                  SERIAL PRIMARY KEY,
  date_time           TEXT,
  year                TEXT,
  month               TEXT,
  day                 TEXT,
  time                TEXT,
  temp_c              TEXT,
  temp_flag           TEXT,
  dew_point_temp_c    TEXT,
  dew_point_temp_flag TEXT,
  rel_hum_percent     TEXT,
  rel_hum_flag        TEXT,
  wind_dir_10s_deg    TEXT,
  wind_dir_flag       TEXT,
  wind_spd_km_h       TEXT,
  wind_spd_flag       TEXT,
  visibility_km       TEXT,
  visibility_flag     TEXT,
  stn_press_kpa       TEXT,
  stn_press_flag      TEXT,
  hmdx                TEXT,
  hmdx_flag           TEXT,
  wind_chill          TEXT,
  wind_chill_flag     TEXT,
  weather             TEXT,
  station_name        TEXT,
  province            TEXT
);

CREATE TABLE IF NOT EXISTS data_source.climate_data_alberta (
  id                  SERIAL PRIMARY KEY,
  date_time           TEXT,
  year                TEXT,
  month               TEXT,
  day                 TEXT,
  time                TEXT,
  temp_c              TEXT,
  temp_flag           TEXT,
  dew_point_temp_c    TEXT,
  dew_point_temp_flag TEXT,
  rel_hum_percent     TEXT,
  rel_hum_flag        TEXT,
  wind_dir_10s_deg    TEXT,
  wind_dir_flag       TEXT,
  wind_spd_km_h       TEXT,
  wind_spd_flag       TEXT,
  visibility_km       TEXT,
  visibility_flag     TEXT,
  stn_press_kpa       TEXT,
  stn_press_flag      TEXT,
  hmdx                TEXT,
  hmdx_flag           TEXT,
  wind_chill          TEXT,
  wind_chill_flag     TEXT,
  weather             TEXT,
  station_name        TEXT,
  province            TEXT
);

CREATE TABLE IF NOT EXISTS data_source.raw_station_inventory (
  id          SERIAL PRIMARY KEY,
  name        TEXT,
  latitude    TEXT,
  longitude   TEXT,
  elevation   TEXT
);

CREATE TABLE IF NOT EXISTS data_source.collision_data_ottawa (
  id                          SERIAL PRIMARY KEY,
  collision_id                TEXT,
  location                    TEXT,
  x                           TEXT,
  y                           TEXT,
  longitude                   TEXT,
  latitude                    TEXT,
  date                        TEXT,
  time                        TEXT,
  environment                 TEXT,
  light                       TEXT,
  surface_condition           TEXT,
  traffic_control             TEXT,
  traffic_control_condition   TEXT,
  collision_classification    TEXT,
  impact_type                 TEXT,
  no_of_pedestrians           TEXT
);

CREATE TABLE IF NOT EXISTS data_source.collision_data_toronto (
  id              SERIAL PRIMARY KEY,
  x               TEXT,
  y               TEXT,
  index_          TEXT,
  accnum          TEXT,
  year            TEXT,
  date            TEXT,
  time            TEXT,
  hour            TEXT,
  street1         TEXT,
  street2         TEXT,
  "offset"        TEXT,
  road_class      TEXT,
  district        TEXT,
  latitude        TEXT,
  longitude       TEXT,
  loccoord        TEXT,
  accloc          TEXT,
  traffctl        TEXT,
  visibility      TEXT,
  light           TEXT,
  rdsfcond        TEXT,
  acclass         TEXT,
  impactype       TEXT,
  invtype         TEXT,
  invage          TEXT,
  injury          TEXT,
  fatal_no        TEXT,
  initdir         TEXT,
  vehtype         TEXT,
  manoeuver       TEXT,
  drivact         TEXT,
  drivcond        TEXT,
  pedtype         TEXT,
  pedact          TEXT,
  pedcond         TEXT,
  cyclistype      TEXT,
  cycact          TEXT,
  cyccond         TEXT,
  pedestrian      TEXT,
  cyclist         TEXT,
  automobile      TEXT,
  motorcycle      TEXT,
  truck           TEXT,
  trsn_city_veh   TEXT,
  emerg_veh       TEXT,
  passenger       TEXT,
  speeding        TEXT,
  ag_driv         TEXT,
  redlight        TEXT,
  alcohol         TEXT,
  disability      TEXT,
  division        TEXT,
  ward_name       TEXT,
  ward_id         TEXT,
  hood_id         TEXT,
  hood_name       TEXT,
  fid             TEXT
);

CREATE TABLE IF NOT EXISTS data_source.collision_data_calgary (
  id                  SERIAL PRIMARY KEY,
  date                TEXT,
  collision_location  TEXT,
  collision_severity  TEXT,
  comm_name           TEXT,
  comm_code           TEXT,
  latitude            TEXT,
  longitude           TEXT,
  point               TEXT,
  "4a3i-ccfj"         TEXT,
  "4b54-tmc4"         TEXT,
  "p8tp-5dkv"         TEXT,
  "kxmf-bzkv"         TEXT
);

/* ACCIDENTS WEATHER DATA MART */

CREATE TABLE IF NOT EXISTS accidents_weather_data_mart.hour_dimension (
  hour_key      INTEGER PRIMARY KEY,
  hour_start    TIME NOT NULL,
  hour_end      TIME NOT NULL,
  date          DATE NOT NULL,
  day_of_week   VARCHAR(10) NOT NULL,
  month         VARCHAR(20) NOT NULL,
  year          VARCHAR(5) NOT NULL,
  is_weekend    BOOLEAN NOT NULL,
  is_holiday    BOOLEAN NOT NULL,
  holiday_name  VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS accidents_weather_data_mart.weather_dimension (
  weather_key               INTEGER PRIMARY KEY,
  station_name              VARCHAR(200) NOT NULL,
  longitude                 FLOAT NOT NULL,
  latitude                  FLOAT NOT NULL,
  elevation                 FLOAT NOT NULL,
  temperature               FLOAT,
  temperature_flag          VARCHAR(20),
  dew_point_temp            FLOAT,
  dew_point_temp_flag       VARCHAR(20),
  relative_humidity         FLOAT,
  relative_humidity_flag    VARCHAR(20),
  wind_direction            FLOAT,
  wind_direction_flag       VARCHAR(20),
  wind_speed                FLOAT,
  wind_speed_flag           VARCHAR(20),
  visibility                FLOAT,
  visibility_flag           VARCHAR(20),
  station_pressure          FLOAT,
  station_pressure_flag     VARCHAR(20),
  humidex                   FLOAT,
  humidex_flag              VARCHAR(20),
  wind_chill                FLOAT,
  wind_chill_flag           VARCHAR(20),
  weather                   VARCHAR(200),
  weather_flag              VARCHAR(20)
);

/* RELATIONS */

CREATE TABLE IF NOT EXISTS relations.weather_hour_relation (
  id SERIAL PRIMARY KEY,
  weather_key INTEGER,
  hour_key INTEGER
);

/* PRE-STAGE DIMENSIONS */

CREATE TABLE IF NOT EXISTS dimension_pre_stage.hour_dimension_pre_stage (
  hour_key      SERIAL PRIMARY KEY,
  hour_start    TIME NOT NULL,
  hour_end      TIME NOT NULL,
  date          DATE NOT NULL,
  day_of_week   VARCHAR(10) NOT NULL,
  month         VARCHAR(20) NOT NULL,
  year          VARCHAR(5) NOT NULL,
  is_weekend    BOOLEAN NOT NULL,
  is_holiday    BOOLEAN NOT NULL,
  holiday_name  VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS dimension_pre_stage.weather_dimension_pre_stage (
  weather_key               SERIAL PRIMARY KEY,
  station_name              VARCHAR(200) NOT NULL,
  longitude                 FLOAT NOT NULL,
  latitude                  FLOAT NOT NULL,
  elevation                 FLOAT NOT NULL,
  date                      DATE NOT NULL,
  time                      TIME NOT NULL,
  temperature               FLOAT,
  temperature_flag          VARCHAR(20),
  dew_point_temp            FLOAT,
  dew_point_temp_flag       VARCHAR(20),
  relative_humidity         FLOAT,
  relative_humidity_flag    VARCHAR(20),
  wind_direction            FLOAT,
  wind_direction_flag       VARCHAR(20),
  wind_speed                FLOAT,
  wind_speed_flag           VARCHAR(20),
  visibility                FLOAT,
  visibility_flag           VARCHAR(20),
  station_pressure          FLOAT,
  station_pressure_flag     VARCHAR(20),
  humidex                   FLOAT,
  humidex_flag              VARCHAR(20),
  wind_chill                FLOAT,
  wind_chill_flag           VARCHAR(20),
  weather                   VARCHAR(200),
  weather_flag              VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS dimension_pre_stage.accident_dimension_pre_stage(
  id                          SERIAL PRIMARY KEY,
  longitude                   FLOAT NOT NULL,
  latitude                    FLOAT NOT NULL,
  date                        DATE NOT NULL,
  time                        TIME NOT NULL,
  street_name                 VARCHAR(50) NOT NULL,
  street1                     VARCHAR(50),
  street2                     VARCHAR(60),
  environment                 VARCHAR(60),
  environment_flag            VARCHAR(60),
  road_surface                VARCHAR(60),
  road_surface_flag           VARCHAR(60),
  traffic_control             VARCHAR(60),
  traffic_control_flag        VARCHAR(60),
  visibility                  VARCHAR(10),
  visibility_flag             VARCHAR(60),
  collision_classification    VARCHAR(60),
  collision_classification_flag VARCHAR(60),
  impact_type                 VARCHAR(60),
  impact_type_flag            VARCHAR(60)
);