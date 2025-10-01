SELECT role, AVG(tips) as avg_tips
FROM employees
GROUP BY role
ORDER BY avg_tips DESC;