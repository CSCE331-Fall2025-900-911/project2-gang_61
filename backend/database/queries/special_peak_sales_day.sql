SELECT 
    DATE_TRUNC('day', o.order_time) AS day,
    SUM(i.price) AS total_sales
FROM orders o
JOIN items i ON o.order_id = i.order_id
GROUP BY day
ORDER BY total_sales DESC
LIMIT 10;