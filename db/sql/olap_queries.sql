--Write OLAP queries here

-- Question 4
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


-- Question 5 - Improved, tracks accidents by year and day of week, and returns fatal count along with
-- Non-fatal ratio (Fatal/Non-fatal)
SELECT
 H.year,
 H.day_of_week,
 COUNT (F.is_fatal) AS total_amount,
 COUNT(F.is_fatal)::float/Non_fatal.count::float as Fatal_NonFatal_ratio
FROM
 accidents_weather_data_mart.accident_fact F,
 accidents_weather_data_mart.hour_dimension H,
 (SELECT count(F1.is_fatal), H1.day_of_week, H1.year
  FROM accidents_weather_data_mart.accident_fact F1,
 	    accidents_weather_data_mart.hour_dimension H1
  WHERE H1.year > '2014' AND H1.hour_key = F1.hour_key AND NOT F1.is_fatal
  GROUP BY H1.day_of_week, H1.year) as Non_fatal
WHERE
	H.year > '2014'
	AND H.hour_key = F.hour_key
	AND F.is_fatal
	AND Non_fatal.day_of_week = H.day_of_week AND Non_fatal.year = H.year
GROUP BY
 H.day_of_week, H.year, Non_fatal.count
ORDER BY
 H.year, CASE WHEN(
 			 H.day_of_week = 'Monday')
			 THEN 0
			 WHEN (
			 H.day_of_week = 'Tuesday')
			 THEN 1
			 WHEN (
			 H.day_of_week = 'Wednesday')
			 THEN 2
			 WHEN (
			 H.day_of_week = 'Thursday')
			 THEN 3
			 WHEN (
			 H.day_of_week = 'Friday')
			 THEN 4
			 WHEN (
			 H.day_of_week = 'Saturday')
			 THEN 5
			 WHEN (
			 H.day_of_week = 'Sunday')
			 THEN 6
			 END;