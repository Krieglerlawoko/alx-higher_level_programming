-- Cities contained in the database hbtn_0d_usa listed
-- Rows of a particular column in a database listed
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
