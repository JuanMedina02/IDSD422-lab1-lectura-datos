

library(readr)  # Importacion de librerias

cat("=========================================\n")
cat(" Carga de datos y estructura\n")
cat("=========================================\n")
ventas_csv <- read_csv("../data/ventas.csv", show_col_types = FALSE)

cat ('Estructura de los datos')
str(ventas_csv)


cat("Generación de una columna derivada 'ticket'\n")
cat("=========================================\n")

ventas_csv$ticket <- ventas_csv$ventas / ventas_csv$clientes
print(head(ventas_csv))


cat("Venta Promedio por sucursal\n")
cat("=========================================\n")
#usanmos la función aggregate 
promedio_sucursal <- aggregate(ventas ~ sucursal, data = ventas_csv, FUN = mean)
print(promedio_sucursal)


cat("\nTicket Promedio (ventas totales / clientes totales):\n")
cat("=========================================\n")
ventas_totales <- sum(ventas_csv$ventas)
clientes_totales <- sum(ventas_csv$clientes)
prom_ticket <- ventas_totales / clientes_totales
cat("=", prom_ticket, "\n")

cat("\n Sucursal con mayores y menores ventas\n")
cat("=========================================\n")
# which.max y which.min son el equivalente directo de idxmax() e idxmin() en pandas
fila_max <- which.max(ventas_csv$ventas)
fila_min <- which.min(ventas_csv$ventas)

sucursal_max <- ventas_csv$sucursal[fila_max]
sucursal_min <- ventas_csv$sucursal[fila_min]

cat("Sucursal con mayores ventas: ", sucursal_max, "\n")
cat("Sucursal con menores ventas: ", sucursal_min, "\n")


cat("\nRegión con mayor venta total:\n")
cat("=========================================\n")
ventas_region <- aggregate(ventas ~ region, data = ventas_csv, FUN = sum)
fila_region_max <- which.max(ventas_region$ventas)

region_max <- ventas_region$region[fila_region_max]
value_region_max <- ventas_region$ventas[fila_region_max]

cat("Región con mayores ventas: ", region_max, "\n")
cat("Con ventas totales de: ", value_region_max, "\n")
