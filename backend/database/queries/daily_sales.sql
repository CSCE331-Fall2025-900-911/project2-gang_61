SELECT DATE(o.order_time) AS day, COUNT(o.order_id) AS total_orders, SUM(i.price) AS total_revenue
FROM orders o
JOIN items i ON o.order_id = i.order_id
WHERE o.order_status = 'Completed'
GROUP BY day
ORDER BY day;