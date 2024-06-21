-- Select and list all cities of California

USE hbtn_0d_usa;

SELECT cities.name 
FROM cities, states 
WHERE states.name = 'California' AND cities.state_id = states.id 
ORDER BY cities.id ASC;
