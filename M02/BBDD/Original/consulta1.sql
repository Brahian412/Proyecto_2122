USE CHOOSE_YOUR_ADVENTURE;
select distinct a.id_adventure, a.adventure_name, s.id_step, s.description, asa.id_option, adv.description, count(asa.id_option) as 'veces_elegidas'
from ADVENTURE a 
inner join STEP s on a.id_adventure = s.id_adventure
inner join ADVENTURE_SAVE asa on s.id_step = asa.id_step
inner join CHOOSE_YOUR_ADVENTURE.OPTION adv on asa.id_option = adv.id_option
group by id_option
order by veces_elegidas desc