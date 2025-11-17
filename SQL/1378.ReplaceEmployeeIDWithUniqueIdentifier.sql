/* Write your T-SQL query statement below */
SELECT eu.unique_id, em.name
FROM Employees em
LEFT JOIN EmployeeUNI eu
ON em.id = eu.id
 