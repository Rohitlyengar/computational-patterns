-- Write your query below
SELECT s.id, s.name
FROM students s
WHERE s.id NOT IN (
    SELECT s.id
    FROM students s
    INNER JOIN departments d
    ON s.department_id = d.id
);
