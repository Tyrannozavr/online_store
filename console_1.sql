-- SELECT title, products_purchases.id, (price * products_purchases.count) as price,
--              discount as size_discount, TIME(datetime) FROM products_purchases
--             INNER JOIN products_products on  products_purchases.product_id = products_products.id
--             INNER JOIN products_discount on products_purchases.discount_id = products_discount.id
--             WHERE DATE(datetime)  = CURRENT_DATE;


-- SELECT name, discount, category_id FROM products_discount
-- WHERE category_id;

-- SELECT name, COUNT(title)  FROM products_purchases
-- INNER JOIN products_products on products_purchases.product_id = products_products.id
-- INNER JOIN products_discount on products_purchases.discount_id = products_discount.id
-- WHERE products_products.category_id = 1
-- GROUP BY products_purchases.discount_id;
--
-- SELECT COUNT(title) AS count FROM products_purchases
-- INNER JOIN products_products on products_purchases.product_id = products_products.id
-- WHERE discount_id = 37
-- GROUP BY DATE(datetime);

-- SELECT * FROM products_discount;

-- SELECT id,  AVG(count) FROM (
--     SELECT products_purchases.id, COUNT(title) AS count FROM products_purchases
--     INNER JOIN products_products on products_purchases.product_id = products_products.id
--     WHERE discount_id = 37
--     GROUP BY DATE(datetime));

SELECT SUM(count), products_category.title FROM products_purchases
JOIN products_products on products_purchases.product_id = products_products.id
JOIN products_category on products_products.category_id = category_id
GROUP BY products_category.title;


-- Скидочная акция
-- Категория
-- Среднее число продаваемых товаров в день со скидкой
-- Среднее число продаваемых товаров в день без скидки
