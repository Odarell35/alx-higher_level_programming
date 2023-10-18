-- script that creates the table id_not_null on your MySQL server.
-- id_not_null description:
-- id INT with the default value 1
-- name VARCHAR(256)
CREATE TABLE id_not_null IF NOT EXISTS(
    id INT DEFAULT 1,
    name    VARCHAR(256)
);