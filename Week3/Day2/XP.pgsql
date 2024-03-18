-- Exercise 1 : Items And Customers


-- select * from items
-- order by item_price asc

-- select * from items
-- where item_price >= 80
-- order by item_price desc

-- select cust_name as name, cust_lastname as lastname from customers
-- order by name LIMIT 3

-- select cust_lastname from customers
-- order by cust_lastname desc



-- Exercise 2 : Dvdrental Database

-- select * from customer

-- select (first_name, last_name) as full_name from customer

-- select distinct create_date from customer

-- select * from customer
-- order by first_name desc

-- select film_id, title, description, release_year, rental_rate from film
-- order by rental_rate asc

-- select address, phone from address
-- where district = 'Texas'

-- select * from film
-- where film_id in (15, 150)

-- select film_id, title, description, length, rental_rate from film
-- where title ilike 'Dune'

-- select film_id, title, description, length, rental_rate from film
-- WHERE left (title, 2) = 'Du' (WHERE title ilike 'Du%')

-- select title as film_name, rental_rate as film_cost from film
-- order by rental_rate asc
-- fetch first 20 rows only

-- select title as film_name, rental_rate as film_cost from film
-- order by rental_rate asc
-- offset 10 rows
-- fetch next 10 rows only

-- select customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- from customer
-- inner join payment on customer.customer_id=payment.customer_id
-- order by customer.customer_id

-- select film.title, inventory.film_id
-- from film
-- left join inventory on film.film_id=inventory.film_id
-- where inventory.film_id is null

-- select city.city, country.country
-- from city
-- inner join country on city.country_id=country.country_id