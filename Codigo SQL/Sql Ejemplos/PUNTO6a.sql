SELECT DISTINCT  rental.customer_id, customer.first_name
FROM rental,customer
WHERE rental.customer_id = customer.customer_id


#, count(rental.inventory_id) as times   order by times desc