-- Create the product_orders table
CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_name VARCHAR(100) NOT NULL
);

-- Create the items table
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES product_orders(order_id)
);

-- Insert sample data into product_orders
INSERT INTO product_orders (order_date, customer_name) VALUES
('2024-06-01', 'John Doe'),
('2024-06-02', 'Jane Smith');

-- Insert sample data into items
INSERT INTO items (order_id, item_name, price) VALUES
(1, 'Item A', 10.50),
(1, 'Item B', 20.75),
(2, 'Item C', 5.00),
(2, 'Item D', 7.25);

-- Create the function to calculate the total price for a given order
CREATE OR REPLACE FUNCTION get_total_price(order_id INT)
RETURNS DECIMAL(10, 2) AS $$
DECLARE
    total_price DECIMAL(10, 2);
BEGIN
    SELECT SUM(price) INTO total_price
    FROM items
    WHERE order_id = $1;
    RETURN total_price;
END;
$$ LANGUAGE plpgsql;

-- Test the function with order_id 1
SELECT get_total_price(1) AS total_price_for_order_1;

-- Test the function with order_id 2
SELECT get_total_price(2) AS total_price_for_order_2;
