USE CHOOSE_YOUR_ADVENTURE;

select a.adventure_name as AVENTURA, o.answer as 'DESCRIPCION PASO', o.description as 'DESCRIPCION RESPUESTA', round(count(ad.id_option)/84,0) as 'VECES JUGADAS'
from ADVENTURE a
inner join STEP s on s.id_adventure = a.id_adventure
inner join CHOOSE_YOUR_ADVENTURE.OPTION o on o.id_adventure = s.id_adventure
inner join ADVENTURE_SAVE ad on  ad.id_option = o.id_option
inner join GAME g on g.id_adventure = a.id_adventure
group by ad.id_option
order by round(count(ad.id_option)/84,0) desc