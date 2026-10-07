-- 01_basic_select
SELECT * FROM orders LIMIT 10;

-- 02_where_filter
SELECT * FROM orders WHERE TotalPrice > (SELECT AVG(TotalPrice) FROM orders) ORDER BY TotalPrice DESC;

-- 03_order_by
SELECT * FROM orders ORDER BY TotalPrice DESC LIMIT 10;

-- 04_group_by_product
SELECT Product, COUNT(*) AS order_count, SUM(TotalPrice) AS total_sales, AVG(TotalPrice) AS average_order_value FROM orders GROUP BY Product ORDER BY total_sales DESC;

-- 05_payment_method
SELECT PaymentMethod, COUNT(*) AS order_count, SUM(TotalPrice) AS total_sales, AVG(TotalPrice) AS average_order_value FROM orders GROUP BY PaymentMethod ORDER BY total_sales DESC;

-- 06_order_status
SELECT OrderStatus, COUNT(*) AS order_count FROM orders GROUP BY OrderStatus ORDER BY order_count DESC;

-- 07_referral_source
SELECT ReferralSource, COUNT(*) AS order_count, SUM(TotalPrice) AS total_sales FROM orders GROUP BY ReferralSource ORDER BY total_sales DESC;

-- 08_quantity_analysis
SELECT Product, COUNT(*) AS order_count, SUM(Quantity) AS total_quantity, AVG(Quantity) AS average_quantity FROM orders GROUP BY Product ORDER BY total_quantity DESC;

-- 09_overall_aggregations
SELECT COUNT(*) AS total_orders, SUM(TotalPrice) AS total_sales, AVG(TotalPrice) AS average_order_value FROM orders;

-- 10_having
SELECT Product, SUM(TotalPrice) AS total_sales
FROM orders
GROUP BY Product
HAVING SUM(TotalPrice) > (
    SELECT AVG(product_sales) FROM (
        SELECT SUM(TotalPrice) AS product_sales
        FROM orders GROUP BY Product
    )
)
ORDER BY total_sales DESC;
