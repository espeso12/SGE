# Ejemplos de diccionarios
diccionario = {'clave1': 100, 'clave2': 200, 'clave3': 300}

# Inserción
print("Después de añadir clave3:", diccionario)

# Borrado
diccionario.pop('clave1')
print("Después de eliminar clave1:", diccionario)

# Actualización
diccionario['clave2'] = 500
print("Después de actualizar clave2:", diccionario)

# Ordenación (ordenar por claves)
diccionario_ordenado = dict(sorted(diccionario.items()))
print("Diccionario ordenado por claves:", diccionario_ordenado)
