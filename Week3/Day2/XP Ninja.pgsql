--Exercise 1: DVD Rental

select rating, count(rating) from film
GROUP BY rating
order by rating

select * from film

select * from film
where rating in ('G', 'PG-13') and length <120 and rental_rate < 3
ORDER BY title asc


update customer
set email = 'vfirfvsirf', address_id = 
where customer_id = 1

select * from customer
where customer_id = 1

update address
set address = 'Bat Yam'
where address_id = 1

select * from address
where address_id = 1


