total_registros = 15000

porcentaje_nulos = 0.08

registros_nulos = total_registros * porcentaje_nulos

registros_limpios = total_registros - registros_nulos

print("-"*20 + "Resultados" + "-"*20)
print(registros_nulos)
print(registros_limpios)