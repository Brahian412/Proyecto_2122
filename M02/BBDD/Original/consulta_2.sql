USE CHOOSE_YOUR_ADVENTURE;
SELECT u.user_name, COUNT(g.id_user) AS veces_jugadas
    FROM GAME g
    JOIN CHOOSE_YOUR_ADVENTURE.USER u
    ON u.id_user = g.id_user
GROUP BY u.user_name
ORDER BY veces_jugadas DESC, u.date_creation asc
LIMIT 1