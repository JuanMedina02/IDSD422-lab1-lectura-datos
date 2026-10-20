
# install.packages('jsonlite')
library(jsonlite)

cat("Lectura de archivos tipo JSON\n")
#fromJSON lee el archivo y lo convierte automáticamente en un data.frame
ventas_json <- fromJSON("../data/ventas.json")
cat("\nImpresión de las primeras filas del archivo JSON:\n")
print(head(ventas_json))

cat("\nDimensiones (filas, columnas):\n")
print(dim(ventas_json))

cat("\nEstructura y tipos por columna:\n")
str(ventas_json)
