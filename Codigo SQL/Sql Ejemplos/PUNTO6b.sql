SELECT  rental.customer_id, customer.first_name ,count(*) as times
FROM rental,customer
WHERE rental.customer_id = customer.customer_id
GROUP BY rental.customer_id, customer.first_name 


#, count(rental.inventory_id) as times   order by times desc