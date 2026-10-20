# leer_excel.py — Cargar el consolidado Excel de finanzas (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_excel.py

# TODO 1: importa pandas
# TODO 2: carga data/ventas.xlsx indicando la hoja correcta
# TODO 3: imprime las dimensiones y las primeras filas
# Lectura de un archivo .xlsx
import pandas as pd

pd_ventas = pd.read_excel("../data/ventas.xlsx", sheet_name='ventas') # Leemos el archivo Excel con pandas

#=============================================================
print('Impresión de las primeras filas del archivo XLSX')

print(pd_ventas.head())

print('Dimensiones: \n', pd_ventas.shape)
print('\nTipos por columna: ')
print(pd_ventas.dtypes)
