CREATE SCHEMA IF NOT EXISTS dimension_pre_stage;

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
)

CREATE TABLE IF NOT EXISTS dimension_pre_stage.weather_dimension_pre_stage (
CREATE TABLE IF NOT EXISTS data_source.collision_data_ottawa_pre_stage (
  id                          INTEGER PRIMARY KEY,
  collision_id                TEXT,
  location                    TEXT,
  x                           TEXT,
  y                           TEXT,
  longitude                   TEXT,
  latitude                    TEXT,
  date                        TEXT,
  time                        TEXT,
  environment                 TEXT,
  environment_flag            TEXT,
  light                       TEXT,
  light_flag                  TEXT,
  surface_condition           TEXT,
  surface_condition_flag      TEXT,
  traffic_control             TEXT,
  traffic_control             TEXT,
  traffic_control_condition   TEXT,
  traffic_control_condition_flag   TEXT,
  collision_classification         TEXT,
  collision_classification_flag    TEXT,
  impact_type                 TEXT,
  impact_type_flag            TEXT,
  no_of_pedestrians           TEXT
);