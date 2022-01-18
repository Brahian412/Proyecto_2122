drop database if exists CHOOSE_YOUR_ADVENTURE;
create database if not exists CHOOSE_YOUR_ADVENTURE;
use CHOOSE_YOUR_ADVENTURE;

-- -----------------------------------------------------
-- Table creation: USER
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.USER;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.USER (
id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
password VARCHAR(45) NOT NULL,
user_name VARCHAR(45) NOT NULL,
user_create VARCHAR(45) NULL,
user_modifications VARCHAR(45) NULL,
date_creation DATE NULL,
date_modification DATE NULL
);

-- -----------------------------------------------------
-- Table creation: CHARACTER
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.CHARACTER;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.CHARACTER (
id_character INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
character_name VARCHAR(45) NOT NULL,
description VARCHAR(1000) NOT NULL,
user_create VARCHAR(45) NULL,
user_modifications VARCHAR(45) NULL,
date_creation DATE NULL,
date_modification DATE NULL
);

-- -----------------------------------------------------
-- Table creation: ADVENTURE
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.ADVENTURE;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.ADVENTURE (
id_adventure INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
adventure_name VARCHAR(45) NOT NULL,
description VARCHAR(1000) NOT NULL,
user_create VARCHAR(45) NULL,
user_modifications VARCHAR(45) NULL,
date_creation DATE NULL,
date_modification DATE NULL
);

-- -----------------------------------------------------
-- Table creation: STEP
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.STEP;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.STEP (
id_step INT NOT NULL AUTO_INCREMENT,
end_step BIT(1) NOT NULL,
description VARCHAR(1000) NOT NULL,
id_adventure INT NOT NULL,
user_create VARCHAR(45) NULL,
user_modifications VARCHAR(45) NULL,
date_creation DATE NULL,
date_modification DATE NULL,
PRIMARY KEY (id_step, id_adventure),
CONSTRAINT FK_ADVENTURE_STEP
FOREIGN KEY (id_adventure)
REFERENCES CHOOSE_YOUR_ADVENTURE.ADVENTURE (id_adventure)
);

-- -----------------------------------------------------
-- Table creation: OPTION
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.OPTION;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.OPTION (
id_option INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
answer VARCHAR(1000) NOT NULL,
last_step INT NOT NULL,
next_step INT NOT NULL,
description VARCHAR(1000) NOT NULL,
user_create VARCHAR(45) NULL,
user_modifications VARCHAR(45) NULL,
date_creation DATE NULL,
date_modification DATE NULL,
CONSTRAINT FK_OPTION_STEP
FOREIGN KEY (last_step)
REFERENCES CHOOSE_YOUR_ADVENTURE.STEP (id_step),
CONSTRAINT FK_STEP_OPTION
FOREIGN KEY (next_step)
REFERENCES CHOOSE_YOUR_ADVENTURE.STEP (id_step)
);

-- -----------------------------------------------------
-- Table creation: GAME
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.GAME;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.GAME (
id_game INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_adventure INT NOT NULL,
id_character INT NOT NULL,
id_user INT NOT NULL,
date DATETIME NOT NULL,
user_create VARCHAR(45) NULL,
user_modifications VARCHAR(45) NULL,
date_creation DATE NULL,
date_modification DATE NULL,
CONSTRAINT FK_ADVENTURE_GAME
FOREIGN KEY (id_adventure)
REFERENCES CHOOSE_YOUR_ADVENTURE.ADVENTURE (id_adventure),
CONSTRAINT FK_CHARACTER_GAME
FOREIGN KEY (id_character)
REFERENCES CHOOSE_YOUR_ADVENTURE.CHARACTER (id_character),
CONSTRAINT FK_USER_GAME
FOREIGN KEY (id_user)
REFERENCES CHOOSE_YOUR_ADVENTURE.USER (id_user)
);

-- -----------------------------------------------------
-- Table creation: ADVENTURE_SAVE
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.ADVENTURE_SAVE;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.ADVENTURE_SAVE (
id_adventure_save INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_game INT NOT NULL,
id_step INT NOT NULL,
id_option INT NOT NULL,
user_create VARCHAR(45) NULL,
user_modifications VARCHAR(45) NULL,
date_creation DATE NULL,
date_modification DATE NULL,
CONSTRAINT FK_GAME_ADVENTURE_SAVE
FOREIGN KEY (id_game)
REFERENCES CHOOSE_YOUR_ADVENTURE.GAME (id_game),
CONSTRAINT FK_STEP_ADVENTURE_SAVE
FOREIGN KEY (id_step)
REFERENCES CHOOSE_YOUR_ADVENTURE.STEP (id_step),
CONSTRAINT FK_OPTION_ADVENTURE_SAVE
FOREIGN KEY (id_option)
REFERENCES CHOOSE_YOUR_ADVENTURE.OPTION (id_option)
);

-- -----------------------------------------------------
-- Table creation: CHARACTER_ADVENTURE
-- -----------------------------------------------------
DROP TABLE IF EXISTS CHOOSE_YOUR_ADVENTURE.CHARACTER_ADVENTURE;

CREATE TABLE IF NOT EXISTS CHOOSE_YOUR_ADVENTURE.CHARACTER_ADVENTURE (
id_character INT NOT NULL AUTO_INCREMENT,
id_adventure INT NOT NULL,
PRIMARY KEY (id_character, id_adventure),
CONSTRAINT FK_CHARACTER_ADVENTURE
FOREIGN KEY (id_character)
REFERENCES CHOOSE_YOUR_ADVENTURE.CHARACTER (id_character),
CONSTRAINT FK_ADVENTURE_CHARACTER
FOREIGN KEY (id_adventure)
REFERENCES CHOOSE_YOUR_ADVENTURE.ADVENTURE (id_adventure)
);


