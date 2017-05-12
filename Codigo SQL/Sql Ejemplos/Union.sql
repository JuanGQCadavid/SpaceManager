select *
from rental, customer
where rental.customer_id = customer.customer_id

union all

SELECT *
FROM rental
inner join customer on rental.customer_id = customer.customer_id