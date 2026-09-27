-- Create DB
CREATE DATABASE IF NOT EXISTS cms;
USE cms;

-- 🔥 FIX: create user properly
CREATE USER IF NOT EXISTS 'cms_user'@'localhost' IDENTIFIED BY 'password123';

-- Give full access to cms DB
GRANT ALL PRIVILEGES ON cms.* TO 'cms_user'@'localhost';

FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255)
);

INSERT INTO users (username, password)
SELECT * FROM (SELECT 'admin', MD5('password123')) AS tmp
WHERE NOT EXISTS (
    SELECT username FROM users WHERE username='admin'
) LIMIT 1;

CREATE TABLE secrets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    secret_key VARCHAR(255)
);

INSERT INTO secrets (secret_key) VALUES ('devkey123');
CREATE USER IF NOT EXISTS 'cms_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON cms.* TO 'cms_user'@'localhost';
FLUSH PRIVILEGES;