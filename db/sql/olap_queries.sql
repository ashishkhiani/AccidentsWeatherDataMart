--Write OLAP queries here

-- Question 5
SELECT L.street_name, L.intersection_1, COUNT(*) AS counted
FROM   accidents_weather_data_mart.accident_fact F,
	accidents_weather_data_mart.hour_dimension H,
	accidents_weather_data_mart.location_dimension L,
	accidents_weather_data_mart.accident_dimension AC,
	accidents_weather_data_mart.weather_dimension W
WHERE  H.year > '2014'
	AND L.is_intersection
	AND H.hour_key = F.hour_key
	AND L.location_key = F.location_key
	AND AC.accident_key = F.accident_key
	AND W.weather_key = F.weather_key
GROUP BY L.street_name, L.intersection_1
ORDER BY counted DESC, L.street_name
LIMIT  10;

-- This is a query below to support the results from the above query; Bank has the most accidents at intersections,
-- however it does since it's so long it is the most common singular street, but does not contain the most common
-- intersection.

-- SELECT L.street_name, L.intersection_1
-- FROM   accidents_weather_data_mart.accident_fact F,
-- 	accidents_weather_data_mart.location_dimension L
-- WHERE L.is_intersection AND L.street_name = 'BANK ST '
-- 	AND L.location_key = F.location_key
-- ORDER BY L.intersection_1


-- Question 6 - Sub-optimal
SELECT
 H.year,
 H.day_of_week,
 COUNT (F.is_fatal) AS average_amount
FROM
 accidents_weather_data_mart.accident_fact F,
 accidents_weather_data_mart.hour_dimension H
WHERE
	H.year > '2014'
	AND H.hour_key = F.hour_key
GROUP BY
 H.day_of_week, H.year
ORDER BY
 H.year, H.day_of_week;