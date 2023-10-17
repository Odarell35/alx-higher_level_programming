-- lists all records with a score greater than or equal to 10 from the second_table of the hbtn_0c_0 database,
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;