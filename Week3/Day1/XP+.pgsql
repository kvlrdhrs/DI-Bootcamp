-- -- Database: bootcamp

-- -- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1252'
--     LC_CTYPE = 'Russian_Russia.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;


-- create table students(
-- 	id serial,
-- 	last_name varchar(255),
-- 	first_name varchar (255),
-- 	birth_date date
-- )


-- insert into students (first_name, last_name, birth_date) values
-- ('Marc', 'Benichou', '02/11/1998'),
-- ('Yoan', 'Cohen', '03/12/2010'),
-- ('Lea', 'Benichou', '27/07/1987'),
-- ('Amelia', 'Dux', '07/04/1996'),
-- ('David', 'Grez', '14/06/2003'),
-- ('Omer', 'Simpson', '03/10/1980')

-- insert into students (first_name, last_name, birth_date)
-- values ('Kanan', 'Shukurlu', '23/08/1995')

-- select * from students

-- select last_name, first_name from students

-- select last_name, first_name from students
-- where id %2 =0

-- select last_name, first_name from students
-- where last_name = 'Benichou' and first_name = 'Marc'

-- select last_name, first_name from students
-- where last_name = 'Benichou' or first_name = 'Marc'

-- select last_name, first_name from students
-- where first_name ilike '%a%'

-- select last_name, first_name from students
-- where first_name ilike 'a%'

-- select last_name, first_name from students
-- where first_name ilike '%a'

-- select last_name, first_name from students
-- where first_name ilike '%a_'

-- select last_name, first_name from students
-- where id % 1 = 0 and id % 3 = 0

-- select * from students
-- where birth_date >= '01/01/2000'
-- order by birth_date asc