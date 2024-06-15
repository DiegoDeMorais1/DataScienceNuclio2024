USE classicmodels;

-- 1
select 
	CONCAT(firstName, ' ' ,lastName)
from employees;

-- 2
select 
	SUBSTRING(lastName, 1, 1) AS first_letter
FROM employees;

-- 3
select UPPER(lastName) 
FROM employees;
-- fazer a mesma coisa para LOWER

-- 4
SELECT LOWER(productName)
FROM products
LIMIT 5;

-- 5
SELECT productName, LENGTH(productName) as length_product
FROM products
ORDER BY length_product DESC
LIMIT 1; 

-- 6
SELECT 
	orderNumber, 
    orderDate, 
    MONTH(orderDate) AS month_date
FROM orders
WHERE MONTH(orderDate) <= 6;

-- 7
SELECT 
	MONTH(orderDate) AS month_date,
    DAY(orderDate) as day_date,
    count(orderNumber)
FROM orders
GROUP BY month_date, day_date;

-- 8
SELECT 
	productName, 
    LENGTH(productName) AS len_prod,
    CASE
		WHEN LENGTH(productName) > 30 THEN 'maior!'
        WHEN LENGTH(productName) < 30 THEN 'menor!'
        else 'igual!'
	END
FROM products
LIMIT 5;

-- 9
-- passo 1: ver as orderdetails ordenadas
-- passo 2: contagem
-- passo 3: minimos e maximos
SELECT 
	MIN(count_orders), 
    MAX(count_orders)
FROM
	(SELECT orderNumber, count(orderNumber) AS count_orders
	FROM orderdetails
	group by orderNumber) AS count_per_detail;
    
-- 10
SELECT 
    customerNumber, 
    checkNumber, 
    amount
FROM
    payments
WHERE
    amount = (SELECT MAX(amount) FROM payments);
    
-- 11
SELECT 
    customerNumber, 
    checkNumber, 
    amount
FROM
    payments
WHERE
    amount > (SELECT 
            AVG(amount)
        FROM
            payments);

-- 12
SELECT 
    customerNumber, 
    customerName,
    phone
FROM
    customers
WHERE
    EXISTS(
		SELECT orderNumber
        FROM
            orders
        WHERE
            status = 'Cancelled'
            and customerNumber = customers.customerNumber
		);

-- 13
SELECT productName
FROM products
WHERE buyPrice > ALL
  (SELECT priceEach
  FROM orderdetails
  WHERE products.productCode = orderdetails.productCode
); 

-- 14
SELECT productName, productDescription
FROM products
WHERE productCode = ANY(
  SELECT productCode
  FROM orderdetails
  WHERE quantityOrdered > 70
); 

select productName, productDescription
FROM products
WHERE EXISTS (
	SELECT productCode
	FROM orderdetails
    WHERE quantityOrdered > 70
    AND productCode = products.productCode
);
  
-- 15
select productName, productDescription, productLine, textDescription
from products
inner join productLines using(productLine);

select productName, productDescription, products.productLine, textDescription
from products
inner join productLines on products.productLine = productLines.productLine;

-- 16
SELECT 
    c.customerNumber, 
    c.customerName, 
    o.orderNumber, 
    o.status
FROM
    customers c
LEFT JOIN orders o 
    ON c.customerNumber = o.customerNumber;
-- WHERE
--    orderNumber IS NULL;
    
-- 17
SELECT concat(firstName,' ',lastName) fullname
FROM employees 
UNION 
SELECT concat(contactFirstName,' ',contactLastName)
FROM  customers
ORDER BY fullname;

-- 18
SELECT 
    productName, sales
FROM
    (SELECT 
        productCode, 
        ROUND(SUM(quantityOrdered * priceEach)) sales
    FROM
        orderdetails
    INNER JOIN orders USING (orderNumber)
    WHERE
        YEAR(shippedDate) = 2003
    GROUP BY productCode
    ORDER BY sales DESC
    LIMIT 5) top5products2003
INNER JOIN
    products USING (productCode);
