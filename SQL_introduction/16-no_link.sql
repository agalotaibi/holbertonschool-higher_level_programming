-- lists all records of the table without the null value
SELECT score, name
FROM second_table
ORDER BY score DESC
WHERE name IS NOT NULL;
