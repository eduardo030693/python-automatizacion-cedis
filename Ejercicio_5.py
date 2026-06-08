"""
── Ejercicio 5: Calcular diferencias automáticamente con pandas ──
Tema: pandas - Columnas calculadas   |   Nivel 5/10  ★★★★★☆☆☆☆☆
Con una sola línea puedes operar columnas enteras. Esta es la magia de pandas en análisis de inventarios.
Instrucciones:
Carga el CSV del ejercicio anterior.
Agrega una columna 'Diferencia' = Sistema - Bodega.
Agrega una columna 'Estado': 'OK' si diferencia es 0, 'FALTANTE' si es negativa, 'SOBRANTE' si es positiva.
Filtra y muestra solo las filas con discrepancias.
Exporta el resultado a comparacion.xlsx con .to_excel().
"""
import pandas as pd

df = pd.read_csv('/Users/macbookair/Documents/Python_proyectos/Automatizacion/Recursos/inventario.csv')
df['Diferencia']= df['Sistema'] - df['Bodega']

def evaluar(diferencia): 

    if diferencia == 0:
        return 'OK'
    elif diferencia < 0:
        return 'FALTANTE'
    else:
        return 'SOBRANTE'


df['Estado'] = df['Diferencia'].apply(evaluar)
filtro = df[df['Diferencia']!=0]
df.to_excel('comparacion.xlsx', index = False)
print(filtro)


    






