-- 3.Seleciona o nome e número de telefone dos clientes cuja taxa de insucesso das encomendas é superior a 30%.
SELECT 
    customerName, phone
FROM
	customers
WHERE EXISTS
		(SELECT status 
        FROM orders 
        WHERE status = 'Cancelled' OR 'Resolved' OR 'Disputed' OR 'OnHold')
;
--
SELECT status FROM orders;
--
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
            status = 'Cancelled' OR 'Resolved' OR 'Disputed' OR 'OnHold'
            and customerNumber = customers.customerNumber
		);