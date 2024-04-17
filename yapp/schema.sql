DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    encrypted_password TEXT NOT NULL,
    encrypted_by TEXT NOT NULL
);
