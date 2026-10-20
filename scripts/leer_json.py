import json
import pandas as pd     # Importación de bibliotecas
with open("../data/ventas.json", encoding="utf-8") as f:  #Abrimos el archivo JSON
    datos = json.load(f)
pd_ventas = pd.json_normalize(datos)      # Normalización y conversion a DataFrame 
#=============================================================
print('Impresión de las primeras filas del archivo JSON')
print(pd_ventas.head())                                                

print('\nDimensiones: ',pd_ventas.shape)              # Diemnsiones del DataFrame
print('\nTipos por columna: ')                     
print(pd_ventas.dtypes) 
