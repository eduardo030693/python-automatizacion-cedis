"""
── Ejercicio 3: Comparar cantidades con diccionarios ──
Tema: Diccionarios   |   Nivel 3/10  ★★★☆☆☆☆☆☆☆
Ahora los datos tienen cantidades. Necesitas saber no solo qué productos difieren, 
sino cuánto difieren.
Instrucciones:
Crea un diccionario sistema_cant con 4 SKUs y cantidades.
Crea un diccionario bodega_cant con los mismos SKUs pero algunas cantidades diferentes.
Recorre las claves del sistema con un for.
Compara cantidades y si son diferentes, imprime la diferencia.
"""

sistema_cant = {'SKU001': 10, 'SKU002': 5, 'SKU003': 20, 'SKU004': 15}
bodega_cant = {'SKU001': 8, 'SKU002': 5, 'SKU003': 18, 'SKU004': 15}

print('SKU          Sistema  Bodega  Diferencia')
print('-' * 45)    

for sku in sistema_cant:
    cant_s = sistema_cant[sku]
    cant_bod = bodega_cant.get(sku,0)
    diff = cant_s - cant_bod
    if diff != 0:
        print(f'{sku:<12} {cant_s:<8} {cant_bod:<7} {diff:+}')   

