USE CHOOSE_YOUR_ADVENTURE;
SELECT a.id_adventure, a.adventure_name, g.date
FROM ADVENTURE a JOIN GAME g ON  g.id_adventure = a.id_adventure
JOIN CHOOSE_YOUR_ADVENTURE.USER u ON u.id_user = g.id_user
where u.id_user = (SELECT id_user FROM CHOOSE_YOUR_ADVENTURE.USER WHERE user_name = 'eric_escrich')
ORDER BY g.date desc 