CREATE TABLE IF NOT EXISTS data_source.collision_data_ottawa (
  id                        SERIAL NOT NULL,
  location                  TEXT,
  x                         TEXT,
  y                         TEXT,
  date                      TEXT,
  time                      TEXT,
  environment               TEXT,
  road_Surface              TEXT,
  traffic_Control           TEXT,
  collision_Location        TEXT,
  light                     TEXT,
  collision_Classification  TEXT,
  impact_Type               TEXT
);

--For 2014 Ottawa Collision Data, file was converted to csv.
COPY data_source.collision_data_ottawa(id, location, x, y, date, time, environment, road_Surface, traffic_Control, collision_Location, light, collision_Classification, impact_Type)
FROM '/Users/AshishK/Desktop/collision_data/ottawa/2014collisionsfinal.csv' CSV HEADER NULL '';

--For 2015 Ottawa Collision Data, file was converted to csv.
COPY data_source.collision_data_ottawa(id, location, x, y, date, time, environment, road_Surface, traffic_Control, collision_Location, light, collision_Classification, impact_Type)
FROM '/Users/AshishK/Desktop/collision_data/ottawa/2015collisionsfinal.csv' CSV HEADER NULL '';

--For 2016 Ottawa Collision Data, file was converted to csv.
COPY data_source.collision_data_ottawa(id, location, x, y, date, time, environment, road_Surface, traffic_Control, collision_Location, light, collision_Classification, impact_Type)
FROM '/Users/AshishK/Desktop/collision_data/ottawa/2016collisionsfinal.csv' CSV HEADER NULL '';

--For 2017 Ottawa Collision Data, Longitude, Latitude and Year columns were removed. File was converted to csv.
COPY data_source.collision_data_ottawa(id, location, x, y, date, time, environment, road_Surface, traffic_Control, collision_Location, light, collision_Classification, impact_Type)
FROM '/Users/AshishK/Desktop/collision_data/ottawa/2017collisionsfinal.csv' CSV HEADER NULL '';



CREATE TABLE IF NOT EXISTS data_source.collision_data_toronto (
  id              SERIAL NOT NULL,
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

COPY data_source.collision_data_toronto(x, y,	index_, accnum, year, date, time, hour, street1, street2, "offset",
                                        road_class, district, latitude, longitude, loccoord, accloc, traffctl,
                                        visibility, light, rdsfcond, acclass, impactype, invtype, invage, injury, fatal_no,
                                        initdir, vehtype, manoeuver, drivact, drivcond, pedtype, pedact, pedcond, cyclistype,
                                        cycact, cyccond, pedestrian, cyclist, automobile, motorcycle, truck, trsn_city_veh,
                                        emerg_veh, passenger, speeding, ag_driv, redlight, alcohol, disability, division,
                                        ward_name, ward_id, hood_id, hood_name, fid)
FROM '/Users/AshishK/Desktop/collision_data/toronto/Fatal_Collisions.csv' CSV HEADER NULL '';



CREATE TABLE IF NOT EXISTS data_source.collision_data_calgary (
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

COPY data_source.collision_data_calgary(date, collision_location, collision_severity, comm_name, comm_code,
                                        latitude, longitude, point, "4a3i-ccfj", "4b54-tmc4", "p8tp-5dkv",
                                        "kxmf-bzkv")
FROM '/Users/AshishK/Desktop/collision_data/calgary/Pedestrian_Motor_Vehicle_Collisions.csv' CSV HEADER NULL '';
