CREATE DATABASE sosayweallbot;
CREATE TABLE sosayweallbot.replied_to (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(15) NOT NULL UNIQUE,
    created_at DATETIME NOT NULL
)