SELECT Product, COUNT(*) AS order_count, SUM(TotalPrice) AS total_sales, AVG(TotalPrice) AS average_order_value FROM orders GROUP BY Product ORDER BY total_sales DESC;
