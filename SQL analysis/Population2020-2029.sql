
-- LOCATION --
SELECT Location from [population_2020-2029]

-- location_population
SELECT Location, ROUND(PopMale, 3) AS Male_population, ROUND(PopFemale, 3) AS Female_population, ROUND((PopMale + PopFemale), 3) AS Total_population 
FROM [population_2020-2029];

-- highest_population_at_each_location
SELECT DISTINCT(Location), Time, ROUND(MAX(PopTotal), 3) AS Maximum_Population
FROM [population_2020-2029]
GROUP BY Location, Time
ORDER BY Maximum_Population DESC;

-- average_male_and_female_population_at_each_location
SELECT DISTINCT(Location), Time, ROUND(AVG(PopMale), 3) AS AvgMalePopulation, ROUND(AVG(PopFemale),3) AS AvgFemalePopulation
FROM [population_2020-2029]
GROUP BY Location, Time
ORDER BY Location;

-- highest_male_and_female_population_at_each_location
SELECT DISTINCT(Location), Time, ROUND(MAX(PopMale), 3) AS HighestMalePopulation, ROUND(MAX(PopFemale), 3) AS HighestFemalePopulation
FROM [population_2020-2029]
GROUP BY Location, Time
ORDER BY Location;

-- highest_male_population_at_each_location
SELECT DISTINCT(Location), Time, ROUND(MAX(PopMale), 3) AS Maximum_Male_Population
FROM [population_2020-2029]
GROUP BY Location, Time
ORDER BY Maximum_Male_Population DESC;

-- highest_female_population_at_each_location
SELECT DISTINCT(Location), Time, ROUND(MAX(PopFemale), 3) AS Maximum_Female_Population
FROM [population_2020-2029]
GROUP BY Location, Time
ORDER BY Maximum_Female_Population DESC;

-- TIME --

-- total_population_by_location
SELECT Location, ROUND(SUM(PopTotal), 3) AS TotalPopulation
FROM [population_2020-2029]
WHERE Time = 2020
GROUP BY Location
ORDER BY TotalPopulation DESC;

-- highest_population_in_each_year
SELECT DISTINCT(Time), ROUND(MAX(PopTotal), 3) AS Maximum_Population
FROM [population_2020-2029]
GROUP BY Time
ORDER BY Maximum_Population DESC;

-- average_male_and_female_population_for_each_year
SELECT DISTINCT(Time), ROUND(AVG(PopMale), 3) AS AvgMalePopulation, ROUND(AVG(PopFemale), 3) AS AvgFemalePopulation
FROM [population_2020-2029]
GROUP BY Time
ORDER BY Time;

-- AGE GROUP --

-- highest_population_of_each_age_group
SELECT DISTINCT(AgeGrp), Time, ROUND(MAX(PopTotal), 3) AS Maximum_Population
FROM [population_2020-2029]
GROUP BY AgeGrp, Time
ORDER BY Maximum_Population DESC;

-- highest_male_population_of_each_age_group
SELECT DISTINCT(AgeGrp), Time, ROUND(MAX(PopMale), 3) AS Maximum_Male_Population
FROM [population_2020-2029]
GROUP BY AgeGrp, Time
ORDER BY Maximum_Male_Population DESC;

-- highest_female_population_of_each_age_group
SELECT DISTINCT(AgeGrp), Time, ROUND(MAX(PopFemale), 3) AS Maximum_Female_Population
FROM [population_2020-2029]
GROUP BY AgeGrp, Time
ORDER BY Maximum_Female_Population DESC;

-- average_male_population_of_each_age_group
SELECT DISTINCT(AgeGrp), Time, ROUND(AVG(PopMale), 3) AS Average_Male_Population
FROM [population_2020-2029]
GROUP BY AgeGrp, Time
ORDER BY Average_Male_Population DESC;

-- average_female_population_of_each_age_group
SELECT DISTINCT(AgeGrp), Time, ROUND(AVG(PopFemale), 3) AS Average_Female_Population
FROM [population_2020-2029]
GROUP BY AgeGrp, Time
ORDER BY Average_Female_Population DESC;

