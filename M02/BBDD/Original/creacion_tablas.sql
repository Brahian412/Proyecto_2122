drop database if exists CHOOSE_YOUR_ADVENTURE;
create database if not exists CHOOSE_YOUR_ADVENTURE;
use CHOOSE_YOUR_ADVENTURE;


-- -----------------------------------------------------
-- Table creation: USER
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.USER;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.USER (
id_user INT,
password VARCHAR(45),
user_name VARCHAR(45),
user_create VARCHAR(45),
user_modifications VARCHAR(45),
date_creation DATE,
date_modification DATE
);


-- -----------------------------------------------------
-- Table creation: CHARACTER
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.CHARACTER;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.CHARACTER (
id_character INT,
character_name VARCHAR(45),
description VARCHAR(1000),
user_create VARCHAR(45),
user_modifications VARCHAR(45),
date_creation DATETIME,
date_modification DATETIME
);


-- -----------------------------------------------------
-- Table creation: ADVENTURE
-- -----------------------------------------------------
DROP TABLE IF EXISTS ADVENTURE;

CREATE TABLE IF NOT EXISTS ADVENTURE (
id_adventure INT,
adventure_name VARCHAR(45),
description VARCHAR(1000),
user_create VARCHAR(45),
user_modifications VARCHAR(45),
date_creation DATETIME,
date_modification DATETIME
);


-- -----------------------------------------------------
-- Table creation: STEP
-- -----------------------------------------------------
DROP TABLE IF EXISTS STEP;

CREATE TABLE IF NOT EXISTS STEP (
id_step INT,
end_step INT,
description VARCHAR(1000),
id_adventure INT,
user_create VARCHAR(45),
user_modifications VARCHAR(45),
date_creation DATETIME,
date_modification DATETIME
);


-- -----------------------------------------------------
-- Table creation: OPTION
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.OPTION;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.OPTION (
id_option INT,
id_adventure INT,
last_step INT,
next_step INT,
description VARCHAR(1000),
answer VARCHAR(1000),
user_create VARCHAR(45),
user_modifications VARCHAR(45),
date_creation DATETIME,
date_modification DATETIME
);


-- -----------------------------------------------------
-- Table creation: GAME
-- -----------------------------------------------------
DROP TABLE IF EXISTS GAME;

CREATE TABLE IF NOT EXISTS GAME (
id_game INT,
id_adventure INT,
id_character INT,
id_user INT,
date DATETIME,
user_create VARCHAR(45),
user_modifications VARCHAR(45),
date_creation DATETIME,
date_modification DATETIME
);


-- -----------------------------------------------------
-- Table creation: ADVENTURE_SAVE
-- -----------------------------------------------------
DROP TABLE IF EXISTS ADVENTURE_SAVE;

CREATE TABLE IF NOT EXISTS ADVENTURE_SAVE (
id_adventure_save INT,
id_game INT,
id_step INT,
id_option INT,
id_adventure INT,
user_create VARCHAR(45),
user_modifications VARCHAR(45),
date_creation DATETIME,
date_modification DATETIME
);


-- -----------------------------------------------------
-- Table creation: CHARACTER_ADVENTURE
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHARACTER_ADVENTURE;

CREATE TABLE IF NOT EXISTS CHARACTER_ADVENTURE (
id_character INT,
id_adventure INT
);


