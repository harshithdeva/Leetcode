/* Write your T-SQL query statement below */
SELECT p.product_name, s.year, s.price
FROM Product p
LEFT JOIN Sales s
ON p.product_id = s.product_id
WHERE s.sale_id IS NOT NULL