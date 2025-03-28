SELECT Region.RegionDescription, SUM(OrderDetail.Quantity * OrderDetail.UnitPrice * (1 - OrderDetail.Discount)) AS TotalSales
FROM Order
JOIN Region ON Order.ShipRegion = Region.RegionDescription
JOIN OrderDetail ON OrderDetail.OrderId = Order.Id
WHERE Order.ShippedDate IS NOT NULL
GROUP BY Region.RegionDescription
ORDER BY TotalSales DESC;