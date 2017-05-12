SELECT customer.first_name, staff.first_name
FROM (rental
INNER JOIN customer on customer.customer_id = rental.customer_id)
inner join staff on staff.staff_id= rental.staff_id
where staff.first_name = "Juan" and staff.last_name = "Perez"
	and staff.first_name != "Luis" and staff.last_name != "Gonzales";