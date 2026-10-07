SELECT * FROM orders WHERE TotalPrice > (SELECT AVG(TotalPrice) FROM orders) ORDER BY TotalPrice DESC;
