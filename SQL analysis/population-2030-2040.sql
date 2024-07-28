SELECT * FROM [population-2030-2040-1 (1)];

DELETE FROM [population-2030-2040-1 (1)] WHERE time='nan'
-- LOCATION --
SELECT Location FROM [population-2030-2040-1 (1)]

-- Population by location
SELECT Location, ROUND(PopMale, 3) AS Male_population, ROUND(PopFemale, 3) AS Female_population, ROUND((PopMale + PopFemale), 3) AS Total_population 
FROM [population-2030-2040-1 (1)];

-- Highest population at each location
SELECT DISTINCT(Location), Time, ROUND(MAX(PopTotal), 3) AS Maximum_Population
FROM [population-2030-2040-1 (1)]
GROUP BY Location, Time
ORDER BY Maximum_Population DESC;

-- Average male and female population at each location
SELECT DISTINCT(Location), Time, ROUND(AVG(PopMale), 3) AS AvgMalePopulation, ROUND(AVG(PopFemale), 3) AS AvgFemalePopulation
FROM [population-2030-2040-1 (1)]
GROUP BY Location, Time
ORDER BY Location;

-- Highest male and female population at each location
SELECT DISTINCT(Location), Time, ROUND(MAX(PopMale), 3) AS HighestMalePopulation, ROUND(MAX(PopFemale), 3) AS HighestFemalePopulation
FROM [population-2030-2040-1 (1)]
GROUP BY Location, Time
ORDER BY Location;

-- Highest male population at each location
SELECT DISTINCT(Location), Time, ROUND(MAX(PopMale), 3) AS Maximum_Male_Population
FROM [population-2030-2040-1 (1)]
GROUP BY Location, Time
ORDER BY Maximum_Male_Population DESC;

-- Highest female population at each location
SELECT DISTINCT(Location), Time, ROUND(MAX(PopFemale), 3) AS Maximum_Female_Population
FROM [population-2030-2040-1 (1)]
GROUP BY Location, Time
ORDER BY Maximum_Female_Population DESC;

-- TIME --

-- Total Population by Location
SELECT Location, ROUND(SUM(PopTotal), 3) AS TotalPopulation
FROM [population-2030-2040-1 (1)]
GROUP BY Location
ORDER BY TotalPopulation DESC;

-- Highest population in each year
SELECT DISTINCT(Time), ROUND(MAX(PopTotal), 3) AS Maximum_Population
FROM [population-2030-2040-1 (1)]
GROUP BY Time
ORDER BY Maximum_Population DESC;

-- Average male and female population for each year
SELECT DISTINCT(Time), ROUND(AVG(PopMale), 3) AS AvgMalePopulation, ROUND(AVG(PopFemale), 3) AS AvgFemalePopulation
FROM [population-2030-2040-1 (1)]
GROUP BY Time
ORDER BY Time;

-- AGE GROUP --

-- Highest population of each age group
SELECT DISTINCT(AgeGrp), Time, ROUND(MAX(PopTotal), 3) AS Maximum_Population
FROM [population-2030-2040-1 (1)]
GROUP BY AgeGrp, Time
ORDER BY Maximum_Population DESC;

-- Highest male population of each age group
SELECT DISTINCT(AgeGrp), Time, ROUND(MAX(PopMale), 3) AS Maximum_Male_Population
FROM [population-2030-2040-1 (1)]
GROUP BY AgeGrp, Time
ORDER BY Maximum_Male_Population DESC;

-- Highest female population of each age group
SELECT DISTINCT(AgeGrp), Time, ROUND(MAX(PopFemale), 3) AS Maximum_Female_Population
FROM [population-2030-2040-1 (1)]
GROUP BY AgeGrp, Time
ORDER BY Maximum_Female_Population DESC;

-- Average male population of each age group
SELECT DISTINCT(AgeGrp), Time, ROUND(AVG(PopMale), 3) AS Average_Male_Population
FROM [population-2030-2040-1 (1)]
GROUP BY AgeGrp, Time
ORDER BY Average_Male_Population DESC;

-- Average female population of each age group
SELECT DISTINCT(AgeGrp), Time, ROUND(AVG(PopFemale), 3) AS Average_Female_Population
FROM [population-2030-2040-1 (1)]
GROUP BY AgeGrp, Time
ORDER BY Average_Female_Population DESC;
