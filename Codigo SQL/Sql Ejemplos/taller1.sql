SELECT customer.first_name
FROM (((customer
inner join address on customer.address_id = address.address_id)
inner join city on address.city_id = city.city_id)
inner join country on country.country_id = city.country_id)
WHERE country.country = "Colombia"
