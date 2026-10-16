-- IBM Applied Data Science Capstone — SpaceX SQL analysis

SELECT * FROM SPACEXTBL LIMIT 20;

SELECT MIN(PayloadMass) AS Minimum_Payload_Mass
FROM SPACEXTBL;

SELECT SUM(PayloadMass) AS Total_Payload_Mass
FROM SPACEXTBL;

SELECT LaunchSite,
       COUNT(Outcome) AS MISSION_OUTCOME_COUNT
FROM SPACEXTBL
GROUP BY LaunchSite;

SELECT DISTINCT LaunchSite
FROM SPACEXTBL;

SELECT LaunchSite,
       COUNT(*) AS launches,
       SUM(Class) AS successful_landings,
       ROUND(100.0 * AVG(Class), 1) AS success_rate_percent
FROM SPACEXTBL
GROUP BY LaunchSite
ORDER BY success_rate_percent DESC;
