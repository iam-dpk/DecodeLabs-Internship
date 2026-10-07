SELECT ReferralSource, COUNT(*) AS order_count, SUM(TotalPrice) AS total_sales FROM orders GROUP BY ReferralSource ORDER BY total_sales DESC;
