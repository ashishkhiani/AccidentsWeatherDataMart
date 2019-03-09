CREATE SCHEMA IF NOT EXISTS accidents_weather_data_mart;
CREATE SCHEMA IF NOT EXISTS relations;

CREATE TABLE IF NOT EXISTS accidents_weather_data_mart.hour_dimension (
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

CREATE TABLE IF NOT EXISTS accidents_weather_data_mart.weather_dimension (
  weather_key               SERIAL PRIMARY KEY,
  station_name              VARCHAR(200) NOT NULL,
  longitude                 FLOAT NOT NULL,
  latitude                  FLOAT NOT NULL,
  elevation                 FLOAT NOT NULL,
  temperature               FLOAT,
  dew_point_temp            FLOAT,
  relative_humidity         FLOAT,
  wind_direction            FLOAT,
  wind_speed                FLOAT,
  wind_speed_flag           VARCHAR(2),
  visibility                FLOAT,
  station_pressure          FLOAT,
  humidex                   FLOAT,
  wind_chill                FLOAT,
  wind_chill_flag           VARCHAR(2),
  weather                   VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS relations.weather_hour_relation (
  id SERIAL PRIMARY KEY,
  weather_key INTEGER,
  hour_key INTEGER
)