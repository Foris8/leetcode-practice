# Write your MySQL query statement below
SELECT a.name as Employee
FROM Employee AS a, Employee AS b
WHERE
    a.salary >= b.salary
    AND a.ManagerId = b.Id