SELECT OrderStatus, COUNT(*) AS order_count FROM orders GROUP BY OrderStatus ORDER BY order_count DESC;
