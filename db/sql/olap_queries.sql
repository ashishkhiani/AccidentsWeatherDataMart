--Total number of fatalities in Ottawa during the 4 years
SELECT
       count(*)
FROM
       accidents_weather_data_mart.accident_fact F,
       accidents_weather_data_mart.location_dimension L,
       accidents_weather_data_mart.hour_dimension H
WHERE
       F.location_key = L.location_key AND
       F.hour_key = H.hour_key AND
       L.city = 'Ottawa' AND
       (H.year = '2014' OR H.year = '2015' OR H.year = '2016' OR H.year = '2017') AND
       F.is_fatal = TRUE;

--Total number of fatalities in Ottawa during 2015
SELECT
       count(*)
FROM
       accidents_weather_data_mart.accident_fact F,
       accidents_weather_data_mart.location_dimension L,
       accidents_weather_data_mart.hour_dimension H
WHERE
       F.location_key = L.location_key AND
       F.hour_key = H.hour_key AND
       L.city = 'Ottawa' AND
       H.year = '2015' AND
       F.is_fatal = TRUE;

-- Total number of fatalities during a Thunderstorm in Ottawa during 2014
SELECT
       count(*)
FROM
       accidents_weather_data_mart.accident_fact F,
       accidents_weather_data_mart.location_dimension L,
       accidents_weather_data_mart.hour_dimension H,
       accidents_weather_data_mart.weather_dimension W
WHERE
       F.location_key = L.location_key AND
       F.hour_key = H.hour_key AND
       F.weather_key = W.weather_key AND
       W.weather LIKE '%Thunderstorm%' AND
       L.city = 'Ottawa' AND
       H.year = '2014';

-- Intersections with the most accidents all time
SELECT
       L.street_name, L.intersection_1, count(*) as c
FROM
       accidents_weather_data_mart.accident_fact F,
       accidents_weather_data_mart.location_dimension L,
       accidents_weather_data_mart.hour_dimension H,
       accidents_weather_data_mart.weather_dimension W,
       accidents_weather_data_mart.accident_dimension A
WHERE
       F.location_key = L.location_key AND
       F.hour_key = H.hour_key AND
       F.weather_key = W.weather_key AND
       F.accident_key = A.accident_key AND
       F.is_intersection = TRUE
GROUP BY
       L.street_name, L.intersection_1

ORDER BY
       c DESC
