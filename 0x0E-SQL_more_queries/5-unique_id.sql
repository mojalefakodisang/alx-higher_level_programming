-- Creates a table with unique constraint on id
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIGUE,
	name VARCHAR(256)
);
