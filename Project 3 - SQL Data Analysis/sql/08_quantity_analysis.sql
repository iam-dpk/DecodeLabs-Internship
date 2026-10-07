SELECT Product, COUNT(*) AS order_count, SUM(Quantity) AS total_quantity, AVG(Quantity) AS average_quantity FROM orders GROUP BY Product ORDER BY total_quantity DESC;
