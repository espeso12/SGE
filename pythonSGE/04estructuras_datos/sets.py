# Ejemplos de sets (conjuntos)
conjunto = {3, 1, 4, 1, 5}

# Inserción
conjunto.add(9)
print("Después de añadir 9:", conjunto)

# Borrado
conjunto.discard(1)
print("Después de eliminar 1:", conjunto)

# Actualización
# No se pueden actualizar elementos específicos, pero se pueden añadir múltiples elementos
conjunto.update([10, 11])
print("Después de actualizar con nuevos elementos:", conjunto)

# Ordenación (los sets no tienen orden, pero podemos convertirlo en una lista para ordenarlo)
conjunto_ordenado = sorted(conjunto)
print("Conjunto ordenado:", conjunto_ordenado)
