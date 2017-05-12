SELECT staff.first_name as Staff_Name, customer.first_name as Cusstomer_name
from rental, staff, customer
where rental.rental_date between "2002-04-01" and "2017-04-30"
		and rental.customer_id = customer.customer_id
        and rental.staff_id = staff.staff_id
