SELECT first_name, last_name 
FROM customer
INNER JOIN address on customer.address_id = address.address_id
INNER JOIN city on address.city_id = city.city_id
INNER  join country on city.country_id = country.country_id
WHERE country.country =  "Colombia"