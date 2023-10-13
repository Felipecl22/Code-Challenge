-- Primeramente se creo una nueva base de datos llamada "Ventas Minoristas, luego sobre esta base de datos y desde tareas se agrego un flat file 
-- y se creo la tabla dbo.Ventas Minoristas.

USE [Ventas Minoristas];

SELECT *
FROM [Ventas Minoristas];

-- Vamos a generar una nueva columna que nos indique el valor total de la venta:

SELECT
	Factura,
	NumeroStock,
	Descripcion,
	Fecha,
	Cantidad,
	PrecioUnitario,
	IDcliente,
	Pais,
	PrecioUnitario*Cantidad as 'Total Venta'
FROM [Ventas Minoristas];

-- Ahora vamos a agregar esta nueva columna a nuestra tabla:
ALTER TABLE dbo.[Ventas Minoristas]
ADD TotalVenta DECIMAL(10, 2);

UPDATE dbo.[Ventas Minoristas]
SET TotalVenta = PrecioUnitario * Cantidad;

-- Vamos a segmentar las ventas solo por el pais France:
SELECT *
FROM [Ventas Minoristas]
WHERE Pais LIKE 'France'
ORDER BY TotalVenta ASC;

-- Vamos a agrupar y generar agregaciones con nuestras columnas por Pais:
SELECT 
	Pais,
	SUM(Cantidad) AS 'Cantidad Total Vendida',
	ROUND(AVG(PrecioUnitario), 2) AS 'Precio Unitario Promedio', 
	MAX(TotalVenta) AS 'Venta Mayor',
	MIN(TotalVenta) AS 'Venta Menor'
FROM [Ventas Minoristas]
GROUP BY Pais;

-- Por último vamos a crear un index que nos permita en el futuro realizar un búsqueda más fácil.
CREATE INDEX NuevoIndex ON dbo.[Ventas Minoristas] (Factura);

-- Fin Código