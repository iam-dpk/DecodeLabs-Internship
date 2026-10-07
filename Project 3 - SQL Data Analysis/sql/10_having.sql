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
