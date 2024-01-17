-- Records in the table second_table listed with a score >= 10 in my MySQL server
-- Records ordered in descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
