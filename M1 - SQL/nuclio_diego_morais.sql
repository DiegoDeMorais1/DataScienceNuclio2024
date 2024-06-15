USE classicmodels;

-- 1.Seleciona o nome, linha de produto e preço médio de revenda (MSRP) dos produtos cujo preço de revenda é pelo menos 2 vezes superior ao preço de compra (buyPrice) e o preço de compra seja superior a 50 euros

SELECT productName, productLine, MSRP
FROM products
WHERE MSRP >= 2*buyPrice
	AND buyPrice>50; 
 
-- 2. Seleciona o nome e a quantidade total dos 10 produtos mais comprados. 

SELECT 
    productName, sales
FROM
    (SELECT 
        productCode, 
        SUM(quantityOrdered) sales
    FROM
        orderdetails
    INNER JOIN orders USING (orderNumber)
    
    GROUP BY productCode
    ORDER BY sales DESC
    LIMIT 10) top10products
INNER JOIN
    products USING (productCode);
    
-- 3.Seleciona o nome e número de telefone dos clientes cuja taxa de insucesso das encomendas é superior a 30%.

WITH TaxaDeInsucessoClientes AS (
    SELECT
        c.customerNumber,
        c.customerName,
        c.phone,
        (COUNT(CASE 
			WHEN o.status IN ('Resolved', 'Cancelled', 'Disputed', 'OnHold') THEN 1 END) * 100.0 / COUNT(o.orderNumber)) 
            AS taxa_de_insucesso
    FROM
        customers c
    LEFT JOIN
        orders o ON c.customerNumber = o.customerNumber
    GROUP BY
        c.customerNumber, c.customerName, c.phone
)
-- Consulta principal para obter os clientes com taxa de insucesso superior a 30%
SELECT
    tc.customerName,
    tc.phone,
    tc.taxa_de_insucesso
FROM
    TaxaDeInsucessoClientes tc
WHERE
    tc.taxa_de_insucesso > 30.0;
