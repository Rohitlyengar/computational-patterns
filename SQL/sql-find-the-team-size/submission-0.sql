-- Write your query below
SELECT employee_id, (
    SELECT COUNT(*)
    FROM employee
    WHERE team_id = e.team_id
)
AS team_size
FROM employee e;
