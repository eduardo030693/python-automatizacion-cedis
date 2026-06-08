"""
── Ejercicio 4: Leer inventario desde CSV con pandas ──
Tema: pandas - Lectura de archivos   |   Nivel 4/10  ★★★★☆☆☆☆☆☆
En la vida real los datos vienen en archivos Excel o CSV. 
Aprenderás a leerlos y explorarlos con pandas.
Instrucciones:
Instala pandas si no lo tienes: pip install pandas.
Crea un archivo inventario.csv con columnas: SKU, Producto, Sistema, Bodega.
Léelo con pd.read_csv().
Muestra las primeras 5 filas con .head().
Muestra un resumen con .describe().
"""

import pandas as pd
#Leer archivo csv
df = pd.read_csv("/Users/macbookair/Documents/Python_proyectos/Automatizacion/Recursos/inventario.csv")
print(df.head(5))
print(df.describe())

"""
Tambien se puede crear un diccionario con la informacion necesaria, luego se crea un dataframe con ese 
diccionario y por ultimo se utiliza el metodo df.to_csv('inventario.csv', index=False) con false en el 
indice para que no lo cree. Y a partir de ese punto entonces se lee el archivo con .read_csv(), y se 
imprimen los df con los metodos head y describe.
"""