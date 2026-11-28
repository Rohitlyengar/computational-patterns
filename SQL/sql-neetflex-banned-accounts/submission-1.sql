-- Write your query below
SELECT DISTINCT a.account_id
FROM log_info a
INNER JOIN log_info b
ON a.account_id = b.account_id
WHERE a.ip_address != b.ip_address
AND a.login <= b.logout
AND a.logout >= b.login;
