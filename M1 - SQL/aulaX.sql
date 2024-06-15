USE classicmodels;
show databases;
show tables;
SELECT * FROM customers LIMIT 0, 1000;

SELECT status, count(orderNumber) as countOrder
	from orders
group by status;

SELECT productLine, avg(msrp) as avgPrice
	from products
group by productLine
having avgPrice > 100;

-- 9
SELECT min(valor_encomenda) as minSumPrice, max(valor_encomenda) as maxSumPrice
FROM
(
	SELECT orderNumber, SUM(priceEach*quantityOrdered) as valor_encomenda
	FROM orderdetails
	GROUP BY orderNumber
) priceOrders;

-- 10
SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT max(amount)
	FROM payments
);

-- 11
SELECT customerNumber, amount
FROM payments
WHERE amount > (
	SELECT AVG(amount)
	FROM payments
);

-- 12
SELECT customerName, customerNumber
FROM customers
WHERE EXISTS (
	SELECT orderNumber
    FROM orders
    WHERE status='Cancelled'
    AND CustomerNumber = customers.CustomerNumber
);