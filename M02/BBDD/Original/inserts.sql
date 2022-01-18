use CHOOSE_YOUR_ADVENTURE;

insert into CHOOSE_YOUR_ADVENTURE.ADVENTURE (adventure_name, description, user_create, date_creation, user_modifications, date_modification)
values ('UN CASUAL DÍA EN LA VIDA DE UN HÉROE','En esta aventura podras vivir un día cotidiano en una vida de fantasía siendo un heroico caballero. 
Podrás desde luchar contra mounstros, hasta salvar a la princesa atrapada en la torre.',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('SEGUNDA AVENTURA','Lorem ipsum dolor sit amet consectetur adipiscing elit donec scelerisque, mauris feugiat fusce quis eros vitae primis tortor, 
augue purus parturient litora egestas pretium at platea. Ac libero imperdiet sem mollis augue ullamcorper viverra odio litora himenaeos, 
natoque fames duis penatibus commodo justo massa posuere. Litora cursus porta vehicula sociis egestas habitant faucibus pretium, 
netus quis non interdum justo sodales proin ac, ante fringilla maecenas facilisi vestibulum donec senectus.',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('TERCERA AVENTURA','Lorem ipsum dolor sit amet consectetur adipiscing elit donec scelerisque, mauris feugiat fusce quis eros vitae primis tortor, 
augue purus parturient litora egestas pretium at platea. Ac libero imperdiet sem mollis augue ullamcorper viverra odio litora himenaeos, 
natoque fames duis penatibus commodo justo massa posuere. Litora cursus porta vehicula sociis egestas habitant faucibus pretium, 
netus quis non interdum justo sodales proin ac, ante fringilla maecenas facilisi vestibulum donec senectus.',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('CUARTA AVENTURA','Lorem ipsum dolor sit amet consectetur adipiscing elit donec scelerisque, mauris feugiat fusce quis eros vitae primis tortor, 
augue purus parturient litora egestas pretium at platea. Ac libero imperdiet sem mollis augue ullamcorper viverra odio litora himenaeos, 
natoque fames duis penatibus commodo justo massa posuere. Litora cursus porta vehicula sociis egestas habitant faucibus pretium, 
netus quis non interdum justo sodales proin ac, ante fringilla maecenas facilisi vestibulum donec senectus.',
'eric_escrich', '2022-01-13', current_user(), current_date())
;

insert into CHOOSE_YOUR_ADVENTURE.STEP (description, end_step, id_adventure, user_create, date_creation, user_modifications, date_modification)
values ('Te suena la alarma, ¿qué haces?', 0, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Logras levantarte exitosamente, ¿qué deberías hacer?', 0, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('¡Te encuentras con un monstruo! ¿Qué deberías hacer?', 0, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Tienes mucha suerte y logras entrar al castillo sin problemas, ¿qué hace?', 0, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Llegas ardiendo a la torre de la princesa, ¿qué deberías hacer?', 0, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Entras al castillo y te encuentras con la princesa y el monstruo cenando, ¿qué deberías hacer?', 0, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Has decidido ser sabio y no correr muchos peligros...', 1, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Te das cuenta de que la princesa no vale la pena y te vas a tomar unas cervezas con el monstruo', 1, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Al parecer se te olvidó que no ibas equipado... Moriste trágicamente', 1, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Parece ser que esta celda no es la de la princesa, caíste en una trampa', 1, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('¡Vaya!, las hojas del suelo eran hojas secas y se acaba quemando todo el bosque. Pobrecito, moriste abrasado', 1, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('¡Parece ser que la princesa no había sido secuestrada! Se había ido por cuenta propia', 1, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('Te das cuenta de que estás siendo un stalker y les dejas ser felices', 1, 1, 'eric_escrich', '2022-01-13', current_user(), current_date()),
('No logras levantarte de la cama y pierdes por vago', 1, 1, 'eric_escrich', '2022-01-13', current_user(), current_date())
;

insert into CHOOSE_YOUR_ADVENTURE.OPTION (description, last_step, next_step, answer, user_create, date_creation, user_modifications, date_modification)
values ('Apagas la alarma porque quieres dormir', 1, 14, 'Hoy no tienes ganas de levantarte de la cama, te quedaras durmiendo un ratito más...',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Te levantas de la cama como dios manda', 1, 2,'Te levantaras de la cama con ganas de rescatar a tu amada princesa de la torre donde está atrapada!',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Decides no ir a por la princesa. Que vaya otro, hay muchos peces en el mar...', 2, 7, 'Al fin y al cabo el amor no es tan importante',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Te equipas apropiadamente y sales a la aventura', 2, 3, 'Te equiparas al completo con tu armadura y tus armas para luchar contra los posibles peligros del exterior',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('No te equipas', 2, 4, 'Decides no equiparte, ya que crees que eres muy poderoso y fuerte. Piensas que no tendras demasiados problemas...',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Decides luchar valerosamente', 3, 5, 'Eres muy valiente y decides luchar tu solo contra un poderoso y furioso mounstro de tres cabezas de gran tamaño... Sin duda, ¡una gran decisión!',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Decides intentar hacerte amigo del monstruo', 3, 8, 'Se te ocurre que no es mala idea intentar engatusar al furioso monstruo con tu carisma y tu labia',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Decides huir', 3, 4, 'Te das cuenta de que no eres tan poderoso ni tan fuerte y escaparas del mounstro y intentaras ir directamente a rescatar a la princesa sin distracciones',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Buscas al boss final para matarle', 4, 9, 'Estás más motivado que Iniesta cuando metió el gol del mundial de 2010 y vas a buscar al boss final para demostrarle todo tu poder',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Buscar la habitación donde está encerrada la princesa', 4, 10, 'Buscarás la habitación por toda la torre. ¿Cuál será la suya?',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Restregarte por el suelo, que por suerte está lleno de hojas', 5, 11, 'Después de una batalla épica con el monstruo donde le has derrotado, acabas ardiendo. Si te tiras al suelo y ruedas se apagará el fuego y podrás volver a tu misión principal, ¡Rescatar a la princesa!',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Te tomas una poción de cuerpo ignífugo del Minecraft y entras al castillo', 5, 6, 'Esta poción te hará inmune al fuego y no sentirás nada de dolor. ¡Viva el Minecraft!',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Rescatas a la pobre princesa de la mala compañía del malvado boss final', 6, 12, 'El boss final está obligando a la princesa a cenar con él, pero no hay nada de lo que preocuparse, ¡estás tú para salvarla!',
'eric_escrich', '2022-01-13', current_user(), current_date()),
('Decides que sean felices y coman perdices', 6, 13, 'Dejarás tranquilos a los dos tortolitos y te irás a casa, que a ti también te está esperando tu madre para cenar y sabes que no le gusta esperar',
'eric_escrich', '2022-01-13', current_user(), current_date())
;

insert into CHOOSE_YOUR_ADVENTURE.CHARACTER (character_name, description, user_create, date_creation, user_modifications, date_modification)
values ('El Dandy de Barcelona', 'Este personaje no domina el mundo porque no quiere. Con tan solo silbar y hacer el mítico movimiento de mano de Ronaldinho Gaucho hipnotiza a sus oponentes y los deja K.O.',
'eric_escrich', '2022-01-14', current_user(), current_date()),
('Harry Potter', 'Este adolescente hace que las cosas se levanten tan solo con decir "Wingardium Leviosa". Sin duda, es un mago muy poderoso',
'eric_escrich', '2022-01-14', current_user(), current_date()),
('Mario Bros', 'Este hombre con tremendo mostacho es capaz de adquirir diferentes cualidades con tan solo comerse setas que va encontrando por el suelo. Sin duda te será muy útil en una infinidad de aventuras',
'eric_escrich', '2022-01-14', current_user(), current_date())
;

insert into CHOOSE_YOUR_ADVENTURE.USER (user_name, password, user_create, date_creation, user_modifications, date_modification)
values ('eric_escrich', '12345', 'eric_escrich', '2022-01-17', current_user(), current_date()),
('Aleix', '12345', 'eric_escrich', '2022-01-17', current_user(), current_date()),
('Brahian', '12345', 'eric_escrich', '2022-01-17', current_user(), current_date())
;

insert into CHOOSE_YOUR_ADVENTURE.GAME (id_adventure, id_character, id_user, date, user_create, date_creation, user_modifications, date_modification)
values (1, 1, 1, current_date(), 'eric_escrich', '2022-01-17', current_user(), current_date()),
(1, 2, 1, current_date(), 'eric_escrich', '2022-01-17', current_user(), current_date())
;

insert into CHOOSE_YOUR_ADVENTURE.ADVENTURE_SAVE (id_game, id_step, id_option, user_create, date_creation, user_modifications, date_modification)
values (1, 1, 1, 'eric_escrich', '2022-01-17', current_user(), current_date()),
(2, 1, 2, 'eric_escrich', '2022-01-17', current_user(), current_date()),
(2, 2, 4, 'eric_escrich', '2022-01-17', current_user(), current_date()),
(2, 3, 6, 'eric_escrich', '2022-01-17', current_user(), current_date()),
(2, 5, 12, 'eric_escrich', '2022-01-17', current_user(), current_date()),
(2, 6, 14, 'eric_escrich', '2022-01-17', current_user(), current_date())
;
