-- number of records with the same score in table second_table in MySQL server listed
-- Records ordered in descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
