-- a
CREATE TABLE category (
    id_category INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL);

CREATE TABLE products (
    id_product INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category(id_category)
        ON DELETE SET NULL
        ON UPDATE CASCADE);

CREATE TABLE nutritions (
    id_nutrition INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    name TEXT NOT NULL,
    calories INTEGER,
    fats INTEGER,
    sugar INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(id_product)
        ON DELETE CASCADE
        ON UPDATE CASCADE);

CREATE TABLE orders (
    id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time DATETIME NOT NULL,
    address TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    customer_ph TEXT NOT NULL,
    total_price INTEGER NOT NULL);

CREATE TABLE products_orders (
    order_id INTEGER,
    product_id INTEGER,
    amount INTEGER NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id_order)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id_product)
        ON DELETE CASCADE
        ON UPDATE CASCADE);

-- b- all of them are one to many excpet for order production which is many to many

-- c - different file, done

-- d
SELECT products.name AS product_name, category.name AS category_name, nutritions.calories, nutritions.fats, nutritions.sugar 
FROM products
LEFT JOIN nutritions ON products.id_product = nutritions.product_id 
LEFT JOIN category ON products.category_id = category.id_category;

SELECT orders.id_order, orders.date_time, orders.customer_name, orders.address, orders.total_price, products.name AS product_name, products_orders.amount
FROM orders
JOIN products_orders ON orders.id_order = products_orders.order_id
JOIN products ON products_orders.product_id = products.id_product;

INSERT INTO products_orders (order_id, product_id, amount) 
SELECT id_order, 1, 1 
FROM orders 
WHERE NOT EXISTS (
    SELECT 1 
    FROM products_orders 
    WHERE products_orders.order_id = orders.id_order 
    AND products_orders.product_id = 1);

UPDATE orders
SET total_price = (
SELECT SUM(products_orders.amount * products.price)
FROM products_orders
JOIN products ON products_orders.product_id = products.id_product
WHERE products_orders.order_id = orders.id_order
GROUP BY products_orders.order_id);

SELECT MAX(total_price) AS most_expensive_order, MIN(total_price) AS least_expensive_order, AVG(total_price) AS average_order_price 
FROM orders;

SELECT customer_name, COUNT(*) AS order_count 
FROM orders 
GROUP BY customer_name 
ORDER BY order_count DESC 
LIMIT 1;

SELECT products.name AS product_name, SUM(products_orders.amount) AS total_sold 
FROM products
JOIN products_orders ON products.id_product = products_orders.product_id 
GROUP BY products.name 
ORDER BY total_sold DESC;

SELECT products.name AS product_name, SUM(products_orders.amount) AS total_sold 
FROM products 
JOIN products_orders ON products.id_product = products_orders.product_id 
GROUP BY products.name 
ORDER BY total_sold ASC 
LIMIT 1;

SELECT AVG(total_sold) AS average_sales 
FROM (SELECT SUM(products_orders.amount) AS total_sold 
FROM products_orders
GROUP BY products_orders.product_id);

SELECT category.name AS category_name, SUM(products_orders.amount) AS total_sold 
FROM category
JOIN products ON category.id_category = products.category_id 
JOIN products_orders ON products.id_product = products_orders.product_id 
GROUP BY category.name 
ORDER BY total_sold DESC;

SELECT category.name AS category_name, SUM(products_orders.amount) AS total_sold 
FROM category
JOIN products ON category.id_category = products.category_id 
JOIN products_orders ON products.id_product = products_orders.product_id 
GROUP BY category.name 
ORDER BY total_sold ASC 
LIMIT 1;

SELECT products.name AS product_name, COUNT(DISTINCT products_orders.order_id) AS order_count 
FROM products
JOIN products_orders ON products.id_product = products_orders.product_id 
GROUP BY products.name 
ORDER BY order_count DESC 
LIMIT 1;