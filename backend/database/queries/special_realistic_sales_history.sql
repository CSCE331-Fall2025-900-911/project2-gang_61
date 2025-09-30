SELECT 
    DATE_PART('hour', o.order_time) AS hour_of_day,
    COUNT(o.order_id) AS total_orders,
    SUM(i.price) AS total_sales
FROM orders o
JOIN items i ON o.order_id = i.order_id
GROUP BY hour_of_day
ORDER BY hour_of_day;
