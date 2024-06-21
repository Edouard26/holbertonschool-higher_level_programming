USE hbtn_0d_usa;

-- Ensure states exist
INSERT IGNORE INTO states (name)
VALUES ('California'), ('Arizona'), ('Texas'), ('Utah');

-- Insert cities
INSERT INTO cities (state_id, name)
VALUES
    ((SELECT id FROM states WHERE name = 'California'), 'San Jose'),
    ((SELECT id FROM states WHERE name = 'California'), 'San Francisco'),
    (NULL, 'Page'),
    (NULL, 'Houston'),
    (NULL, 'Dallas'),
    (NULL, 'Paris');

-- List all states
SELECT id, name
FROM states;

-- List all cities of California, Arizona, Texas, and Utah
SELECT cities.name
FROM cities
WHERE cities.state_id IN (SELECT id FROM states WHERE name IN ('California', 'Arizona', 'Texas', 'Utah'))
ORDER BY cities.id ASC;

