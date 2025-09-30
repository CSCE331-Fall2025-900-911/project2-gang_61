SELECT 
    o.order_time::date AS day, 
    SUM(i.price) AS daily_total
FROM orders o
JOIN items i ON i.order_id = o.order_id
GROUP BY day
ORDER BY daily_total DESC
LIMIT 10;
--summing prices from items table