-- Script that selects only the best student
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
