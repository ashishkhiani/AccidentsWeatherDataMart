CREATE SCHEMA IF NOT EXISTS accidents_weather_data_mart;

CREATE TABLE IF NOT EXISTS accidents_weather_data_mart.hour_dimension (
  hour_key SERIAL PRIMARY KEY,
  hour_start TIME NOT NULL,
  hour_end TIME NOT NULL,
  date DATE NOT NULL,
  day_of_week VARCHAR(10) NOT NULL,
  month VARCHAR(20) NOT NULL,
  year VARCHAR(5) NOT NULL,
  is_weekend BOOLEAN NOT NULL,
  is_holiday BOOLEAN NOT NULL,
  holiday_name VARCHAR(200)
);