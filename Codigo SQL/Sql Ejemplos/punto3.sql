SELECT rental.rental_id, customer.first_name
FROM rental, customer
where rental.inventory_id = 1 and rental.customer_id = customer.customer_id