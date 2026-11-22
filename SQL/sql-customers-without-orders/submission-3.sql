-- Write your query below
SELECT DISTINCT c.name
FROM customers c
WHERE c.id NOT IN (
    SELECT o.customer_id
    FROM orders o
);
