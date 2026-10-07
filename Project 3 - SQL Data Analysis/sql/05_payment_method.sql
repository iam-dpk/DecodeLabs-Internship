SELECT PaymentMethod, COUNT(*) AS order_count, SUM(TotalPrice) AS total_sales, AVG(TotalPrice) AS average_order_value FROM orders GROUP BY PaymentMethod ORDER BY total_sales DESC;
