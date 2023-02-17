-- script that displays the average temperature (Fahrenheit) 
-- by city ordered by temperature (descending)
SELECT city, AVG((value * 1.8) + 32) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
