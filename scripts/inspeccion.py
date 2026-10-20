# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

 # Escrito por: Juan Medina
import pandas as pd    #Importación de bibliotecas

print('Lectura de archivos tipo CSV')    
pd_ventas_CSV=pd.read_csv("../data/ventas.csv")    #Lectura del archivo ventas.csv

print('\nTipos por columna: \n', pd_ventas_CSV.dtypes) # Impresión de dataTypes

#=====================================================================
# Generación de la columna "Ticket" = ventas/clientes
pd_ventas_CSV['Ticket'] = pd_ventas_CSV['ventas']/pd_ventas_CSV['clientes']
print('\nDataFrame con nueva columna ',pd_ventas_CSV.head())  # Impresión 

#=====================================================================
print('\nVenta promedio por sucursal')
sucursales = pd_ventas_CSV.groupby('sucursal')['ventas']
print(sucursales.mean())

#=====================================================================
print('\nTicket Promedio (ventas totales/clientes totales) ')
ventas_totales = pd_ventas_CSV['ventas'].sum()
clientes_totales =pd_ventas_CSV['clientes'].sum()
prom_ticket = ventas_totales / clientes_totales 
print('=', prom_ticket)

#=====================================================================
print('\n Sucursal con mayor y menor venta')
fila_max = pd_ventas_CSV['ventas'].idxmax() # Fila con mayores ventas 
fila_min = pd_ventas_CSV['ventas'].idxmin() #Fila con menores ventas

sucursal_max = pd_ventas_CSV.loc[fila_max, 'sucursal']
sucursal_min = pd_ventas_CSV.loc[fila_min, 'sucursal']

print('Sucursal con mayores ventas: ', sucursal_max)
print('Sucursal con menores ventas: ', sucursal_min)

#=====================================================================
print('\nRegión con mayor venta total ')
regiones = pd_ventas_CSV.groupby('region')['ventas'].sum() #Agrupar regiones
region_max = regiones.idxmax()
value_region_max = regiones.max()
print('Región con mayores ventas: ', region_max)
print('Con ventas totales de: ', value_region_max)




