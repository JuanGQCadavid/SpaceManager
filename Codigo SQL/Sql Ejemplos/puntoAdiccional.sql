select actor.first_name,actor.last_name, count(*) as times
from rental inner join inventory on (rental.inventory_id = inventory.inventory_id)
inner join film on (inventory.film_id = film.film_id)
inner join film_actor on (film_actor.film_id = film.film_id)
inner join actor on (film_actor.actor_id = actor.actor_id)

where rental.rental_date >= '1990-04-01' and rental.rental_date <= '2008-04-30' 

group by actor.first_name,actor.last_name
having times 




order by times desc






