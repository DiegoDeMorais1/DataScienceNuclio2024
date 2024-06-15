USE classicmodels;

-- 1
CREATE TABLE review (
	reviewNumber int(11) NOT NULL,
    productCode varchar(15) NOT NULL,
    customerNumber int(11) NOT NULL,
    star int(11) NOT NULL,
    description varchar(50),
    PRIMARY KEY (reviewNumber),
    FOREIGN KEY (productCode) REFERENCES products(productCode),
    FOREIGN KEY (customerNumber) REFERENCES customers(customerNumber)
);

-- 2
ALTER TABLE review
MODIFY COLUMN star float(11);

ALTER TABLE review
ADD image blob;

ALTER TABLE review
DROP COLUMN image;

-- 3
INSERT INTO review (reviewNumber, productCode, customerNumber, star, description)
VALUES (1, 'S10_1678', 103, 4.5, 'produto maravilha!!');

INSERT INTO review (reviewNumber, productCode, customerNumber, star)
VALUES (2, 'S10_1678', 103, 2);

-- 4
UPDATE review
SET star=2.9, description='produto assim-assim'
WHERE reviewNumber=1;

-- 5
DELETE FROM review
WHERE reviewNumber=1;

DROP TABLE review;

-- 6
select firstName, lastName
from employees;

-- 7
select employeeNumber, firstName, LastName, jobTitle
from employees
where jobTitle='Sales Rep';
-- firstName = 'Leslie';
-- AND 

-- 8
select orderNumber, orderDate, status
from orders
where status='In Process';
-- and status='Cancelled';

-- 9
select orderNumber, quantityOrdered, priceEach,
	(priceEach*quantityOrdered) AS totalPrice
from orderdetails
where (priceEach*quantityOrdered);

-- 10

select employeeNumber, firstName, lastName
from employees
where firstName LIKE 'm%';

-- 11
select customerName, creditLimit
from customers
order by creditLimit desc
limit 5;

-- 12
select distinct country, state
from customers
order by country, state;

-- 13
select 
	productCode,
	min(quantityOrdered) as minQuantity,
	max(quantityOrdered) as maxQuantity,
    avg(quantityOrdered) as avgQuantity,
    count(orderNumber) as countQuantity
from orderdetails
where productCode = 'S10_1678';

select productCode from orderdetails;

-- 14
select 
	status, 
    count(orderNumber) as countOrder,
    max(shippedDate) as recentOrder
from orders
group by status;

-- 15
select productLine, avg(msrp) as avgPrice
from products
where buyPrice > 50
group by productLine
having avgPrice > 85
order by avgPrice asc;









