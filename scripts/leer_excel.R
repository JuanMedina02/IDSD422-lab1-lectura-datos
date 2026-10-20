# install.packages('readxl') 
library(readxl)

cat("Lectura de archivos tipo XLSX\n")
#read_excel  nos permite especificar la hoja a leer
ventas_xlsx <- read_excel("../data/ventas.xlsx", sheet = "ventas")

cat("\nImpresión de las primeras filas del archivo XLSX:\n")
print(head(ventas_xlsx))

cat("\nDimensiones (filas, columnas):\n")
print(dim(ventas_xlsx))

cat("\nEstructura y tipos por columna:\n")
str(ventas_xlsx)
