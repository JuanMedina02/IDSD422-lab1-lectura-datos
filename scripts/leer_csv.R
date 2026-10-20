# install.packages('readr')
library(readr)
ventas_csv <- read_csv("../data/ventas.csv")

cat("\nImpresión de las primeras filas del archivo CSV:\n")
print(head(ventas_csv))

cat("\nDimensiones (filas, columnas):\n")
print(dim(ventas_csv))

cat("\nEstructura y tipos por columna:\n")
str(ventas_csv)
