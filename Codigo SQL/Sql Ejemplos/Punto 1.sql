SELECT actor_id,concat(first_name, " ",last_name) as nombreCompleto
FROM actor
WHERE first_name like 'ANG%'
order by nombreCompleto;