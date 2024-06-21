-- Display cities.id, cities.name and states.name
-- cities.id by ASC order
SELECT
    cities.id, cities.name, states.name
FROM
    cities
JOIN
    states ON cities.state_id = states.id
ORDER BY
    cities.id ASC;
