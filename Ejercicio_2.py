"""── Ejercicio 2: Comparar dos listas de productos ──
Tema: Listas y Conjuntos   |   Nivel 2/10  ★★☆☆☆☆☆☆☆☆
Tienes dos listas: productos en el sistema web y productos en tu bodega. 
Necesitas saber cuáles faltan en cada lado.
Instrucciones:
Crea la lista sistema = ['SKU001','SKU002','SKU003','SKU005'].
Crea la lista bodega = ['SKU001','SKU003','SKU004','SKU005'].
Convierte ambas en conjuntos con set().
Encuentra productos que están en sistema pero NO en bodega (faltantes en bodega).
Encuentra productos que están en bodega pero NO en sistema (no registrados).
Imprime ambos resultados.
"""

sistema = set(['SKU001','SKU002','SKU003','SKU005'])
bodega = set(['SKU001','SKU003','SKU004','SKU005'])
sis_no_bod = sistema-bodega
bod_no_sis = bodega-sistema
print(f"Productos que están en sistema pero NO en bodega: {sis_no_bod}")
print(f"Productos que están en bodega pero NO en sistema: {bod_no_sis}")

"""
Este ejercicio se puede resolver convirtiendo en conjunto la lista desde que se define la 
variable sistema y bodega, pero tambien se pueden convertir en conjunto al momento de hacer
la comparacion, set(sistema) - set(bodega)
"""