SELECT order_id, order_time, order_status
FROM orders
WHERE order_status = 'Completed'
ORDER BY order_time DESC
LIMIT 50;