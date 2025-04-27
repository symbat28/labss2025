CREATE TABLE IF NOT EXISTS "user" (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS "user_score" (
    user_id INT REFERENCES "user"(user_id) ON DELETE CASCADE,
    level INT DEFAULT 1,
    score INT DEFAULT 0,
    PRIMARY KEY (user_id, level)
);

SELECT * FROM user_score