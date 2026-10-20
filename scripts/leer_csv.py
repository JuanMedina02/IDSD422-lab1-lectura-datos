#Escrito por Juan Medina

import pandas as pd    #Importación de bibliotecas

print('Lectura de archivos tipo CSV')
pd_ventas_CSV=pd.read_csv("../data/ventas.csv")    #Lectura CSV

print('Impresión de las primeras filas del archivo CSV')
print(pd_ventas_CSV.head())                                                
print('\nDimensiones: \n',pd_ventas_CSV.shape)         #Dimensiones del DataFrame
print('\nTipos por columna: \n', pd_ventas_CSV.dtypes) #Variables de cada columna 
