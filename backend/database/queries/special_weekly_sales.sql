SELECT 
    DATE_TRUNC('week', o.order_time) AS week_start,
    COUNT(o.order_id) AS total_orders
FROM orders o
GROUP BY week_start
ORDER BY week_start;
-- this generates num sales per week.  ~40 weeks