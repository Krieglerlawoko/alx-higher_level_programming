-- Records of the table second_table having a name value in MySQL server listed
-- Records ordered in descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
