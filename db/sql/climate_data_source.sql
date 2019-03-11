CREATE SCHEMA IF NOT EXISTS data_source;

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

COPY data_source.climate_data_ontario(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/ontario_1_1.csv' CSV HEADER NULL '';

COPY data_source.climate_data_ontario(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/ontario_1_2.csv' CSV HEADER NULL '';

COPY data_source.climate_data_ontario(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/ontario_2_1.csv' CSV HEADER NULL '';

COPY data_source.climate_data_ontario(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/ontario_2_2.csv' CSV HEADER NULL '';

COPY data_source.climate_data_ontario(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/ontario_3.csv' CSV HEADER NULL '';

COPY data_source.climate_data_ontario(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/ontario_4.csv' CSV HEADER NULL '';

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

COPY data_source.climate_data_alberta(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/alberta_1_1.csv' CSV HEADER NULL '';

COPY data_source.climate_data_alberta(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/alberta_1_2.csv' CSV HEADER NULL '';

COPY data_source.climate_data_alberta(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/alberta_2_1.csv' CSV HEADER NULL '';

COPY data_source.climate_data_alberta(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/alberta_2_2.csv' CSV HEADER NULL '';

COPY data_source.climate_data_alberta(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/alberta_3_1.csv' CSV HEADER NULL '';

COPY data_source.climate_data_alberta(date_time, year, month, day, time, temp_c, temp_flag, dew_point_temp_c,
                              dew_point_temp_flag, rel_hum_percent, rel_hum_flag, wind_dir_10s_deg,
                              wind_dir_flag, wind_spd_km_h, wind_spd_flag, visibility_km, visibility_flag,
                              stn_press_kpa, stn_press_flag, hmdx, hmdx_flag, wind_chill, wind_chill_flag,
                              weather, station_name, province)
FROM '/Users/AshishK/Desktop/climate_data_files/alberta_3_2.csv' CSV HEADER NULL '';


CREATE TABLE data_source.climate_data_calgary AS
SELECT * FROM data_source.climate_data_alberta
WHERE station_name in (
  'CALGARY INT''L A',
  'CALGARY INT''L CS',
  'CALGARY INTL A',
  'COP UPPER');

CREATE TABLE data_source.climate_data_ottawa AS
SELECT * FROM data_source.climate_data_ontario
WHERE station_name in (
    'OTTAWA CDA RCS',
    'OTTAWA MACDONALD-CARTIER INT''L A',
    'OTTAWA INTL A');


CREATE TABLE data_source.climate_data_toronto AS
SELECT * FROM data_source.climate_data_ontario
WHERE station_name in (
    'PA MATTAMY ATHLETIC CENTRE',
    'TORONTO CITY',
    'TORONTO CITY CENTRE',
    'PA ROYAL CANADIAN YACHT CLUB',
    'PA DUFFERIN AND ST. CLAIR CIBC',
    'PA TORONTO HYUNDAI',
    'PA SCARBOROUGH TORONTO HUNT',
    'PA TORONTO NORTH YORK MOTORS',
    'PA ATMOS NORTH YORK',
    'PA DOWNSVIEW PARK',
    'PA DOWNSVIEW',
    'PA YORK UNIVERSITY',
    'PA MARKHAM NORTH TOYOTA',
    'TORONTO INTL A',
    'TORONTO LESTER B. PEARSON INT''L A',
    'PA U OF T SCARBOROUGH TENNIS CENTRE',
    'PA HERSHEY CENTRE',
    'PA CONCORD RYDER',
    'TORONTO BUTTONVILLE A'
    'PA MONOPOLY PROPERTY MANAGEMENT',
    'PA ATMOS MISSISSAUGA');


CREATE TABLE IF NOT EXISTS data_source.raw_station_inventory (
  id          SERIAL PRIMARY KEY,
  name        TEXT,
  latitude    TEXT,
  longitude   TEXT,
  elevation   TEXT
);

COPY data_source.raw_station_inventory(name, latitude, longitude, elevation)
FROM '/Users/AshishK/Desktop/station_inventory.csv' CSV HEADER NULL '';

CREATE TABLE data_source.station_inventory AS
SELECT * FROM data_source.raw_station_inventory
WHERE name in (
    'CALGARY INT''L A',
    'CALGARY INT''L CS',
    'CALGARY INTL A',
    'COP UPPER',
    'OTTAWA CDA RCS',
    'OTTAWA MACDONALD-CARTIER INT''L A',
    'OTTAWA INTL A',
    'PA MATTAMY ATHLETIC CENTRE',
    'TORONTO CITY',
    'TORONTO CITY CENTRE',
    'PA ROYAL CANADIAN YACHT CLUB',
    'PA DUFFERIN AND ST. CLAIR CIBC',
    'PA TORONTO HYUNDAI',
    'PA SCARBOROUGH TORONTO HUNT',
    'PA TORONTO NORTH YORK MOTORS',
    'PA ATMOS NORTH YORK',
    'PA DOWNSVIEW PARK',
    'PA DOWNSVIEW',
    'PA YORK UNIVERSITY',
    'PA MARKHAM NORTH TOYOTA',
    'TORONTO INTL A',
    'TORONTO LESTER B. PEARSON INT''L A',
    'PA U OF T SCARBOROUGH TENNIS CENTRE',
    'PA HERSHEY CENTRE',
    'PA CONCORD RYDER',
    'TORONTO BUTTONVILLE A'
    'PA MONOPOLY PROPERTY MANAGEMENT',
    'PA ATMOS MISSISSAUGA');