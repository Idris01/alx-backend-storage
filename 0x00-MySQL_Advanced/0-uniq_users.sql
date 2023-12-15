-- Creates table named user with attributes id, email
-- and name

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
);
