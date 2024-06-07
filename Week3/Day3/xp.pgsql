-- DVD Rental Exercise 1

-- Get a list of all the languages from the language table.
SELECT * FROM language;

-- Get a list of all films joined with their languages – select the following details: film title, description, and language name.
SELECT film.title, film.description, language.name AS language_name
FROM film
JOIN language ON film.language_id = language.language_id;

-- Get all languages, even if there are no films in those languages – select the following details: film title, description, and language name.
SELECT film.title, film.description, language.name AS language_name
FROM language
LEFT JOIN film ON language.language_id = film.language_id;

-- Create a new table called new_film with the following columns: id, name. Add some new films to the table.
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES ('Film 1'), ('Film 2'), ('Film 3');

-- Create a new table called customer_review, which will contain film reviews that customers will make.
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add 2 movie reviews
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Great Film', 9, 'I really enjoyed this film.'),
(2, 2, 'Not Bad', 7, 'It was an okay movie.');

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id = 1;

-- DVD Rental Exercise 2

-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- Show the table structure
SELECT 
    tc.table_schema, 
    tc.table_name, 
    kcu.column_name, 
    ccu.table_schema AS foreign_table_schema,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name 
FROM 
    information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kcu
      ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='customer';

-- Drop the customer_review table.
DROP TABLE customer_review;

-- Find out how many rentals are still outstanding (i.e., have not been returned to the store yet).
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

-- Find the 30 most expensive movies which are outstanding (i.e., have not been returned to the store yet).
SELECT film.title, film.rental_rate
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE rental.return_date IS NULL
ORDER BY film.rental_rate DESC
LIMIT 30;

-- Help your friend find the movies he wants to rent.

-- The 1st film: The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT film.title
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe'
AND film.description LIKE '%sumo%';

-- The 2nd film: A short documentary (less than 1 hour long), rated “R”.
SELECT title
FROM film
WHERE length < 60 AND rating = 'R' AND description LIKE '%documentary%';

-- The 3rd film: A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT film.title
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
AND rental.rental_rate > 4.00
AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- The 4th film: His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT film.title
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
AND (film.title LIKE '%boat%' OR film.description LIKE '%boat%')
ORDER BY film.replacement_cost DESC
LIMIT 1;