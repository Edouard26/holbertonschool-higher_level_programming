-- create_user.sql

-- Create user 'user_0d_1'@'localhost' if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Ensure the user has the correct password
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to 'user_0d_1'@'localhost'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure that the changes take effect
FLUSH PRIVILEGES;
