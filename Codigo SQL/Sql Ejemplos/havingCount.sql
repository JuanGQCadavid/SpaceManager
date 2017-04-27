select customer.first_name, customer.last_name
from customer inner join rental on (customer.customer_id = rental.customer_id)
group by customer.customer_id
having count(*) > 5