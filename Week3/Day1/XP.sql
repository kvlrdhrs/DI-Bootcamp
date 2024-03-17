-- -- Database: public

-- -- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1252'
--     LC_CTYPE = 'Russian_Russia.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- create table items()
-- create table customers()
-- alter table items
-- add column item_id serial
-- alter table items add item_name varchar(255)
-- alter table items add item_price integer
-- select * from items

-- insert into items(item_name, item_price)
-- values ('Small Desk', '100'), ('Large Desk', '300'), ('Fan', '80')

-- select * from items

-- alter table customers
-- add cust_id serial
-- alter table customers
-- add cust_name varchar (255)
-- alter table customers
-- add cust_surname varchar (255)

-- select * from customers

-- insert into customers (cust_name, cust_surname)
-- values ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson')

-- select * from customers

-- select * from items

select * from items
where item_price > 80
