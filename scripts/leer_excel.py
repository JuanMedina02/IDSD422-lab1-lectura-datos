
import pandas as pd

pd_ventas = pd.read_excel("../data/ventas.xlsx", sheet_name='ventas') # Leemos el archivo Excel con pandas

#=============================================================
print('Impresión de las primeras filas del archivo XLSX')

print(pd_ventas.head())

print('Dimensiones: \n', pd_ventas.shape)
print('\nTipos por columna: ')
print(pd_ventas.dtypes)
