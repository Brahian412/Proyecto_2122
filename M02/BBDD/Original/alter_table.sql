USE CHOOSE_YOUR_ADVENTURE;

-- -----------------------------------------------------
-- Table modification: USER
-- -----------------------------------------------------
ALTER TABLE CHOOSE_YOUR_ADVENTURE.USER MODIFY id_user  INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.USER MODIFY password VARCHAR(45) NOT NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.USER MODIFY user_name VARCHAR(45) NOT NULL UNIQUE;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.USER MODIFY user_create VARCHAR(45) NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.USER MODIFY user_modifications VARCHAR(45) NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.USER MODIFY date_creation DATETIME NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.USER MODIFY date_modification DATETIME NULL;


-- -----------------------------------------------------
-- Table modification: CHARACTER
-- -----------------------------------------------------
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY id_character INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY character_name VARCHAR(45) NOT NULL UNIQUE;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY description VARCHAR(1000) NOT NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY user_create VARCHAR(45) NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY user_modifications VARCHAR(45) NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY date_creation DATETIME NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY date_modification DATETIME NULL;


-- -----------------------------------------------------
-- Table modification: ADVENTURE
-- -----------------------------------------------------    
ALTER TABLE ADVENTURE MODIFY id_adventure INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE;
ALTER TABLE ADVENTURE MODIFY adventure_name VARCHAR(45) NOT NULL;
ALTER TABLE ADVENTURE MODIFY description VARCHAR(1000) NOT NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY user_create VARCHAR(45) NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY user_modifications VARCHAR(45) NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY date_creation DATETIME NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.CHARACTER MODIFY date_modification DATETIME NULL;


-- -----------------------------------------------------
-- Table modification: STEP
-- -----------------------------------------------------
ALTER TABLE STEP MODIFY id_step INT NOT NULL AUTO_INCREMENT UNIQUE;
ALTER TABLE STEP MODIFY end_step INT NOT NULL;
ALTER TABLE STEP MODIFY description VARCHAR(1000) NOT NULL;
ALTER TABLE STEP MODIFY id_adventure INT NOT NULL;
ALTER TABLE STEP MODIFY user_create VARCHAR(45) NULL;
ALTER TABLE STEP MODIFY user_modifications VARCHAR(45) NULL;
ALTER TABLE STEP MODIFY date_creation DATETIME NULL;
ALTER TABLE STEP MODIFY date_modification DATETIME NULL;
ALTER TABLE STEP ADD CONSTRAINT PRIMARY KEY (id_step, id_adventure);
ALTER TABLE STEP ADD CONSTRAINT FK_ADVENTURE_STEP
FOREIGN KEY (id_adventure)
	REFERENCES ADVENTURE (id_adventure);

    
-- -----------------------------------------------------
-- Table modification: OPTION
-- -----------------------------------------------------
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY id_option INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY id_adventure INT NOT NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY last_step INT NOT NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY next_step INT NOT NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY description VARCHAR(1000) NOT NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY answer VARCHAR(1000) NOT NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY user_create VARCHAR(45) NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY user_modifications VARCHAR(45) NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY date_creation DATETIME NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION MODIFY date_modification DATETIME NULL;
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION ADD CONSTRAINT FK_OPTION_STEP
FOREIGN KEY (last_step)
	REFERENCES STEP (id_step);
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION ADD CONSTRAINT FK_STEP_OPTION
FOREIGN KEY (next_step)
	REFERENCES STEP (id_step);
ALTER TABLE CHOOSE_YOUR_ADVENTURE.OPTION ADD CONSTRAINT FK_STEP_ADVENTURE_OPTION
FOREIGN KEY (id_adventure)
	REFERENCES STEP (id_adventure);


-- -----------------------------------------------------
-- Table modification: GAME
-- -----------------------------------------------------
ALTER TABLE GAME MODIFY id_game INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE;
ALTER TABLE GAME MODIFY id_adventure INT NOT NULL;
ALTER TABLE GAME MODIFY id_character INT NOT NULL;
ALTER TABLE GAME MODIFY id_user INT NOT NULL;
ALTER TABLE GAME MODIFY date DATETIME NOT NULL;
ALTER TABLE GAME MODIFY user_create VARCHAR(45) NULL;
ALTER TABLE GAME MODIFY user_modifications VARCHAR(45) NULL;
ALTER TABLE GAME MODIFY date_creation DATETIME NULL;
ALTER TABLE GAME MODIFY date_modification DATETIME NULL;
ALTER TABLE GAME ADD CONSTRAINT FK_ADVENTURE_GAME
FOREIGN KEY (id_adventure)
	REFERENCES ADVENTURE (id_adventure);
ALTER TABLE GAME ADD CONSTRAINT FK_CHARACTER_GAME
FOREIGN KEY (id_character)
	REFERENCES CHOOSE_YOUR_ADVENTURE.CHARACTER (id_character);
ALTER TABLE GAME ADD CONSTRAINT FK_USER_GAME
FOREIGN KEY (id_user)
	REFERENCES CHOOSE_YOUR_ADVENTURE.USER (id_user);


-- -----------------------------------------------------
-- Table modification: ADVENTURE_SAVE
-- -----------------------------------------------------
ALTER TABLE ADVENTURE_SAVE MODIFY id_adventure_save INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE;
ALTER TABLE ADVENTURE_SAVE MODIFY id_game INT NOT NULL;
ALTER TABLE ADVENTURE_SAVE MODIFY id_step INT NOT NULL;
ALTER TABLE ADVENTURE_SAVE MODIFY id_option INT NOT NULL;
ALTER TABLE ADVENTURE_SAVE MODIFY id_adventure INT NOT NULL;
ALTER TABLE ADVENTURE_SAVE MODIFY user_create VARCHAR(45) NULL;
ALTER TABLE ADVENTURE_SAVE MODIFY user_modifications VARCHAR(45) NULL;
ALTER TABLE ADVENTURE_SAVE MODIFY date_creation DATETIME NULL;
ALTER TABLE ADVENTURE_SAVE MODIFY date_modification DATETIME NULL;
ALTER TABLE ADVENTURE_SAVE ADD CONSTRAINT FK_GAME_ADVENTURE_SAVE
FOREIGN KEY (id_game)
	REFERENCES CHOOSE_YOUR_ADVENTURE.GAME (id_game);
ALTER TABLE ADVENTURE_SAVE ADD CONSTRAINT FK_STEP_ADVENTURE_SAVE
FOREIGN KEY (id_step)
	REFERENCES CHOOSE_YOUR_ADVENTURE.STEP (id_step);
ALTER TABLE ADVENTURE_SAVE ADD CONSTRAINT FK_OPTION_ADVENTURE_SAVE
FOREIGN KEY (id_option)
	REFERENCES CHOOSE_YOUR_ADVENTURE.OPTION (id_option);
ALTER TABLE ADVENTURE_SAVE ADD CONSTRAINT FK_STEP_ADVENTURE_ADVENTURE_SAVE
FOREIGN KEY (id_adventure)
	REFERENCES STEP (id_adventure);


-- -----------------------------------------------------
-- Table modification: CHARACTER_ADVENTURE
-- -----------------------------------------------------
ALTER TABLE CHARACTER_ADVENTURE MODIFY id_character INT NOT NULL;
ALTER TABLE CHARACTER_ADVENTURE MODIFY id_adventure INT NOT NULL;
ALTER TABLE CHARACTER_ADVENTURE ADD PRIMARY KEY (id_character, id_adventure);
ALTER TABLE CHARACTER_ADVENTURE ADD CONSTRAINT FK_CHARACTER_ADVENTURE
FOREIGN KEY (id_character)
	REFERENCES CHOOSE_YOUR_ADVENTURE.CHARACTER (id_character);
ALTER TABLE CHARACTER_ADVENTURE ADD CONSTRAINT FK_ADVENTURE_CHARACTER
FOREIGN KEY (id_adventure)
	REFERENCES CHOOSE_YOUR_ADVENTURE.ADVENTURE (id_adventure);  
    