-- lists the number of records with the same score
11;rgb:2b2b/2b2b/2b2bSELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER number DESC;
