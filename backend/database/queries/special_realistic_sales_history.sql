SELECT 
    date_trunc('hour', o.order_time) AS hour_start,
    COUNT(o.order_id) AS orders_count,
    SUM(i.price) AS total_sales
FROM orders o
JOIN items i ON o.order_id = i.order_id
GROUP BY hour_start
ORDER BY hour_start;
-- summing the prices from the items table